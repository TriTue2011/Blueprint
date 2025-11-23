# Bộ sưu tập Blueprint và Hướng dẫn độc đáo cho Home Assistant

_Tất cả blueprint trong bộ sưu tập này được tinh chỉnh để hoạt động tối ưu với **Gemini 2.5 Flash**. Các mô hình ngôn ngữ khác có thể cần điều chỉnh nhỏ để đạt hiệu quả tương tự._

Biến Home Assistant thành một trợ lý cá nhân thực thụ với bộ sưu tập blueprint và hướng dẫn chi tiết. Mọi kịch bản đều đã được kiểm chứng trong thực tế, đi kèm giải thích rõ ràng, ví dụ lệnh thoại và mẹo triển khai để bạn có thể áp dụng ngay cho ngôi nhà thông minh của mình.

**[Click here for the English version](/README.en.md)**

---

**Lưu ý:** Hãy đọc kỹ mô tả và hướng dẫn đi kèm mỗi blueprint trước khi cài đặt hoặc cập nhật.

---

## ⏱️ Voice Assist - Điều khiển Lịch trình & Hẹn giờ Thiết bị

Tự động tạo, gia hạn, tạm dừng, tiếp tục hoặc hủy **lịch trình điều khiển thiết bị** bằng giọng nói tự nhiên. Mỗi lịch trình có thể áp dụng cho một hoặc nhiều thiết bị và sẽ **tự động khôi phục sau khi Home Assistant khởi động lại**.

**✨ Tính năng nổi bật:**

- **Quản lý linh hoạt:** Hỗ trợ đầy đủ các hành động: `start` (bắt đầu), `extend` (gia hạn), `pause` (tạm dừng), `resume` (tiếp tục), `cancel` (hủy), `list` (liệt kê).
- **Đa nhiệm:** Quản lý đồng thời nhiều thiết bị và nhiều lịch trình độc lập.
- **Bền bỉ:** Tự động khôi phục tất cả lịch trình đang hoạt động sau khi Home Assistant khởi động lại.
- **Thông minh:** Tích hợp sẵn với Voice Assist (LLM) để hiểu lệnh thoại đa ngôn ngữ một cách tự nhiên.

**🗣️ Ví dụ lệnh thoại:**

- "Đặt lịch tắt quạt phòng khách sau 15 phút."
- "Gia hạn lịch tắt đèn bếp thêm 10 phút."
- "Thêm lịch tắt điều hòa phòng ngủ lúc 6 giờ sáng."
- "Các lịch trình đang chạy là gì?"

**💡 Ứng dụng thực tế:**

- Hẹn giờ tắt các thiết bị như đèn, quạt, điều hòa, bình nóng lạnh để tiết kiệm điện.
- Đặt lịch cho các công việc cần chạy trong một khoảng thời gian nhất định, ví dụ: sạc xe điện trong 2 giờ.
- Dễ dàng thay đổi hoặc hủy lịch trình bằng giọng nói mà không cần mở ứng dụng.

Để sử dụng đầy đủ tính năng, bạn cần cài đặt **cả 3 blueprint** sau:

1. **Blueprint Điều khiển (LLM):** Xử lý lệnh thoại và điều phối hành động.
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fdevices_schedules_controller_full_llm.yaml)
2. **Blueprint Lõi Lịch trình:** Chịu trách nhiệm tạo và quản lý các lịch trình.
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fdevices_schedules.yaml)
3. **Blueprint Khôi phục:** Tự động khôi phục các lịch trình đang hoạt động khi Home Assistant khởi động lại.
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fdevices_schedules_restart_handler.yaml)

---

## 🧠 Voice Assist - Ghi nhớ Mọi thứ

Biến Voice Assist thành "bộ nhớ mở rộng" của bạn để lưu trữ, tra cứu, và quản lý các thông tin cá nhân hoặc gia đình.

**✨ Tính năng nổi bật:**

