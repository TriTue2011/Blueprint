# 🔊 Loa Bluetooth trong Home Assistant — không cần add-on

Quét, ghép đôi, kết nối và phát ra **loa Bluetooth bất kỳ** ngay trên giao diện Home
Assistant, **không cài add-on nào**. Dành cho **HA Container** (Docker) — chạy trên máy
Debian/Ubuntu, trong VM, hay trong **LXC trên Proxmox** — nơi add-on không cài được.

- Chọn loa trong danh sách, bấm **Kết nối** — đổi loa lúc nào cũng được, không sửa cấu hình.
- Phát bằng `media_player` của tích hợp **MPD** có sẵn trong HA: TTS, nhạc, YouTube,
  automation.
- Chỉ Bluetooth "cổ điển" A2DP (loa, soundbar, tai nghe). Chiều ngược lại (điện thoại phát
  vào HA) và LE Audio không có.

## Mục lục

1. [Nó chạy thế nào](#1-nó-chạy-thế-nào)
2. [Chọn trường hợp của bạn](#2-chọn-trường-hợp-của-bạn)
3. [Trường hợp A — máy Debian / Ubuntu / VM có Bluetooth](#3-trường-hợp-a--máy-debian--ubuntu--vm-có-bluetooth)
4. [Trường hợp B — HA Container trong LXC trên Proxmox](#4-trường-hợp-b--ha-container-trong-lxc-trên-proxmox)
5. [Phần Home Assistant (chung cho A và B)](#5-phần-home-assistant-chung-cho-a-và-b)
6. [Sử dụng](#6-sử-dụng)
7. [Kiểm tra từng tầng khi không ra tiếng](#7-kiểm-tra-từng-tầng-khi-không-ra-tiếng)
8. [Gỡ lỗi thường gặp](#8-gỡ-lỗi-thường-gặp)
9. [Gỡ cài đặt](#9-gỡ-cài-đặt)

---

## 1. Nó chạy thế nào

```
                ┌──────────── máy có Bluetooth ────────────┐
Home Assistant ─┼─D-Bus─► BlueZ ────────────► USB/mainboard ┼──► loa
  │             │            ▲                              │
  │ nút Quét,   │            │                              │
  │ Kết nối…    │         bluez-alsa (tiếng A2DP)           │
  │             │            ▲                              │
  └─media_player┼──► MPD ────┘  (ALSA "bluealsa")           │
     (MPD)      └───────────────────────────────────────────┘
```

| Thành phần | Việc |
|---|---|
| **BlueZ** (`bluez`) | Dịch vụ Bluetooth của Linux: quét, ghép đôi, kết nối |
| **bluez-alsa** (`bluez-alsa-utils`) | Đưa tiếng ra loa A2DP; thiết bị ALSA tên `bluealsa` |
| **MPD** (`mpd`) | Trình phát nhạc nhỏ; HA điều khiển qua tích hợp MPD có sẵn |
| `loa_bluetooth.py` | Chạy trong container HA, nói chuyện với BlueZ qua D-Bus |
| `packages/loa_bluetooth.yaml` | Danh sách chọn loa + 4 nút: Quét / Kết nối / Ngắt / Quên |

MPD xuất ra `bluealsa` không ghi địa chỉ loa, nghĩa là **loa A2DP kết nối gần nhất** —
nên đổi loa chỉ cần bấm Kết nối loa khác.

## 2. Chọn trường hợp của bạn

Hai câu hỏi: **(1)** Bluetooth lấy từ đâu — có sẵn trên mainboard, hay cắm USB ngoài;
**(2)** HA chạy trên gì — HA OS, Debian (máy thật), hay Proxmox (VM hoặc LXC).

Bluetooth có sẵn trên mainboard (thường đi chung card Wi-Fi Intel/Realtek) và USB cắm ngoài
**với Linux đều là một thiết bị USB** — nên cách làm chỉ khác ở chỗ *cắm vào đâu*.

| # | HA chạy trên | Bluetooth | Làm gì | Hướng dẫn |
|---|---|---|---|---|
| 1 | **Debian / Ubuntu** máy thật, HA Container | Có sẵn trên mainboard | Cài firmware nếu thiếu, dùng luôn | **[A](#3-trường-hợp-a--máy-debian--ubuntu--vm-có-bluetooth)** |
| 2 | **Debian / Ubuntu** máy thật, HA Container | Không có → cắm USB (vd TP-Link UB500) | Cắm USB, dùng luôn | **[A](#3-trường-hợp-a--máy-debian--ubuntu--vm-có-bluetooth)** |
| 3 | **Proxmox → VM** (Debian) chạy HA Container | Có sẵn trên mainboard | Cho VM mượn thiết bị Bluetooth của mainboard (USB passthrough theo mã, xem dưới) | **[A](#3-trường-hợp-a--máy-debian--ubuntu--vm-có-bluetooth)** làm *trong VM* |
| 4 | **Proxmox → VM** (Debian) chạy HA Container | Cắm USB | USB passthrough vào VM | **[A](#3-trường-hợp-a--máy-debian--ubuntu--vm-có-bluetooth)** làm *trong VM* |
| 5 | **Proxmox → LXC** chạy HA Container | Có sẵn **hoặc** cắm USB | **Không** passthrough; máy Proxmox giữ Bluetooth, LXC mượn D-Bus | **[B](#4-trường-hợp-b--ha-container-trong-lxc-trên-proxmox)** |
| 6 | **HA OS** máy thật | Có sẵn hoặc cắm USB | HA OS tự nhận; phát loa bằng add-on | [Bluetooth Audio Manager](https://github.com/scyto/ha-bluetooth-audio-manager) |
| 7 | **Proxmox → VM HA OS** | Có sẵn hoặc cắm USB | USB passthrough vào VM; phát loa bằng add-on | [Bluetooth Audio Manager](https://github.com/scyto/ha-bluetooth-audio-manager) |

**HA OS (#6, #7) không dùng được bộ này:** HA OS khoá hệ thống, không cài được bluez-alsa và
MPD bằng tay — muốn phát ra loa Bluetooth thì phải qua add-on. Bộ này dành cho HA Container.

### Xem máy có Bluetooth không

```bash
lsusb                              # tìm dòng Bluetooth / TP-Link / Realtek / Intel ... (8087:xxxx)
ls /sys/class/bluetooth/           # sau khi cài bluez phải có hci0
dmesg | grep -i bluetooth          # báo lỗi firmware nếu có
```

Mainboard có Wi-Fi mà `lsusb` không thấy Bluetooth: xem BIOS có tắt Bluetooth / Wi-Fi không,
và trên card Wi-Fi rời, Bluetooth cần dây nối vào **cổng USB 9 chân trên mainboard** (F_USB).

### Cho VM mượn Bluetooth (#3, #4)

Proxmox → chọn VM → **Hardware → Add → USB Device → Use USB Vendor/Device ID** → chọn
thiết bị Bluetooth (USB ngoài: vd `2357:0604 TP-Link UB500`; mainboard: vd `8087:0029 Intel`).
Hoặc lệnh (thay số VM và mã thiết bị theo `lsusb`):

```bash
qm set 110 -usb0 host=2357:0604      # 110 = số VM của bạn
```

Tắt hẳn rồi bật lại VM; trong VM `lsusb` phải thấy thiết bị. Thiết bị đã cho VM mượn thì
máy Proxmox **không** dùng được nữa — một Bluetooth chỉ về một nơi.

**Vì sao LXC phải làm khác:** nhân Linux chỉ cho mở kết nối Bluetooth ở *không gian mạng
gốc* của máy. LXC có không gian mạng riêng, nên dù passthrough USB vào LXC thì chương trình
trong đó vẫn bị từ chối — kể cả LXC privileged, kể cả Docker `network_mode: host` bên trong.
Tự kiểm trong LXC:

```bash
python3 -c "import socket; socket.socket(socket.AF_BLUETOOTH, socket.SOCK_RAW, socket.BTPROTO_HCI); print('dùng được')"
# LXC: [Errno 97] Address family not supported by protocol
```

---

## 3. Trường hợp A — máy Debian / Ubuntu / VM có Bluetooth

Mọi lệnh chạy bằng `root` (hoặc thêm `sudo`) **trên máy chạy Docker của HA**.

### A1. Cài Bluetooth và bluez-alsa

```bash
apt update
apt install -y bluez bluez-alsa-utils alsa-utils
systemctl enable --now bluetooth bluealsa
```

Kiểm:

```bash
bluetoothctl list          # ✅ "Controller AA:BB:CC:DD:EE:FF tên-máy [default]"
systemctl is-active bluealsa   # ✅ active
```

Không thấy `Controller`: xem `dmesg | grep -i bluetooth`. Hay gặp nhất là thiếu firmware —
chip Realtek cần tệp trong `/lib/firmware/rtl_bt/` (Debian: gói `firmware-realtek`, nhánh
`non-free-firmware`), chip Intel cần `firmware-iwlwifi`. Cài xong rút ra cắm lại USB.

VM: nhớ cắm USB Bluetooth vào VM (Proxmox: VM → Hardware → Add → USB Device) trước khi làm.

### A2. Chỉnh bluez-alsa (khuyên làm)

Chỉ phát RA loa, giữ kênh 5 giây giữa hai câu (hai thông báo liền nhau khỏi kết nối lại), bỏ
dòng gỡ lỗi `D:` mà bản Debian in mỗi lần thiết bị BLE hiện/mất (~15.000 dòng/ngày):

```bash
mkdir -p /etc/systemd/system/bluealsa.service.d
nano /etc/systemd/system/bluealsa.service.d/loa.conf
```

Dán vào:

```ini
[Service]
ExecStart=
ExecStart=/bin/sh -c "/usr/bin/bluealsa --keep-alive=5 -p a2dp-source 2>&1 | grep --line-buffered -v ': D: '"
```

```bash
systemctl daemon-reload && systemctl restart bluealsa
systemctl is-active bluealsa   # ✅ active
```

### A3. Cài MPD

```bash
apt install -y --no-install-recommends mpd
cp /etc/mpd.conf /etc/mpd.conf.goc        # giữ bản gốc
nano /etc/mpd.conf
```

Thay toàn bộ bằng:

```
music_directory     "/var/lib/mpd/music"
playlist_directory  "/var/lib/mpd/playlists"
db_file             "/var/lib/mpd/tag_cache"
state_file          "/var/lib/mpd/state"
sticker_file        "/var/lib/mpd/sticker.sql"
user                "mpd"
bind_to_address     "127.0.0.1"
port                "6600"
audio_output {
    type        "alsa"
    name        "Loa Bluetooth"
    device      "bluealsa"          # loa A2DP kết nối GẦN NHẤT
    mixer_type  "software"
}
```

bluez-alsa chỉ cho `root` và nhóm **`audio`** phát ra loa — cho MPD vào nhóm đó rồi bật:

```bash
usermod -aG audio mpd
systemctl disable --now mpd.socket
systemctl enable --now mpd
systemctl restart mpd
```

Kiểm:

```bash
systemctl is-active mpd        # ✅ active
ss -ltn | grep 6600            # ✅ 127.0.0.1:6600
```

`127.0.0.1` là có chủ ý: HA dùng `network_mode: host` nên vẫn tới được, còn máy khác trong
mạng thì không điều khiển được MPD.

### A4. Compose của Home Assistant

HA phải dùng mạng của máy và thấy D-Bus của máy (các dòng khác giữ nguyên):

```yaml
services:
  homeassistant:
    network_mode: host
    volumes:
      - /run/dbus:/run/dbus:ro
```

Thiếu thì thêm rồi `docker compose up -d homeassistant` (Portainer: sửa stack → Update).
Kiểm:

```bash
docker exec homeassistant ls /run/dbus      # ✅ system_bus_socket
```

Xong → sang **[phần 5](#5-phần-home-assistant-chung-cho-a-và-b)**.

---

## 4. Trường hợp B — HA Container trong LXC trên Proxmox

Bluetooth để **máy Proxmox** giữ (BlueZ + bluez-alsa); LXC **mượn D-Bus** của máy Proxmox.
Ví dụ: LXC số `102`, Debian 12 — thay bằng số của bạn (`pct list`). **Không** passthrough USB
vào LXC.

### B1. Máy Proxmox: Bluetooth và bluez-alsa

Trên Shell của Proxmox — giống hệt [A1](#a1-cài-bluetooth-và-bluez-alsa) và
[A2](#a2-chỉnh-bluez-alsa-khuyên-làm) (Proxmox thường có sẵn firmware Realtek).

### B2. Máy Proxmox: cho LXC mượn D-Bus

```bash
cp /etc/pve/lxc/102.conf /root/102.conf.goc
echo 'lxc.mount.entry: /run/dbus mnt/dbus-host none bind,create=dir 0 0' >> /etc/pve/lxc/102.conf
pct reboot 102
```

Gắn vào **`/mnt`**, không phải `/run`: systemd trong LXC phủ một `/run` mới lên lúc khởi động,
che mất chỗ gắn (thấy thư mục rỗng). Kiểm:

```bash
pct exec 102 -- ls /mnt/dbus-host          # ✅ system_bus_socket
```

LXC **privileged** (`unprivileged: 0` trong `102.conf`) chạy ngay. LXC unprivileged thì root
trong LXC không phải root máy Proxmox, D-Bus có thể từ chối — đổi sang privileged, hoặc thêm
chính sách D-Bus cho uid `100000` trên máy Proxmox.

### B3. Trong LXC: MPD và bộ nối bluez-alsa

Mở Console của LXC (hoặc `pct enter 102`):

```bash
apt update
apt install -y --no-install-recommends mpd libasound2-plugin-bluez bluez-alsa-utils bluez alsa-utils
# KHÔNG chạy BlueZ / bluealsa trong LXC — dùng của máy Proxmox:
systemctl mask bluetooth bluealsa
```

`bluez-alsa-utils` cài chỉ để có `/etc/alsa/conf.d/20-bluealsa.conf` — thiếu tệp này MPD báo
`Unknown PCM bluealsa`.

`/etc/mpd.conf` giống [A3](#a3-cài-mpd) **nhưng** `user "root"` (bluez-alsa trên máy Proxmox
không biết nhóm `audio` của LXC; LXC privileged thì root trong LXC = root máy Proxmox). Rồi
cho MPD dùng D-Bus mượn:

```bash
mkdir -p /etc/systemd/system/mpd.service.d
printf '[Service]\nEnvironment=DBUS_SYSTEM_BUS_ADDRESS=unix:path=/mnt/dbus-host/system_bus_socket\n' \
  > /etc/systemd/system/mpd.service.d/bluetooth.conf
systemctl daemon-reload
systemctl disable --now mpd.socket
systemctl enable --now mpd
```

Tuỳ chọn — dùng `bluetoothctl` ngay trong LXC: tạo `/usr/local/bin/bluetoothctl`

```sh
#!/bin/sh
DBUS_SYSTEM_BUS_ADDRESS=unix:path=/mnt/dbus-host/system_bus_socket exec /usr/bin/bluetoothctl "$@"
```

rồi `chmod +x /usr/local/bin/bluetoothctl`; `bluetoothctl list` phải thấy Controller của máy
Proxmox.

### B4. Compose của Home Assistant

```yaml
services:
  homeassistant:
    network_mode: host
    volumes:
      - /mnt/dbus-host:/run/dbus:ro        # D-Bus mượn của máy Proxmox
```

`docker compose up -d homeassistant` (Portainer: sửa stack → Update). Kiểm:

```bash
docker exec homeassistant ls /run/dbus      # ✅ system_bus_socket
```

---

## 5. Phần Home Assistant (chung cho A và B)

### 5.1. Chép hai tệp

| Tệp trong thư mục này | Chép tới (thư mục cấu hình HA, vd `/opt/homeassistant`) |
|---|---|
| [`loa_bluetooth.py`](loa_bluetooth.py) | `/config/loa_bluetooth.py` |
| [`packages/loa_bluetooth.yaml`](packages/loa_bluetooth.yaml) | `/config/packages/loa_bluetooth.yaml` |

Tải thẳng trên máy:

```bash
cd /opt/homeassistant          # thư mục config của HA
mkdir -p packages
wget -O loa_bluetooth.py https://raw.githubusercontent.com/TriTue2011/Blueprint/main/loa_bluetooth/loa_bluetooth.py
wget -O packages/loa_bluetooth.yaml https://raw.githubusercontent.com/TriTue2011/Blueprint/main/loa_bluetooth/packages/loa_bluetooth.yaml
```

`configuration.yaml` phải bật packages (chưa có thì thêm):

```yaml
homeassistant:
  packages: !include_dir_named packages
```

### 5.2. Kiểm và khởi động lại HA

**Developer Tools → YAML → Check configuration** (✅ Configuration valid), rồi **Settings →
System → Restart**. `shell_command` mới chỉ nạp khi khởi động lại.

Kiểm mã chạy được trong container HA:

```bash
docker exec homeassistant python3 /config/loa_bluetooth.py ds
# ✅ {"ok": true, "loa": [...]}
```

### 5.3. Thêm tích hợp MPD

**Settings → Devices & services → Add integration → Music Player Daemon (MPD)**:
Host `127.0.0.1`, Port `6600` → có `media_player.music_player_daemon`.

### 5.4. Thẻ điều khiển

Dashboard → Edit → Add card → Manual:

```yaml
type: entities
title: Loa Bluetooth
entities:
  - entity: input_select.loa_bluetooth
  - entity: script.loa_bluetooth_quet
  - entity: script.loa_bluetooth_ket_noi
  - entity: script.loa_bluetooth_ngat
  - entity: script.loa_bluetooth_quen
  - entity: media_player.music_player_daemon
```

---

## 6. Sử dụng

1. Bật **chế độ ghép đôi** trên loa (thường giữ nút Bluetooth tới khi đèn **nháy nhanh**), để
   loa gần bộ Bluetooth. Tắt Bluetooth trên điện thoại đang nối với loa.
2. Bấm **Quét** — quét 12 giây. Danh sách có loa; kết quả hiện ở thông báo (chuông) của HA.
   Ký hiệu: `🔊` đang kết nối, `✓` đã ghép đôi.
3. **Chọn đúng tên loa** (danh sách luôn đứng ở `(chọn loa)` sau khi quét — không tự chọn
   thiết bị lạ), bấm **Kết nối**. Lần đầu tự ghép đôi và đánh dấu tin cậy (~5–15 giây); lần
   sau chỉ kết nối. Thông báo phải có `🔊 đang kết nối — <tên loa>`.
4. Phát thử — Developer Tools → Actions:
   ```yaml
   action: tts.speak
   target:
     entity_id: tts.google_translate_vi_com      # TTS của bạn
   data:
     media_player_entity_id: media_player.music_player_daemon
     message: "Xin chào, đây là loa Bluetooth."
   ```
   Nhạc / YouTube / radio: chọn `Music Player Daemon` làm loa phát như mọi loa khác.
5. **Đổi loa:** Ngắt loa cũ → chọn loa mới → Kết nối. **Quên** = xoá ghép đôi hẳn.

Loa tắt rồi bật lại: bấm **Kết nối** lại (đã ghép đôi nên không cần chế độ ghép đôi).

Chạy tay (trong máy chạy HA):

```bash
docker exec homeassistant python3 /config/loa_bluetooth.py quet 10
docker exec homeassistant python3 /config/loa_bluetooth.py noi AA:BB:CC:DD:EE:FF
docker exec homeassistant python3 /config/loa_bluetooth.py ngat AA:BB:CC:DD:EE:FF
```

---

## 7. Kiểm tra từng tầng khi không ra tiếng

Đi từ dưới lên; tầng nào ❌ thì dừng ở đó. Máy có Bluetooth = máy Debian (A) hoặc máy
Proxmox (B).

| # | Kiểm | Lệnh (chạy ở đâu) | ✅ Đúng |
|---|---|---|---|
| 1 | Loa đã kết nối | `bluetoothctl devices Connected` (máy có Bluetooth) | Thấy tên loa |
| 2 | bluez-alsa thấy loa | `bluealsa-aplay -L` (máy có Bluetooth) | Dòng `bluealsa:…DEV=<địa chỉ loa>,PROFILE=a2dp` |
| 3 | Loa kêu được | `aplay -D bluealsa /usr/share/sounds/alsa/Front_Center.wav` (máy có Bluetooth) | Loa đọc "Front center" |
| 4 | MPD chạy | `systemctl status mpd` (A: máy Debian · B: trong LXC) | `active (running)` |
| 5 | MPD mở được loa | `journalctl -u mpd -n 30` (như trên) | Không có `Failed to open` |
| 6 | HA điều khiển MPD | trạng thái `media_player.music_player_daemon` | `playing` khi phát |

## 8. Gỡ lỗi thường gặp

| Hiện tượng | Nguyên nhân / cách sửa |
|---|---|
| Quét không thấy loa | Loa chưa ở chế độ ghép đôi, hoặc đang nối với điện thoại — tắt Bluetooth điện thoại, bật lại chế độ ghép đôi |
| `org.bluez.Error.AuthenticationFailed` khi Kết nối | Bấm **Quên**, bật lại chế độ ghép đôi, Quét, Kết nối |
| MPD dừng ngay khi phát, log `PCM not found` | Chưa loa nào kết nối (tầng 1) |
| MPD: `Unknown PCM bluealsa` | Thiếu `/etc/alsa/conf.d/20-bluealsa.conf` nơi chạy MPD — cài `bluez-alsa-utils` |
| MPD: `Failed to open ALSA device "bluealsa"`, loa đã nối | A: `mpd` chưa ở nhóm `audio` (`id mpd`). B: thiếu `Environment=DBUS_SYSTEM_BUS_ADDRESS` cho MPD |
| MPD: `CURL failed … 403` | Nguồn nhạc từ chối (link hết hạn / bị chặn tạm) — phát lại |
| HA không thấy Bluetooth / `loa_bluetooth.py` báo lỗi D-Bus | `docker exec homeassistant ls /run/dbus` phải có `system_bus_socket` (xem A4/B4) |
| Nhạc giật, BLE (cảm biến) chập chờn | Một bộ Bluetooth vừa quét BLE cho HA vừa phát A2DP. Bật *Passive scanning* (Settings → Bluetooth → Configure) hoặc cắm bộ Bluetooth thứ hai riêng cho loa |
| Log hệ thống đầy dòng `bluealsa … D:` | Làm bước A2 |

## 9. Gỡ cài đặt

1. HA: xoá `packages/loa_bluetooth.yaml`, `loa_bluetooth.py`, tích hợp MPD; khởi động lại HA.
2. A: `systemctl disable --now mpd bluealsa; cp /etc/mpd.conf.goc /etc/mpd.conf` (giữ `bluez`
   nếu HA còn dùng Bluetooth).
   B: trong LXC `systemctl disable --now mpd`; trên Proxmox `systemctl disable --now bluealsa`,
   xoá dòng `lxc.mount.entry … dbus-host` trong `102.conf` (hoặc chép lại `102.conf.goc`), sửa
   compose về như cũ.
