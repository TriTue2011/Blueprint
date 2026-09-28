# 🔊 Loa Bluetooth trong Home Assistant — không cần add-on

Quét, ghép đôi, kết nối và phát ra **loa Bluetooth bất kỳ** ngay trên giao diện Home
Assistant. Chạy được với **HA Container** (Docker), kể cả khi HA nằm trong **LXC trên
Proxmox** — nơi các add-on như *Bluetooth Audio Manager* không cài được.

- Chọn loa trong danh sách, bấm **Kết nối** — đổi loa lúc nào cũng được, không sửa cấu hình.
- Phát bằng `media_player` của tích hợp **MPD** có sẵn trong HA: TTS, nhạc, automation.
- Chỉ Bluetooth "cổ điển" A2DP (loa, soundbar, tai nghe). Chiều ngược lại (điện thoại phát
  vào HA) và LE Audio không có.

## Cách nó chạy

```
Home Assistant ──D-Bus──► BlueZ (quét, ghép đôi, kết nối)
      │
      └─ media_player (MPD) ──► MPD ──► bluez-alsa ──► loa kết nối GẦN NHẤT
```

| Tệp | Đặt ở đâu | Làm gì |
|---|---|---|
| `loa_bluetooth.py` | `/config/loa_bluetooth.py` | Nói chuyện với BlueZ: quét, ghép đôi, kết nối, ngắt, quên |
| `packages/loa_bluetooth.yaml` | `/config/packages/` | Danh sách chọn loa + 4 nút (script) + `shell_command` |

## ⚠️ HA trong LXC: vì sao không chỉ passthrough USB

Nhân Linux **chỉ cho mở kết nối Bluetooth ở không gian mạng gốc của máy**. LXC có không
gian mạng riêng, nên passthrough USB Bluetooth vào LXC thì chương trình trong đó vẫn bị
từ chối (`[Errno 97] Address family not supported`) — kể cả LXC privileged, kể cả container
Docker `network_mode: host` bên trong. Kiểm trong LXC:

```bash
python3 -c "import socket; socket.socket(socket.AF_BLUETOOTH, socket.SOCK_RAW, socket.BTPROTO_HCI); print('dùng được')"
```

Cách làm: để **máy Proxmox** giữ Bluetooth (BlueZ + bluez-alsa), rồi **cho LXC mượn D-Bus**
của máy Proxmox. Mọi lệnh Bluetooth và tiếng đều đi qua D-Bus, nên HA trong LXC điều khiển
được như máy có Bluetooth thật.

HA chạy thẳng trên máy thật hay trong VM (có USB Bluetooth) thì bỏ qua bước 1–2, làm bước
3–5 trên chính máy đó (không cần `mnt/dbus-host`, dùng luôn `/run/dbus`).

## Cài đặt

Ví dụ dưới đây: HA chạy trong LXC số `102` (Debian 12), USB Bluetooth cắm vào máy Proxmox.
Thay `102` bằng số LXC của bạn (`pct list`).

### 1. Máy Proxmox: bật Bluetooth và bluez-alsa

```bash
lsusb                                      # thấy USB Bluetooth (vd TP-Link UB500)
apt install -y bluez bluez-alsa-utils
systemctl enable --now bluetooth bluealsa
bluetoothctl list                          # phải có dòng "Controller xx:xx:… [default]"
```

Chỉ phát RA loa, giữ kênh 5 giây giữa hai câu, và bỏ dòng gỡ lỗi `D:` (bản Debian in một
dòng mỗi lần thiết bị BLE hiện/mất — ~15.000 dòng/ngày). Tạo
`/etc/systemd/system/bluealsa.service.d/loa.conf`:

```ini
[Service]
ExecStart=
ExecStart=/bin/sh -c "/usr/bin/bluealsa --keep-alive=5 -p a2dp-source 2>&1 | grep --line-buffered -v ': D: '"
```

rồi `systemctl daemon-reload && systemctl restart bluealsa`.

Không thấy Controller: `dmesg | grep -i bluetooth` — thường thiếu firmware (chip Realtek
cần tệp trong `/lib/firmware/rtl_bt/`, Proxmox thường có sẵn).

### 2. Máy Proxmox: cho LXC mượn D-Bus

Thêm vào cuối `/etc/pve/lxc/102.conf`:

```
lxc.mount.entry: /run/dbus mnt/dbus-host none bind,create=dir 0 0
```

Gắn vào **`/mnt`**, không phải `/run`: systemd trong LXC phủ một `/run` mới lên lúc khởi
động, che mất chỗ gắn. Rồi `pct reboot 102` và kiểm:

```bash
pct exec 102 -- ls /mnt/dbus-host          # phải thấy system_bus_socket
```

LXC **privileged** (`unprivileged: 0`) chạy ngay. LXC unprivileged thì root trong LXC không
phải root máy Proxmox, D-Bus có thể từ chối — cần thêm chính sách D-Bus trên máy Proxmox
hoặc đổi sang privileged.

### 3. Compose của Home Assistant

Đổi volume D-Bus sang D-Bus mượn (các dòng khác giữ nguyên):

```yaml
services:
  homeassistant:
    network_mode: host
    volumes:
      - /mnt/dbus-host:/run/dbus:ro      # thay cho /run/dbus:/run/dbus:ro
```