- **Lưu trữ đa dạng:** Ghi nhớ mọi thứ từ mật khẩu, địa chỉ, đến các ghi chú nhanh.
- **Tìm kiếm linh hoạt:** Truy xuất thông tin theo "key" chính xác (`get`) hoặc tìm kiếm theo từ khóa/ngữ nghĩa (`search`).
- **Phạm vi lưu trữ:** Có thể chọn lưu thông tin cho riêng bạn (`user`), cả nhà (`household`), hoặc chỉ trong phiên làm việc (`session`).
- **Tự động hết hạn:** Tùy chọn đặt thời gian để ghi nhớ tự động xóa sau một số ngày nhất định.

**🗣️ Ví dụ lệnh thoại:**

- "Ghi nhớ mật khẩu Wi-Fi cho khách là `khachdenchoi123`."
- "Ghi nhớ chỗ đậu xe là hầm B2, cột D5, và tự xóa sau 1 ngày."
- "Nhắc tôi địa chỉ công ty ABC là 18 Lý Thường Kiệt, Hà Nội."
- "Tìm ghi nhớ về chỗ đậu xe."
- "Mật khẩu Wi-Fi cho khách là gì?"

**💡 Ứng dụng thực tế:**

- **An toàn & cá nhân:** Lưu các thông tin cá nhân ít dùng nhưng quan trọng (số hộ chiếu, mã thành viên, thông tin bảo hành) với phạm vi `user`.
- **Tiện ích gia đình:** Lưu thông tin dùng chung cho cả nhà (mật khẩu Wi-Fi khách, mã cửa) với phạm vi `household`.
- **Ghi chú tạm thời:** Lưu các thông tin có thời hạn (vị trí đỗ xe, địa chỉ lạ, tên một cuốn sách được giới thiệu).

_Tùy chọn phiên bản bạn muốn sử dụng:_

**Phiên bản LLM (Đa ngôn ngữ):**
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fmemory_tool_full_llm.yaml)

**Phiên bản Local (Chỉ tiếng Anh, hoạt động offline):**
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fmemory_tool_local.yaml)

---

## 👀 Voice Assist - "Nhìn" Thấy Xung Quanh

Cho phép Voice Assist truy cập vào các camera an ninh của bạn để trả lời các câu hỏi về những gì đang diễn ra.

**✨ Tính năng nổi bật:**

- **Phân tích hình ảnh:** Trích xuất nội dung từ ảnh chụp camera và trả lời câu hỏi của bạn.
- **Hỗ trợ đa camera:** Cho phép cấu hình nhiều camera để Voice Assist có "tầm nhìn" rộng hơn.
- **Phản hồi tức thì:** Nhận câu trả lời gần như ngay lập tức sau khi đặt câu hỏi.

**🗣️ Ví dụ lệnh thoại:**

- "Xem các camera xem con mèo đang ở đâu."
- "Kiểm tra cam cổng xem có ai ở đó không."
- "Trong sân có xe lạ không?"

**💡 Ứng dụng thực tế:**

- Kiểm tra nhanh sân trước, sân sau hoặc phòng của trẻ nhỏ mà không cần mở ứng dụng camera.
- Tìm kiếm thú cưng hoặc xác nhận một hoạt động bất thường khi bạn không ở gần màn hình.

Để sử dụng tính năng này, bạn cần cài đặt **cả 2 blueprint**:

1. **Blueprint Chụp ảnh:** Chụp lại hình ảnh từ camera được yêu cầu.
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fcamera_snapshot_full_llm.yaml)
2. **Blueprint Phân tích (LLM):** Gửi ảnh chụp cho mô hình ngôn ngữ để phân tích và trả lời.
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Ffile_content_analyzer_full_llm.yaml)

---

## 🗓️ Voice Assist - Quản lý Lịch

Quản lý lịch trình cá nhân của bạn bằng giọng nói một cách tự nhiên và hiệu quả.

### Tạo Sự kiện Lịch

