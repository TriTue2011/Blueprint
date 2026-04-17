# 🏠 Home Assistant Blueprints - TriTue2011

Bộ sưu tập **Home Assistant Blueprints** tích hợp AI (LLM) để tự động hóa nhà thông minh. Các blueprint được tối ưu cho **Gemini 2.5 Flash** — các mô hình khác có thể cần điều chỉnh nhỏ.

**[English version click here](/README.en.md)**

---

## 📑 Mục lục

- [Yêu cầu chung](#-yêu-cầu-chung)
- **Tạo ảnh AI**
  - [Tạo ảnh AI](#️-tạo-ảnh-ai)
  - [Tạo ảnh AI kèm ảnh tham chiếu](#️-tạo-ảnh-ai-kèm-ảnh-tham-chiếu)
  - [Tạo ảnh thời tiết bằng AI](#️-tạo-ảnh-thời-tiết-bằng-ai)
  - [Tạo ảnh danh lam thắng cảnh](#-tạo-ảnh-danh-lam-thắng-cảnh)
- **Camera & Giám sát**
  - [Kiểm tra camera bằng AI (Voice)](#-kiểm-tra-camera-bằng-ai-voice)
  - [Chụp ảnh camera (Voice)](#-chụp-ảnh-camera-voice)
  - [Phân tích file / ảnh (LLM)](#-phân-tích-file--ảnh-llm)
  - [Cảnh báo người qua camera bằng AI](#-cảnh-báo-người-qua-camera-bằng-ai)
  - [LLM Vision Camera](#️-llm-vision-camera)
- **Gửi tin nhắn**
  - [Gửi Telegram (Voice + xóa file)](#-gửi-telegram-voice--xóa-file)
  - [Gửi Zalo Bot chính thức (Voice)](#-gửi-zalo-bot-chính-thức-voice)
  - [Gửi Zalo Custom Bot (Voice + xóa file)](#-gửi-zalo-custom-bot-voice--xóa-file)
- **Tiện ích**
  - [Thông báo lịch âm & thời tiết](#️-thông-báo-lịch-âm--thời-tiết)
  - [Danh ngôn tự động hàng ngày](#-danh-ngôn-tự-động-hàng-ngày)
  - [Kiểm tra thiết bị (Multi-Entity)](#-kiểm-tra-thiết-bị-multi-entity)
- **Quản lý & Cập nhật**
  - [Tự động cập nhật Blueprints](#-tự-động-cập-nhật-blueprints)
  - [Tự động cập nhật Pyscript](#-tự-động-cập-nhật-pyscript)
- **Hướng dẫn nâng cao**
  - [Tạo Sensor trong configuration.yaml](#-tạo-sensor-trong-configurationyaml)
  - [Tạo Shell Command](#-tạo-shell-command)
  - [Tạo Input Helper](#-tạo-input-helper)
  - [Cài đặt Scripts (Shell)](#-cài-đặt-scripts-shell)
  - [Cấu hình Cloudflare Tunnel](#-cấu-hình-cloudflare-tunnel)

---

## ⚙️ Yêu cầu chung

| Yêu cầu | Chi tiết |
|----------|----------|
| **Home Assistant** | Phiên bản tối thiểu tùy blueprint (2024.10.0 – 2025.8.0) |
| **AI Model** | Khuyến nghị **Gemini 2.5 Flash** (hỗ trợ tạo ảnh & phân tích) |
| **AI Task Entity** | Cần tạo và cấu hình trong **Settings → General** (cho các blueprint tạo ảnh/phân tích) |
| **Voice Assistant** | Tùy chọn — cần cho các blueprint điều khiển bằng giọng nói |

> **Lưu ý quan trọng:** Sau khi tạo script từ blueprint, hãy **expose script cho Assist** để có thể điều khiển bằng giọng nói. Không thay đổi tên script mặc định.

---

## 🖼️ Tạo ảnh AI

Tạo ảnh theo prompt bằng mô hình AI. Chỉ cần nói hoặc nhập mô tả, hệ thống sẽ tự sinh ảnh và lưu về Home Assistant.

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Script |
| **HA tối thiểu** | 2025.8.0 |
| **Yêu cầu** | AI Task Entity hỗ trợ tạo ảnh |

**Cấu hình:**
- **AI Task Entity:** Chọn entity AI Task hỗ trợ tạo ảnh (để trống = dùng mặc định hệ thống)
- **Output Directory:** Thư mục lưu ảnh (mặc định: `/media`)
- **Filename Prefix:** Tiền tố tên file (mặc định: `ai_generated_`)

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fai_image_generator_full_llm.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 🖼️ Tạo ảnh AI kèm ảnh tham chiếu

Tạo ảnh AI với ảnh tham chiếu đính kèm (kính, trang phục, phụ kiện). Hỗ trợ nhớ ngữ cảnh và xử lý lỗi tốt hơn.

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Automation |
| **HA tối thiểu** | 2024.10.0 |
| **Yêu cầu** | Input Text Helper |

**Yêu cầu thiết lập trước — tạo Input Text Helper:**

```
Vào Settings → Devices & Services → Helpers
Nhấn "+ Create Helper" → Chọn "Text"
Đặt tên phù hợp, max length 255
Lưu lại
```

> Xem thêm: [Hướng dẫn tạo Input Helper](#-tạo-input-helper)

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fai_image_attrack.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 🌤️ Tạo ảnh thời tiết bằng AI

Tự động tạo ảnh phù hợp với thời tiết hiện tại theo buổi trong ngày (sáng, trưa, chiều, tối, đêm).

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Automation |
| **HA tối thiểu** | 2024.10.0 |
| **Yêu cầu** | Shell Command + Template Sensor |

**Yêu cầu thiết lập trước** — thêm vào `configuration.yaml`:

**1. Tạo Shell Command** để di chuyển file ảnh:

```yaml
shell_command:
  copy_weather_image: >
    mv "{{ source }}" "{{ destination }}"
```
hoặc dùng api nvidia
trong configuration.yaml
```yaml
pyscript:
  allow_all_imports: true
  hass_is_global: true
  nvidia_api_key: !secret nvidia_api_key
 ```
 trong secrets.yaml
```yaml
nvidia_api_key: "nvapi-xxx"
```
tải file https://github.com/TriTue2011/Blueprint/blob/main/scripts/weather_image.py cho vào folder pyscript. các cài pyscript https://github.com/custom-components/pyscript
**2. Tạo Template Sensor** nhận diện buổi trong ngày:

```yaml
template:
  - sensor:
      - name: "Buổi trong ngày"
        unique_id: time_of_day_vn
        icon: >-
          {% set h = now().hour %}
          {% if 6 <= h < 11 %} mdi:weather-sunny
          {% elif 11 <= h < 13 %} mdi:white-balance-sunny
          {% elif 13 <= h < 18 %} mdi:weather-sunset
          {% elif 18 <= h < 21 %} mdi:weather-night
          {% else %} mdi:weather-night
          {% endif %}
        state: >-
          {% set h = now().hour %}
          {% if 6 <= h < 11 %} Sáng
          {% elif 11 <= h < 13 %} Trưa
          {% elif 13 <= h < 18 %} Chiều
          {% elif 18 <= h < 21 %} Tối
          {% else %} Đêm
          {% endif %}
        attributes:
          hour: "{{ now().hour }}"
          is_night: >-
            {% set h = now().hour %}
            {{ h < 6 or h >= 21 }}
          is_daytime: >-
            {% set h = now().hour %}
            {{ h >= 6 and h < 18 }}
          period_english: >-
            {% set h = now().hour %}
            {% if 6 <= h < 11 %} Morning
            {% elif 11 <= h < 13 %} Noon
            {% elif 13 <= h < 18 %} Afternoon
            {% elif 18 <= h < 21 %} Evening
            {% else %} Night
            {% endif %}
```

> Xem thêm: [Hướng dẫn tạo Sensor](#-tạo-sensor-trong-configurationyaml) | [Hướng dẫn tạo Shell Command](#-tạo-shell-command)

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fai_creat_image_weather.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 🌍 Tạo ảnh danh lam thắng cảnh

Tự động tạo ảnh các danh lam thắng cảnh, công trình nổi tiếng trên thế giới bằng AI theo lịch trình hoặc khi được yêu cầu.

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Automation |
| **HA tối thiểu** | 2024.10.0 |

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fworld_landmarks_image_generator.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 📸 Kiểm tra camera bằng AI (Voice)

Dùng giọng nói để yêu cầu AI phân tích camera — phát hiện người, thú cưng, phương tiện. Hỗ trợ khớp tên chính xác, tìm theo alias, hoặc kiểm tra tất cả camera cùng lúc.

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Script |
| **HA tối thiểu** | 2025.8.0 |
| **Yêu cầu** | AI Task Entity, Camera entities |

**Tính năng:**
- Ưu tiên tìm camera theo `friendly_name` chính xác
- Hỗ trợ tìm theo alias (template sensor)
- Nếu không tìm thấy → kiểm tra tất cả camera (multi-mode)
- Hỗ trợ chế độ Parallel (nhanh) hoặc Sequential

**Cấu hình:**
- **Entity Aliases:** Sensor alias để ánh xạ tên camera
- **AI Task Entity:** Chọn entity AI Task (để trống = mặc định)
- **Multi-Camera Check Mode:** Parallel (nhanh) hoặc Sequential

**Ví dụ lệnh giọng nói:**
- "Kiểm tra cửa trước có ai không?"
- "Camera sân có con chó không?"

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fvoice_camera_ai_analyzer.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 📷 Chụp ảnh camera (Voice)

Dùng giọng nói để ra lệnh chụp ảnh từ camera và lưu thành file. Dùng kết hợp với blueprint phân tích ảnh.

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Script |
| **HA tối thiểu** | 2025.8.0 |

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fcamera_snapshot_full_llm.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 🔍 Phân tích file / ảnh (LLM)

Gửi ảnh hoặc file cho mô hình ngôn ngữ lớn (LLM) để phân tích nội dung và nhận câu trả lời thông minh.

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Script |
| **HA tối thiểu** | 2025.8.0 |
| **Yêu cầu** | AI Task Entity |

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Ffile_content_analyzer_full_llm.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 🚨 Cảnh báo người qua camera bằng AI

Tự động phân tích sự kiện camera bằng AI Task khi phát hiện có người đi qua vùng giám sát. Gửi thông báo kèm ảnh và phân tích AI qua điện thoại, Telegram, Zalo và TTS ra loa.

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Automation |
| **HA tối thiểu** | 2025.7.0 |
| **Yêu cầu** | Binary sensor (trigger), Camera entity |

**Cấu hình:**
- **Trigger Sensor:** Cảm biến kích hoạt (cửa, motion sensor) — domain: `binary_sensor`
- **Trigger States:** Chọn trạng thái from/to (mặc định: off → on)
- **Person Occupancy Sensor:** (Tùy chọn) Đợi phát hiện người trước khi phân tích
- **Maximum Wait Time:** Thời gian tối đa đợi phát hiện người (0 = không giới hạn)

**Kênh thông báo hỗ trợ:**
- Mobile App (điện thoại)
- Telegram
- Zalo Bot / Zalo Custom Bot
- TTS (phát qua loa)

**Gemini**
[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Falarm_person_camera.yaml)

**Open ai**
[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Falarm_person_camera_2.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 👁️ LLM Vision Camera

Tóm tắt sự kiện cửa ra vào bằng AI với phát hiện người. Hỗ trợ gửi thông báo qua điện thoại, Zalo và phân tích camera khi cửa mở.

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Automation |
| **HA tối thiểu** | 2024.10.0 |
| **Yêu cầu** | Door Contact Sensor, Person Occupancy Sensor, Camera |

**Cấu hình:**
- **Door Contact Sensor:** Cảm biến cửa (`binary_sensor`)
- **Door States:** Trạng thái from/to (mặc định: off → on)
- **Person Occupancy Sensor:** Cảm biến phát hiện người
- **Wait for Person Detection:** Có đợi phát hiện người hay không
- **Person Detection Wait Time:** Thời gian tối đa chờ

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fllmvison_camera.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 📩 Gửi Telegram (Voice + xóa file)

Gửi tin nhắn, ảnh hoặc file qua Telegram bằng giọng nói. Hỗ trợ tự động xóa file sau khi gửi.

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Automation |
| **HA tối thiểu** | 2024.10.0 |
| **Yêu cầu** | Telegram Bot integration |

**Ví dụ lệnh giọng nói:**
- "Gửi ảnh camera sân vào Telegram"
- "Gửi thông báo nhiệt độ phòng khách lên Telegram"

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fsend_to_telegram_full_llm.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 💬 Gửi Zalo Bot chính thức (Voice)

Gửi tin nhắn đến Zalo qua bot chính thức bằng giọng nói. Địa điểm tự động được kèm link Google Maps.

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Automation |
| **HA tối thiểu** | 2024.10.0 |
| **Yêu cầu** | Zalo Bot integration (HACS) |

**Ví dụ lệnh giọng nói:**
- "Tìm nhà hàng ngon ở Hà Nội và gửi lên Zalo"
- "Gửi địa chỉ Văn Miếu lên Zalo"

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fsend_to_zalo_bot_full_llm.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 🧩 Gửi Zalo Custom Bot (Voice + xóa file)

Gửi tin nhắn, ảnh, video qua Zalo Custom Bot. Hỗ trợ webhook, đồng bộ trạng thái và xóa file sau khi gửi.

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Script |
| **HA tối thiểu** | 2024.10.0 |
| **Yêu cầu** | Zalo Bot integration (HACS) + [delete-file-home-assistant](https://github.com/chomupashchuk/delete-file-home-assistant) |

**Cấu hình Zalo:**
- **Account:** Số điện thoại tài khoản Zalo
- **Thread ID:** ID cuộc hội thoại
- **Type of Receiver:** User (0) hoặc Group (1)
- **TTL:** Thời gian tự hủy tin nhắn (ms), 0 = không tự hủy
- **Delete After Send:** Tự động xóa file ảnh sau khi gửi

**Ví dụ lệnh giọng nói:**
- "Gửi ảnh camera sân cho nhóm gia đình qua Zalo"
- "Gửi địa chỉ Hồ Tây cho vợ qua Zalo"

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fsend_to_zalo_custom_bot_full_llm.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 🗓️ Thông báo lịch âm & thời tiết

Tự động nhắc nhở các sự kiện âm lịch kèm theo thông tin thời tiết hàng ngày. AI biên tập tin nhắn tự nhiên, sáng tạo mỗi ngày một kiểu khác nhau.

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Automation |
| **HA tối thiểu** | 2024.10.0 |

**Tính năng:**
- Bật/tắt riêng cho Lịch Âm và Thời Tiết
- AI biên tập tin nhắn và TTS tự nhiên
- Khi có sự kiện lịch: kết hợp cả lịch + thời tiết
- Khi không có sự kiện: chỉ thông báo thời tiết

**Cấu hình:**
- **Nhắc trước bao nhiêu ngày:** Danh sách ngày, ví dụ `[15, 7, 5, 3, 1]`
- **Thời điểm thông báo:** Danh sách giờ, ví dụ `["08:00:00", "20:00:00"]`
- **Loại sự kiện:** Tất cả / Chỉ ngày giỗ / Mồng 1 & Rằm / Tùy chỉnh sensors

**Kênh thông báo hỗ trợ:**
- Mobile App
- Telegram
- Zalo Bot / Zalo Custom Bot
- TTS (phát qua loa)

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fcalendar_weather_notification.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 💬 Danh ngôn tự động hàng ngày

Tự động lấy câu danh ngôn, châm ngôn, ca dao, tục ngữ ngẫu nhiên từ AI và cập nhật vào `input_text`.

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Automation |
| **HA tối thiểu** | 2025.7.0 |
| **Yêu cầu** | Input Text Helper |

**Tính năng:**
- Lấy quote theo khoảng thời gian tùy chỉnh (15 phút → mỗi ngày)
- Đa dạng nguồn: danh ngôn quốc tế, ca dao, tục ngữ Việt Nam
- AI chọn ngẫu nhiên, tránh lặp lại

**Cấu hình:**
- **Khoảng thời gian cập nhật:** Mỗi 15 phút, 30 phút, 1 giờ, ..., mỗi ngày
- **Input Text Helper:** Entity `input_text` để lưu quote (giới hạn 255 ký tự)
- **Loại quote:** Danh ngôn quốc tế, ca dao Việt Nam, tục ngữ Việt Nam (chọn nhiều)

> **Yêu cầu tạo trước:** Input Text Helper — xem [hướng dẫn tạo Input Helper](#-tạo-input-helper)

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fdaily_quote.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 🔧 Kiểm tra thiết bị (Multi-Entity)

Phân biệt 3 nguồn điều khiển thiết bị: **Tay vật lý** (manual) / **App** / **Automation** (auto). Hỗ trợ nhiều entity trong 1 automation.

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Automation |
| **HA tối thiểu** | 2024.10.0 |
| **Yêu cầu** | Input Select Helper cho mỗi entity |

**Cách hoạt động:**
- Theo dõi các entity `switch` và `light`
- Phân tích `context` của trigger để xác định nguồn:
  - `parent_id` có giá trị → **auto** (từ automation)
  - `user_id` có giá trị → **app** (từ ứng dụng)
  - Còn lại → **manual** (bật/tắt vật lý)
- Cập nhật kết quả vào `input_select`

**Quy ước đặt tên Input Select:**

```
input_select.source_<entity_object_id>
```

Ví dụ: Entity `switch.den_phong_khach` → tạo `input_select.source_den_phong_khach`

**Tạo Input Select Helper:**

```
Vào Settings → Devices & Services → Helpers
Nhấn "+ Create Helper" → Chọn "Dropdown"
Đặt tên: source_<tên_thiết_bị>
Options: manual, app, auto
Lưu lại
```

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fcheck_device.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 🔄 Tự động cập nhật Blueprints

Quản lý việc kiểm tra và cập nhật blueprints tự động, với thông báo qua Zalo khi có phiên bản mới.

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Automation |
| **HA tối thiểu** | 2024.10.0 |
| **Yêu cầu** | Shell script `blueprints_update.sh` |

**Chế độ cập nhật:**

| Chế độ | Mô tả |
|--------|-------|
| **Check** | Chỉ kiểm tra, không cập nhật |
| **Update All** | Cập nhật tất cả blueprints |
| **Update Self** | Chỉ cập nhật blueprint này |
| **Update Specific** | Cập nhật 1 blueprint cụ thể theo đường dẫn |
| **Update Multiple** | Cập nhật nhiều blueprints (mỗi dòng 1 đường dẫn) |

**Cấu hình:**
- **Lịch tự động:** Bật/tắt kiểm tra định kỳ
- **Giờ kiểm tra:** 0–23 (mặc định: 3h sáng)
- **Reload sau cập nhật:** Tự động reload automations và scripts
- **Thông báo:** Hỗ trợ Zalo khi có cập nhật mới

> **Cài đặt script:** Xem [hướng dẫn cài đặt Scripts](#-cài-đặt-scripts-shell)

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2FBlueprints_update_manager.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 🐍 Tự động cập nhật Pyscript

Tự động đồng bộ file / thư mục từ GitHub về `/config/pyscript`, giữ script luôn ở phiên bản mới nhất.

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Automation |
| **HA tối thiểu** | 2024.10.0 |
| **Yêu cầu** | Shell script `pyscript_sync_from_urls.sh` + manifest file |

**Chế độ hoạt động:**

| Chế độ | Mô tả |
|--------|-------|
| **Dùng .conf** | Tôn trọng cấu hình trong file `.conf` |
| **Ép kiểm tra** | Chỉ check, không ghi file |
| **Ép cập nhật** | Ghi file dù `.conf` đặt `auto_update=false` |

**Cấu hình:**
- **Lịch tự động:** Bật/tắt chạy định kỳ
- **Giờ chạy:** 0–23 (mặc định: 3h sáng)
- **Reload pyscript sau cập nhật:** Tự động hoặc thủ công
- **Thông báo Mobile:** Gửi kết quả đến thiết bị mobile

> **Cài đặt script:** Xem [hướng dẫn cài đặt Scripts](#-cài-đặt-scripts-shell)

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2FBlueprint_pyscript_update_manager.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

# 📖 Hướng dẫn nâng cao

## 📐 Tạo Sensor trong configuration.yaml

Một số blueprint yêu cầu tạo template sensor. Đây là hướng dẫn chi tiết.

### Cách thêm sensor

Mở file `configuration.yaml` (thường ở `/config/configuration.yaml`) và thêm phần `template:` nếu chưa có:

```yaml
template:
  - sensor:
      - name: "Tên Sensor"
        unique_id: ten_sensor_unique
        state: >-
          # Template Jinja2 ở đây
          {{ states('sensor.xxx') }}
```

### Ví dụ: Sensor "Buổi trong ngày" (bắt buộc cho blueprint Thời Tiết)

```yaml
template:
  - sensor:
      - name: "Buổi trong ngày"
        unique_id: time_of_day_vn
        icon: >-
          {% set h = now().hour %}
          {% if 6 <= h < 11 %} mdi:weather-sunny
          {% elif 11 <= h < 13 %} mdi:white-balance-sunny
          {% elif 13 <= h < 18 %} mdi:weather-sunset
          {% elif 18 <= h < 21 %} mdi:weather-night
          {% else %} mdi:weather-night
          {% endif %}
        state: >-
          {% set h = now().hour %}
          {% if 6 <= h < 11 %} Sáng
          {% elif 11 <= h < 13 %} Trưa
          {% elif 13 <= h < 18 %} Chiều
          {% elif 18 <= h < 21 %} Tối
          {% else %} Đêm
          {% endif %}
        attributes:
          hour: "{{ now().hour }}"
          is_night: >-
            {% set h = now().hour %}
            {{ h < 6 or h >= 21 }}
          is_daytime: >-
            {% set h = now().hour %}
            {{ h >= 6 and h < 18 }}
          period_english: >-
            {% set h = now().hour %}
            {% if 6 <= h < 11 %} Morning
            {% elif 11 <= h < 13 %} Noon
            {% elif 13 <= h < 18 %} Afternoon
            {% elif 18 <= h < 21 %} Evening
            {% else %} Night
            {% endif %}
```

### Áp dụng thay đổi

Sau khi thêm sensor, bạn cần reload:

1. Vào **Developer Tools → YAML → RELOAD TEMPLATE ENTITIES**
2. Hoặc khởi động lại Home Assistant

---

## 🐚 Tạo Shell Command

Shell Command cho phép Home Assistant chạy lệnh hệ thống. Một số blueprint cần shell command để thao tác file.

### Cách thêm Shell Command

Thêm vào `configuration.yaml`:

```yaml
shell_command:
  ten_lenh: "lệnh shell ở đây"
```

### Ví dụ: Lệnh di chuyển file ảnh (bắt buộc cho blueprint Thời Tiết)

```yaml
shell_command:
  copy_weather_image: >
    mv "{{ source }}" "{{ destination }}"
```

### Áp dụng thay đổi

1. Vào **Developer Tools → YAML → RELOAD SHELL COMMANDS**
2. Hoặc khởi động lại Home Assistant

---

## 📝 Tạo Input Helper

Nhiều blueprint yêu cầu Input Helper (Text, Select, Number...) để lưu trữ trạng thái.

### Tạo Input Text Helper (cho blueprint Tạo ảnh AI tham chiếu, Danh ngôn)

```
1. Vào Settings → Devices & Services → Helpers
2. Nhấn "+ Create Helper"
3. Chọn "Text"
4. Đặt tên phù hợp (ví dụ: "AI Reference Image", "Daily Quote")
5. Đặt Max Length: 255
6. Lưu lại
```

### Tạo Input Select Helper (cho blueprint Kiểm tra thiết bị)

```
1. Vào Settings → Devices & Services → Helpers
2. Nhấn "+ Create Helper"
3. Chọn "Dropdown"
4. Đặt tên: source_<tên_entity> (ví dụ: source_den_phong_khach)
5. Thêm Options: manual, app, auto
6. Lưu lại
```

> **Lưu ý:** Tên Input Select phải tuân theo quy ước `source_<entity_object_id>` để blueprint Kiểm tra thiết bị hoạt động đúng.

---

## 🛠️ Cài đặt Scripts (Shell)

Thư mục `scripts/` chứa các shell script hỗ trợ cập nhật tự động. Cần copy vào Home Assistant.

### 1. Script cập nhật Blueprints (`blueprints_update.sh`)

**Phiên bản:** 1.0.3-docker

**Cài đặt:**

```bash
# Copy script và config vào Home Assistant
mkdir -p /config/scripts
cp blueprints_update.sh /config/scripts/
cp blueprints_update.sh.conf /config/scripts/
chmod +x /config/scripts/blueprints_update.sh
```

**Cấu hình** (`blueprints_update.sh.conf`):

```bash
_blueprints_update_auto_update="false"         # false = chỉ kiểm tra
_blueprints_update_curl_options="--silent"
```

> **Lưu ý:** Script này **KHÔNG cần** cấu hình server HA hay Long-lived access token. Script chỉ tải file từ GitHub và ghi đè local. Việc reload automations/scripts được blueprint automation xử lý qua HA internal actions (`automation.reload`, `script.reload`).

**Sử dụng:**

```bash
# Chỉ kiểm tra
bash /config/scripts/blueprints_update.sh

# Kiểm tra và cập nhật
bash /config/scripts/blueprints_update.sh --update

# Chế độ debug
bash /config/scripts/blueprints_update.sh --debug
```

**Cách hoạt động:**
1. Quét tất cả file `.yaml` trong `/config/blueprints/`
2. Đọc `source_url` từ mỗi blueprint
3. Chuyển đổi GitHub URL → raw URL
4. So sánh phiên bản local vs remote
5. Cập nhật nếu có thay đổi (khi dùng `--update`)

---

### 2. Script đồng bộ Pyscript (`pyscript_sync_from_urls.sh`)

**Phiên bản:** 1.4.0

**Cài đặt:**

```bash
# Copy script và config vào Home Assistant
mkdir -p /config/scripts
cp pyscript_sync_from_urls.sh /config/scripts/
cp pyscript_sync.conf /config/scripts/
chmod +x /config/scripts/pyscript_sync_from_urls.sh
```

**Cấu hình** (`pyscript_sync.conf`):

```bash
_pyscript_sync_dir="/config/pyscript"                         # Thư mục pyscript
_pyscript_sync_manifest="${_pyscript_sync_dir}/_sources.txt"  # File manifest
_pyscript_sync_auto_update="false"                            # false = chỉ check
_pyscript_sync_token=""                                       # Token GitHub (trống = public repo)
_pyscript_sync_reload="true"                                  # Tự động reload pyscript
_pyscript_sync_curl_options="--silent"
_pyscript_sync_debug="false"
```

> **Lưu ý:** Script này **KHÔNG cần** server HA hay Long-lived access token. Chỉ cần GitHub token nếu repo là private. Reload pyscript được thực hiện qua lệnh `ha` CLI local.

**Tạo file manifest** (`/config/pyscript/_sources.txt`):

```bash
# Format: url|destination[|option]
# File đơn lẻ:
https://github.com/user/repo/blob/main/script.py|script.py

# Thư mục (không đệ quy):
https://github.com/user/repo/tree/main/folder|folder/

# Thư mục (đệ quy):
https://github.com/user/repo/tree/main/folder|folder/|recursive
```

**Sử dụng:**

```bash
# Chỉ kiểm tra
bash /config/scripts/pyscript_sync_from_urls.sh

# Kiểm tra và cập nhật
bash /config/scripts/pyscript_sync_from_urls.sh --update

# Dùng GitHub token (cho private repo)
bash /config/scripts/pyscript_sync_from_urls.sh --update --token ghp_xxx

# Chế độ debug
bash /config/scripts/pyscript_sync_from_urls.sh --debug

# Không reload pyscript sau cập nhật
bash /config/scripts/pyscript_sync_from_urls.sh --update --no-reload
```

**Tính năng:**
- Hỗ trợ cả file đơn lẻ và thư mục GitHub
- Tự động phát hiện loại URL (file / folder)
- Chuyển đổi GitHub URL → raw / API URL
- Hỗ trợ GitHub token cho private repo
- Đồng bộ đệ quy thư mục con
- Tự động reload pyscript sau cập nhật
- Parse JSON bằng `jq` hoặc `python3`

**Yêu cầu hệ thống:**
- `bash`, `curl`
- `jq` hoặc `python3` (để parse JSON từ GitHub API)
- Trên HA OS: `apk add jq`

---

## 🔒 Cấu hình Cloudflare Tunnel

Nếu bạn sử dụng Cloudflare Tunnel để truy cập Home Assistant từ bên ngoài, cần cho phép các domain sau trong tường lửa / allowlist:

```
cfargotunnel.com
cloudflare.com
cloudflared.com
workers.dev
trycloudflare.com
argotunnel.com
cloudflareaccess.com
cfipaddress.com
update.argotunnel.com
update.cloudflareclient.com
```

---

## 📊 Tổng quan Blueprints

| # | Blueprint | Loại | HA Min | Tính năng chính |
|---|-----------|------|--------|-----------------|
| 1 | Tạo ảnh AI | Script | 2025.8.0 | Tạo ảnh từ prompt văn bản |
| 2 | Tạo ảnh AI + tham chiếu | Automation | 2024.10.0 | Tạo ảnh kèm ảnh mẫu |
| 3 | Tạo ảnh thời tiết | Automation | 2024.10.0 | Ảnh AI theo thời tiết/buổi |
| 4 | Danh lam thắng cảnh | Automation | 2024.10.0 | Ảnh AI danh lam thế giới |
| 5 | Camera AI (Voice) | Script | 2025.8.0 | Phân tích camera bằng giọng nói |
| 6 | Chụp camera (Voice) | Script | 2025.8.0 | Chụp ảnh camera bằng giọng nói |
| 7 | Phân tích file/ảnh | Script | 2025.8.0 | Gửi file cho LLM phân tích |
| 8 | Cảnh báo người camera | Automation | 2025.7.0 | Phát hiện người + cảnh báo |
| 9 | LLM Vision Camera | Automation | 2024.10.0 | Phân tích camera real-time |
| 10 | Gửi Telegram | Automation | 2024.10.0 | Gửi tin/ảnh qua Telegram |
| 11 | Gửi Zalo Bot | Automation | 2024.10.0 | Gửi tin qua Zalo chính thức |
| 12 | Gửi Zalo Custom | Script | 2024.10.0 | Gửi tin/ảnh qua Zalo Custom |
| 13 | Lịch âm & thời tiết | Automation | 2024.10.0 | Nhắc lịch âm + thời tiết |
| 14 | Danh ngôn hàng ngày | Automation | 2025.7.0 | Quote AI tự động |
| 15 | Kiểm tra thiết bị | Automation | 2024.10.0 | Phân biệt nguồn điều khiển |
| 16 | Cập nhật Blueprints | Automation | 2024.10.0 | Auto-update blueprints |
| 17 | Cập nhật Pyscript | Automation | 2024.10.0 | Auto-sync pyscript từ GitHub |

---

**Nếu bạn thấy các blueprint này hữu ích, hãy chia sẻ cho cộng đồng Home Assistant và theo dõi để cập nhật thêm nhiều blueprint mới!**
