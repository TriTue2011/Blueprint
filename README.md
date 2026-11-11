# 🏠 Home Assistant Blueprints - TriTue2011

Bộ sưu tập **Home Assistant Blueprints** tích hợp AI (LLM) để tự động hóa nhà thông minh. Các blueprint được tối ưu cho **Gemini 2.5 Flash** — các mô hình khác có thể cần điều chỉnh nhỏ.

**[English version click here](/README.en.md)**

---

## 📑 Mục lục

- [Yêu cầu chung](#️-yêu-cầu-chung)
- **Tạo ảnh AI**
  - [Tạo ảnh AI](#️-tạo-ảnh-ai)
  - [Tạo ảnh AI kèm ảnh tham chiếu](#️-tạo-ảnh-ai-kèm-ảnh-tham-chiếu)
  - [Tạo ảnh thời tiết bằng AI](#️-tạo-ảnh-thời-tiết-bằng-ai)
  - [Tạo ảnh danh lam thắng cảnh](#-tạo-ảnh-danh-lam-thắng-cảnh)
- **Camera & Giám sát**
  - [Kiểm tra camera bằng AI (Voice)](#-kiểm-tra-camera-bằng-ai-voice)
  - [Chụp ảnh hoặc quay video camera (Voice)](#-chụp-ảnh-hoặc-quay-video-camera-voice)
  - [Phân tích file / ảnh (LLM)](#-phân-tích-file--ảnh-llm)
  - [Cảnh báo người qua camera bằng AI](#-cảnh-báo-người-qua-camera-bằng-ai)
  - [Cảnh báo camera AI 4 — cửa lọc, ảnh đôi, video](#-cảnh-báo-camera-ai-4--cửa-lọc-ảnh-đôi-video)
  - [Giữ model AI thức trong khung giờ](#-giữ-model-ai-thức-trong-khung-giờ)
  - [LLM Vision Camera](#️-llm-vision-camera)
- **Gửi tin nhắn**
  - [Gửi Telegram (Voice + xóa file)](#-gửi-telegram-voice--xóa-file)
  - [Gửi Zalo Bot chính thức (Voice)](#-gửi-zalo-bot-chính-thức-voice)
  - [Gửi Zalo Custom Bot (Voice + xóa file)](#-gửi-zalo-custom-bot-voice--xóa-file)
  - [🔗 Zalo Calling trong các blueprint cũ](#-zalo-calling-trong-các-blueprint-cũ)
  - [🎤 Voice gửi Zalo Calling (nhiều người và nhóm)](#-voice-gửi-zalo-calling-nhiều-người-và-nhóm)
  - [📞 Zalo Call gọi cảnh báo khi cảm biến kích hoạt](#-zalo-call-gọi-cảnh-báo-khi-cảm-biến-kích-hoạt)
  - [🔘 Zalo Call một nút bấm nghe máy, cúp máy hoặc gọi đi](#-zalo-call-một-nút-bấm-nghe-máy-cúp-máy-hoặc-gọi-đi)
  - [📲 Zalo Call quy tắc cho cuộc gọi đến](#-zalo-call-quy-tắc-cho-cuộc-gọi-đến)
  - [💬 Zalo Call Messenger tuỳ biến](#-zalo-call-messenger-tuỳ-biến)
  - [⏰ Zalo Call gọi hoặc nhắn nhắc hẹn theo lịch](#-zalo-call-gọi-hoặc-nhắn-nhắc-hẹn-theo-lịch)
  - [🔁 Automation của luuquangvu (webhook, hẹn giờ, liên kết)](#-automation-của-luuquangvu-webhook-hẹn-giờ-liên-kết)
  - [🧠 Script của luuquangvu cho Assist (tìm kiếm, lịch, bộ nhớ, hẹn giờ)](#-script-của-luuquangvu-cho-assist-tìm-kiếm-lịch-bộ-nhớ-hẹn-giờ)
- **Tiện ích**
  - [Thông báo lịch âm & thời tiết](#️-thông-báo-lịch-âm--thời-tiết)
  - [Danh ngôn tự động hàng ngày](#-danh-ngôn-tự-động-hàng-ngày)
  - [Kiểm tra thiết bị (Multi-Entity)](#-kiểm-tra-thiết-bị-multi-entity)
  - [⏳ Hẹn giờ có phục hồi sau khởi động lại](#-hẹn-giờ-có-phục-hồi-sau-khởi-động-lại)
  - [Loa Bluetooth trong HA (không cần add-on)](#-loa-bluetooth-trong-ha-không-cần-add-on)
- **Quản lý & Cập nhật**
  - [Tự động cập nhật Blueprints](#-tự-động-cập-nhật-blueprints)
  - [Tự động cập nhật Pyscript](#-tự-động-cập-nhật-pyscript)
- **Hướng dẫn nâng cao**
  - [Tạo Sensor trong configuration.yaml](#-tạo-sensor-trong-configurationyaml)
  - [Tạo Shell Command](#-tạo-shell-command)
  - [Tạo Input Helper](#-tạo-input-helper)
  - [Tạo Sensor alias cho Assist](#️-tạo-sensor-alias-cho-assist)
  - [Cài đặt Scripts (Shell)](#️-cài-đặt-scripts-shell)
  - [Cấu hình Cloudflare Tunnel](#-cấu-hình-cloudflare-tunnel)
  - [Kiểm tra blueprint trước khi đẩy lên](#-kiểm-tra-blueprint-trước-khi-đẩy-lên)

---

## ⚙️ Yêu cầu chung

| Yêu cầu | Chi tiết |
|----------|----------|
| **Home Assistant** | Phiên bản tối thiểu tùy blueprint (2024.10.0 – 2025.8.0) |
| **AI Model** | Khuyến nghị **Gemini 2.5 Flash** (hỗ trợ tạo ảnh & phân tích) |
| **AI Task Entity** | Cần tạo và cấu hình trong **Settings → General** (cho các blueprint tạo ảnh/phân tích) |
| **Voice Assistant** | Tùy chọn — cần cho các blueprint điều khiển bằng giọng nói |

> **Lưu ý quan trọng:** Sau khi tạo script từ blueprint, hãy **expose script cho Assist** để có thể điều khiển bằng giọng nói. Không thay đổi tên script mặc định.


**Blueprint nào cần file `.py` nào** (file nằm trong `scripts/`; cách cài ở mục «Cài đặt Pyscript»):

| File `.py` | Blueprint dùng nó |
|---|---|
| `common_utilities.py` | `devices_schedules_restart_handler.yaml`, `telegram_bot_webhook.yaml`, `zalo_bot_webhook.yaml`, `memory_tool_local.yaml`, `devices_schedules.yaml` |
| `date_conversion_tool.py` | `create_lunar_events.yaml`, `date_lookup_and_conversion_full_llm.yaml` |
| `devices_scheduler.py` | `devices_schedules_controller_v2_full_llm.yaml` |
| `flow_image.py` | `ai_creat_image_weather_3.yaml` |
| `memory.py` | `memory_tool_local.yaml`, `memory_tool_full_llm.yaml` |
| `telegram_bot_handle_tool.py` | `send_to_telegram_full_llm.yaml`, `telegram_bot_webhook.yaml` |
| `weather_image.py` | `ai_creat_image_weather_2.yaml`, `ai_creat_image_weather_3.yaml` |
| `youtube_data_tool.py` | `advanced_youtube_search_full_llm.yaml` |
| `zalo_bot_handle_tool.py` | `ai_creat_image_weather_3.yaml`, `alarm_person_camera.yaml`, `alarm_person_camera_2.yaml`, `alarm_person_camera_3.yaml`, `alarm_person_camera_4.yaml`, `calendar_weather_notification.yaml`, `send_to_zalo_bot_full_llm.yaml`, `zalo_bot_webhook.yaml` |

---

## 🖼️ Tạo ảnh AI

Tạo ảnh theo prompt bằng mô hình AI. Chỉ cần nói hoặc nhập mô tả, hệ thống sẽ tự sinh ảnh và lưu về Home Assistant.

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Script |
| **HA tối thiểu** | 2025.8.0 |
| **Yêu cầu** | AI Task Entity hỗ trợ tạo ảnh |

> **Chạy chatgpt2api thì đừng cài blueprint này.** Cổng
> [chatgpt2api](https://github.com/TriTue2011/chatgpt2api) đã có sẵn công cụ `generate_image`
> vẽ được từ mọi kênh — Zalo, Telegram lẫn trợ lý trong nhà — kèm `library_media` để xem lại
> và `delete_media` để dọn. Vào **Cài đặt → Home Assistant → Giới hạn chức năng** tích ô
> **🎨 Ảnh** là nói với loa «vẽ con mèo» sẽ ra ảnh, không cần script nào trong HA cả.
>
> Cài cả hai thì hỏng theo hai đường. Một là trợ lý có hai công cụ cùng nói "tôi vẽ ảnh" nên
> chọn nhầm. Hai là mô tả trường của hai blueprint này nặng **3 918 ký tự**, và chúng đi vào
> tool schema **mỗi lượt chat** — kể cả lượt bạn chỉ hỏi giờ. Để so: cả năm script gửi tin và
> phân tích file cộng lại, sau khi đã nén, chỉ tốn 1 784 ký tự.
>
> Không dùng chatgpt2api thì blueprint này vẫn chạy độc lập bình thường.

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
| **Loại** | Script |
| **HA tối thiểu** | 2025.8.0 |
| **Yêu cầu** | Input Text Helper |

> **Chạy chatgpt2api thì đừng cài blueprint này.** Cổng
> [chatgpt2api](https://github.com/TriTue2011/chatgpt2api) đã có sẵn công cụ `generate_image`
> vẽ được từ mọi kênh — Zalo, Telegram lẫn trợ lý trong nhà — kèm `library_media` để xem lại
> và `delete_media` để dọn. Vào **Cài đặt → Home Assistant → Giới hạn chức năng** tích ô
> **🎨 Ảnh** là nói với loa «vẽ con mèo» sẽ ra ảnh, không cần script nào trong HA cả.
>
> Cài cả hai thì hỏng theo hai đường. Một là trợ lý có hai công cụ cùng nói "tôi vẽ ảnh" nên
> chọn nhầm. Hai là mô tả trường của hai blueprint này nặng **3 918 ký tự**, và chúng đi vào
> tool schema **mỗi lượt chat** — kể cả lượt bạn chỉ hỏi giờ. Để so: cả năm script gửi tin và
> phân tích file cộng lại, sau khi đã nén, chỉ tốn 1 784 ký tự.
>
> Không dùng chatgpt2api thì blueprint này vẫn chạy độc lập bình thường.

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
| **HA tối thiểu** | 2025.10.0 |
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
tải file https://github.com/TriTue2011/Blueprint/blob/main/scripts/weather_image.py cho vào folder pyscript. cách cài pyscript https://github.com/custom-components/pyscript.

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

**Dùng Gemini. Sử dụng addon (dockercompse) https://github.com/luuquangvu/Gemini-FastAPI và tích hợp https://github.com/luuquangvu/hass_local_openai_llm** 

**Cần file Pyscript:** `weather_image.py`, `flow_image.py`, `zalo_bot_handle_tool.py` (trong thư mục `scripts/`, chép vào `/config/pyscript/`).

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fai_creat_image_weather.yaml)

**Dùng api nvidia. đăng ký tại https://build.nvidia.com và dùng tích hợp https://github.com/luuquangvu/hass_local_openai_llm**

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fai_creat_image_weather_2.yaml)

**Gộp 2 blueprint kèm gửi ảnh qua zalo**

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fai_creat_image_weather_3.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 🌍 Tạo ảnh danh lam thắng cảnh

Tự động tạo ảnh các danh lam thắng cảnh, công trình nổi tiếng trên thế giới bằng AI theo lịch trình hoặc khi được yêu cầu.

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Automation |
| **HA tối thiểu** | 2025.10.0 |

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
- **Entity Aliases:** Sensor alias để ánh xạ tên camera — phải tạo trước, xem [hướng dẫn tạo Sensor alias cho Assist](#️-tạo-sensor-alias-cho-assist)
- **AI Task Entity:** Chọn entity AI Task (để trống = mặc định)
- **Multi-Camera Check Mode:** Parallel (nhanh) hoặc Sequential

**Ví dụ lệnh giọng nói:**
- "Kiểm tra cửa trước có ai không?"
- "Camera sân có con chó không?"

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fvoice_camera_ai_analyzer.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 📷 Chụp ảnh hoặc quay video camera (Voice)

Nói tên camera là chụp một tấm, hoặc **quay một đoạn 1–60 giây**. Trả về đường dẫn file để blueprint khác dùng tiếp — ghép với [Phân tích file / ảnh (LLM)](#-phân-tích-file--ảnh-llm) là thành "chụp rồi kể xem thấy gì".

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Script |
| **HA tối thiểu** | 2024.12.0 |
| **Yêu cầu** | Sensor alias (xem [hướng dẫn](#️-tạo-sensor-alias-cho-assist)), Camera entities |

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
| **HA tối thiểu** | 2025.7.0 (bản Gemini và bản OpenAI) — 2026.3.0 (bản gộp) |
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

**Cần file Pyscript:** `zalo_bot_handle_tool.py` (trong thư mục `scripts/`, chép vào `/config/pyscript/`).

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Falarm_person_camera.yaml)

**Open ai**

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Falarm_person_camera_2.yaml)

**Gộp Open ai và Gemini thêm phân tích động vật**

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Falarm_person_camera_3.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 🎥 Cảnh báo camera AI 4 — cửa lọc, ảnh đôi, video

Bản viết lại của blueprint trên, cho **nhà ở** — chung cư và nhà đất — chứ không phải nơi đông người qua lại. Ba thứ mới: một cửa lọc rẻ tiền chặn báo động ảo trước khi tốn công, ảnh cho AI đọc tách khỏi ảnh gửi cho bạn xem, và một nhánh video chạy song song với nhánh ảnh.

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Automation |
| **HA tối thiểu** | 2026.3.0 |
| **Yêu cầu** | Binary sensor (kích hoạt), Camera entity, một AI Task entity |
| **Chạy được với** | Google Gemini, OpenAI, Ollama, và mọi AI Task provider khác |

### Cửa lọc một ảnh

Bật lên thì mỗi lần cảm biến kêu, blueprint chụp **một** tấm bằng camera phân tích rồi hỏi AI đúng một câu: có người hay không. Không có ai thì dừng ngay — khỏi chụp tiếp, khỏi quay video, khỏi phân tích. Prompt của bước này viết cực ngắn có chủ đích, vì nó chạy cả những lần chẳng có ai.

### Ảnh cho AI và ảnh gửi bạn là hai bộ riêng

Đây là chỗ khác lớn nhất so với bản 3. Bạn khai hai camera:

- **Camera cho AI đọc** — chọn luồng phụ, thường có đuôi `-sub`.
- **Camera cho ảnh gửi đi** — chọn luồng chính, để ảnh nhận được thật nét.

Mỗi nhịp chụp bấm **cả hai tấm cùng lúc**, rồi mới chờ hết giãn cách mới sang nhịp sau. Nhờ vậy khi AI chấm "khung số 2 rõ nhất" thì tấm nét số 2 đúng là khoảnh khắc đó.

Vì sao đáng làm, đo trên máy thật với Qwen3-VL-4B:

| Đưa vào AI | Token | Thời gian |
|---|---|---|
| 3 ảnh luồng phụ | 978 | ~1,0 giây |
| 3 ảnh luồng chính | 8 425 | ~20 giây |

Cùng cảnh đó, cùng số người nhận ra, mô tả như nhau. Ảnh nét chỉ để mắt người xem, đưa vào AI là trả giá gấp hai mươi lần mà không được gì thêm.

### Sáu trường hợp gửi

Ảnh, video và kết quả phân tích, mỗi thứ có ô riêng với ba lựa chọn: gửi mọi lượt, chỉ khi có người, hoặc chỉ khi mất an ninh. Kết quả phân tích không bao giờ đi một mình — nó chỉ kèm theo khi ảnh hoặc video đã được gửi, nên ba nhân ba rút xuống còn sáu tình huống thật.

| # | Nguồn gửi khi | Phân tích gửi khi | Bạn nhận được gì |
|---|---|---|---|
| 1 | Mọi lượt | Cùng lúc | Ảnh tới ngay, chữ tới sau khi phân tích xong |
| 2 | Mọi lượt | Khi có người | Lượt nào cũng có ảnh, phòng trống thì không kèm chữ |
| 3 | Mọi lượt | Khi mất an ninh | Lượt nào cũng có ảnh, chỉ chuyện đáng ngờ mới kèm chữ |
| 4 | Khi có người | Cùng lúc | Im khi không có ai; có người thì đủ cả hai |
| 5 | Khi có người | Khi mất an ninh | Có người là thấy ảnh, chữ chỉ tới khi đáng ngờ |
| 6 | Khi mất an ninh | Cùng lúc | Im hoàn toàn trừ lúc đáng ngờ — ít làm phiền nhất |

Ba dòng có dính "mất an ninh" chỉ dùng được ở chế độ phân tích **An ninh**, vì ba chế độ kia không hỏi AI câu đáng ngờ hay không. Chọn nhầm thì blueprint tự hạ xuống "khi có người" và ghi một dòng vào nhật ký cho bạn biết, thay vì im lặng không gửi gì.

### Một ảnh hoặc một video thì phân tích đi kèm luôn

Telegram và Zalo cá nhân đều cho gửi ảnh hoặc video kèm chú thích, nên bạn nhận đúng **một tin** có cả hình lẫn lời. Chỉ khi gửi nhiều ảnh mới phải tách hai lần, vì dịch vụ gửi chùm không có chỗ đặt chú thích.

Trần từng kênh khác nhau và blueprint đã tính sẵn: Telegram gộp tối đa 10 ảnh một chùm, Zalo cá nhân tới 50, Zalo Bot không có chùm nên mỗi tấm một tin, còn thông báo điện thoại thì mỗi tấm một thông báo.

### Bấm vào thông báo là mở đúng tấm ảnh đó

Đường dẫn ảnh để tương đối, nên ứng dụng tự nối với chính máy chủ đã gửi thông báo: ở nhà thì đi mạng LAN, ra ngoài thì đi tên miền. Bạn không phải khai địa chỉ nào cả.

### Loa đọc câu do AI viết lại

Câu hiện trên màn hình có emoji, dấu hai chấm và giờ giấc viết tắt — đọc nguyên văn ra loa nghe rất kỳ. Bật ô này thì AI viết lại thành một câu nói được: bỏ ký hiệu, đọc số thành chữ, dưới ba mươi từ. Tắt thì quay về câu ghép sẵn.

### Đánh thức model ngay khi cảm biến kêu

Dành cho ai chạy model tại nhà và cho nó ngủ lúc rảnh để nhường GPU. Blueprint gửi một lời gọi rỗng ngay lúc kích hoạt, chạy song song với việc chờ xác nhận, nên model nạp xong trước khi cần hỏi thật. Đo trên máy tại nhà: gọi lúc model đang ngủ mất 11,8 giây, gọi lúc đang thức mất 1,0 giây — bật ô này thì phần lớn quãng đó trôi qua trong lúc bạn còn đang chờ.

### Cấu hình

Mười hai mục, 63 ô. Những ô đáng để ý nhất:

- **Cách xác nhận** — một ô chọn ba giá trị: không xác nhận, chờ rồi kiểm lại chính cảm biến đó, hoặc theo dõi một cảm biến khác. Chỉ một đường chạy, không cộng dồn thời gian chờ như bản cũ.
- **Camera cho AI đọc** và **Camera cho ảnh gửi đi** — hai luồng khác nhau, xem phần trên.
- **Phân tích cái gì** — chỉ người, chỉ động vật, cả hai, hoặc an ninh.
- **AI Task cho cửa lọc** — để riêng được, vì bước này chỉ hỏi một câu nên giao cho model nhỏ, kể cả khi phần phân tích đầy đủ giao cho model lớn ngoài mạng.
- **Thời lượng video** và **lấy thêm mấy giây trước lúc kích hoạt** — Home Assistant giữ sẵn một đoạn đệm nên lấy ngược lại được cả khoảnh khắc người ta vừa bước vào khung hình.

### Yêu cầu cấu hình

Thêm vào `configuration.yaml` để Home Assistant nhận đúng thư mục media:

```yaml
homeassistant:
  media_dirs:
    local: /media
```

Thiếu dòng này thì AI Task và thông báo điện thoại không đọc được ảnh.

Nhánh video muốn cho AI đọc thẳng tệp mp4 thì phải dùng provider đọc được video, hiện là Google Gemini. Model chạy tại nhà qua Ollama hay llama.cpp chỉ nhận ảnh tĩnh, nên với chúng hãy để video ở chế độ chỉ gửi kèm — đó cũng là mặc định.

**Cần file Pyscript:** `zalo_bot_handle_tool.py` (trong thư mục `scripts/`, chép vào `/config/pyscript/`).

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Falarm_person_camera_4.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## ⏰ Giữ model AI thức trong khung giờ

Dành cho ai chạy model tại nhà và đã cho nó ngủ lúc rảnh để nhường GPU. Automation gọi model một lời gọi rỗng theo chu kỳ, đủ để nó không kịp ngủ, nhưng chỉ trong khung giờ bạn cần báo động nhạy nhất.

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Automation |
| **HA tối thiểu** | 2026.3.0 |
| **Yêu cầu** | Một AI Task entity trỏ tới model chạy tại nhà |

### Vì sao cần

Đo trên RTX 2060 SUPER với Qwen3-VL-4B:

| Gọi lúc | Thời gian |
|---|---|
| Model đang ngủ | **11 804 ms** |
| Model đang thức | 1 044 ms |

Mười giây chênh lệch đó **không rút ngắn được bằng tham số**. Đã thử năm cấu hình, mỗi cấu hình hai lượt: bản gốc, thêm `--mlock`, hạ cửa sổ ngữ cảnh còn một nửa, kết hợp cả hai, và nén bộ nhớ đệm KV xuống q8_0. Cả mười lượt đều rơi vào 10,1–10,4 giây. Nó là chi phí dựng lại ngữ cảnh CUDA và đẩy trọng số lên card, không có cờ nào chạm tới được.

Nên cách duy nhất là **ít phải thức dậy hơn**. Automation này giữ model thức suốt khung giờ bạn chọn, để mọi báo động trong khoảng đó trả lời trong một giây.

### Cái giá

Model giữ VRAM suốt khung giờ ấy — với Qwen3-VL-4B là khoảng 4,4 GB trên card 8 GB. Vì vậy hãy chọn khung giờ mà GPU không phải làm việc gì khác. Ban đêm thường là lựa chọn đúng: đó vừa là lúc báo động cần nhạy nhất, vừa là lúc bạn không ra lệnh bằng giọng nói hay dịch phụ đề.

### Một điều dễ đặt sai

**Chu kỳ gọi phải ngắn hơn ngưỡng ngủ của model.** Model đặt `--sleep-idle-seconds 300` thì gọi mỗi 4 phút là vừa. Nếu ngưỡng ngủ chỉ 30 giây thì automation này không đuổi kịp — hãy nâng ngưỡng ngủ lên trước, rồi mới dùng.

### Cấu hình

- **AI Task** — thực thể trỏ tới model chạy tại nhà. Đừng trỏ vào dịch vụ ngoài mạng tính tiền theo lượt gọi, vì automation gọi vài trăm lần mỗi đêm.
- **Gọi mỗi bao nhiêu phút** — mặc định 4.
- **Bắt đầu** và **thôi giữ thức** — đặt giờ kết thúc sớm hơn giờ bắt đầu là khung qua nửa đêm, ví dụ 22:00 tới 06:00, Home Assistant hiểu đúng.
- **Điều kiện thêm** — ví dụ chỉ giữ thức khi báo động đang bật, hoặc khi có người ở nhà.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fgiu_model_thuc.yaml)

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
| **Loại** | Script |
| **HA tối thiểu** | 2024.10.0 |
| **Yêu cầu** | Telegram Bot integration |

**Ví dụ lệnh giọng nói:**
- "Gửi ảnh camera sân vào Telegram"
- "Gửi thông báo nhiệt độ phòng khách lên Telegram"

**Cần file Pyscript:** `telegram_bot_handle_tool.py` (trong thư mục `scripts/`, chép vào `/config/pyscript/`).

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fsend_to_telegram_full_llm.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 💬 Gửi Zalo Bot chính thức (Voice)

Gửi tin nhắn đến Zalo qua bot chính thức bằng giọng nói. Địa điểm tự động được kèm link Google Maps.

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Script |
| **HA tối thiểu** | 2024.10.0 |
| **Yêu cầu** | Zalo Bot integration (HACS) |

> **Gửi ảnh không cần mở Home Assistant ra Internet.** Zalo Bot chỉ nhận ảnh qua URL công khai
> — nó tự đi tải về — nên mặc định blueprint chép ảnh vào `/config/www/zalo` rồi đưa URL đó cho
> Zalo, tức máy chủ HA của bạn phải ra được Internet. Ai đang chạy `zalo-server` của dự án
> [chatgpt2api](https://github.com/TriTue2011/chatgpt2api) thì đặt ô **Hành động gửi ảnh** để đẩy
> thẳng tệp lên server; server lưu vào kho ảnh công khai của nó rồi mới gọi Zalo. Khai trước một
> `shell_command`:
>
> ```yaml
> shell_command:
>   zalo_gui_anh: >
>     curl -s -m 30 -X POST http://172.16.10.38:3030/api/zalo-bot/send
>     -H "authorization: Bearer {{ token }}"
>     -F "text={{ text }}"
>     -F "photo=@{{ duong_dan }}"
> ```
>
> Đường này còn tự chuyển ảnh không phải PNG sang PNG, vì Zalo trả sai content-type khi byte
> JPEG nằm trong tệp `.png`. Đổi lại: `shell_command` không trả kết quả về, nên blueprint báo
> "đã gửi đi, chưa có xác nhận" chứ không dám nói đã tới nơi — xem log zalo-server nếu nghi ngờ.

**Ví dụ lệnh giọng nói:**
- "Tìm nhà hàng ngon ở Hà Nội và gửi lên Zalo"
- "Gửi địa chỉ Văn Miếu lên Zalo"

**Cần file Pyscript:** `zalo_bot_handle_tool.py` (trong thư mục `scripts/`, chép vào `/config/pyscript/`).

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

> **Đây là nhánh riêng của kho này.** Ngày 18/08/2026 kho gốc [luuquangvu/tutorials](https://github.com/luuquangvu/tutorials) đã bỏ đường Zalo Custom Bot để gộp hết về bot OA chính thức. Blueprint dưới đây vẫn được giữ và tự bảo trì ở đây, vì nó gửi qua **tài khoản Zalo cá nhân** — việc mà bot OA không làm được. Đừng cài đồng thời nó và [Gửi Zalo Bot chính thức](#-gửi-zalo-bot-chính-thức-voice): hai script cùng nhận lệnh gửi Zalo sẽ làm trợ lý chọn nhầm.

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

## 📞 Zalo Call gọi cảnh báo khi cảm biến kích hoạt

Cảm biến kích hoạt (có người, khói, rò nước, cửa mở, mất điện...) thì **gọi điện Zalo** cho người bạn chọn: máy đọc cảnh báo rồi nối thẳng loa, mic, camera trong nhà. Gọi **lần lượt** từng người cho tới khi có người nghe máy. **Mọi thứ chọn từ danh sách**, không phải gõ mã.

**Cần:** Zalo Call từ bản 2026.11.11.2; người nhận chọn ở *Zalo Call → Cấu hình*.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fzalo_call_alert_sensor.yaml)

---

## 🔘 Zalo Call một nút bấm nghe máy, cúp máy hoặc gọi đi

**Cùng một nút bấm, việc khác nhau tuỳ lúc:** có cuộc gọi đến thì nghe máy, đang trong cuộc gọi thì cúp, rảnh thì gọi đi / gọi cảnh báo / nhắn tin. Nút chọn bằng bộ chọn trigger (nút giữa loa R1, nút Zigbee, nút ảo...).

**Cần:** Zalo Call từ bản 2026.11.11.2; cảm biến «Trạng thái cuộc gọi» của Zalo Call.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fzalo_call_nut_bam.yaml)

---

## 📲 Zalo Call quy tắc cho cuộc gọi đến

Quy định hệ thống làm gì khi **có người gọi đến**: **báo ra loa** cho cả nhà biết, **tự nghe máy**, cho **AI nói chuyện**, và **bật thiết bị nhà nào** khi người nhà nói trực tiếp (tích Mic / Loa / Camera, tích Camera là cuộc gọi video). Áp cho một người, mọi người trong danh bạ, người lạ hoặc mọi nhóm.

**Cần:** Zalo Call từ bản 2026.11.11.2.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fzalo_call_incoming_rule.yaml)

---

## 💬 Zalo Call Messenger tuỳ biến

Nhắn tin Zalo (hoặc gọi) khi thiết bị thay đổi, **tuỳ biến rộng nhưng chỉ chọn từ danh sách**: thiết bị theo dõi, chế độ (mọi thay đổi, bật, tắt, vượt ngưỡng, báo cáo hằng ngày), câu có sẵn, kiểu chữ (emoji, đậm, màu, cỡ chữ), người nhận.

**Cần:** Zalo Call từ bản 2026.11.11.2; người nhận chọn ở *Zalo Call → Cấu hình*.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fzalo_call_messenger.yaml)

---

## ⏰ Zalo Call gọi hoặc nhắn nhắc hẹn theo lịch

Đúng giờ đã chọn, **gọi điện Zalo đọc lời nhắc** (hoặc nhắn tin): uống thuốc, đi ngủ, thức dậy, ăn cơm, uống nước, tập thể dục, họp, tưới cây. Hợp cho người lớn tuổi ít nhìn tin nhắn.

**Cần:** Zalo Call từ bản 2026.11.11.2; người nhận chọn ở *Zalo Call → Cấu hình*.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fzalo_call_nhac_hen.yaml)

---

## 🎤 Voice gửi Zalo Calling (nhiều người và nhóm)

Script cho **Voice Assistant** (Assist): gửi tin nhắn, vị trí hoặc ảnh cho **nhiều người và nhóm cùng lúc** qua **Zalo Calling**. Người nhận **chọn từ danh sách** (thực thể `notify.zalo_call_...`), không gõ mã Zalo. Cùng khuôn với «Gửi Zalo Custom Bot», nhưng không cần số điện thoại tài khoản và mã nhóm.

**Cần:** Zalo Calling từ bản 2026.11.11.3; người nhận chọn ở *Zalo Call → Cấu hình*.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fsend_to_zalo_call_full_llm.yaml)

---

## 🔗 Zalo Calling trong các blueprint cũ

Các blueprint sau **đã có thêm nhóm «Zalo Calling»** (cạnh Zalo Bot / Zalo Custom): bật nó, chọn người nhận từ danh sách (người và nhóm lẫn lộn đều được), và blueprint gửi **song song** qua Zalo Calling. Cần Zalo Calling từ bản `2026.11.11.3`.

| Blueprint | Gửi qua Zalo Calling |
|---|---|
| Cảnh báo người qua camera bằng AI (1, 2, 3) | Ảnh chụp kèm chú thích, kết quả AI, tin báo lỗi |
| Cảnh báo camera AI 4 | Ảnh sớm/muộn, video sớm/muộn, kết quả AI, chữ riêng, tin báo lỗi |
| LLM Vision Camera | Kết quả AI kèm ảnh khung hình hoặc ảnh chụp |
| Tạo ảnh thời tiết bằng AI | Ảnh vừa tạo |
| Thông báo lịch âm & thời tiết | Tin lịch âm và tin thời tiết |
| Tự động cập nhật Blueprints, Tự động cập nhật Pyscript | Báo cáo cập nhật |

---

## 🔁 Automation của luuquangvu (webhook, hẹn giờ, liên kết)

Bản chép từ [luuquangvu/tutorials](https://github.com/luuquangvu/tutorials) (giấy phép MIT, xem `scripts/LICENSE-luuquangvu`). Các file `.py` nằm trong thư mục `scripts/` của kho này.

Cài tích hợp **Pyscript** (HACS), bật `allow_all_imports` và `hass_is_global`, chép các file `.py` cần vào `/config/pyscript/` (chép cả `requirements.txt`). Chi tiết ở mục «Cài đặt Pyscript» bên dưới.

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Automation |
| **HA tối thiểu** | 2024.12.0 / 2025.8.0 |

- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fdevices_schedules_restart_handler.yaml) — `devices_schedules_restart_handler.yaml`: Khôi phục hẹn giờ thiết bị sau khi HA khởi động lại (bản cũ); cần `common_utilities.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Flink_multiple_devices.yaml) — `link_multiple_devices.yaml`: Liên kết trạng thái bật/tắt của nhiều thiết bị; không cần file `.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Ftelegram_bot_webhook.yaml) — `telegram_bot_webhook.yaml`: Bot Telegram hai chiều với Home Assistant (webhook); cần `telegram_bot_handle_tool.py`, `common_utilities.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fzalo_bot_webhook.yaml) — `zalo_bot_webhook.yaml`: Bot Zalo hai chiều với Home Assistant (webhook); cần `zalo_bot_handle_tool.py`, `common_utilities.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fcheck_the_device_turns_on_manually.yaml) — `check_the_device_turns_on_manually.yaml`: Phát hiện thiết bị bị bật tay; không cần file `.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fstate_activated_device_with_timer.yaml) — `state_activated_device_with_timer.yaml`: Thiết bị bật thì tự tắt sau một khoảng thời gian; không cần file `.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fmemory_tool_local.yaml) — `memory_tool_local.yaml`: Bộ nhớ cục bộ cho Assist (dọn bộ nhớ theo lịch); cần `memory.py`, `common_utilities.py`

---

## 🧠 Script của luuquangvu cho Assist (tìm kiếm, lịch, bộ nhớ, hẹn giờ)

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Script |
| **HA tối thiểu** | 2024.12.0 |

- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fadvanced_youtube_search_full_llm.yaml) — `advanced_youtube_search_full_llm.yaml`: Tìm video YouTube cho Assist; cần `youtube_data_tool.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fget_youtube_video_info_full_llm.yaml) — `get_youtube_video_info_full_llm.yaml`: Lấy thông tin một video YouTube; không cần file `.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fplay_youtube_video_full_llm.yaml) — `play_youtube_video_full_llm.yaml`: Phát video YouTube lên thiết bị; không cần file `.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fadvanced_google_search_full_llm.yaml) — `advanced_google_search_full_llm.yaml`: Tìm kiếm Google cho Assist; không cần file `.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fweather_forecast_full_llm.yaml) — `weather_forecast_full_llm.yaml`: Dự báo thời tiết cho Assist; không cần file `.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fcalendar_events_lookup_full_llm.yaml) — `calendar_events_lookup_full_llm.yaml`: Tra cứu sự kiện lịch cho Assist; không cần file `.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fcreate_calendar_event_full_llm.yaml) — `create_calendar_event_full_llm.yaml`: Tạo sự kiện lịch bằng giọng nói; không cần file `.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fcreate_lunar_events.yaml) — `create_lunar_events.yaml`: Tạo sự kiện lịch âm hằng năm; cần `date_conversion_tool.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fdate_lookup_and_conversion_full_llm.yaml) — `date_lookup_and_conversion_full_llm.yaml`: Tra ngày và đổi dương lịch ↔ âm lịch cho Assist; cần `date_conversion_tool.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fcontrol_music_full_llm.yaml) — `control_music_full_llm.yaml`: Điều khiển nhạc bằng giọng nói; không cần file `.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fac_mode_and_fan_control_full_llm.yaml) — `ac_mode_and_fan_control_full_llm.yaml`: Điều khiển điều hoà (chế độ, quạt); không cần file `.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Ffan_speed_and_oscillation_control_full_llm.yaml) — `fan_speed_and_oscillation_control_full_llm.yaml`: Điều khiển tốc độ và xoay quạt; không cần file `.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fdevice_location_lookup_full_llm.yaml) — `device_location_lookup_full_llm.yaml`: Tìm vị trí thiết bị trong nhà; không cần file `.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fdevice_ringing_full_llm.yaml) — `device_ringing_full_llm.yaml`: Làm điện thoại kêu để tìm máy; không cần file `.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fdevices_schedules_controller_v2_full_llm.yaml) — `devices_schedules_controller_v2_full_llm.yaml`: Hẹn giờ nhiều thiết bị bằng giọng nói (bản mới); cần `devices_scheduler.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fdevices_schedules.yaml) — `devices_schedules.yaml`: Hẹn giờ nhiều thiết bị (bản cũ, nền cho controller cũ); cần `common_utilities.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fdevices_schedules_controller_full_llm.yaml) — `devices_schedules_controller_full_llm.yaml`: Điều khiển hẹn giờ bằng giọng nói (bản cũ, cần script «Devices Schedules»); không cần file `.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fmemory_tool_full_llm.yaml) — `memory_tool_full_llm.yaml`: Bộ nhớ ghi nhớ cho Assist; cần `memory.py`

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

**Cần file Pyscript:** `zalo_bot_handle_tool.py` (trong thư mục `scripts/`, chép vào `/config/pyscript/`).

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

## 🔊 Loa Bluetooth trong HA (không cần add-on)

Quét, ghép đôi, kết nối và phát ra loa Bluetooth bất kỳ ngay trên giao diện Home Assistant —
chạy với **HA Container**, kể cả HA trong **LXC trên Proxmox** (nơi add-on không cài được).
Chọn loa trong danh sách, bấm **Kết nối**; phát bằng `media_player` của tích hợp MPD.

Không phải blueprint mà là một gói cấu hình (`packages/`) kèm một tệp Python. Hướng dẫn cài
đủ các bước (máy Proxmox, LXC, compose, MPD, HA) và cách dùng:
**[loa_bluetooth/README.md](loa_bluetooth/README.md)**.

---

## ⏳ Hẹn giờ có phục hồi sau khởi động lại

Khi một thực thể chuyển trạng thái theo cấu hình, **bật hẹn giờ**, **lưu thời điểm hết hạn** và **tự phục hồi sau khi Home Assistant khởi động lại hoặc mất điện**; hết giờ thì chạy hành động bạn chọn.

| Thông tin | Chi tiết |
|-----------|----------|
| **Loại** | Automation |
| **HA tối thiểu** | 2024.10.0 |
| **Yêu cầu** | Một Timer helper và một Input Datetime helper |

**Đầu vào:** thực thể kích hoạt, trạng thái từ/đến, Timer helper, Input Datetime lưu thời điểm hết hạn, hành động khi hết giờ.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Funiversal_cooldown_recovery.yaml)

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

> **Cài đặt script:** Xem [hướng dẫn cài đặt Scripts](#️-cài-đặt-scripts-shell)

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

> **Cài đặt script:** Xem [hướng dẫn cài đặt Scripts](#️-cài-đặt-scripts-shell)

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

## 🏷️ Tạo Sensor alias cho Assist

Hai blueprint **Kiểm tra camera bằng AI (Voice)** và **Chụp ảnh camera (Voice)** tra tên
camera theo biệt danh (alias) bạn đặt trong Assist. Chúng đọc biệt danh từ một sensor
template mà bạn phải tạo trước — thiếu nó thì việc tìm theo alias không chạy, và Home
Assistant **không báo lỗi gì cả**, nên rất khó đoán ra.

### Vì sao không chép đoạn cấu hình cũ trên mạng

Home Assistant đã đổi khoá lưu biệt danh trong `.storage/core.entity_registry` từ
`aliases` sang `aliases_v2`. Mọi hướng dẫn viết trước tháng 6/2026 đều đọc khoá `aliases`,
nên trên bản Home Assistant mới nó trả về danh sách rỗng. Đoạn dưới đây đọc được cả hai khoá.

### Thêm vào `configuration.yaml`

```yaml
shell_command:
  get_entity_alias: >-
    jq '[.data.entities[] | select(.options.conversation.should_expose == true) | {entity_id, aliases: (if has("aliases_v2") then ((if (.aliases_v2 | type) == "array" then .aliases_v2 else [] end) | map(select(. != null and . != ""))) else (if (.aliases | type) == "array" then .aliases else [] end) end)} | select(.aliases | length > 0)]' ./.storage/core.entity_registry
template:
  - triggers:
      - trigger: homeassistant
        event: start
      - trigger: event
        event_type: event_template_reloaded
    actions:
      - action: shell_command.get_entity_alias
        response_variable: response
    sensor:
      - name: "Assist: Entity IDs and Aliases"
        unique_id: entity_ids_and_aliases
        icon: mdi:format-list-bulleted
        device_class: timestamp
        state: "{{ now().isoformat() }}"
        attributes:
          entities: "{{ response.stdout }}"
```

Sensor này chỉ nạp lại vào hai lúc: khi Home Assistant khởi động, và khi bạn reload
template entities. Vậy nên **đặt thêm alias cho một camera xong thì phải reload**, nếu
không blueprint vẫn dùng danh sách cũ.

### Kiểm tra sensor đã chạy đúng

Vào **Developer Tools → Template** và dán:

```jinja
{{ state_attr('sensor.assist_entity_ids_and_aliases', 'entities') }}
```

Kết quả phải là một danh sách JSON có `entity_id` và `aliases`. Ra `None` hoặc `[]` thì
có ba nguyên nhân theo thứ tự hay gặp: chưa entity nào được expose cho Assist, chưa
entity nào được đặt alias, hoặc bản Home Assistant của bạn thiếu lệnh `jq` (bản
Container và Core cài thủ công hay thiếu — bản OS và Supervised thì có sẵn).

*Nguồn đoạn cấu hình: [luuquangvu/tutorials](https://github.com/luuquangvu/tutorials).*

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

### 3. Cài đặt Pyscript (cho các blueprint cần file `.py`)

1. Cài tích hợp **Pyscript** qua HACS.
2. Trong `configuration.yaml`: `pyscript:` với `allow_all_imports: true` và `hass_is_global: true`.
3. Chép các file `.py` cần dùng và `requirements.txt` từ `scripts/` vào `/config/pyscript/` (hoặc dùng blueprint «Tự động cập nhật Pyscript» ở trên).
4. Token bot đặt trong `secrets.yaml` (ví dụ `zalo_bot_token`, `telegram_bot_token`) như hướng dẫn trong mô tả từng blueprint.

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

## ✅ Kiểm tra blueprint trước khi đẩy lên

Một blueprint sai schema hay sai một dấu ngoặc Jinja2 vẫn nằm yên trong kho, chỉ nổ lúc
người dùng bấm Import. Cũng vậy, README dài nghìn dòng thì một bảng khai sai phiên bản
Home Assistant có thể nằm đó hàng tháng. Thư mục [`tools/`](/tools) có hai trình soát
chặn cả hai chuyện đó.

**Soát blueprint** — nạp thẳng schema thật của Home Assistant Core, bắt sai schema
blueprint, sai định nghĩa selector, sai cú pháp Jinja2, và tham chiếu `!input` tới input
chưa hề khai báo:

```bash
uv run --no-project --python 3.14 --with 'homeassistant>=2026.8.0' \
  python tools/validate_blueprints.py .
```

**Soát README** — đọc chính các file YAML rồi đối chiếu với những gì README nói: bảng
khai sai Loại hay HA tối thiểu, nút Import trỏ vào file không có, file trong kho mà
README quên nhắc, liên kết mục lục trỏ vào tiêu đề không tồn tại. Chỉ dùng thư viện
chuẩn:

```bash
python3 tools/check_readme.py .
```

Cả hai chạy tự động qua
[`.github/workflows/soat-blueprint.yaml`](/.github/workflows/soat-blueprint.yaml) mỗi lần
push vào `main` và mỗi pull request; riêng push vào `main` thì workflow còn đồng bộ
`source_url` của mọi blueprint theo nhánh rồi commit lại. Xem thêm
[`tools/README.md`](/tools/README.md).

---

## 📊 Tổng quan Blueprints

| # | Blueprint | Loại | HA Min | Tính năng chính (file .py cần) |
|---|-----------|------|--------|-----------------|
| 1 | Tạo ảnh AI | Script | 2025.8.0 | Tạo ảnh từ prompt văn bản |
| 2 | Tạo ảnh AI + tham chiếu | Script | 2025.8.0 | Tạo ảnh kèm ảnh mẫu |
| 3 | Tạo ảnh thời tiết | Automation | 2025.10.0 | Ảnh AI theo thời tiết/buổi |
| 4 | Danh lam thắng cảnh | Automation | 2025.10.0 | Ảnh AI danh lam thế giới |
| 5 | Camera AI (Voice) | Script | 2025.8.0 | Phân tích camera bằng giọng nói |
| 6 | Chụp / quay camera (Voice) | Script | 2024.12.0 | Chụp ảnh hoặc quay video bằng giọng nói |
| 7 | Phân tích file/ảnh | Script | 2025.8.0 | Gửi file cho LLM phân tích |
| 8 | Cảnh báo người camera (1–3) | Automation | 2025.7.0 | Phát hiện người + cảnh báo |
| 9 | Cảnh báo camera AI 4 | Automation | 2026.3.0 | Cửa lọc, ảnh đôi, nhánh video |
| 10 | Giữ model AI thức | Automation | 2026.3.0 | Gọi định kỳ cho model chạy tại nhà |
| 11 | LLM Vision Camera | Automation | 2024.10.0 | Phân tích camera real-time |
| 12 | Gửi Telegram | Script | 2024.10.0 | Gửi tin/ảnh qua Telegram |
| 13 | Gửi Zalo Bot | Script | 2024.10.0 | Gửi tin qua Zalo chính thức |
| 14 | Gửi Zalo Custom | Script | 2024.10.0 | Gửi tin/ảnh qua Zalo cá nhân |
| 15 | Lịch âm & thời tiết | Automation | 2024.10.0 | Nhắc lịch âm + thời tiết |
| 16 | Danh ngôn hàng ngày | Automation | 2025.7.0 | Quote AI tự động |
| 17 | Kiểm tra thiết bị | Automation | 2024.10.0 | Phân biệt nguồn điều khiển |
| 18 | Cập nhật Blueprints | Automation | 2024.10.0 | Auto-update blueprints |
| 19 | Cập nhật Pyscript | Automation | 2024.10.0 | Auto-sync pyscript từ GitHub |
| 20 | Zalo Call gọi cảnh báo | Automation | 2026.3.0 | Gọi cảnh báo khi cảm biến kích hoạt |
| 21 | Zalo Call một nút bấm | Automation | 2026.3.0 | Nghe máy / cúp / gọi đi bằng một nút |
| 22 | Zalo Call quy tắc cuộc gọi đến | Automation | 2026.3.0 | Báo ra loa, tự nghe, AI, thiết bị nhà |
| 23 | Zalo Call Messenger | Automation | 2026.3.0 | Nhắn tin hoặc gọi tuỳ biến theo thiết bị |
| 24 | Zalo Call nhắc hẹn | Automation | 2026.3.0 | Gọi hoặc nhắn nhắc theo lịch |
| 25 | Hẹn giờ phục hồi | Automation | 2024.10.0 | Hẹn giờ tự phục hồi sau khởi động lại |
| 26 | Voice gửi Zalo Calling | Script | 2026.3.0 | Gửi tin/vị trí/ảnh tới nhiều người và nhóm |
| 27 | Khôi phục hẹn giờ thiết bị sau khi HA khởi động lại | Automation | — | common_utilities.py |
| 28 | Liên kết trạng thái bật/tắt của nhiều thiết bị | Automation | 2024.12.0 | — |
| 29 | Bot Telegram hai chiều với Home Assistant | Automation | 2025.8.0 | telegram_bot_handle_tool.py, common_utilities.py |
| 30 | Bot Zalo hai chiều với Home Assistant | Automation | 2025.8.0 | zalo_bot_handle_tool.py, common_utilities.py |
| 31 | Phát hiện thiết bị bị bật tay | Automation | 2024.12.0 | — |
| 32 | Thiết bị bật thì tự tắt sau một khoảng thời gian | Automation | 2024.12.0 | — |
| 33 | Bộ nhớ cục bộ cho Assist | Automation | 2024.12.0 | memory.py, common_utilities.py |
| 34 | Tìm video YouTube cho Assist | Script | 2024.12.0 | youtube_data_tool.py |
| 35 | Lấy thông tin một video YouTube | Script | 2024.12.0 | — |
| 36 | Phát video YouTube lên thiết bị | Script | 2024.12.0 | — |
| 37 | Tìm kiếm Google cho Assist | Script | 2024.12.0 | — |
| 38 | Dự báo thời tiết cho Assist | Script | 2024.12.0 | — |
| 39 | Tra cứu sự kiện lịch cho Assist | Script | 2024.12.0 | — |
| 40 | Tạo sự kiện lịch bằng giọng nói | Script | 2024.12.0 | — |
| 41 | Tạo sự kiện lịch âm hằng năm | Script | 2024.12.0 | date_conversion_tool.py |
| 42 | Tra ngày và đổi dương lịch ↔ âm lịch cho Assist | Script | 2024.12.0 | date_conversion_tool.py |
| 43 | Điều khiển nhạc bằng giọng nói | Script | 2024.12.0 | — |
| 44 | Điều khiển điều hoà | Script | 2024.12.0 | — |
| 45 | Điều khiển tốc độ và xoay quạt | Script | 2024.12.0 | — |
| 46 | Tìm vị trí thiết bị trong nhà | Script | 2024.12.0 | — |
| 47 | Làm điện thoại kêu để tìm máy | Script | 2024.12.0 | — |
| 48 | Hẹn giờ nhiều thiết bị bằng giọng nói | Script | 2024.12.0 | devices_scheduler.py |
| 49 | Hẹn giờ nhiều thiết bị | Script | 2024.12.0 | common_utilities.py |
| 50 | Điều khiển hẹn giờ bằng giọng nói | Script | 2024.12.0 | — |
| 51 | Bộ nhớ ghi nhớ cho Assist | Script | 2024.12.0 | memory.py |

---

**Nếu bạn thấy các blueprint này hữu ích, hãy chia sẻ cho cộng đồng Home Assistant và theo dõi để cập nhật thêm nhiều blueprint mới!**