Sắp xếp lịch trình bằng giọng nói như đang trò chuyện với trợ lý. Blueprint tự động hóa việc tạo sự kiện cho mọi lời nhắc, cuộc họp hay chuyến du lịch vào lịch của bạn.

**✨ Tính năng nổi bật:**

- **Nhận diện ngôn ngữ tự nhiên:** Tự động phân tích ngày, giờ, và thời lượng từ câu lệnh của bạn.
- **Tạo sự kiện nhanh:** Thêm sự kiện vào lịch mà không cần nhập liệu thủ công.
- **Tích hợp liền mạch:** Hoạt động hoàn hảo với Lịch Google đã được cấu hình trong Home Assistant.

**🗣️ Ví dụ lệnh thoại:**

- "Tạo lịch 2 giờ chiều mai đi cắt tóc."
- "Lên lịch 9 giờ sáng mai họp trong 3 tiếng."
- "Thêm lịch thứ bảy này về quê."

**💡 Ứng dụng thực tế:**

- Nhanh chóng tạo lời nhắc, lịch hẹn khi đang lái xe hoặc bận tay.
- Thêm các sự kiện gia đình, công việc vào lịch ngay khi nghĩ ra.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fcreate_calendar_event_full_llm.yaml)

### Tra cứu Sự kiện trong Lịch

Hỏi và nhận thông tin về các sự kiện đã có trong lịch của bạn như sinh nhật, cuộc hẹn, ngày kỷ niệm.

**🗣️ Ví dụ lệnh thoại:**

- "Tuần này có lịch gì không?"
- "Tháng này có sự kiện gì đáng chú ý không?"

**💡 Ứng dụng thực tế:**

- Kiểm tra nhanh lịch trình trong ngày hoặc tuần mà không cần mở ứng dụng lịch.
- Đảm bảo bạn không bỏ lỡ các sự kiện quan trọng.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fcalendar_events_lookup_full_llm.yaml)

---

## 🌙 Voice Assist - Trợ lý Lịch Âm

Các công cụ giúp bạn theo dõi và quản lý các sự kiện theo lịch Âm một cách chính xác.

### Tra cứu & chuyển đổi Lịch Âm

Chuyển đổi tức thì giữa lịch Âm và lịch Dương, hoạt động 100% offline. Cung cấp đầy đủ thông tin Can Chi, tiết khí, ngày tốt/xấu, và giờ hoàng đạo.

**✨ Tính năng nổi bật:**

- **Hoạt động Offline:** Xử lý cực nhanh và không cần Internet.
- **Thông tin chi tiết:** Cung cấp đầy đủ dữ liệu lịch Âm truyền thống.
- **Đếm ngược sự kiện:** Cho biết số ngày còn lại đến các ngày lễ lớn như Tết Nguyên Đán.

**🗣️ Ví dụ lệnh thoại:**

- "Chủ nhật tuần này là ngày bao nhiêu âm?"
- "Rằm Trung Thu vào thứ mấy?"
- "Còn bao nhiêu ngày nữa đến Tết?"

**💡 Ứng dụng thực tế:**

- Xem ngày âm để chuẩn bị cho các ngày lễ, giỗ, cúng bái.
- Tra cứu ngày tốt/xấu, giờ hoàng đạo cho các công việc quan trọng.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fdate_lookup_and_conversion_full_llm.yaml)

### Tạo Sự kiện theo Lịch Âm

Tự động thêm các sự kiện quan trọng tính theo lịch Âm (giỗ, ngày kỷ niệm, cưới hỏi...) vào lịch của bạn.

**Lưu ý:** Blueprint này được thiết kế để **chạy thủ công** hoặc thông qua tự động hóa, yêu cầu người dùng điền thông tin trực tiếp qua giao diện Home Assistant. Nó **không hỗ trợ lệnh thoại** qua Voice Assist.

**✨ Tính năng nổi bật:**

