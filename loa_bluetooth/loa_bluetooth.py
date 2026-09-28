"""Loa Bluetooth cho Home Assistant: quét, ghép đôi, kết nối, ngắt, quên — qua BlueZ D-Bus.

Chạy trong container Home Assistant, nói chuyện với BlueZ qua D-Bus hệ thống (/run/dbus).
HA chạy trong LXC thì Bluetooth thật nằm trên máy Proxmox, D-Bus của nó được gắn vào LXC —
xem README.md cùng thư mục. Tiếng đi bằng bluez-alsa; MPD phát vào loa A2DP kết nối GẦN
NHẤT — đổi loa không phải sửa gì.

Gọi từ shell_command của HA; in ra MỘT dòng JSON:
    python3 /config/loa_bluetooth.py ds                 loa đã biết
    python3 /config/loa_bluetooth.py quet [giay]        quét rồi liệt kê
    python3 /config/loa_bluetooth.py noi AA:BB:…        ghép đôi (nếu chưa) + tin cậy + kết nối
    python3 /config/loa_bluetooth.py ngat AA:BB:…
    python3 /config/loa_bluetooth.py quen AA:BB:…       xoá ghép đôi
"""
import asyncio
import json
import re
import sys

from dbus_fast import BusType, Message, Variant
from dbus_fast.aio import MessageBus
from dbus_fast.service import ServiceInterface, method

BLUEZ = "org.bluez"
LOA = "0000110b-0000-1000-8000-00805f9b34fb"          # A2DP Audio Sink
AGENT = "/c2a/loa_agent"


class _Agent(ServiceInterface):
    """Agent NoInputNoOutput: loa không có bàn phím — nhận mọi yêu cầu ghép đôi kiểu Just Works."""

    def __init__(self):
        super().__init__("org.bluez.Agent1")

    @method()
    def Release(self):
        pass

    @method()
    def RequestConfirmation(self, device: "o", passkey: "u"):  # noqa: F821
        pass

    @method()
    def RequestAuthorization(self, device: "o"):  # noqa: F821
        pass

    @method()
    def AuthorizeService(self, device: "o", uuid: "s"):  # noqa: F821
        pass

    @method()
    def RequestPinCode(self, device: "o") -> "s":  # noqa: F821
        return "0000"

    @method()
    def RequestPasskey(self, device: "o") -> "u":  # noqa: F821
        return 0

    @method()
    def Cancel(self):
        pass


async def _goi(bus, path, iface, member, sig="", body=None, cho=30):
    r = await asyncio.wait_for(bus.call(Message(destination=BLUEZ, path=path, interface=iface,
                                                member=member, signature=sig, body=body or [])), cho)
    if r.message_type.name == "ERROR":
        raise RuntimeError(f"{r.error_name}: {r.body[0] if r.body else ''}")
    return r.body


async def _adapter_va_thiet_bi(bus):
    (objs,) = await _goi(bus, "/", "org.freedesktop.DBus.ObjectManager", "GetManagedObjects")
    adapter = next(p for p, v in objs.items() if "org.bluez.Adapter1" in v)
    return adapter, objs


def _loa(objs):
    ra = []
    for p, v in objs.items():
        d = v.get("org.bluez.Device1")
        if not d:
            continue
        uuids = d["UUIDs"].value if "UUIDs" in d else []
        lop = d["Class"].value if "Class" in d else 0
        # Loa: có A2DP Sink, hoặc lớp thiết bị Audio/Video (major 0x04) khi chưa đọc được UUID.
        if LOA not in uuids and (lop >> 8) & 0x1F != 0x04:
            continue
        ra.append({"dia_chi": d["Address"].value,
                   "ten": (d["Alias"].value if "Alias" in d else d["Address"].value),
                   "da_ghep": bool(d["Paired"].value) if "Paired" in d else False,
                   "dang_noi": bool(d["Connected"].value) if "Connected" in d else False})
    return sorted(ra, key=lambda x: (not x["dang_noi"], not x["da_ghep"], x["ten"]))


def _duong(adapter, dia_chi):
    if not re.fullmatch(r"[0-9A-F]{2}(:[0-9A-F]{2}){5}", dia_chi.upper()):
        raise ValueError(f"địa chỉ không hợp lệ: {dia_chi}")
    return f"{adapter}/dev_{dia_chi.upper().replace(':', '_')}"


async def chinh(argv):
    lenh = argv[1] if len(argv) > 1 else "ds"
    bus = await MessageBus(bus_type=BusType.SYSTEM).connect()
    adapter, objs = await _adapter_va_thiet_bi(bus)
    if lenh == "quet":
        giay = min(max(int(argv[2]) if len(argv) > 2 and argv[2].isdigit() else 12, 3), 40)
        await _goi(bus, adapter, "org.bluez.Adapter1", "SetDiscoveryFilter", "a{sv}",
                   [{"Transport": Variant("s", "bredr")}])
        await _goi(bus, adapter, "org.bluez.Adapter1", "StartDiscovery")
        try:
            await asyncio.sleep(giay)
        finally:
            await _goi(bus, adapter, "org.bluez.Adapter1", "StopDiscovery")
        _a, objs = await _adapter_va_thiet_bi(bus)
        return {"ok": True, "loa": _loa(objs)}
    if lenh == "ds":
        return {"ok": True, "loa": _loa(objs)}
    if len(argv) < 3:
        raise ValueError("thiếu địa chỉ loa")
    p = _duong(adapter, argv[2])
    if p not in objs:
        raise ValueError("chưa thấy loa này — bấm Quét khi loa đang ở chế độ ghép đôi")
    dev = "org.bluez.Device1"
    if lenh == "noi":
        d = objs[p][dev]
        if not d["Paired"].value:
            bus.export(AGENT, _Agent())
            await _goi(bus, "/org/bluez", "org.bluez.AgentManager1", "RegisterAgent", "os",
                       [AGENT, "NoInputNoOutput"])
            try:
                await _goi(bus, p, dev, "Pair", cho=25)
            finally:
                await _goi(bus, "/org/bluez", "org.bluez.AgentManager1", "UnregisterAgent", "o",
                           [AGENT])
        await _goi(bus, p, "org.freedesktop.DBus.Properties", "Set", "ssv",
                   [dev, "Trusted", Variant("b", True)])
        await _goi(bus, p, dev, "Connect", cho=25)
    elif lenh == "ngat":
        await _goi(bus, p, dev, "Disconnect")
    elif lenh == "quen":
        await _goi(bus, adapter, "org.bluez.Adapter1", "RemoveDevice", "o", [p])
    else:
        raise ValueError(f"lệnh lạ: {lenh}")
    _a, objs = await _adapter_va_thiet_bi(bus)
    return {"ok": True, "loa": _loa(objs)}


if __name__ == "__main__":
    try:
        kq = asyncio.run(chinh(sys.argv))
    except Exception as exc:  # noqa: BLE001 — trả lỗi thành JSON cho HA đọc
        kq = {"ok": False, "loi": str(exc)[:300]}
    print(json.dumps(kq, ensure_ascii=False))
