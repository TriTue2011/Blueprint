# Unique Home Assistant Blueprints & Tutorials

*All blueprints in this collection are fine-tuned to work best with **Gemini 2.5 Flash**. Other models may require minor adjustments to behave as expected.*

Transform Home Assistant into a fully-fledged personal teammate with this curated collection of blueprints and guides. Every scenario has been proven in real homes, backed by clear explanations, example voice prompts, and deployment tips so you can bring each idea to life right away.

**[Vietnamese version click here](/README.md)**

---

## ⏱ Voice Assist - Devices Schedules / Timers

Automatically create, extend, pause, resume, or cancel **device schedules** through natural voice commands.
Each schedule controls one or multiple smart devices (such as lights, fans, or air conditioners) and automatically restores itself after Home Assistant restarts.

Unlike Home Assistant's built-in timers, this tool manages **device-based schedules** independently, supports **multiple concurrent schedules**, and performs **automatic actions** (turning devices on or off when the schedule ends).
You can simply speak naturally - Voice Assist (an LLM such as Gemini/GPT) will interpret, create, and manage these schedules automatically.

**Key Features:**

- Supports modes: **start**, **extend**, **pause**, **resume**, **cancel**, **cancel_all**, **list**
- Manage **multiple devices and schedules simultaneously**
- **Auto-restores** schedules after Home Assistant restarts
- **Integrated with Voice Assist (LLMs)** for natural multi-language commands
- Customizable end actions: turn on/off devices, send notifications, or trigger other scripts

**Example Voice Commands:**

- "Set a schedule to turn off the living room fan in 15 minutes."
- "Extend the kitchen light schedule by 10 minutes."
- "Add a schedule to turn off the bedroom air conditioner at 6 a.m."
- "Cancel all device schedules."
- "What device schedules are currently active?"

**Use Cases:**

- Schedule **lights, fans, air conditioners, heaters, or water heaters**
- Run **multiple independent schedules** per device
- Pause, resume, or extend existing schedules easily
- Serve as a **foundation for voice-driven device automation** in smart homes

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fdevices_schedules.yaml)

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fdevices_schedules_restart_handler.yaml)

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fdevices_schedules_controller_full_llm.yaml)

*Please carefully read each blueprint description before getting started.*

---

## 🧠 Voice Assist - Remember Anything (Memory Tool)

Turn Voice Assist into your personal memory vault - capable of storing, updating, recalling, or forgetting information using only your voice.
Save things like Wi-Fi passwords, parking spots, birthdays, or quick reminders - and retrieve them in seconds without touching your phone or scrolling through notes.

**Key Features:**

- Store and manage memories through natural voice commands
- Update, overwrite, or delete existing entries easily
- Smart keyword and semantic search for accurate recall
- Works **entirely offline** with no internet required
- Optional TTL (time-to-live) for temporary memories

**Example Voice Commands:**

- "Remember my parking spot is basement B2, R10."
- "Where did I park?"
- "Remember the guest Wi-Fi password is 123456789."
- "What's the guest Wi-Fi password?"

### LLM Version (Multiple Languages)

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fmemory_tool_full_llm.yaml)

### Local Version (English Only)

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fmemory_tool_local.yaml)

*Please carefully read each blueprint description before getting started.*

---

## 👀 Voice Assist - "See" Around

Give Voice Assist eyes on your surroundings. Share the cameras you want it to access, then ask it to check doorways, hunt down pets, or confirm activity around the house-all through natural conversation with near-instant responses.

**Example voice commands:**

- Show the cameras to see where the cat is
- Check the gate camera to see if anyone's there

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Ffile_content_analyzer_full_llm.yaml)

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fcamera_snapshot_full_llm.yaml)

*Please carefully read each blueprint description before getting started.*

---

## 🗓️ Voice Assist - Create Calendar Events

Plan your schedule as if you were chatting with a personal assistant. This blueprint turns reminders, meetings, and getaways into calendar entries, and pairs perfectly with the calendar lookup blueprint when you need timely nudges.

**Example voice commands:**

- Schedule a haircut tomorrow at 2 PM
- Schedule a 3-hour meeting tomorrow at 9 AM
- Add an event this Saturday to visit family
- Create an event next Sunday for a 1-week trip to Phu Quoc

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fcreate_calendar_event_full_llm.yaml)

*Please carefully read each blueprint description before getting started.*

---

## 🤝 Two-Way Interaction with Zalo (Official Zalo Bot)