- **Chuyển đổi tự động:** Tự động tính toán và tạo sự kiện vào ngày dương lịch tương ứng hàng năm.
- **Chính xác & Tiện lợi:** Không còn phải tự quy đổi thủ công hay sợ quên các ngày lễ truyền thống.

**💡 Ứng dụng thực tế:**

- Đảm bảo không bao giờ bỏ lỡ các ngày giỗ, cúng bái quan trọng của gia đình.
- Tự động nhắc nhở các ngày kỷ niệm, sinh nhật tính theo lịch âm.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fcreate_lunar_events.yaml)

---

## 💬 Tương tác hai chiều với Telegram / Zalo

Xây dựng bot để trò chuyện và điều khiển Home Assistant. Bot có thể hỏi lại để làm rõ yêu cầu và nhận/gửi hình ảnh.

**✨ Tính năng nổi bật:**

- **Hội thoại hai chiều:** Bot có thể đặt câu hỏi để làm rõ yêu cầu của bạn trước khi thực hiện.
- **Hỗ trợ đa phương tiện:** Gửi ảnh từ camera để phân tích, hoặc nhận file từ bot.
- **Điều khiển nhà thông minh:** Ra lệnh trực tiếp trong giao diện chat để điều khiển thiết bị.

**💡 Ứng dụng thực tế:**

- Điều khiển nhà từ xa qua app chat mà không cần mở ứng dụng Home Assistant.
- Gửi ảnh một cái cây trong vườn và hỏi "Đây là cây gì và cần chăm sóc thế nào?".

_Cài đặt blueprint webhook cho nền tảng bạn chọn. Để phân tích hình ảnh, cài thêm blueprint Phân tích._

**Webhook cho Telegram:**
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Ftelegram_bot_webhook.yaml)

**Webhook cho Zalo (Official Account):**
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fzalo_bot_webhook.yaml)

**Webhook cho Zalo (Custom Bot):**
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fzalo_custom_bot_webhook.yaml)

**(Tùy chọn) Blueprint Phân tích Hình ảnh:**
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Ffile_content_analyzer_full_llm.yaml)

---

## ✉️ Voice Assist → Gửi tin nhắn & hình ảnh qua Telegram / Zalo

Dùng giọng nói để gửi tin nhắn, hình ảnh, địa điểm, hoặc kết quả tìm kiếm tới bạn bè và nhóm chat.

**✨ Tính năng nổi bật:**

- **Hỗ trợ đa nội dung:** Gửi tin nhắn văn bản, ảnh chụp từ camera, hoặc file media.
- **Tích hợp bản đồ & tìm kiếm:** Tự động đính kèm liên kết Google Maps cho địa điểm và Google Search cho các nội dung khác.
- **Gửi đến nhóm hoặc cá nhân:** Hỗ trợ gửi tin nhắn đến cả cuộc trò chuyện riêng tư và nhóm.

**🗣️ Ví dụ lệnh thoại:**

- "Gửi danh sách quán ăn ngon ở Nha Trang lên nhóm Telegram gia đình."
- "Gửi địa chỉ Hoàng Thành Thăng Long lên Zalo cho vợ anh."
- "Gửi ảnh ở cam cổng cho nhóm Telegram."

**💡 Ứng dụng thực tế:**

- Chia sẻ nhanh một địa điểm, hình ảnh hay thông tin thú vị cho người thân khi đang di chuyển.
- Gửi kết quả tìm kiếm bằng giọng nói cho người khác để họ tham khảo.

_Cài đặt blueprint cho nền tảng bạn muốn gửi tin đến:_

**Gửi đến Telegram:**
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fsend_to_telegram_full_llm.yaml)

**Gửi đến Zalo (Official Bot):**
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fsend_to_zalo_bot_full_llm.yaml)

**Gửi đến Zalo (Custom Bot):**
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fsend_to_zalo_custom_bot_full_llm.yaml)

---

## 🔍 Voice Assist - Tìm kiếm Google Nâng cao

