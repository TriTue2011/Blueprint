# 🏠 Home Assistant Blueprints - TriTue2011

A collection of **Home Assistant Blueprints** powered by AI (LLM) to automate your smart home. All blueprints are fine-tuned for **Gemini 2.5 Flash** — other models may need minor adjustments.

**[Phiên bản tiếng Việt / Vietnamese version click here](/README.md)**

---

## 📑 Table of Contents

- [🖼️ AI Image Generator](#️-ai-image-generator)
- [🖼️ AI Image Generator with Reference Image](#️-ai-image-generator-with-reference-image)
- [🌤️ AI Weather Image Generator](#️-ai-weather-image-generator)
- [🌍 World Landmarks Image Generator](#-world-landmarks-image-generator)
- [📸 Smart Camera AI Analyzer (Voice)](#-smart-camera-ai-analyzer-voice)
- [📷 Capture Camera Snapshot (Voice)](#-capture-camera-snapshot-voice)
- [🔍 File / Image Content Analyzer (LLM)](#-file--image-content-analyzer-llm)
- [🚨 Person Detection Camera Alarm](#-person-detection-camera-alarm)
- [👁️ LLM Vision Camera](#️-llm-vision-camera)
- [📩 Send to Telegram (Voice + Delete File)](#-send-to-telegram-voice--delete-file)
- [💬 Send to Zalo Official Bot (Voice)](#-send-to-zalo-official-bot-voice)
- [🧩 Send to Zalo Custom Bot (Voice + Delete File)](#-send-to-zalo-custom-bot-voice--delete-file)
- [🗓️ Lunar Calendar & Weather Notification](#️-lunar-calendar--weather-notification)
- [💬 Daily Quote Automation](#-daily-quote-automation)
- [🔧 Check Device Source (Multi-Entity)](#-check-device-source-multi-entity)
- [🔄 Auto-Update Blueprints](#-auto-update-blueprints)
- [🐍 Auto-Update Pyscript](#-auto-update-pyscript)

---

## 🖼️ AI Image Generator

Generate images from a text prompt using AI. Just describe what you want and the system creates and saves the image directly to Home Assistant.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fai_image_generator_full_llm.yaml)

*Please carefully read the blueprint description before getting started.*

---

## 🖼️ AI Image Generator with Reference Image

Generate AI images with an attached reference image (glasses, clothing, accessories). Includes memory support and improved error handling.

**Pre-setup required:**

```
Go to Settings → Devices & Services → Helpers
Click "+ Create Helper" → Choose "Text"
Name it appropriately, set max length to 255
Save
```

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fai_image_attrack.yaml)

*Please carefully read the blueprint description before getting started.*

---

## 🌤️ AI Weather Image Generator

Automatically generate weather-appropriate images based on current conditions and time of day (morning, noon, afternoon, evening, night).

**Pre-setup required** — add to `configuration.yaml`:

```yaml
shell_command:
  copy_weather_image: >
    mv "{{ source }}" "{{ destination }}"

template:
  - sensor:
      - name: "Time of Day"
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
          {% if 6 <= h < 11 %} Morning
          {% elif 11 <= h < 13 %} Noon
          {% elif 13 <= h < 18 %} Afternoon
          {% elif 18 <= h < 21 %} Evening
          {% else %} Night
          {% endif %}
        attributes:
          hour: "{{ now().hour }}"
          is_night: >-
            {% set h = now().hour %}
            {{ h < 6 or h >= 21 }}
          is_daytime: >-
            {% set h = now().hour %}
            {{ h >= 6 and h < 18 }}
```

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fai_creat_image_weather.yaml)

*Please carefully read the blueprint description before getting started.*

---

## 🌍 World Landmarks Image Generator

Automatically generate AI images of famous world landmarks and monuments on a schedule or on demand.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fworld_landmarks_image_generator.yaml)

*Please carefully read the blueprint description before getting started.*

---

## 📸 Smart Camera AI Analyzer (Voice)

Use voice commands to ask AI to analyze your cameras — detecting people, pets, and vehicles. Supports exact name matching or scanning all cameras simultaneously.

**Example voice commands:**
- "Check the front door camera, is anyone there?"
- "Is there a dog in the yard camera?"

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fvoice_camera_ai_analyzer.yaml)

*Please carefully read the blueprint description before getting started.*

---

## 📷 Capture Camera Snapshot (Voice)

Use voice commands to take a snapshot from any camera and save it as a file. Works best when combined with the File Content Analyzer blueprint.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fcamera_snapshot_full_llm.yaml)

*Please carefully read the blueprint description before getting started.*

---

## 🔍 File / Image Content Analyzer (LLM)

Send an image or file to a large language model (LLM) for content analysis and receive intelligent responses.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Ffile_content_analyzer_full_llm.yaml)

*Please carefully read the blueprint description before getting started.*

---

## 🚨 Person Detection Camera Alarm

Automatically trigger an alarm when AI detects a person passing through a camera's monitored zone.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Falarm_person_camera.yaml)

*Please carefully read the blueprint description before getting started.*

---

## 👁️ LLM Vision Camera

Integrate an LLM vision model with Home Assistant cameras for real-time image analysis and understanding.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fllmvison_camera.yaml)

*Please carefully read the blueprint description before getting started.*

---

## 📩 Send to Telegram (Voice + Delete File)

Send messages, images, or files to Telegram by voice. Automatically deletes files after sending.

**Example voice commands:**
- "Send the yard camera snapshot to Telegram"
- "Send the living room temperature to Telegram"

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fsend_to_telegram_full_llm.yaml)

*Please carefully read the blueprint description before getting started.*

---

## 💬 Send to Zalo Official Bot (Voice)

Send messages to Zalo via the official bot using voice commands. Locations automatically include a Google Maps link.

**Example voice commands:**
- "Find great restaurants in Hanoi and send to Zalo"
- "Send the address of the Temple of Literature to Zalo"

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fsend_to_zalo_bot_full_llm.yaml)

*Please carefully read the blueprint description before getting started.*

---

## 🧩 Send to Zalo Custom Bot (Voice + Delete File)

Send messages, images, and videos via a Zalo Custom Bot. Supports webhooks, state syncing, and automatic file deletion after sending.

> **Requires:** [delete-file-home-assistant](https://github.com/chomupashchuk/delete-file-home-assistant) integration

**Example voice commands:**
- "Send the yard camera photo to the family Zalo group"
- "Send West Lake address to my wife on Zalo"

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fsend_to_zalo_custom_bot_full_llm.yaml)

*Please carefully read the blueprint description before getting started.*

---

## 🗓️ Lunar Calendar & Weather Notification

Automatically send daily reminders for lunar calendar events combined with current weather information.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fcalendar_weather_notification.yaml)

*Please carefully read the blueprint description before getting started.*

---

## 💬 Daily Quote Automation

Automatically fetch a random quote, proverb, or saying from AI and update it into an `input_text` helper daily.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fdaily_quote.yaml)

*Please carefully read the blueprint description before getting started.*

---

## 🔧 Check Device Source (Multi-Entity)

Check the source state of multiple devices at once. Useful for debugging and system monitoring.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fcheck_device.yaml)

*Please carefully read the blueprint description before getting started.*

---

## 🔄 Auto-Update Blueprints

Automatically check for and apply blueprint updates, with Zalo notifications when new versions are available.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2FBlueprints_update_manager.yaml)

*Please carefully read the blueprint description before getting started.*

---

## 🐍 Auto-Update Pyscript

Automatically sync files and folders from GitHub to `/config/pyscript`, keeping your scripts always up to date.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2FBlueprint_pyscript_update_manager.yaml)

*Please carefully read the blueprint description before getting started.*

---

**If you find these blueprints helpful, please share them with the Home Assistant community — and follow along for more unique blueprints coming soon!**
