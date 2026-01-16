
## 🔗 Tạo ảnh Ai

Tạo ảnh theo promt.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fai_image_generator_full_llm.yaml
)

*Hãy đọc kỹ mô tả của từng blueprint và làm theo hướng dẫn trong đó nhé.*
## 🔗 kiểm tra camera

Tạo ảnh theo promt.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fvoice_camera_ai_analyzer.yaml
)
## 🔗 Gửi zalo có delete
Delete file homeassistant: https://github.com/chomupashchuk/delete-file-home-assistant
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fsend_to_zalo_custom_bot_full_llm.yaml
)
## 🔗 Gửi tele có delete
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fsend_to_telegram_full_llm.yaml
)
## 🔗 Tạo ảnh có đính kèm ảnh
 ```
Go to Settings → Devices & Services → Helpers
Click "+ Create Helper"
Choose "Text"
Name it appropriately
Set a max length (e.g., 255)
Save it
 ```
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fai_image_attrack.yaml
)
## 🔗 Tạo ảnh theo thời tiết
```
template
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
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2FAI_Weather_Image_Generator.yaml
)
## 🔗 Blueprint Phân tích (LLM):** Gửi ảnh chụp cho mô hình ngôn ngữ để phân tích và trả lời.
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Ffile_content_analyzer_full_llm.yaml
)