Thực hiện các truy vấn Google phức tạp bằng giọng nói và nhận về câu trả lời đã được tóm tắt, súc tích và cập nhật.

**✨ Tính năng nổi bật:**

- **Tóm tắt thông minh:** Trả về câu trả lời ngắn gọn thay vì một danh sách kết quả dài.
- **Hiểu câu hỏi mở:** Xử lý tốt các câu hỏi phức tạp, đòi hỏi tổng hợp thông tin.
- **Luôn cập nhật:** Lấy dữ liệu mới nhất trực tiếp từ kết quả tìm kiếm của Google.

**🗣️ Ví dụ lệnh thoại:**

- "Điểm chuẩn Đại học Bách Khoa Hà Nội năm nay là bao nhiêu?"
- "Những công nghệ AI nào đang là xu hướng trong tuần này?"

**💡 Ứng dụng thực tế:**

- Nhanh chóng tra cứu thông tin, sự kiện, kiến thức mà không cần đọc qua nhiều trang web.
- Giải đáp các câu hỏi bất chợt trong cuộc sống hàng ngày ("diễn viên chính của phim X là ai?").

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fadvanced_google_search_full_llm.yaml)

---

## 📺 Voice Assist - Tìm kiếm và Phát video YouTube

Tìm kiếm nội dung YouTube rồi phát trên TV hoặc thiết bị media bằng giọng nói.

**✨ Tính năng nổi bật:**

- **Tìm kiếm theo ngữ nghĩa:** Tìm video dựa trên chủ đề, nhân vật, sự kiện thay vì chỉ từ khóa.
- **Phát tự động:** Tự động chọn video phù hợp nhất và phát trên thiết bị bạn chỉ định.
- **Hỗ trợ đa dạng câu hỏi:** Trả lời các câu hỏi kiến thức bằng cách tìm và phát video liên quan.

**🗣️ Ví dụ lệnh thoại:**

- "Tìm video về cuộc đời và sự nghiệp của ông Lê Đức Thọ."
- "Ai là nhà khoa học nữ xuất sắc nhất thế kỷ 20? Tìm video về bà ấy."

**💡 Ứng dụng thực tế:**

- Tìm và phát một video hướng dẫn nấu ăn, sửa chữa khi đang bận tay.
- Mở nhanh các chương trình giải trí, âm nhạc cho cả gia đình.

Để sử dụng tính năng này, bạn cần cài đặt **cả 2 blueprint**:

1. **Blueprint Tìm kiếm (LLM):** Phân tích câu hỏi và tìm kiếm video phù hợp.
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fadvanced_youtube_search_full_llm.yaml)
2. **Blueprint Phát video:** Lấy thông tin video và phát trên media player.
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fplay_youtube_video_full_llm.yaml)

---

## 📡 Voice Assist - Kênh YouTube Yêu thích

Tự động phát hiện video mới nhất từ các kênh bạn theo dõi và phát ngay trên thiết bị mong muốn.

**✨ Tính năng nổi bật:**

- **Kiểm tra video mới:** Tự động kiểm tra các kênh YouTube bạn đã định sẵn.
- **Phát video mới nhất:** Dễ dàng phát video vừa được đăng tải chỉ bằng một câu lệnh.
- **Thông báo tùy chọn:** Có thể cài đặt để nhận thông báo ngay khi có video mới.

**🗣️ Ví dụ lệnh thoại:**

- "Hoa Ban Food có video mới không?"
- "Phát video mới nhất của Sang vlog lên TV."

**💡 Ứng dụng thực tế:**

- Tạo một kịch bản "chào buổi sáng" tự động phát video tin tức mới nhất từ kênh bạn tin tưởng.
- Đảm bảo bạn không bao giờ bỏ lỡ nội dung từ các nhà sáng tạo yêu thích.

[**Xem hướng dẫn chi tiết**](/home_assistant_play_favorite_youtube_channel_videos.md)

Để sử dụng tính năng này, bạn cần cài đặt **cả 2 blueprint**:

