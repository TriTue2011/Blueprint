# 🏠 Home Assistant Blueprints - TriTue2011

A collection of **Home Assistant Blueprints** powered by AI (LLM) to automate your smart home. Most blueprints are tuned for **Gemini 2.5 Flash** — other models may need minor adjustments. The newest camera blueprints run on any AI Task provider, including models hosted at home.

**[Phiên bản tiếng Việt / Vietnamese version click here](/README.md)**

---

## 📑 Table of Contents

- [⚙️ General Requirements](#️-general-requirements)
- **AI Image Generation**
  - [🖼️ AI Image Generator](#️-ai-image-generator)
  - [🖼️ AI Image Generator with Reference Image](#️-ai-image-generator-with-reference-image)
  - [🌤️ AI Weather Image Generator](#️-ai-weather-image-generator)
  - [🌍 World Landmarks Image Generator](#-world-landmarks-image-generator)
- **Cameras & Surveillance**
  - [📸 Smart Camera AI Analyzer (Voice)](#-smart-camera-ai-analyzer-voice)
  - [📷 Capture Camera Snapshot or Record Video (Voice)](#-capture-camera-snapshot-or-record-video-voice)
  - [🔍 File / Image Content Analyzer (LLM)](#-file--image-content-analyzer-llm)
  - [🚨 Person Detection Camera Alarm](#-person-detection-camera-alarm)
  - [🎥 Camera AI Alarm 4 — Filter Gate, Dual Snapshots, Video](#-camera-ai-alarm-4--filter-gate-dual-snapshots-video)
  - [⏰ Keep the AI Model Awake](#-keep-the-ai-model-awake)
  - [👁️ LLM Vision Camera](#️-llm-vision-camera)
- **Messaging**
  - [📩 Send to Telegram (Voice + Delete File)](#-send-to-telegram-voice--delete-file)
  - [💬 Send to Zalo Official Bot (Voice)](#-send-to-zalo-official-bot-voice)
  - [🧩 Send to Zalo Custom Bot (Voice + Delete File)](#-send-to-zalo-custom-bot-voice--delete-file)
  - [🔗 Zalo Calling in the older blueprints](#-zalo-calling-in-the-older-blueprints)
  - [🎤 Voice send to Zalo Calling (many people and groups)](#-voice-send-to-zalo-calling-many-people-and-groups)
  - [🧭 One button, many jobs (most recent request wins)](#-one-button-many-jobs-most-recent-request-wins)
  - [🎮 R1 speaker middle button, every gesture in one automation](#-r1-speaker-middle-button-every-gesture-in-one-automation)
  - [📞 Zalo Call alert call when a sensor triggers](#-zalo-call-alert-call-when-a-sensor-triggers)
  - [🔘 Zalo Call one button to answer, hang up or call](#-zalo-call-one-button-to-answer-hang-up-or-call)
  - [📲 Zalo Call incoming-call rules](#-zalo-call-incoming-call-rules)
  - [💬 Zalo Call custom Messenger](#-zalo-call-custom-messenger)
  - [💬 Zalo Call two-way chat with the assistant](#-zalo-call-two-way-chat-with-the-assistant)
  - [⏰ Zalo Call scheduled reminder call or message](#-zalo-call-scheduled-reminder-call-or-message)
  - [📱 Zalo Call custom outgoing call](#-zalo-call-custom-outgoing-call)
  - [🔔 Zalo Call button for incoming calls](#-zalo-call-button-for-incoming-calls)
  - [🎥 Zalo Call caller asks to switch to video](#-zalo-call-caller-asks-to-switch-to-video)
  - [🔁 luuquangvu automations (webhooks, timers, linking)](#-luuquangvu-automations-webhooks-timers-linking)
  - [🧠 luuquangvu scripts for Assist (search, calendar, memory, timers)](#-luuquangvu-scripts-for-assist-search-calendar-memory-timers)
- **Utilities**
  - [🗓️ Lunar Calendar & Weather Notification](#️-lunar-calendar--weather-notification)
  - [💬 Daily Quote Automation](#-daily-quote-automation)
  - [🔧 Check Device Source (Multi-Entity)](#-check-device-source-multi-entity)
  - [⏳ Cooldown timer that survives restarts](#-cooldown-timer-that-survives-restarts)
- **Management & Updates**
  - [🔄 Auto-Update Blueprints](#-auto-update-blueprints)
  - [🐍 Auto-Update Pyscript](#-auto-update-pyscript)
- **Advanced Guides**
  - [🏷️ Create the Assist Alias Sensor](#️-create-the-assist-alias-sensor)
  - [✅ Validate Blueprints Before Pushing](#-validate-blueprints-before-pushing)
  - [📊 Blueprint Overview](#-blueprint-overview)

---

## ⚙️ General Requirements

| Requirement | Details |
|-------------|---------|
| **Home Assistant** | Minimum version varies per blueprint (2024.10.0 – 2026.3.0) |
| **AI Model** | **Gemini 2.5 Flash** recommended (supports both generation and analysis) |
| **AI Task Entity** | Must be created and configured in **Settings → General** (needed by the image/analysis blueprints) |
| **Voice Assistant** | Optional — required only for the voice-driven blueprints |

> **Important:** after you create a script from a blueprint, **expose the script to Assist** so it can be voice-controlled. Do not rename the default script.


**Which blueprint needs which `.py` file** (files are in `scripts/`; install steps in “Install Pyscript”):

| `.py` file | Blueprints that use it |
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

## 🖼️ AI Image Generator

Generate images from a text prompt using AI. Just describe what you want and the system creates and saves the image directly to Home Assistant.

| Info | Details |
|------|---------|
| **Type** | Script |
| **HA minimum** | 2025.8.0 |
| **Requires** | An AI Task entity that supports image generation |

> **Running chatgpt2api? Do not install this blueprint.** The
> [chatgpt2api](https://github.com/TriTue2011/chatgpt2api) gateway already ships a
> `generate_image` tool that works from every channel — Zalo, Telegram and the in-house
> assistant — plus `library_media` to browse results and `delete_media` to clean up. Tick
> **🎨 Ảnh** under **Settings → Home Assistant → capability limits** and saying "draw me a cat"
> to a speaker produces an image, with no script in Home Assistant at all.
>
> Installing both breaks in two ways. First, the assistant ends up with two tools both claiming
> "I draw images" and picks the wrong one. Second, the field descriptions of these two
> blueprints weigh **3,918 characters**, and they enter the tool schema on **every single chat
> turn** — including turns where you only asked what time it is. For comparison: all five
> messaging and file-analysis scripts combined, after compression, cost 1,784.
>
> Without chatgpt2api the blueprint still works standalone.

**Configuration:**
- **AI Task Entity:** pick an AI Task entity capable of generating images (leave empty to use the system default)
- **Output Directory:** where images are saved (default: `/media`)
- **Filename Prefix:** filename prefix (default: `ai_generated_`)

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fai_image_generator_full_llm.yaml)

*Please read the blueprint description carefully before getting started.*

---

## 🖼️ AI Image Generator with Reference Image

Generate AI images with an attached reference image (glasses, clothing, accessories). Includes context memory and improved error handling.

| Info | Details |
|------|---------|
| **Type** | Script |
| **HA minimum** | 2025.8.0 |
| **Requires** | Input Text Helper |

> **Running chatgpt2api? Do not install this blueprint.** The
> [chatgpt2api](https://github.com/TriTue2011/chatgpt2api) gateway already ships a
> `generate_image` tool that works from every channel — Zalo, Telegram and the in-house
> assistant — plus `library_media` to browse results and `delete_media` to clean up. Tick
> **🎨 Ảnh** under **Settings → Home Assistant → capability limits** and saying "draw me a cat"
> to a speaker produces an image, with no script in Home Assistant at all.
>
> Installing both breaks in two ways. First, the assistant ends up with two tools both claiming
> "I draw images" and picks the wrong one. Second, the field descriptions of these two
> blueprints weigh **3,918 characters**, and they enter the tool schema on **every single chat
> turn** — including turns where you only asked what time it is. For comparison: all five
> messaging and file-analysis scripts combined, after compression, cost 1,784.
>
> Without chatgpt2api the blueprint still works standalone.

**Pre-setup required — create an Input Text Helper:**

```
Go to Settings → Devices & Services → Helpers
Click "+ Create Helper" → Choose "Text"
Name it appropriately, set max length to 255
Save
```

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fai_image_attrack.yaml)

*Please read the blueprint description carefully before getting started.*

---

## 🌤️ AI Weather Image Generator

Automatically generate weather-appropriate images based on current conditions and time of day (morning, noon, afternoon, evening, night).

| Info | Details |
|------|---------|
| **Type** | Automation |
| **HA minimum** | 2025.10.0 |
| **Requires** | Shell Command + Template Sensor |

**Pre-setup required** — add to `configuration.yaml`:

**1. A Shell Command** to move the generated image:

```yaml
shell_command:
  copy_weather_image: >
    mv "{{ source }}" "{{ destination }}"
```

Or use the NVIDIA API instead. In `configuration.yaml`:

```yaml
pyscript:
  allow_all_imports: true
  hass_is_global: true
  nvidia_api_key: !secret nvidia_api_key
```

In `secrets.yaml`:

```yaml
nvidia_api_key: "nvapi-xxx"
```

Then download [`scripts/weather_image.py`](/scripts/weather_image.py) into your `pyscript` folder. Pyscript installation instructions: <https://github.com/custom-components/pyscript>.

**2. A Template Sensor** that reports the time of day:

```yaml
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

**Gemini version.** Uses the [Gemini-FastAPI](https://github.com/luuquangvu/Gemini-FastAPI) add-on together with the [hass_local_openai_llm](https://github.com/luuquangvu/hass_local_openai_llm) integration.

**Needs Pyscript file(s):** `weather_image.py`, `flow_image.py`, `zalo_bot_handle_tool.py` (in the `scripts/` folder, copy to `/config/pyscript/`).

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fai_creat_image_weather.yaml)

**NVIDIA API version.** Register at <https://build.nvidia.com> and use the [hass_local_openai_llm](https://github.com/luuquangvu/hass_local_openai_llm) integration.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fai_creat_image_weather_2.yaml)

**Merged version** — both of the above, plus sending the image over Zalo.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fai_creat_image_weather_3.yaml)

*Please read the blueprint description carefully before getting started.*

---

## 🌍 World Landmarks Image Generator

Automatically generate AI images of famous world landmarks and monuments on a schedule or on demand.

| Info | Details |
|------|---------|
| **Type** | Automation |
| **HA minimum** | 2025.10.0 |

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fworld_landmarks_image_generator.yaml)

*Please read the blueprint description carefully before getting started.*

---

## 📸 Smart Camera AI Analyzer (Voice)

Use voice commands to ask AI to analyze your cameras — detecting people, pets, and vehicles. Matches camera names exactly, falls back to aliases, or checks every camera at once.

| Info | Details |
|------|---------|
| **Type** | Script |
| **HA minimum** | 2025.8.0 |
| **Requires** | AI Task entity, camera entities, alias sensor |

**Features:**
- Matches the exact `friendly_name` first
- Falls back to alias lookup (template sensor)
- If nothing matches, checks every camera (multi-mode)
- Parallel (fast) or sequential execution

**Configuration:**
- **Entity Aliases:** the alias sensor that maps camera names — must be created first, see [Create the Assist Alias Sensor](#️-create-the-assist-alias-sensor)
- **AI Task Entity:** pick an AI Task entity (leave empty for the default)
- **Multi-Camera Check Mode:** parallel (fast) or sequential

**Example voice commands:**
- "Check the front door camera, is anyone there?"
- "Is there a dog in the yard camera?"

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fvoice_camera_ai_analyzer.yaml)

*Please read the blueprint description carefully before getting started.*

---

## 📷 Capture Camera Snapshot or Record Video (Voice)

Name a camera to take a snapshot, or **record a 1–60 second clip**. Returns the file path for another blueprint to pick up — pair it with [File / Image Content Analyzer](#-file--image-content-analyzer-llm) to get "capture it, then tell me what you see".

| Info | Details |
|------|---------|
| **Type** | Script |
| **HA minimum** | 2024.12.0 |
| **Requires** | Alias sensor (see [guide](#️-create-the-assist-alias-sensor)), camera entities |

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fcamera_snapshot_full_llm.yaml)

*Please read the blueprint description carefully before getting started.*

---

## 🔍 File / Image Content Analyzer (LLM)

Send an image or file to a large language model for content analysis and get an intelligent answer back.

| Info | Details |
|------|---------|
| **Type** | Script |
| **HA minimum** | 2025.8.0 |
| **Requires** | AI Task entity |

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Ffile_content_analyzer_full_llm.yaml)

*Please read the blueprint description carefully before getting started.*

---

## 🚨 Person Detection Camera Alarm

Analyze camera events with AI Task when someone enters the monitored zone. Sends a notification with the snapshot and the AI analysis to your phone, Telegram, Zalo, and TTS speakers.

| Info | Details |
|------|---------|
| **Type** | Automation |
| **HA minimum** | 2025.7.0 (Gemini and OpenAI versions) — 2026.3.0 (merged version) |
| **Requires** | Binary sensor (trigger), camera entity |

**Configuration:**
- **Trigger Sensor:** the sensor that fires the automation (door, motion) — domain `binary_sensor`
- **Trigger States:** from/to states (default: off → on)
- **Person Occupancy Sensor:** (optional) wait for person detection before analyzing
- **Maximum Wait Time:** how long to wait for person detection (0 = no limit)

**Notification channels:** mobile app, Telegram, Zalo Bot / Zalo Custom Bot, and TTS.

**Gemini**

**Needs Pyscript file(s):** `zalo_bot_handle_tool.py` (in the `scripts/` folder, copy to `/config/pyscript/`).

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Falarm_person_camera.yaml)

**OpenAI**

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Falarm_person_camera_2.yaml)

**Merged OpenAI + Gemini**, with animal analysis added.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Falarm_person_camera_3.yaml)

*Please read the blueprint description carefully before getting started.*

---

## 🎥 Camera AI Alarm 4 — Filter Gate, Dual Snapshots, Video

A rewrite of the blueprint above, aimed at **homes** — apartments and houses — rather than busy public spaces. Three things are new: a cheap filter gate that stops false alarms before any real work happens, a separation between the images the AI reads and the images you receive, and a video branch that runs alongside the image branch.

| Info | Details |
|------|---------|
| **Type** | Automation |
| **HA minimum** | 2026.3.0 |
| **Requires** | Binary sensor (trigger), camera entity, one AI Task entity |
| **Works with** | Google Gemini, OpenAI, Ollama, and every other AI Task provider |

### The single-image filter gate

When enabled, every sensor trigger captures **one** frame from the analysis camera and asks the AI exactly one question: is there a person or not. If nobody is there, the run stops immediately — no further captures, no video, no analysis. The prompt for this step is deliberately tiny, because it runs on every trigger including the empty ones.

### Two separate camera streams

This is the biggest change from version 3. You configure two cameras:

- **Camera the AI reads** — pick the substream, usually suffixed `-sub`.
- **Camera for the images sent to you** — pick the main stream so the pictures you receive are sharp.

Each capture beat grabs **both frames at the same instant**, and only then waits out the interval before the next beat. So when the AI reports "frame 2 was the clearest", the sharp frame 2 really is that moment.

Why it is worth doing, measured on real hardware with Qwen3-VL-4B:

| Fed to the AI | Tokens | Time |
|---|---|---|
| 3 substream images | 978 | ~1.0 s |
| 3 main-stream images | 8,425 | ~20 s |

Same scene, same people recognized, same description. High-resolution frames are for human eyes; feeding them to the AI costs twenty times more for nothing.

### Six delivery cases

Images, video, and the analysis text each get their own option with three choices: send always, send only when a person is present, or send only on a security concern. The analysis never travels alone — it is attached only when an image or a video has already been sent, so three by three collapses into six real situations.

| # | Send media when | Send analysis when | What you get |
|---|---|---|---|
| 1 | Always | Alongside | Image arrives immediately, text follows once analysis finishes |
| 2 | Always | Person present | Every trigger brings an image; an empty room brings no text |
| 3 | Always | Security concern | Every trigger brings an image; only suspicious events add text |
| 4 | Person present | Alongside | Silent when nobody is there; both when someone is |
| 5 | Person present | Security concern | A person means an image; text only when it looks suspicious |
| 6 | Security concern | Alongside | Completely silent except when suspicious — the least intrusive |

The three rows involving "security concern" only work in **Security** analysis mode, because the other three modes never ask the AI whether something is suspicious. Choose the wrong combination and the blueprint quietly downgrades it to "person present" and writes a line to the log so you know, rather than silently sending nothing.

### A single image or video carries its analysis with it

Telegram and personal Zalo both allow a caption on an image or video, so you receive exactly **one** message with both the picture and the words. Only multi-image sends have to split into two messages, because the album API has no place for a caption.

Each channel has a different ceiling and the blueprint accounts for it: Telegram groups up to 10 images per album, personal Zalo up to 50, Zalo Bot has no album so each image is its own message, and phone notifications get one notification per image.

### Tapping the notification opens that exact image

Image paths are left relative, so the app resolves them against whichever server sent the notification: your LAN at home, your domain when you are out. You never configure an address.

### The speaker reads a sentence the AI rewrote

The on-screen sentence has emoji, colons, and abbreviated timestamps — read aloud verbatim it sounds bizarre. Enable this option and the AI rewrites it into something speakable: symbols dropped, numbers spelled out, under thirty words. Disable it and you get the pre-built sentence.

### Waking the model the moment the sensor fires

For anyone running a model at home and letting it sleep to free the GPU. The blueprint fires an empty call the instant the trigger happens, in parallel with waiting for confirmation, so the model finishes loading before it is actually needed. Measured at home: calling a sleeping model takes 11.8 seconds, calling an awake one takes 1.0 second — with this enabled most of that gap elapses while you are still waiting anyway.

### Configuration

Twelve sections, 63 fields. The ones worth attention:

- **Confirmation method** — one field with three values: no confirmation, wait then re-check the same sensor, or watch a different sensor. One path only, no stacked waiting like the old version.
- **Camera the AI reads** and **Camera for images sent to you** — two different streams, see above.
- **What to analyze** — people only, animals only, both, or security.
- **AI Task for the filter gate** — can be set separately, because this step asks a single question and can go to a small model even when full analysis goes to a large one off-site.
- **Video duration** and **seconds of lookback before the trigger** — Home Assistant keeps a rolling buffer, so you can reach back and capture the moment the person first stepped into frame.

### Configuration requirement

Add this to `configuration.yaml` so Home Assistant resolves the media directory correctly:

```yaml
homeassistant:
  media_dirs:
    local: /media
```

Without it, neither AI Task nor phone notifications can read the images.

If you want the video branch to feed the mp4 directly to the AI, you need a provider that reads video — currently Google Gemini. Models running at home through Ollama or llama.cpp accept still images only, so with those keep video on send-only, which is also the default.

**Needs Pyscript file(s):** `zalo_bot_handle_tool.py` (in the `scripts/` folder, copy to `/config/pyscript/`).

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Falarm_person_camera_4.yaml)

*Please read the blueprint description carefully before getting started.*

---

## ⏰ Keep the AI Model Awake

For anyone running a model at home who has already configured it to sleep when idle to free the GPU. This automation sends one empty call on a cycle, often enough that the model never falls asleep — but only during the hours when you need alarms to be fastest.

| Info | Details |
|------|---------|
| **Type** | Automation |
| **HA minimum** | 2026.3.0 |
| **Requires** | An AI Task entity pointing at a locally hosted model |

### Why it is needed

Measured on an RTX 2060 SUPER with Qwen3-VL-4B:

| Called while | Time |
|---|---|
| Model asleep | **11,804 ms** |
| Model awake | 1,044 ms |

Those ten seconds **cannot be tuned away**. Five configurations were tried, two runs each: stock, plus `--mlock`, context window halved, both combined, and KV cache quantized to q8_0. All ten runs landed between 10.1 and 10.4 seconds. It is the cost of rebuilding the CUDA context and pushing weights onto the card, and no flag reaches it.

So the only remedy is to **wake up less often**. This automation keeps the model awake through the window you choose, so every alarm in that window answers within a second.

### The cost

The model holds VRAM for the whole window — around 4.4 GB on an 8 GB card for Qwen3-VL-4B. Pick a window where the GPU has nothing else to do. Night is usually the right answer: it is both when alarms matter most and when you are not issuing voice commands or translating subtitles.

### One thing that is easy to get wrong

**The call interval must be shorter than the model's idle timeout.** With `--sleep-idle-seconds 300`, calling every 4 minutes is right. If your idle timeout is only 30 seconds this automation cannot keep up — raise the timeout first, then use it.

### Configuration

- **AI Task** — the entity pointing at your local model. Do not point it at a metered cloud service; this automation makes hundreds of calls per night.
- **Call every N minutes** — default 4.
- **Start** and **Stop keeping awake** — setting the end time earlier than the start time means the window crosses midnight, e.g. 22:00 to 06:00, and Home Assistant reads it correctly.
- **Additional conditions** — for example only stay awake while the alarm is armed, or while somebody is home.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fgiu_model_thuc.yaml)

*Please read the blueprint description carefully before getting started.*

---

## 👁️ LLM Vision Camera

Summarize door events with AI, including person detection. Sends notifications to your phone and Zalo, and analyzes the camera when the door opens.

| Info | Details |
|------|---------|
| **Type** | Automation |
| **HA minimum** | 2024.10.0 |
| **Requires** | Door contact sensor, person occupancy sensor, camera |

**Configuration:**
- **Door Contact Sensor:** the door sensor (`binary_sensor`)
- **Door States:** from/to states (default: off → on)
- **Person Occupancy Sensor:** the person detection sensor
- **Wait for Person Detection:** whether to wait at all
- **Person Detection Wait Time:** how long to wait

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fllmvison_camera.yaml)

*Please read the blueprint description carefully before getting started.*

---

## 📩 Send to Telegram (Voice + Delete File)

Send messages, images, or files to Telegram by voice. Can delete the file automatically after sending.

| Info | Details |
|------|---------|
| **Type** | Script |
| **HA minimum** | 2024.10.0 |
| **Requires** | Telegram Bot integration |

**Example voice commands:**
- "Send the yard camera snapshot to Telegram"
- "Send the living room temperature to Telegram"

**Needs Pyscript file(s):** `telegram_bot_handle_tool.py` (in the `scripts/` folder, copy to `/config/pyscript/`).

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fsend_to_telegram_full_llm.yaml)

*Please read the blueprint description carefully before getting started.*

---

## 💬 Send to Zalo Official Bot (Voice)

Send messages to Zalo via the official bot using voice commands. Locations automatically include a Google Maps link.

| Info | Details |
|------|---------|
| **Type** | Script |
| **HA minimum** | 2024.10.0 |
| **Requires** | Zalo Bot integration (HACS) |

**Example voice commands:**
- "Find great restaurants in Hanoi and send to Zalo"
- "Send the address of the Temple of Literature to Zalo"

**Needs Pyscript file(s):** `zalo_bot_handle_tool.py` (in the `scripts/` folder, copy to `/config/pyscript/`).

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fsend_to_zalo_bot_full_llm.yaml)

*Please read the blueprint description carefully before getting started.*

---

## 🧩 Send to Zalo Custom Bot (Voice + Delete File)

Send messages, images, and videos through a personal Zalo account. Supports webhooks, state syncing, and deleting the file after sending.

| Info | Details |
|------|---------|
| **Type** | Script |
| **HA minimum** | 2024.10.0 |
| **Requires** | Zalo Bot integration (HACS) + [delete-file-home-assistant](https://github.com/chomupashchuk/delete-file-home-assistant) |

> **This is a fork-local branch.** On 2026-08-18 the upstream repository [luuquangvu/tutorials](https://github.com/luuquangvu/tutorials) dropped the Zalo Custom Bot path and folded everything into the official OA bot. The blueprint below is kept and maintained here instead, because it sends through a **personal Zalo account** — something the OA bot cannot do. Do not install it alongside [Send to Zalo Official Bot](#-send-to-zalo-official-bot-voice): two scripts both claiming to send to Zalo will make the assistant pick the wrong one.

**Zalo configuration:**
- **Account:** the Zalo account phone number
- **Thread ID:** the conversation ID
- **Type of Receiver:** user (0) or group (1)
- **TTL:** self-destruct time in ms, 0 = never
- **Delete After Send:** remove the image file after sending

**Example voice commands:**
- "Send the yard camera photo to the family Zalo group"
- "Send West Lake address to my wife on Zalo"

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fsend_to_zalo_custom_bot_full_llm.yaml)

*Please read the blueprint description carefully before getting started.*

---

## 📞 Zalo Call alert call when a sensor triggers

When a sensor triggers (person, smoke, water leak, open door, power loss...) **call the person you pick on Zalo**: the alert is read out, then the home speaker, mic and camera are connected. Calls people **one after another** until someone answers. **Everything is picked from lists**, no typing ids.

**Needs:** Zalo Call 2026.11.11.2 or newer; recipients picked in *Zalo Call → Configure*.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fzalo_call_alert_sensor.yaml)

---

## 🔘 Zalo Call one button to answer, hang up or call

**One button, different jobs depending on the moment:** incoming call → answer, in a call → hang up, idle → call / alert call / message. Pick the button with the trigger picker (R1 speaker center key, Zigbee button, virtual button...).

**Needs:** Zalo Call 2026.11.11.2 or newer; the Zalo Call «Call status» sensor.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fzalo_call_nut_bam.yaml)

---

## 📲 Zalo Call incoming-call rules

Decide what happens when **someone calls in**: **announce on a speaker**, **auto-answer**, let the **AI talk**, and **which home devices to connect** when a person takes over (tick Mic / Speaker / Camera; ticking Camera makes it a video call). Apply to one person, all contacts, strangers or all groups.

**Video switch request:** pick «Auto-accept» per person; it only takes effect when the **«Cho phép đồng ý chuyển sang video»** switch (video-switch consent) on the Zalo Call device is **ON** (off by default; there is a box that turns it on when Home Assistant starts). Applies to incoming and outgoing calls.

**Needs:** Zalo Call 2026.11.11.2 or newer.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fzalo_call_incoming_rule.yaml)

---

## 💬 Zalo Call custom Messenger

Send a Zalo message (or call) when a device changes, **widely customizable but only by picking from lists**: watched devices, mode (any change, on, off, above/below a threshold, daily report), ready-made sentences, text style (emoji, bold, color, size), recipients.

**Needs:** Zalo Call 2026.11.11.2 or newer; recipients picked in *Zalo Call → Configure*.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fzalo_call_messenger.yaml)

---

## 💬 Zalo Call two-way chat with the assistant

Whoever messages your Zalo account (the people or groups you pick) gets a reply from the **Home Assistant conversation assistant**, which keeps the thread per person/group. Pick people/groups from the address book or paste a **Zalo ID** for strangers; in groups it only answers when the message contains the **trigger word**. **No Pyscript, no bot token, no separate webhook**: the integration receives the messages from the app.

**Needs:** Zalo Call connected to the app and a conversation assistant with an AI model selected. Do not enable it together with Zalo Call's `reply_ai` rule for the same person/group (each message would be answered twice).

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fzalo_call_webhook.yaml)

---

## ⏰ Zalo Call scheduled reminder call or message

At the chosen time, **call someone on Zalo and read a reminder** (or message them): medicine, bedtime, wake-up, meals, water, exercise, meetings, watering plants. Great for older relatives who rarely read messages.

**Needs:** Zalo Call 2026.11.11.2 or newer; recipients picked in *Zalo Call → Configure*.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fzalo_call_nhac_hen.yaml)

---

## 📱 Zalo Call custom outgoing call

Call one person on **any event** (button, time, sensor): voice or video, what to say, AI or not, mic/speaker/camera and volume. Only calls when idle.

**Needs:** Zalo Call 2026.11.11.4 or newer.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fzalo_call_goi_di.yaml)

---

## 🔔 Zalo Call button for incoming calls

Give one button one job: **answer**, **reject**, **hang up**, **volume up/down**. Only acts at the right moment (ringing / in a call).

**Needs:** Zalo Call 2026.11.11.4 or newer.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fzalo_call_nut_cuoc_goi_den.yaml)

---

## 🎥 Zalo Call caller asks to switch to video

The caller asks to switch from voice to video: **ask on your phone** (Accept / Decline), accept automatically, or accept and send a camera; can announce on a speaker. Never accepts by default.

**Auto-accept** is a separate path that only happens when the **«Cho phép đồng ý chuyển sang video»** switch (video-switch consent) on the Zalo Call device is **ON** (off by default) **and** that person has an «Auto-accept» rule (the «incoming-call rules» blueprint). The caller asks with the camera button at the top right of the call screen.

**Needs:** Zalo Call 2026.11.11.4 or newer.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fzalo_call_video_request.yaml)

---

## 🧭 One button, many jobs (most recent request wins)

One button does whatever is needed: define up to 6 “jobs” (entity + state meaning it needs handling + action); on press it picks the job with the **most recent request** (e.g. an alarm rings, then a call comes in: press = answer; the call ends while the alarm still rings: press = dismiss the alarm). No job needed: run the default action (e.g. place a call). Works with the R1 middle button (from 0.17.0 the speaker has no built-in button actions).

**Needs:** a button with a trigger (R1 middle button, Zigbee button...).

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fmot_nut_nhieu_viec.yaml)

---

## 🎮 R1 speaker middle button, every gesture in one automation

**One automation for the whole R1 middle button**: pick the speaker, then for **each gesture** (single, double, triple press, hold) define up to 4 “jobs” (entity + state that needs handling + action) and a default action. On press it runs the job with the **most recent request**, otherwise the default (e.g. single press = stop alarm / answer / hang up / call, depending on the moment). No need for several automations per button.

**Needs:** the Phicomm R1 integration (middle button). Set that gesture's built-in action to “Do nothing (only fire the event)”, otherwise both run.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fr1_nut_giua_nhieu_cu_chi.yaml)

---

## 🎤 Voice send to Zalo Calling (many people and groups)

A script for the **Voice Assistant** (Assist): send a message, a location or an image to **several people and groups at once** through **Zalo Calling**. Recipients are **picked from a list** (`notify.zalo_call_...` entities), no typing Zalo ids. Same shape as «Send to Zalo Custom Bot», without the account phone number and group id.

**Needs:** Zalo Calling 2026.11.11.3 or newer; recipients picked in *Zalo Call → Configure*.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fsend_to_zalo_call_full_llm.yaml)

---

## 🔗 Zalo Calling in the older blueprints

These blueprints **now have a «Zalo Calling» group** (next to Zalo Bot / Zalo Custom): turn it on, pick recipients from a list (people and groups mixed), and the blueprint sends **in parallel** through Zalo Calling. Needs Zalo Calling `2026.11.11.3` or newer.

| Blueprint | Sent through Zalo Calling |
|---|---|
| Person Camera Alarm (1, 2, 3) | Snapshot with caption, AI result, error message |
| Camera AI Alarm 4 | Early/late images, early/late video, AI result, extra text, error message |
| LLM Vision Camera | AI result with the key frame or snapshot |
| AI Weather Image | The generated image |
| Lunar Calendar & Weather | Lunar and weather messages |
| Auto-Update Blueprints, Auto-Update Pyscript | Update report |

---

## 🔁 luuquangvu automations (webhooks, timers, linking)

Copied from [luuquangvu/tutorials](https://github.com/luuquangvu/tutorials) (MIT licence, see `scripts/LICENSE-luuquangvu`). The `.py` files are in this repo's `scripts/` folder.

Install the **Pyscript** integration (HACS), enable `allow_all_imports` and `hass_is_global`, and copy the needed `.py` files (and `requirements.txt`) into `/config/pyscript/`. See “Install Pyscript” below.

| Info | Details |
|------|---------|
| **Type** | Automation |
| **HA minimum** | 2024.12.0 / 2025.8.0 |

- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fdevices_schedules_restart_handler.yaml) — `devices_schedules_restart_handler.yaml`: Restore device timers after Home Assistant restarts (legacy); needs `common_utilities.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Flink_multiple_devices.yaml) — `link_multiple_devices.yaml`: Link the on/off state of several devices; no `.py` file needed
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Ftelegram_bot_webhook.yaml) — `telegram_bot_webhook.yaml`: Two-way Telegram bot for Home Assistant (webhook); needs `telegram_bot_handle_tool.py`, `common_utilities.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fzalo_bot_webhook.yaml) — `zalo_bot_webhook.yaml`: Two-way Zalo bot for Home Assistant (webhook); needs `zalo_bot_handle_tool.py`, `common_utilities.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fcheck_the_device_turns_on_manually.yaml) — `check_the_device_turns_on_manually.yaml`: Detect a device turned on manually; no `.py` file needed
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fstate_activated_device_with_timer.yaml) — `state_activated_device_with_timer.yaml`: Turn a device off after a delay once it is on; no `.py` file needed
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fmemory_tool_local.yaml) — `memory_tool_local.yaml`: Local memory for Assist (scheduled cleanup); needs `memory.py`, `common_utilities.py`

---

## 🧠 luuquangvu scripts for Assist (search, calendar, memory, timers)

| Info | Details |
|------|---------|
| **Type** | Script |
| **HA minimum** | 2024.12.0 |

- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fadvanced_youtube_search_full_llm.yaml) — `advanced_youtube_search_full_llm.yaml`: Search YouTube videos for Assist; needs `youtube_data_tool.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fget_youtube_video_info_full_llm.yaml) — `get_youtube_video_info_full_llm.yaml`: Get information about a YouTube video; no `.py` file needed
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fplay_youtube_video_full_llm.yaml) — `play_youtube_video_full_llm.yaml`: Play a YouTube video on a device; no `.py` file needed
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fadvanced_google_search_full_llm.yaml) — `advanced_google_search_full_llm.yaml`: Google search for Assist; no `.py` file needed
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fweather_forecast_full_llm.yaml) — `weather_forecast_full_llm.yaml`: Weather forecast for Assist; no `.py` file needed
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fcalendar_events_lookup_full_llm.yaml) — `calendar_events_lookup_full_llm.yaml`: Look up calendar events for Assist; no `.py` file needed
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fcreate_calendar_event_full_llm.yaml) — `create_calendar_event_full_llm.yaml`: Create calendar events by voice; no `.py` file needed
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fcreate_lunar_events.yaml) — `create_lunar_events.yaml`: Create yearly lunar-calendar events; needs `date_conversion_tool.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fdate_lookup_and_conversion_full_llm.yaml) — `date_lookup_and_conversion_full_llm.yaml`: Date lookup and solar ↔ lunar conversion for Assist; needs `date_conversion_tool.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fcontrol_music_full_llm.yaml) — `control_music_full_llm.yaml`: Control music by voice; no `.py` file needed
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fac_mode_and_fan_control_full_llm.yaml) — `ac_mode_and_fan_control_full_llm.yaml`: Control the air conditioner (mode, fan); no `.py` file needed
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Ffan_speed_and_oscillation_control_full_llm.yaml) — `fan_speed_and_oscillation_control_full_llm.yaml`: Control fan speed and oscillation; no `.py` file needed
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fdevice_location_lookup_full_llm.yaml) — `device_location_lookup_full_llm.yaml`: Find where a device is in the home; no `.py` file needed
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fdevice_ringing_full_llm.yaml) — `device_ringing_full_llm.yaml`: Ring a phone to find it; no `.py` file needed
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fdevices_schedules_controller_v2_full_llm.yaml) — `devices_schedules_controller_v2_full_llm.yaml`: Multi-device timers by voice (new version); needs `devices_scheduler.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fdevices_schedules.yaml) — `devices_schedules.yaml`: Multi-device timers (legacy, base for the old controller); needs `common_utilities.py`
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fdevices_schedules_controller_full_llm.yaml) — `devices_schedules_controller_full_llm.yaml`: Voice device timers (legacy, needs the “Devices Schedules” script); no `.py` file needed
- [Import](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fmemory_tool_full_llm.yaml) — `memory_tool_full_llm.yaml`: Memory tool for Assist; needs `memory.py`

---

## 🗓️ Lunar Calendar & Weather Notification

Daily reminders for lunar calendar events combined with weather information. The AI writes the message fresh each day so it never reads the same way twice.

| Info | Details |
|------|---------|
| **Type** | Automation |
| **HA minimum** | 2024.10.0 |

**Features:**
- Lunar calendar and weather can be toggled independently
- The AI writes both the message and the TTS line naturally
- When a calendar event exists: lunar event and weather combined
- When no event exists: weather only

**Configuration:**
- **Days of advance notice:** a list, e.g. `[15, 7, 5, 3, 1]`
- **Notification times:** a list, e.g. `["08:00:00", "20:00:00"]`
- **Event type:** all / death anniversaries only / 1st and 15th / custom sensors

**Notification channels:** mobile app, Telegram, Zalo Bot / Zalo Custom Bot, and TTS.

**Needs Pyscript file(s):** `zalo_bot_handle_tool.py` (in the `scripts/` folder, copy to `/config/pyscript/`).

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fcalendar_weather_notification.yaml)

*Please read the blueprint description carefully before getting started.*

---

## 💬 Daily Quote Automation

Fetch a random quote, proverb, or Vietnamese folk saying from the AI and write it into an `input_text` helper.

| Info | Details |
|------|---------|
| **Type** | Automation |
| **HA minimum** | 2025.7.0 |
| **Requires** | Input Text Helper |

**Features:**
- Refresh on a configurable interval (15 minutes → once a day)
- Multiple sources: international quotes, Vietnamese folk verse, Vietnamese proverbs
- The AI picks at random and avoids repeating itself

**Configuration:**
- **Update interval:** every 15 minutes, 30 minutes, 1 hour, …, daily
- **Input Text Helper:** the `input_text` entity that stores the quote (255-character limit)
- **Quote type:** international quotes, Vietnamese folk verse, Vietnamese proverbs (multi-select)

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fdaily_quote.yaml)

*Please read the blueprint description carefully before getting started.*

---

## 🔧 Check Device Source (Multi-Entity)

Tell apart three ways a device was switched: **physically by hand** (manual), **from an app**, or **by an automation** (auto). Handles many entities in a single automation.

| Info | Details |
|------|---------|
| **Type** | Automation |
| **HA minimum** | 2024.10.0 |
| **Requires** | One Input Select helper per entity |

**How it works:**
- Watches `switch` and `light` entities
- Reads the trigger `context` to determine the source:
  - `parent_id` is set → **auto** (an automation did it)
  - `user_id` is set → **app** (someone used the UI or app)
  - Neither → **manual** (a physical switch)
- Writes the result into the matching `input_select`

**Input Select naming convention:**

```
input_select.source_<entity_object_id>
```

Example: entity `switch.den_phong_khach` → create `input_select.source_den_phong_khach`

**Create the Input Select helper:**

```
Go to Settings → Devices & Services → Helpers
Click "+ Create Helper" → Choose "Dropdown"
Name it: source_<device_name>
Options: manual, app, auto
Save
```

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fcheck_device.yaml)

*Please read the blueprint description carefully before getting started.*

---

## ⏳ Cooldown timer that survives restarts

When an entity changes state as configured, **start a timer**, **store the expiry time** and **recover automatically after a Home Assistant restart or power loss**; when time is up your chosen actions run.

| Info | Details |
|------|---------|
| **Type** | Automation |
| **HA minimum** | 2024.10.0 |
| **Requires** | A Timer helper and an Input Datetime helper |

**Inputs:** trigger entity, from/to state, Timer helper, Input Datetime that stores the expiry time, actions when finished.

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Funiversal_cooldown_recovery.yaml)

*Read the blueprint description before using it.*

---

## 🔄 Auto-Update Blueprints

Check for and apply blueprint updates automatically, with a Zalo notification when a new version lands.

| Info | Details |
|------|---------|
| **Type** | Automation |
| **HA minimum** | 2024.10.0 |
| **Requires** | The `blueprints_update.sh` shell script |

**Update modes:**

| Mode | Description |
|------|-------------|
| **Check** | Check only, change nothing |
| **Update All** | Update every blueprint |
| **Update Self** | Update only this blueprint |
| **Update Specific** | Update one blueprint by path |
| **Update Multiple** | Update several blueprints (one path per line) |

**Configuration:**
- **Schedule:** enable or disable the periodic check
- **Check hour:** 0–23 (default: 3 AM)
- **Reload after update:** reload automations and scripts automatically
- **Notifications:** Zalo notification when an update is available

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2FBlueprints_update_manager.yaml)

*Please read the blueprint description carefully before getting started.*

---

## 🐍 Auto-Update Pyscript

Sync files and folders from GitHub into `/config/pyscript`, keeping your scripts current.

| Info | Details |
|------|---------|
| **Type** | Automation |
| **HA minimum** | 2024.10.0 |
| **Requires** | The `pyscript_sync_from_urls.sh` shell script + a manifest file |

**Modes:**

| Mode | Description |
|------|-------------|
| **Use .conf** | Honor the settings in the `.conf` file |
| **Force check** | Check only, write nothing |
| **Force update** | Write files even if `.conf` sets `auto_update=false` |

**Configuration:**
- **Schedule:** enable or disable the periodic run
- **Run hour:** 0–23 (default: 3 AM)
- **Reload pyscript after update:** automatic or manual
- **Mobile notification:** send the result to a mobile device

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2FBlueprint_pyscript_update_manager.yaml)

*Please read the blueprint description carefully before getting started.*

---

# 📖 Advanced Guides

## 🏷️ Create the Assist Alias Sensor

The **Smart Camera AI Analyzer (Voice)** and **Capture Camera Snapshot (Voice)** blueprints look up cameras by the aliases you set in Assist. They read those aliases from a template sensor you have to create yourself — without it, alias lookup silently does nothing and Home Assistant **reports no error at all**, which makes it very hard to diagnose.

### Why not to copy an older snippet from the web

Home Assistant changed the key that stores aliases in `.storage/core.entity_registry` from `aliases` to `aliases_v2`. Every guide written before June 2026 reads the `aliases` key, so on current Home Assistant it returns an empty list. The snippet below reads both.

### Add to `configuration.yaml`

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

This sensor only refreshes at two moments: when Home Assistant starts, and when you reload template entities. So **after adding an alias to a camera you must reload**, otherwise the blueprint keeps using the old list.

### Verify the sensor works

Go to **Developer Tools → Template** and paste:

```jinja
{{ state_attr('sensor.assist_entity_ids_and_aliases', 'entities') }}
```

You should get a JSON list containing `entity_id` and `aliases`. If you get `None` or `[]`, the three usual causes in order of likelihood: no entity is exposed to Assist yet, no entity has an alias yet, or your Home Assistant install lacks the `jq` command (Container and manually installed Core often do; OS and Supervised ship it).

*Snippet source: [luuquangvu/tutorials](https://github.com/luuquangvu/tutorials).*

### 3. Install Pyscript (for blueprints that need a `.py` file)

1. Install the **Pyscript** integration through HACS.
2. In `configuration.yaml`: `pyscript:` with `allow_all_imports: true` and `hass_is_global: true`.
3. Copy the needed `.py` files and `requirements.txt` from `scripts/` into `/config/pyscript/` (or use the “Auto-Update Pyscript” blueprint above).
4. Put bot tokens in `secrets.yaml` (for example `zalo_bot_token`, `telegram_bot_token`) as described in each blueprint.

---

## ✅ Validate Blueprints Before Pushing

A blueprint with a broken schema or one bad Jinja2 brace sits quietly in the repository and only explodes when a user hits Import. Likewise, in a thousand-line README a table declaring the wrong Home Assistant version can sit there for months. The [`tools/`](/tools) folder holds two checkers that stop both.

**Blueprint checker** — loads Home Assistant Core's real schemas to catch invalid blueprint schema, invalid selector definitions, broken Jinja2 syntax, and `!input` references to inputs that were never declared:

```bash
uv run --no-project --python 3.14 --with 'homeassistant>=2026.8.0' \
  python tools/validate_blueprints.py .
```

**README checker** — reads the YAML files themselves and compares them against what the README claims: a table declaring the wrong type or minimum version, an Import button pointing at a file that does not exist, a file in the repository the README forgot, a table-of-contents link pointing at a heading that is not there. Standard library only:

```bash
python3 tools/check_readme.py .
```

Both run automatically via [`.github/workflows/soat-blueprint.yaml`](/.github/workflows/soat-blueprint.yaml) on every push to `main` and every pull request; pushes to `main` additionally sync every blueprint's `source_url` to the branch and commit the result. See [`tools/README.md`](/tools/README.md) for details.

---

## 📊 Blueprint Overview

| # | Blueprint | Type | HA Min | Main feature (needed .py) |
|---|-----------|------|--------|--------------|
| 1 | AI Image Generator | Script | 2025.8.0 | Generate an image from a text prompt |
| 2 | AI Image + reference | Script | 2025.8.0 | Generate an image from a reference photo |
| 3 | AI Weather Image | Automation | 2025.10.0 | Image matched to weather and time of day |
| 4 | World Landmarks | Automation | 2025.10.0 | AI images of world landmarks |
| 5 | Camera AI (Voice) | Script | 2025.8.0 | Analyze cameras by voice |
| 6 | Snapshot / Record (Voice) | Script | 2024.12.0 | Capture a snapshot or record a clip by voice |
| 7 | File / Image Analyzer | Script | 2025.8.0 | Send a file to the LLM for analysis |
| 8 | Person Camera Alarm (1–3) | Automation | 2025.7.0 | Person detection plus alerting |
| 9 | Camera AI Alarm 4 | Automation | 2026.3.0 | Filter gate, dual snapshots, video branch |
| 10 | Keep AI Model Awake | Automation | 2026.3.0 | Periodic calls to a locally hosted model |
| 11 | LLM Vision Camera | Automation | 2024.10.0 | Real-time camera analysis |
| 12 | Send to Telegram | Script | 2024.10.0 | Send text and images over Telegram |
| 13 | Send to Zalo Bot | Script | 2024.10.0 | Send over the official Zalo bot |
| 14 | Send to Zalo Custom | Script | 2024.10.0 | Send over a personal Zalo account |
| 15 | Lunar Calendar & Weather | Automation | 2024.10.0 | Lunar event and weather reminders |
| 16 | Daily Quote | Automation | 2025.7.0 | Automatic AI quote |
| 17 | Check Device Source | Automation | 2024.10.0 | Tell manual from app from automation |
| 18 | Auto-Update Blueprints | Automation | 2024.10.0 | Auto-update blueprints |
| 19 | Auto-Update Pyscript | Automation | 2024.10.0 | Auto-sync pyscript from GitHub |
| 20 | Zalo Call Alert | Automation | 2026.3.0 | Alert call when a sensor triggers |
| 21 | Zalo Call One Button | Automation | 2026.3.0 | Answer / hang up / call with one button |
| 22 | Zalo Call Incoming Rules | Automation | 2026.3.0 | Announce, auto-answer, AI, home devices |
| 23 | Zalo Call Messenger | Automation | 2026.3.0 | Customizable message or call by device |
| 24 | Zalo Call Reminder | Automation | 2026.3.0 | Scheduled reminder call or message |
| 25 | Cooldown Recovery | Automation | 2024.10.0 | Timer that recovers after a restart |
| 26 | Voice send to Zalo Calling | Script | 2026.3.0 | Send text/location/image to many people and groups |
| 27 | Restore device timers after Home Assistant restarts | Automation | — | common_utilities.py |
| 28 | Link the on/off state of several devices | Automation | 2024.12.0 | — |
| 29 | Two-way Telegram bot for Home Assistant | Automation | 2025.8.0 | telegram_bot_handle_tool.py, common_utilities.py |
| 30 | Two-way Zalo bot for Home Assistant | Automation | 2025.8.0 | zalo_bot_handle_tool.py, common_utilities.py |
| 31 | Detect a device turned on manually | Automation | 2024.12.0 | — |
| 32 | Turn a device off after a delay once it is on | Automation | 2024.12.0 | — |
| 33 | Local memory for Assist | Automation | 2024.12.0 | memory.py, common_utilities.py |
| 34 | Search YouTube videos for Assist | Script | 2024.12.0 | youtube_data_tool.py |
| 35 | Get information about a YouTube video | Script | 2024.12.0 | — |
| 36 | Play a YouTube video on a device | Script | 2024.12.0 | — |
| 37 | Google search for Assist | Script | 2024.12.0 | — |
| 38 | Weather forecast for Assist | Script | 2024.12.0 | — |
| 39 | Look up calendar events for Assist | Script | 2024.12.0 | — |
| 40 | Create calendar events by voice | Script | 2024.12.0 | — |
| 41 | Create yearly lunar-calendar events | Script | 2024.12.0 | date_conversion_tool.py |
| 42 | Date lookup and solar ↔ lunar conversion for Assist | Script | 2024.12.0 | date_conversion_tool.py |
| 43 | Control music by voice | Script | 2024.12.0 | — |
| 44 | Control the air conditioner | Script | 2024.12.0 | — |
| 45 | Control fan speed and oscillation | Script | 2024.12.0 | — |
| 46 | Find where a device is in the home | Script | 2024.12.0 | — |
| 47 | Ring a phone to find it | Script | 2024.12.0 | — |
| 48 | Multi-device timers by voice | Script | 2024.12.0 | devices_scheduler.py |
| 49 | Multi-device timers | Script | 2024.12.0 | common_utilities.py |
| 50 | Voice device timers | Script | 2024.12.0 | — |
| 51 | Memory tool for Assist | Script | 2024.12.0 | memory.py |
| 52 | Zalo Call custom outgoing call | Automation | 2026.3.0 | Zalo Call custom outgoing call |
| 53 | Zalo Call button for incoming calls | Automation | 2026.3.0 | Zalo Call button for incoming calls |
| 54 | Zalo Call caller asks to switch to video | Automation | 2026.3.0 | Zalo Call caller asks to switch to video |
| 55 | One button, many jobs | Automation | 2026.3.0 | Most recent request wins |
| 56 | Zalo Call two-way chat with the assistant | Automation | 2026.3.0 | The assistant answers Zalo messages |
| 57 | R1 speaker middle button, every gesture in one automation | Automation | 2026.3.0 | Many jobs per gesture |

---

**If you find these blueprints helpful, please share them with the Home Assistant community — and follow along for more coming soon!**