Connect Home Assistant to your Zalo Official Account for natural, two-way conversations. Control devices, send images for instant analysis, and let the bot ask clarifying questions before it takes action.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fzalo_bot_webhook.yaml)

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Ffile_content_analyzer_full_llm.yaml)

*Please carefully read each blueprint description before getting started.*

---

## 📩 Voice Assist → Zalo (Official Bot)

Send anything to a Zalo recipient with your voice alone. Mention a location to auto-generate Google Maps links, while other content gets a companion Google Search link for instant follow-up.

**Example voice commands:**

- Find the best restaurants in Nha Trang and send them to Zalo
- Send the address of Thang Long Citadel to Zalo

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fsend_to_zalo_bot_full_llm.yaml)

*Please carefully read each blueprint description before getting started.*

---

## 🧩 Two-Way Interaction with Zalo (Custom Bot)

Build your own Zalo bot without giving up conversational smarts. The blueprint handles webhooks, state syncing, and rich media (images, video, audio, documents) so you can focus on the experience instead of the plumbing.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fzalo_custom_bot_webhook.yaml)

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Ffile_content_analyzer_full_llm.yaml)

*Please carefully read each blueprint description before getting started.*

---

## 📬 Voice Assist → Zalo (Custom Bot)

Dictate messages through your custom Zalo bot and deliver them to people or group chats. Mention a destination to generate Google Maps links automatically; everything else ships with a Google Search link so recipients can dive deeper right away.

**Example voice commands:**

- Share the best restaurants in Nha Trang with the family Zalo group
- Send the address of Thang Long Citadel to my wife's Zalo

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fsend_to_zalo_custom_bot_full_llm.yaml)

*Please carefully read each blueprint description before getting started.*

---

## 💬 Two-Way Interaction with Telegram

Spin up a Telegram bot that keeps up with natural, multi-turn conversations. Trigger automations, receive contextual replies, attach snapshots or clips from cameras, and continue chatting without losing context.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Ftelegram_bot_webhook.yaml)

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Ffile_content_analyzer_full_llm.yaml)

*Please carefully read each blueprint description before getting started.*

---

## ✉️ Voice Assist → Telegram

Talk to friends or groups on Telegram via Voice Assist. Locations automatically turn into Google Maps links, while every other message includes a Google Search link so recipients can fact-check or explore further on the spot.

**Example voice commands:**

- Find the best restaurants around My Dinh and send them to Telegram
- Send the address of Yen So Park to Telegram

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fsend_to_telegram_full_llm.yaml)

*Please carefully read each blueprint description before getting started.*

---

## 🔍 Voice Assist - Advanced Google Search

Run sophisticated Google searches by voice and hear concise, up-to-date answers. Ask open-ended questions, filter by topic, and receive summarized results that highlight what matters most.

**Example voice commands:**

- What's the entry score for Hanoi University of Science and Technology this year?
- Which AI technologies are trending this week?

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fadvanced_google_search_full_llm.yaml)

*Please carefully read each blueprint description before getting started.*

---

## ⏱️ Voice Assist - Device Control Timer (Obsoleted)

**Use the new version `Voice Assist - Devices Schedules / Timers` for more features**

Set timers for any device with natural speech-from living room lights to bedroom AC units. Schedule a specific shutoff time or a countdown, and apply the command to multiple devices at once without writing any YAML.

**Example voice commands:**

- Turn off the living room lights and fan in 30 minutes
- Turn off the bedroom air conditioner at 6 AM

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fdevice_control_timer_full_llm.yaml)

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fdevice_control_tool.yaml)

*Please carefully read each blueprint description before getting started.*

---

## 🚨 Traffic Fine Notifications

Stay on top of traffic fines linked to your vehicle and get alerts as soon as the national traffic police system records a new violation. Notifications flow straight into Home Assistant so you can handle them before deadlines slip by.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Ftraffic_fine_notification.yaml)

*Please carefully read each blueprint description before getting started.*

---

## 🛑 Voice Assist - Traffic Fine Lookup

Check traffic fines for any vehicle with live data from the national traffic police portal. It's ideal for monitoring family cars or double-checking a used vehicle before you buy.

**Example voice commands:**

- Check traffic fines for the car 30G12345

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Ftraffic_fine_lookup_full_llm.yaml)

*Please carefully read each blueprint description before getting started.*

---

## 📺 Voice Assist - YouTube Search & Playback

Search YouTube and play videos on any media device using conversation alone. Hunt by topic, person, or event and let the blueprint queue the most relevant clip automatically.

**Example voice commands:**