1. **Blueprint Lấy thông tin (LLM):** Kiểm tra kênh và lấy thông tin video mới nhất.
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fget_youtube_video_info_full_llm.yaml)
2. **Blueprint Phát video:** Lấy thông tin video và phát trên media player (có thể tái sử dụng từ blueprint ở trên).
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fplay_youtube_video_full_llm.yaml)

---

## 🌬️ Voice Assist - Điều khiển Quạt

Điều chỉnh tốc độ và chế độ xoay của một hoặc nhiều quạt trong nhà bằng giọng nói.

**✨ Tính năng nổi bật:**

- **Điều khiển tốc độ:** Tăng, giảm hoặc đặt tốc độ quạt theo phần trăm.
- **Điều khiển chế độ xoay:** Bật hoặc tắt chế độ xoay của quạt.
- **Hỗ trợ nhiều quạt:** Ra lệnh cho nhiều quạt cùng lúc.

**🗣️ Ví dụ lệnh thoại:**

- "Tăng tốc độ quạt phòng bếp."
- "Chỉnh tốc độ quạt phòng ngủ xuống 50%."
- "Bật chế độ xoay cho quạt phòng khách."

**💡 Ứng dụng thực tế:**

- Thay đổi mức gió hoặc hướng gió của quạt mà không cần di chuyển.
- Nhanh chóng điều chỉnh không khí trong phòng cho phù hợp với nhu cầu.

_Cài đặt blueprint cho chức năng bạn muốn sử dụng:_

**Điều khiển Tốc độ quạt:**
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Ffan_speed_control_full_llm.yaml)

**Điều khiển Xoay quạt:**
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Ffan_oscillation_control_full_llm.yaml)

---

## 📍 Voice Assist - Tìm vị trí Thiết bị Di động

Định vị thiết bị di động hoặc thẻ BLE trong nhà bằng giọng nói và kích hoạt chuông để tìm kiếm dễ dàng hơn.

**✨ Tính năng nổi bật:**

- **Xác định vị trí:** Báo cáo vị trí gần đúng của thiết bị trong nhà (theo phòng).
- **Kích hoạt chuông:** Khiến thiết bị đổ chuông để bạn có thể tìm thấy bằng âm thanh.
- **Hỗ trợ nhiều thiết bị:** Tìm kiếm đồng thời nhiều điện thoại, máy tính bảng.

**🗣️ Ví dụ lệnh thoại:**

- "Tìm xem mấy cái điện thoại đang ở đâu?"
- "Tìm cái iPad và cho nó đổ chuông."

**💡 Ứng dụng thực tế:**

- Nhanh chóng tìm thấy điện thoại, máy tính bảng bị thất lạc trong nhà.
- Kiểm tra xem con cái có để quên thiết bị ở nhà hay không.

[**Xem hướng dẫn chi tiết**](/home_assistant_device_location_lookup_guide_en.md)

Để sử dụng tính năng này, bạn cần cài đặt **cả 2 blueprint**:

1. **Blueprint Tìm vị trí (LLM):** Xử lý yêu cầu và tìm vị trí thiết bị.
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fdevice_location_lookup_full_llm.yaml)
2. **Blueprint Đổ chuông (LLM):** Kích hoạt thiết bị đổ chuông.
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fdevice_ringing_full_llm.yaml)

---

## 🚦 Voice Assist - Tra cứu Phạt nguội

Tra cứu tình trạng phạt nguội của bất kỳ phương tiện nào bằng giọng nói, sử dụng dữ liệu trực tiếp từ Cổng thông tin của Cục CSGT.

**Lưu ý:** Tính năng này chỉ áp dụng cho hệ thống tra cứu phạt nguội tại Việt Nam.

**🗣️ Ví dụ lệnh thoại:**

- "Kiểm tra phạt nguội ô tô 30G-123.45."
- "Xe máy 29-T1 567.89 có bị phạt nguội không?"

