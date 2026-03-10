# 🏠 Home Assistant Blueprints - TriTue2011

Bộ sưu tập **Home Assistant Blueprints** tích hợp AI (LLM) để tự động hóa nhà thông minh. Các blueprint được tối ưu cho **Gemini 2.5 Flash** — các mô hình khác có thể cần điều chỉnh nhỏ.

**[English version click here](/README.en.md)**

---

## 📑 Mục lục

- [🖼️ Tạo ảnh AI](#️-tạo-ảnh-ai)
- [🖼️ Tạo ảnh AI kèm ảnh tham chiếu](#️-tạo-ảnh-ai-kèm-ảnh-tham-chiếu)
- [🌤️ Tạo ảnh thời tiết bằng AI](#️-tạo-ảnh-thời-tiết-bằng-ai)
- [🌍 Tạo ảnh danh lam thắng cảnh](#-tạo-ảnh-danh-lam-thắng-cảnh)
- [📸 Kiểm tra camera bằng AI (Voice)](#-kiểm-tra-camera-bằng-ai-voice)
- [📷 Chụp ảnh camera (Voice)](#-chụp-ảnh-camera-voice)
- [🔍 Phân tích file / ảnh (LLM)](#-phân-tích-file--ảnh-llm)
- [🚨 Cảnh báo người qua camera bằng AI](#-cảnh-báo-người-qua-camera-bằng-ai)
- [👁️ LLM Vision Camera](#️-llm-vision-camera)
- [📩 Gửi Telegram (Voice + xóa file)](#-gửi-telegram-voice--xóa-file)
- [💬 Gửi Zalo Bot chính thức (Voice)](#-gửi-zalo-bot-chính-thức-voice)
- [🧩 Gửi Zalo Custom Bot (Voice + xóa file)](#-gửi-zalo-custom-bot-voice--xóa-file)
- [🗓️ Thông báo lịch âm & thời tiết](#️-thông-báo-lịch-âm--thời-tiết)
- [💬 Danh ngôn tự động hàng ngày](#-danh-ngôn-tự-động-hàng-ngày)
- [🔧 Kiểm tra thiết bị (Multi-Entity)](#-kiểm-tra-thiết-bị-multi-entity)
- [🔄 Tự động cập nhật Blueprints](#-tự-động-cập-nhật-blueprints)
- [🐍 Tự động cập nhật Pyscript](#-tự-động-cập-nhật-pyscript)

---

## 🖼️ Tạo ảnh AI

Tạo ảnh theo prompt bằng mô hình AI. Chỉ cần nói hoặc nhập mô tả, hệ thống sẽ tự sinh ảnh và lưu về Home Assistant.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fai_image_generator_full_llm.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 🖼️ Tạo ảnh AI kèm ảnh tham chiếu

Tạo ảnh AI với ảnh tham chiếu đính kèm (kính, trang phục, phụ kiện). Hỗ trợ nhớ ngữ cảnh và xử lý lỗi tốt hơn.

**Yêu cầu thiết lập trước:**

```
Vào Settings → Devices & Services → Helpers
Nhấn "+ Create Helper" → Chọn "Text"
Đặt tên phù hợp, max length 255
Lưu lại
```

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fai_image_attrack.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 🌤️ Tạo ảnh thời tiết bằng AI

Tự động tạo ảnh phù hợp với thời tiết hiện tại (sáng, trưa, chiều, tối, đêm).

**Yêu cầu thiết lập trước** — thêm vào `configuration.yaml`:

```yaml
shell_command:
  copy_weather_image: >
    mv "{{ source }}" "{{ destination }}"

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

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fai_creat_image_weather.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 🌍 Tạo ảnh danh lam thắng cảnh

Tự động tạo ảnh các danh lam thắng cảnh, công trình nổi tiếng trên thế giới bằng AI theo lịch trình hoặc khi được yêu cầu.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fworld_landmarks_image_generator.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 📸 Kiểm tra camera bằng AI (Voice)

Dùng giọng nói để yêu cầu AI phân tích camera — phát hiện người, thú cưng, phương tiện. Hỗ trợ khớp tên chính xác hoặc kiểm tra tất cả camera cùng lúc.

**Ví dụ lệnh giọng nói:**
- "Kiểm tra cửa trước có ai không?"
- "Camera sân có con chó không?"

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fvoice_camera_ai_analyzer.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 📷 Chụp ảnh camera (Voice)

Dùng giọng nói để ra lệnh chụp ảnh từ camera và lưu thành file. Dùng kết hợp với blueprint phân tích ảnh.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fcamera_snapshot_full_llm.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 🔍 Phân tích file / ảnh (LLM)

Gửi ảnh hoặc file cho mô hình ngôn ngữ lớn (LLM) để phân tích nội dung và nhận câu trả lời thông minh.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Ffile_content_analyzer_full_llm.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 🚨 Cảnh báo người qua camera bằng AI

Tự động phát cảnh báo khi AI phát hiện có người đi qua vùng giám sát của camera.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Falarm_person_camera.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 👁️ LLM Vision Camera

Tích hợp mô hình thị giác LLM với camera Home Assistant để phân tích hình ảnh thời gian thực.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fllmvison_camera.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 📩 Gửi Telegram (Voice + xóa file)

Gửi tin nhắn, ảnh hoặc file qua Telegram bằng giọng nói. Hỗ trợ tự động xóa file sau khi gửi.

**Ví dụ lệnh giọng nói:**
- "Gửi ảnh camera sân vào Telegram"
- "Gửi thông báo nhiệt độ phòng khách lên Telegram"

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fsend_to_telegram_full_llm.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 💬 Gửi Zalo Bot chính thức (Voice)

Gửi tin nhắn đến Zalo qua bot chính thức bằng giọng nói. Địa điểm tự động được kèm link Google Maps.

**Ví dụ lệnh giọng nói:**
- "Tìm nhà hàng ngon ở Hà Nội và gửi lên Zalo"
- "Gửi địa chỉ Văn Miếu lên Zalo"

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fsend_to_zalo_bot_full_llm.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 🧩 Gửi Zalo Custom Bot (Voice + xóa file)

Gửi tin nhắn, ảnh, video qua Zalo Custom Bot. Hỗ trợ webhook, đồng bộ trạng thái và xóa file sau khi gửi.

> **Yêu cầu:** Tích hợp xóa file Home Assistant — [delete-file-home-assistant](https://github.com/chomupashchuk/delete-file-home-assistant)

**Ví dụ lệnh giọng nói:**
- "Gửi ảnh camera sân cho nhóm gia đình qua Zalo"
- "Gửi địa chỉ Hồ Tây cho vợ qua Zalo"

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fsend_to_zalo_custom_bot_full_llm.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 🗓️ Thông báo lịch âm & thời tiết

Tự động nhắc nhở các sự kiện âm lịch kèm theo thông tin thời tiết hàng ngày.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fcalendar_weather_notification.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 💬 Danh ngôn tự động hàng ngày

Tự động lấy câu danh ngôn, châm ngôn, ca dao, tục ngữ ngẫu nhiên từ AI và cập nhật vào `input_text`.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fdaily_quote.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 🔧 Kiểm tra thiết bị (Multi-Entity)

Kiểm tra trạng thái nguồn gốc của nhiều thiết bị cùng lúc. Hữu ích cho debug và giám sát hệ thống.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fcheck_device.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 🔄 Tự động cập nhật Blueprints

Quản lý việc kiểm tra và cập nhật blueprints tự động, với thông báo qua Zalo khi có phiên bản mới.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2FBlueprints_update_manager.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

## 🐍 Tự động cập nhật Pyscript

Tự động đồng bộ file / thư mục từ GitHub về `/config/pyscript`, giữ script luôn ở phiên bản mới nhất.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2FBlueprint_pyscript_update_manager.yaml)

*Hãy đọc kỹ mô tả blueprint trước khi sử dụng.*

---

**Nếu bạn thấy các blueprint này hữu ích, hãy chia sẻ cho cộng đồng Home Assistant và theo dõi để cập nhật thêm nhiều blueprint mới!**