- Find a video about the life and career of Le Duc Tho
- Who was the most outstanding female scientist of the 20th century? Find a video about her

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fadvanced_youtube_search_full_llm.yaml)

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fplay_youtube_video_full_llm.yaml)

*Please carefully read each blueprint description before getting started.*

---

## 🌬️ Voice Assist - Fan Speed Control

Adjust the speed of one or many fans across your home with simple voice prompts. Increase, decrease, or set specific percentages-even coordinate multiple rooms in one request.

**Example voice commands:**

- Increase the kitchen fan speed
- Set the bedroom fan speed to 50

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Ffan_speed_control_full_llm.yaml)

*Please carefully read each blueprint description before getting started.*

---

## 🔄 Voice Assist - Fan Oscillation Control

Toggle oscillation for multiple fans at once using nothing but your voice. Perfect when you want to rotate airflow between zones or lock a fan onto a single spot.

**Example voice commands:**

- Start oscillation for the living room and kitchen fans
- Stop oscillation for the bedroom fan

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Ffan_oscillation_control_full_llm.yaml)

*Please carefully read each blueprint description before getting started.*

---

## 📡 Voice Assist - Favorite YouTube Channels

Automatically surface the newest videos from your must-watch channels and play them on your chosen devices. Optionally get notified the moment a fresh upload drops so you never miss a thing.

**Example voice commands:**

- Does Hoa Ban Food have a new video?
- Play the latest Sang vlog on the TV

[**Detailed guide**](/home_assistant_play_favorite_youtube_channel_videos.md)

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fget_youtube_video_info_full_llm.yaml)

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fplay_youtube_video_full_llm.yaml)

*Please carefully read each blueprint description before getting started.*

---

## 📍 Voice Assist - Device Location Lookup

Track down phones, tablets, smartwatches, or BLE tags around your home with a quick command. Voice Assist reports the most recent room and can trigger a ring so you locate the device in moments.

**Example voice commands:**

- Where are the phones right now?
- Find the iPad and make it ring

[**Detailed guide**](/home_assistant_device_location_lookup_guide_en.md)

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fdevice_location_lookup_full_llm.yaml)

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fdevice_ringing_full_llm.yaml)

*Please carefully read each blueprint description before getting started.*

---

## 🌙 Voice Assist - Lunar Calendar Conversion

Switch between solar and lunar calendars instantly-completely offline and lightning fast. Get full Can Chi details, solar terms, auspicious/inauspicious ratings, lucky hours, and countdowns to important milestones.

**Example voice commands:**

- What's the lunar date this Sunday?
- When is Mid-Autumn Festival?
- How many days until Tet?
- Is tomorrow a good or bad day?

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fdate_lookup_and_conversion_full_llm.yaml)

*Please carefully read each blueprint description before getting started.*

---

## 📆 Voice Assist - Calendar Events Lookup

Ask what's already on your calendar-birthdays, anniversaries, work commitments, or personal reminders. Voice Assist reads everything back with timing so you can plan your day with confidence.

**Example voice commands:**

- What events are happening this week?
- What's on the calendar this month?

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fcalendar_events_lookup_full_llm.yaml)

*Please carefully read each blueprint description before getting started.*

---

## 🗓️ Create Lunar Calendar Events

Add lunar-based occasions-memorials, anniversaries, weddings-to your solar calendar accurately and effortlessly. No more manual conversions or missed traditional milestones.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fcreate_lunar_events.yaml)

*Please carefully read each blueprint description before getting started.*

---

## 🔗 Device State Synchronization

Mirror on/off states across multiple devices just like a two-way staircase switch. It works with any toggleable entity, keeping switches, sensors, and automations perfectly in sync.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Flink_multiple_devices.yaml)

*Please carefully read each blueprint description before getting started.*

---

## 📘 Tutorials

- [**How to write custom system instructions for Voice Assist**](/home_assistant_voice_instructions.md)
- [**Play new videos from favorite YouTube channels**](/home_assistant_play_favorite_youtube_channel_videos.md)
- [**Get and summarize daily news with AI**](/home_assistant_get_and_summary_daily_news.md)
- [**Monitor unavailable devices**](/home_assistant_unavailable_devices.md)
- [**Auto-switch iOS Themes**](/home_assistant_ios_themes.md)
- [**Device location lookup guide**](/home_assistant_device_location_lookup_guide_en.md)

---

**If you find these blueprints helpful, please share them with the Home Assistant community - and be sure to follow along for more unique blueprints coming soon!**