**💡 Ứng dụng thực tế:**

- Kiểm tra định kỳ xe của gia đình.
- Kiểm tra xe cũ trước khi mua để tránh các khoản phạt tồn đọng.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Ftraffic_fine_lookup_full_llm.yaml)

---

## 🚨 Thông báo Phạt nguội Tự động

Nhận cảnh báo ngay khi có vi phạm giao thông mới được ghi nhận trên hệ thống của Cục CSGT cho xe của bạn.

**Lưu ý:** Tính năng này chỉ áp dụng cho hệ thống tra cứu phạt nguội tại Việt Nam.

**✨ Tính năng nổi bật:**

- **Tự động kiểm tra:** Định kỳ quét hệ thống để phát hiện vi phạm mới.
- **Thông báo tức thì:** Gửi thông báo đến Home Assistant ngay khi có phạt nguội.
- **Hỗ trợ nhiều xe:** Dễ dàng cấu hình để theo dõi nhiều biển số xe cùng lúc.

**💡 Ứng dụng thực tế:**

- Giúp bạn nắm được thông tin vi phạm sớm để xử lý kịp thời.
- Quản lý tình trạng phạt nguội cho tất cả phương tiện của gia đình một cách tự động.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Ftraffic_fine_notification.yaml)

---

## 🔗 Đồng bộ Trạng thái Thiết bị

Đồng bộ trạng thái `on/off` giữa nhiều thiết bị, hoạt động tương tự như một công tắc cầu thang hai chiều ảo.

**💡 Ứng dụng thực tế:**

- Một công tắc vật lý có thể điều khiển một bóng đèn thông minh không nối dây trực tiếp.
- Bật một đèn thì các đèn khác trong cùng khu vực cũng bật theo.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Flink_multiple_devices.yaml)

---

## ⚠️ Blueprint đã lỗi thời

### Hẹn giờ Bật/Tắt Thiết bị

**Sử dụng phiên bản mới [Voice Assist - Điều khiển Lịch trình & Hẹn giờ Thiết bị](#️-voice-assist---điều-khiển-lịch-trình--hẹn-giờ-thiết-bị) để có nhiều tính năng hơn.**

Để sử dụng, bạn cần cài đặt **cả 2 blueprint**:

1. **Blueprint Điều khiển (LLM):**
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fdevice_control_timer_full_llm.yaml)
2. **Blueprint Công cụ Hẹn giờ:**
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fdevice_control_tool.yaml)

---

## 📘 Hướng dẫn Thêm

- [**Tùy chỉnh chỉ dẫn hệ thống (system instruction) cho Voice Assist**](/home_assistant_voice_instructions.md)
- [**Phát video mới từ kênh YouTube yêu thích**](/home_assistant_play_favorite_youtube_channel_videos.md)
- [**Tự động cập nhật và tóm tắt tin tức mỗi ngày**](/home_assistant_get_and_summary_daily_news.md)
- [**Theo dõi các thiết bị mất kết nối (unavailable)**](/home_assistant_unavailable_devices.md)
- [**Tự động chuyển đổi giao diện (theme) sáng/tối**](/home_assistant_ios_themes.md)
- [**Hướng dẫn cài đặt tìm kiếm vị trí thiết bị**](/home_assistant_device_location_lookup_guide_en.md)

---

**Nếu bạn thấy bộ sưu tập này hữu ích, đừng ngần ngại chia sẻ với cộng đồng Home Assistant nhé! Hãy theo dõi để cập nhật thêm nhiều blueprint độc đáo khác trong tương lai!**


---

## 🔗 Tạo ảnh Ai

Tạo ảnh theo promt.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fai_image_generator_full_llm.yaml
)

*Hãy đọc kỹ mô tả của từng blueprint và làm theo hướng dẫn trong đó nhé.*
## 🔗 kiểm tra camera

Tạo ảnh theo promt.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fvoice_camera_ai_analyzer.yaml
)