Dựng lại container HA. Tích hợp **Bluetooth** của HA sẽ tự nhận USB Bluetooth.

### 4. MPD trong LXC (trình phát cho HA điều khiển)

```bash
apt install -y --no-install-recommends mpd libasound2-plugin-bluez bluez-alsa-utils bluez
# KHÔNG chạy BlueZ / bluealsa trong LXC — dùng của máy Proxmox. bluez-alsa-utils cài chỉ để
# có /etc/alsa/conf.d/20-bluealsa.conf: thiếu tệp này MPD báo "Unknown PCM bluealsa".
systemctl mask bluetooth bluealsa
```

`/etc/mpd.conf` (sao lưu bản gốc trước):

```
music_directory     "/var/lib/mpd/music"
playlist_directory  "/var/lib/mpd/playlists"
db_file             "/var/lib/mpd/tag_cache"
state_file          "/var/lib/mpd/state"
sticker_file        "/var/lib/mpd/sticker.sql"
user                "root"
bind_to_address     "127.0.0.1"
port                "6600"
audio_output {
    type        "alsa"
    name        "Loa Bluetooth"
    device      "bluealsa"          # không ghi DEV = loa kết nối GẦN NHẤT
    mixer_type  "software"
}
```

Cho MPD dùng D-Bus mượn rồi bật:

```bash
mkdir -p /etc/systemd/system/mpd.service.d
printf '[Service]\nEnvironment=DBUS_SYSTEM_BUS_ADDRESS=unix:path=/mnt/dbus-host/system_bus_socket\n' \
  > /etc/systemd/system/mpd.service.d/bluetooth.conf
systemctl daemon-reload
systemctl disable --now mpd.socket
systemctl enable --now mpd
```

`user "root"` và cổng chỉ nghe `127.0.0.1` là có chủ ý: bluez-alsa trên máy Proxmox chỉ cho
root (hoặc nhóm `audio` của máy Proxmox) dùng; HA dùng mạng của máy nên vẫn tới được MPD.

(Tuỳ chọn) dùng `bluetoothctl` ngay trong LXC — tạo `/usr/local/bin/bluetoothctl`:

```sh
#!/bin/sh
DBUS_SYSTEM_BUS_ADDRESS=unix:path=/mnt/dbus-host/system_bus_socket exec /usr/bin/bluetoothctl "$@"
```

### 5. Home Assistant

1. Chép `loa_bluetooth.py` vào `/config/` và `packages/loa_bluetooth.yaml` vào
   `/config/packages/`. `configuration.yaml` phải có:
   ```yaml
   homeassistant:
     packages: !include_dir_named packages
   ```
2. **Developer Tools → YAML → Check configuration**, rồi **khởi động lại HA** (`shell_command`
   mới chỉ nạp khi khởi động).
3. **Settings → Devices & services → Add integration → Music Player Daemon (MPD)**:
   máy `127.0.0.1`, cổng `6600` → có `media_player.music_player_daemon`.

## Sử dụng

Thẻ điều khiển — thêm vào dashboard (Edit → Add card → Manual):

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

1. Bật chế độ ghép đôi trên loa (giữ nút Bluetooth tới khi đèn nháy nhanh), để gần USB
   Bluetooth.
2. Bấm **Quét** (12 giây) → danh sách có loa. Ký hiệu: `🔊` đang kết nối, `✓` đã ghép đôi.
3. Chọn loa → **Kết nối** (lần đầu tự ghép đôi và đánh dấu tin cậy; lần sau chỉ kết nối).
4. Phát thử — Developer Tools → Actions:
   ```yaml
   action: tts.speak
   target:
     entity_id: tts.google_translate_vi_com      # TTS của bạn
   data:
     media_player_entity_id: media_player.music_player_daemon
     message: "Xin chào, đây là loa Bluetooth."
   ```
5. Đổi loa: **Ngắt** loa cũ, chọn loa mới, **Kết nối**. Không dùng nữa thì **Quên**.

Kết quả mỗi lần bấm hiện ở thông báo (chuông) của HA. Chạy tay trong container HA:

```bash
docker exec homeassistant python3 /config/loa_bluetooth.py quet 10
docker exec homeassistant python3 /config/loa_bluetooth.py noi AA:BB:CC:DD:EE:FF
```

## Gỡ lỗi

| Hiện tượng | Kiểm |
|---|---|
| Quét không thấy loa | Loa chưa ở chế độ ghép đôi, hoặc đang nối với điện thoại — tắt Bluetooth điện thoại |
| `org.bluez.Error.AuthenticationFailed` khi Kết nối | Bấm **Quên**, bật lại chế độ ghép đôi, Quét, Kết nối |
| Kết nối được mà MPD không ra tiếng | Máy Proxmox: `systemctl status bluealsa`; `bluealsa-aplay -L` phải liệt kê loa |
| MPD: `Unknown PCM bluealsa` | Thiếu `/etc/alsa/conf.d/20-bluealsa.conf` trong LXC — cài `bluez-alsa-utils` (bước 4) |
| MPD báo lỗi mở thiết bị ALSA | Chưa loa nào kết nối; hoặc thiếu `Environment=DBUS_SYSTEM_BUS_ADDRESS` cho MPD |
| HA không thấy Bluetooth | `docker exec homeassistant ls /run/dbus` phải có `system_bus_socket` của máy Proxmox |
