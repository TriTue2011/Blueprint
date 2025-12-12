# Bộ sưu tập Blueprint và Hướng dẫn độc đáo cho Home Assistant

**Gần đây, Google đã cắt giảm đáng kể API Gemini miễn phí, khiến nó gần như không thể đáp ứng nhu cầu sử dụng của Home Assistant. Các bạn có thể tham khảo [một giải pháp thay thế hoàn toàn miễn phí tại đây](https://github.com/luuquangvu/ha-addons).**

_Tất cả blueprint trong bộ sưu tập này được tinh chỉnh để hoạt động tối ưu với **Gemini 2.5 Flash**. Các mô hình ngôn ngữ khác có thể cần điều chỉnh nhỏ để đạt hiệu quả tương tự._

Biến Home Assistant thành một trợ lý cá nhân thực thụ với bộ sưu tập blueprint và hướng dẫn chi tiết. Mọi kịch bản đều đã được kiểm chứng trong thực tế, đi kèm giải thích rõ ràng, ví dụ lệnh thoại và mẹo triển khai để bạn có thể áp dụng ngay cho ngôi nhà thông minh của mình.

**[Click here for the English version](/README.en.md)**

---

## Mục lục

- [Bộ sưu tập Blueprint và Hướng dẫn độc đáo cho Home Assistant](#bộ-sưu-tập-blueprint-và-hướng-dẫn-độc-đáo-cho-home-assistant)
  - [Mục lục](#mục-lục)
  - [Voice Assist - Hẹn giờ \& Lên lịch Thông minh](#voice-assist---hẹn-giờ--lên-lịch-thông-minh)
  - [Voice Assist - Ghi nhớ và Truy xuất Thông tin](#voice-assist---ghi-nhớ-và-truy-xuất-thông-tin)
  - [Voice Assist - Phân tích Hình ảnh Camera](#voice-assist---phân-tích-hình-ảnh-camera)
  - [Voice Assist - Quản lý Lịch trình \& Sự kiện](#voice-assist---quản-lý-lịch-trình--sự-kiện)
    - [Tạo Sự kiện Lịch](#tạo-sự-kiện-lịch)
    - [Tra cứu Sự kiện trong Lịch](#tra-cứu-sự-kiện-trong-lịch)
  - [Voice Assist - Tra cứu \& Chuyển đổi Lịch Âm](#voice-assist---tra-cứu--chuyển-đổi-lịch-âm)
    - [Tra cứu \& chuyển đổi Lịch Âm](#tra-cứu--chuyển-đổi-lịch-âm)
    - [Tạo Sự kiện theo Lịch Âm](#tạo-sự-kiện-theo-lịch-âm)
  - [Chatbot Tương tác \& Điều khiển Nhà thông minh](#chatbot-tương-tác--điều-khiển-nhà-thông-minh)
  - [Voice Assist - Gửi Tin nhắn \& Hình ảnh](#voice-assist---gửi-tin-nhắn--hình-ảnh)
  - [Voice Assist - Tra cứu Thông tin Internet](#voice-assist---tra-cứu-thông-tin-internet)
  - [Voice Assist - Tìm kiếm \& Phát Video YouTube](#voice-assist---tìm-kiếm--phát-video-youtube)
  - [Voice Assist - Theo dõi Kênh YouTube Yêu thích](#voice-assist---theo-dõi-kênh-youtube-yêu-thích)
  - [Voice Assist - Điều khiển Quạt Thông minh](#voice-assist---điều-khiển-quạt-thông-minh)
  - [Voice Assist - Điều khiển Điều hòa Thông minh](#voice-assist---điều-khiển-điều-hòa-thông-minh)
  - [Voice Assist - Định vị \& Tìm kiếm Thiết bị](#voice-assist---định-vị--tìm-kiếm-thiết-bị)
  - [Voice Assist - Tra cứu Phạt nguội](#voice-assist---tra-cứu-phạt-nguội)
  - [Tự động Cảnh báo Phạt nguội](#tự-động-cảnh-báo-phạt-nguội)
  - [Đồng bộ Trạng thái Thiết bị](#đồng-bộ-trạng-thái-thiết-bị)
  - [Các Blueprint đã lỗi thời](#các-blueprint-đã-lỗi-thời)
    - [Voice Assist - Hẹn giờ Bật/Tắt Thiết bị (Cũ)](#voice-assist---hẹn-giờ-bậttắt-thiết-bị-cũ)
  - [Hướng dẫn Thêm](#hướng-dẫn-thêm)
    - [Tùy chỉnh chỉ dẫn hệ thống (system instruction) cho Voice Assist](#tùy-chỉnh-chỉ-dẫn-hệ-thống-system-instruction-cho-voice-assist)
    - [Phát video mới từ kênh YouTube yêu thích](#phát-video-mới-từ-kênh-youtube-yêu-thích)
    - [Theo dõi các thiết bị mất kết nối (unavailable)](#theo-dõi-các-thiết-bị-mất-kết-nối-unavailable)
    - [Tự động chuyển đổi giao diện (theme) sáng/tối](#tự-động-chuyển-đổi-giao-diện-theme-sángtối)
    - [Hướng dẫn cài đặt tìm kiếm vị trí thiết bị](#hướng-dẫn-cài-đặt-tìm-kiếm-vị-trí-thiết-bị)

---

**Lưu ý:** Hãy đọc kỹ mô tả và hướng dẫn đi kèm mỗi blueprint trước khi cài đặt hoặc cập nhật.

---

## Voice Assist - Hẹn giờ & Lên lịch Thông minh

Bạn muốn bật điều hòa trong 30 phút rồi tự tắt? Hay muốn đèn ngủ tự động giảm độ sáng sau 1 tiếng?
Blueprint này biến Voice Assist thành một trợ lý quản lý thời gian thực thụ. Bạn có thể ra lệnh giọng nói tự nhiên để **tạo, gia hạn, tạm dừng, tiếp tục hoặc hủy** lịch trình cho bất kỳ thiết bị nào.

**Tính năng nổi bật:**

- **Hiểu ngôn ngữ tự nhiên:** Chỉ cần nói "Bật quạt 1 tiếng nữa tắt", không cần đúng cú pháp cứng nhắc.
- **Quản lý toàn diện:** Hỗ trợ đầy đủ các lệnh như tạo mới, gia hạn thêm giờ, tạm dừng lịch đang chạy hoặc hủy bỏ.
- **Bền bỉ & Tin cậy:** Mọi lịch trình đều được lưu lại và **tự động khôi phục** nếu Home Assistant khởi động lại. Bạn không lo bị mất hẹn giờ khi mất điện.
- **Điều khiển đa dạng:** Hỗ trợ hầu hết các loại thiết bị: Đèn (độ sáng, màu), Rèm (đóng/mở/vị trí), Quạt (tốc độ/tuốc năng), Điều hòa, Robot hút bụi, Media Player, v.v.
- **Nhận diện thông minh:** Tự động nhận diện thiết bị qua tên gọi thân mật (alias) mà bạn hay dùng.
- **Phản hồi chi tiết:** Khi hỏi "Có lịch nào đang chạy không?", trợ lý sẽ liệt kê rõ ràng tên thiết bị và thời gian còn lại.

**Ví dụ lệnh thoại:**

- "Bật đèn phòng khách màu vàng 50% trong 2 tiếng."
- "Mở rèm phòng ngủ 15 phút để thoáng khí rồi đóng lại."
- "Gia hạn thêm 30 phút cho quạt phòng bé."
- "Tạm dừng lịch tưới cây."
- "Có thiết bị nào đang hẹn giờ không?"

**Ứng dụng thực tế:**

- **Tiết kiệm điện:** Hẹn giờ tắt máy sưởi, bình nóng lạnh hoặc quạt khi đi ngủ.
- **Tiện nghi:** Tự động điều chỉnh ánh sáng, rèm cửa theo ngữ cảnh sinh hoạt mà không cần cầm điện thoại.
- **Yên tâm:** Không lo quên tắt các thiết bị quan trọng nhờ tính năng tự động khôi phục sau khởi động lại.

Để sử dụng đầy đủ tính năng, bạn cần cài đặt **cả 3 blueprint** sau:

1. **Blueprint Điều khiển (LLM):** Xử lý lệnh thoại và điều phối hành động.
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fdevices_schedules_controller_full_llm.yaml)
2. **Blueprint Lõi Lịch trình:** Chịu trách nhiệm tạo và quản lý các lịch trình.
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fdevices_schedules.yaml)
3. **Blueprint Khôi phục:** Tự động khôi phục các lịch trình đang hoạt động khi Home Assistant khởi động lại.
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fdevices_schedules_restart_handler.yaml)

---

## Voice Assist - Ghi nhớ và Truy xuất Thông tin

Bạn hay quên mật khẩu Wi-Fi? Hay không nhớ đã để xe ở cột nào dưới hầm? Hãy để Voice Assist làm "bộ não thứ hai" của bạn.

**Tính năng nổi bật:**

- **Ghi nhớ mọi thứ:** Từ những việc nhỏ nhặt như "Chìa khóa để ở ngăn kéo bàn" đến những nhắc nhở cần thiết như "Mã số khách hàng của cửa hàng ABC".
- **Truy xuất thông minh:** Không cần nhớ từ khóa chính xác. Chỉ cần hỏi "Xe đậu ở đâu?" hay "Pass wifi là gì?", trợ lý sẽ tự tìm thông tin liên quan nhất.
- **Phân loại linh hoạt:**
  - **Cá nhân (User):** Dành cho thông tin riêng (ví dụ: size quần áo, thực đơn ăn kiêng).
  - **Gia đình (Household):** Chia sẻ cho cả nhà (ví dụ: mật khẩu cổng, lịch đổ rác).
  - **Tạm thời (Session):** Chỉ nhớ trong lúc trò chuyện.
- **Tự động dọn dẹp:** Thiết lập thời gian tự hủy cho các ghi nhớ ngắn hạn (ví dụ: vị trí đỗ xe tại trung tâm thương mại).

**Ví dụ lệnh thoại:**

- "Ghi nhớ mật khẩu Wi-Fi khách là `khachdenchoi123`."
- "Lưu lại vị trí đỗ xe là hầm B2 cột D5, nhớ trong 1 ngày thôi."
- "Nhắc tôi số điện thoại của bác sĩ là 0912345678."
- "Tìm xem xe đang đỗ ở đâu?"
- "Mật khẩu Wi-Fi khách là gì nhỉ?"

**Ứng dụng thực tế:**

- Lưu trữ an toàn các thông tin ít dùng nhưng quan trọng.
- Chia sẻ thông tin chung cho các thành viên trong gia đình mà không cần nhắn tin đi lại.
- Ghi chú nhanh các việc cần làm hoặc vị trí đồ vật ngay khi vừa nghĩ ra.

_Tùy chọn phiên bản bạn muốn sử dụng:_

**Phiên bản LLM (Đa ngôn ngữ):**
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fmemory_tool_full_llm.yaml)

**Phiên bản Local (Chỉ tiếng Anh, hoạt động offline):**
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fmemory_tool_local.yaml)

---

## Voice Assist - Phân tích Hình ảnh Camera

Biến camera an ninh thành "đôi mắt" thông minh cho trợ lý ảo. Không cần mở ứng dụng soi từng góc, hãy để Voice Assist nhìn giúp bạn.

**Tính năng nổi bật:**

- **Thị giác máy tính:** Voice Assist có thể "xem" hình ảnh từ camera và mô tả chi tiết những gì đang diễn ra.
- **Quan sát toàn diện:** Hỗ trợ kết nối nhiều camera cùng lúc (cổng, sân, phòng khách...) để có cái nhìn bao quát.
- **Phản hồi tức thì:** Chụp ảnh và phân tích ngay tại thời điểm bạn hỏi.

**Ví dụ lệnh thoại:**

- "Xem camera cổng có ai đang đứng đó không?"
- "Kiểm tra xem con mèo đang ở sân trước hay sân sau?"
- "Nhìn xem cửa gara đã đóng chưa?"
- "Ngoài sân có xe lạ nào không?"

**Ứng dụng thực tế:**

- **An ninh:** Kiểm tra nhanh tình hình quanh nhà khi nghe tiếng động lạ vào ban đêm.
- **Giám sát:** Trông chừng trẻ nhỏ hoặc thú cưng mà không cần dán mắt vào màn hình điện thoại.
- **Tiện lợi:** Xác nhận nhanh các trạng thái vật lý (cửa đóng/mở, đèn sáng/tắt) mà cảm biến có thể bỏ sót.

Để sử dụng tính năng này, bạn cần cài đặt **cả 2 blueprint**:

1. **Blueprint Chụp ảnh:** Chụp lại hình ảnh từ camera được yêu cầu.
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fcamera_snapshot_full_llm.yaml)
2. **Blueprint Phân tích (LLM):** Gửi ảnh chụp cho mô hình ngôn ngữ để phân tích và trả lời.
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Ffile_content_analyzer_full_llm.yaml)

---

## Voice Assist - Quản lý Lịch trình & Sự kiện

Quản lý lịch trình cá nhân của bạn bằng giọng nói một cách tự nhiên và hiệu quả.

### Tạo Sự kiện Lịch

Sắp xếp lịch trình bằng giọng nói như đang trò chuyện với trợ lý. Blueprint tự động hóa việc tạo sự kiện cho mọi lời nhắc, cuộc họp hay chuyến du lịch vào lịch của bạn.

**Tính năng nổi bật:**

- **Nhận diện ngôn ngữ tự nhiên:** Tự động phân tích ngày, giờ, và thời lượng từ câu lệnh của bạn.
- **Tạo sự kiện nhanh:** Thêm sự kiện vào lịch mà không cần nhập liệu thủ công.
- **Tích hợp liền mạch:** Hoạt động hoàn hảo với Lịch Google đã được cấu hình trong Home Assistant.

**Ví dụ lệnh thoại:**

- "Tạo lịch 2 giờ chiều mai đi cắt tóc."
- "Lên lịch 9 giờ sáng mai họp trong 3 tiếng."
- "Thêm lịch thứ bảy này về quê."

**Ứng dụng thực tế:**

- Nhanh chóng tạo lời nhắc, lịch hẹn khi đang lái xe hoặc bận tay.
- Thêm các sự kiện gia đình, công việc vào lịch ngay khi nghĩ ra.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fcreate_calendar_event_full_llm.yaml)

### Tra cứu Sự kiện trong Lịch

Hỏi và nhận thông tin về các sự kiện đã có trong lịch của bạn như sinh nhật, cuộc hẹn, ngày kỷ niệm.

**Ví dụ lệnh thoại:**

- "Tuần này có lịch gì không?"
- "Tháng này có sự kiện gì đáng chú ý không?"

**Ứng dụng thực tế:**

- Kiểm tra nhanh lịch trình trong ngày hoặc tuần mà không cần mở ứng dụng lịch.
- Đảm bảo bạn không bỏ lỡ các sự kiện quan trọng.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fcalendar_events_lookup_full_llm.yaml)

---

## Voice Assist - Tra cứu & Chuyển đổi Lịch Âm

Mang văn hóa truyền thống vào ngôi nhà thông minh. Tra cứu ngày âm, xem ngày tốt xấu hay đếm ngược đến Tết ngay trên Home Assistant.

### Tra cứu & chuyển đổi Lịch Âm

Công cụ chuyển đổi lịch Âm - Dương mạnh mẽ, hoạt động hoàn toàn **Offline** (không cần internet), đảm bảo tốc độ phản hồi tức thì.

**Tính năng nổi bật:**

- **Siêu tốc & Riêng tư:** Xử lý nội bộ, không phụ thuộc vào API bên ngoài.
- **Thông tin chuyên sâu:** Cung cấp đầy đủ Can Chi (Giáp Thìn, Ất Tỵ...), Tiết khí, Giờ hoàng đạo.
- **Tư vấn ngày tốt/xấu:** Biết ngay hôm nay nên làm gì, kiêng gì theo phong tục.
- **Đếm ngược sự kiện:** Luôn biết chính xác còn bao nhiêu ngày nữa đến Tết Nguyên Đán hay các ngày lễ lớn.

**Ví dụ lệnh thoại:**

- "Hôm nay là bao nhiêu âm?"
- "Chủ nhật tuần này là ngày tốt hay xấu?"
- "Còn bao nhiêu ngày nữa đến Tết?"
- "Đổi ngày 20/11 dương lịch sang âm lịch."

**Ứng dụng thực tế:**

- Lên kế hoạch cho các công việc quan trọng (cưới hỏi, động thổ, khai trương).
- Theo dõi các ngày rằm, mùng 1 để chuẩn bị đồ cúng lễ.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fdate_lookup_and_conversion_full_llm.yaml)

### Tạo Sự kiện theo Lịch Âm

Tự động thêm các sự kiện quan trọng tính theo lịch Âm (giỗ, ngày kỷ niệm, cưới hỏi...) vào lịch của bạn.

**Lưu ý:** Blueprint này được thiết kế để **chạy thủ công** hoặc thông qua tự động hóa, yêu cầu người dùng điền thông tin trực tiếp qua giao diện Home Assistant. Nó **không hỗ trợ lệnh thoại** qua Voice Assist.

**Tính năng nổi bật:**

- **Chuyển đổi tự động:** Tự động tính toán và tạo sự kiện vào ngày dương lịch tương ứng hàng năm.
- **Chính xác & Tiện lợi:** Không còn phải tự quy đổi thủ công hay sợ quên các ngày lễ truyền thống.

**Ứng dụng thực tế:**

- Đảm bảo không bao giờ bỏ lỡ các ngày giỗ, cúng bái quan trọng của gia đình.
- Tự động nhắc nhở các ngày kỷ niệm, sinh nhật tính theo lịch âm.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fcreate_lunar_events.yaml)

---

## Chatbot Tương tác & Điều khiển Nhà thông minh

Đừng chỉ ra lệnh, hãy trò chuyện với ngôi nhà của bạn. Tạo Bot Telegram hoặc Zalo để điều khiển nhà từ xa với khả năng hiểu ngữ cảnh và phản hồi thông minh.

**Tính năng nổi bật:**

- **Hội thoại hai chiều:** Bot không chỉ nhận lệnh mà còn biết hỏi lại để làm rõ ý bạn (ví dụ: "Bạn muốn bật điều hòa phòng nào?").
- **Nhận diện hình ảnh:** Gửi ảnh một thiết bị hỏng hay một loài cây lạ, bot sẽ phân tích và trả lời bạn.
- **Điều khiển mọi lúc mọi nơi:** Tắt đèn, mở cổng hay kiểm tra camera ngay trên giao diện chat quen thuộc.

**Ứng dụng thực tế:**

- Bạn đang đi làm và muốn kiểm tra xem đã tắt bếp chưa? Chỉ cần nhắn tin hỏi bot.
- Gửi ảnh đồng hồ điện/nước để bot đọc chỉ số giúp bạn.

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

## Voice Assist - Gửi Tin nhắn & Hình ảnh

Đang lái xe hoặc tay dính dầu mỡ? Hãy dùng giọng nói để gửi tin nhắn, chia sẻ vị trí hoặc hình ảnh camera tới người thân qua Telegram/Zalo.

**Tính năng nổi bật:**

- **Nhắn tin rảnh tay:** Đọc nội dung tin nhắn và Assistant sẽ gửi đi ngay lập tức.
- **Chia sẻ thông minh:** Tự động đính kèm link Google Maps khi bạn nhắc đến một địa điểm.
- **Báo cáo hình ảnh:** Ra lệnh chụp ảnh từ camera an ninh và gửi ngay vào nhóm chat gia đình.

**Ví dụ lệnh thoại:**

- "Gửi danh sách quán ăn ngon ở Nha Trang lên nhóm Telegram gia đình."
- "Gửi vị trí Hoàng Thành Thăng Long qua Zalo cho vợ."
- "Chụp ảnh camera cổng gửi vào nhóm chat."

**Ứng dụng thực tế:**

- Thông báo nhanh cho người thân khi bạn đang bận không thể cầm điện thoại.
- Chia sẻ ngay lập tức một khoảnh khắc thú vị hoặc một địa điểm đẹp vừa tìm thấy.

_Cài đặt blueprint cho nền tảng bạn muốn gửi tin đến:_

**Gửi đến Telegram:**
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fsend_to_telegram_full_llm.yaml)

**Gửi đến Zalo (Official Bot):**
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fsend_to_zalo_bot_full_llm.yaml)

**Gửi đến Zalo (Custom Bot):**
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fsend_to_zalo_custom_bot_full_llm.yaml)

---

## Voice Assist - Tra cứu Thông tin Internet

Đừng để Assistant chỉ biết tắt/bật đèn. Hãy biến nó thành một cuốn bách khoa toàn thư sống, sẵn sàng giải đáp mọi thắc mắc của bạn với dữ liệu cập nhật từ Google.

**Lưu ý:** Tính năng này chỉ áp dụng cho Gemini, vì nó được tích hợp với Google Tìm kiếm để truy cập và cung cấp thông tin cập nhật.

**Tính năng nổi bật:**

- **Kiến thức vô tận:** Truy cập kho dữ liệu khổng lồ của Google để trả lời mọi câu hỏi từ lịch sử, địa lý đến tin tức thời sự.
- **Tóm tắt thông minh:** Không đọc một danh sách link dài dòng. Assistant sẽ tổng hợp và trả lời ngắn gọn, súc tích đúng trọng tâm.
- **Cập nhật realtime:** Biết được giá vàng hôm nay, kết quả bóng đá tối qua hay sự kiện đang hot trên mạng xã hội.

**Ví dụ lệnh thoại:**

- "Điểm chuẩn Đại học Bách Khoa Hà Nội năm nay là bao nhiêu?"
- "Tóm tắt diễn biến chính của trận chung kết World Cup vừa rồi."
- "Giá iPhone 17 Pro Max hiện tại là bao nhiêu?"
- "Công thức nấu món Phở bò chuẩn vị Bắc."

**Ứng dụng thực tế:**

- Tra cứu nhanh thông tin khi đang làm bếp, lái xe hoặc trò chuyện cùng bạn bè.
- Giải đáp thắc mắc của trẻ nhỏ về thế giới xung quanh một cách chính xác.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fadvanced_google_search_full_llm.yaml)

---

## Voice Assist - Tìm kiếm & Phát Video YouTube

Biến TV của bạn thành rạp chiếu phim thông minh. Không cần remote, không cần gõ phím, chỉ cần nói những gì bạn muốn xem.

**Tính năng nổi bật:**

- **Hiểu ý người xem:** Tìm video theo mô tả nội dung ("nhạc thư giãn buổi sáng", "review xe VinFast") thay vì từ khóa cứng nhắc.
- **Chọn lọc thông minh:** Tự động chọn video phù hợp nhất (nhiều view, chất lượng cao) để phát.
- **Học tập & Giải trí:** Tìm video bài giảng cho con hoặc video ca nhạc cho bố mẹ chỉ trong tích tắc.

**Ví dụ lệnh thoại:**

- "Mở video nhạc không lời nhẹ nhàng để đọc sách."
- "Tìm phim tài liệu về chiến thắng Điện Biên Phủ."
- "Xem review iPhone 17 Pro Max mới nhất."

**Ứng dụng thực tế:**

- Giúp người lớn tuổi và trẻ nhỏ dễ dàng xem nội dung yêu thích mà không cần thao tác phức tạp trên remote.
- Vừa nấu ăn vừa ra lệnh mở video hướng dẫn công thức.

Để sử dụng tính năng này, bạn cần cài đặt **cả 2 blueprint**:

1. **Blueprint Tìm kiếm (LLM):** Phân tích câu hỏi và tìm kiếm video phù hợp.
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fadvanced_youtube_search_full_llm.yaml)
2. **Blueprint Phát video:** Lấy thông tin video và phát trên media player.
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fplay_youtube_video_full_llm.yaml)

---

## Voice Assist - Theo dõi Kênh YouTube Yêu thích

Bạn là fan cứng của "Trực Tiếp Game" hay "MixiGaming"? Blueprint này giúp bạn không bao giờ bỏ lỡ video mới nhất từ các idol.

**Tính năng nổi bật:**

- **Cập nhật liên tục:** Tự động kiểm tra các kênh bạn theo dõi.
- **Phát ngay lập tức:** Lệnh "Có video mới không?" sẽ tự động phát video vừa ra lò lên TV.
- **Thông báo chủ động:** Nhận tin nhắn ngay khi kênh yêu thích đăng tải nội dung mới.

**Ví dụ lệnh thoại:**

- "Kênh Khoai Lang Thang có gì mới không?"
- "Mở video mới nhất của HOA BAN FOOD"

**Ứng dụng thực tế:**

- Xem tin tức buổi sáng từ các kênh thời sự uy tín chỉ với một câu lệnh khi vừa thức dậy.
- Giải trí buổi tối với các vlog du lịch mới nhất mà không cần lướt điện thoại tìm kiếm.

[**Xem hướng dẫn chi tiết**](/home_assistant_play_favorite_youtube_channel_videos.md)

Để sử dụng tính năng này, bạn cần cài đặt **cả 2 blueprint**:

1. **Blueprint Lấy thông tin (LLM):** Kiểm tra kênh và lấy thông tin video mới nhất.
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fget_youtube_video_info_full_llm.yaml)
2. **Blueprint Phát video:** Lấy thông tin video và phát trên media player (có thể tái sử dụng từ blueprint ở trên).
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fplay_youtube_video_full_llm.yaml)

---

## Voice Assist - Điều khiển Quạt Thông minh

Nóng quá? Chỉ cần than thở một câu, quạt sẽ tự tăng tốc. Blueprint giúp bạn điều khiển luồng gió chính xác theo ý muốn.

**Tính năng nổi bật:**

- **Điều chỉnh linh hoạt:** Tăng/giảm tốc độ theo phần trăm cụ thể hoặc mức độ mong muốn.
- **Kiểm soát hướng gió:** Bật/tắt tuốc năng (quay) bằng giọng nói.
- **Đồng bộ:** Ra lệnh cho một quạt cụ thể hoặc tất cả quạt trong nhà cùng lúc.

**Ví dụ lệnh thoại:**

- "Tăng quạt phòng khách lên mạnh nhất."
- "Cho quạt phòng ngủ quay đi, nóng quá."
- "Giảm tốc độ quạt bàn ăn xuống 30%."

**Ứng dụng thực tế:**

- Điều chỉnh gió cho phù hợp với nhiệt độ phòng mà không cần rời khỏi giường hay ghế sofa.
- Tắt nhanh tất cả quạt khi ra khỏi nhà.

_Cài đặt blueprint cho chức năng bạn muốn sử dụng:_

**Điều khiển Tốc độ quạt:**
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Ffan_speed_control_full_llm.yaml)

**Điều khiển Xoay quạt:**
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Ffan_oscillation_control_full_llm.yaml)

---

## Voice Assist - Điều khiển Điều hòa Thông minh

Giữ không khí trong lành và nhiệt độ lý tưởng trong nhà chỉ bằng giọng nói. Blueprint này giúp bạn kiểm soát máy điều hòa một cách toàn diện, từ chế độ hoạt động đến tốc độ quạt.

**Tính năng nổi bật:**

- **Kiểm soát chế độ:** Chuyển đổi giữa các chế độ làm mát, sưởi ấm, hút ẩm, chỉ quạt hoặc tự động một cách dễ dàng.
- **Điều chỉnh tốc độ quạt:** Thiết lập tốc độ quạt theo các mức cài đặt sẵn (thấp, trung bình, cao) hoặc các giá trị định lượng như "mạnh nhất", "nhẹ nhất".
- **Hỗ trợ alias:** Nhận diện điều hòa qua tên thân mật hoặc tên bạn đã đặt trong Home Assistant.
- **Xử lý nhiều thiết bị:** Điều khiển một hoặc nhiều điều hòa cùng lúc.

**Ví dụ lệnh thoại:**

- "Bật điều hòa phòng khách sang chế độ làm mát và quạt tốc độ trung bình."
- "Chuyển điều hòa phòng ngủ sang chế độ khô."
- "Tăng quạt điều hòa ở hành lang lên tốc độ cao."
- "Tắt tất cả điều hòa."

**Ứng dụng thực tế:**

- Điều chỉnh môi trường sống theo ý muốn mà không cần tìm remote.
- Tiết kiệm năng lượng bằng cách thiết lập chế độ phù hợp.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fac_mode_and_fan_control_full_llm.yaml)

---

## Voice Assist - Định vị & Tìm kiếm Thiết bị

"Điện thoại mình đâu rồi?" - Câu hỏi kinh điển mỗi sáng. Hãy để Assistant giúp bạn tìm nó ngay lập tức.

**Tính năng nổi bật:**

- **Định vị trong nhà:** Cho biết điện thoại đang ở phòng nào (dựa trên sóng Bluetooth/Wi-Fi).
- **Kích hoạt chuông:** Bắt điện thoại đổ chuông ầm ĩ kể cả khi đang để chế độ im lặng.
- **Hỗ trợ đa thiết bị:** Tìm iPhone, Android, iPad hay bất kỳ thiết bị nào có cài app Home Assistant.

**Ví dụ lệnh thoại:**

- "Tìm xem điện thoại của bố đang ở đâu?"
- "Làm cho cái iPad đổ chuông đi, mình tìm không thấy."

**Ứng dụng thực tế:**

- Tiết kiệm thời gian tìm kiếm đồ đạc mỗi khi vội ra khỏi nhà.
- Giám sát xem con cái đã đi học về nhà an toàn chưa (thiết bị đã kết nối mạng nhà).

[**Xem hướng dẫn chi tiết**](/home_assistant_device_location_lookup_guide.md)

Để sử dụng tính năng này, bạn cần cài đặt **cả 2 blueprint**:

1. **Blueprint Tìm vị trí (LLM):** Xử lý yêu cầu và tìm vị trí thiết bị.
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fdevice_location_lookup_full_llm.yaml)
2. **Blueprint Đổ chuông (LLM):** Kích hoạt thiết bị đổ chuông.
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fdevice_ringing_full_llm.yaml)

---

## Voice Assist - Tra cứu Phạt nguội

Tra cứu tình trạng phạt nguội của bất kỳ phương tiện nào bằng giọng nói, sử dụng dữ liệu trực tiếp từ Cổng thông tin của Cục CSGT.

**Lưu ý:** Tính năng này chỉ áp dụng cho hệ thống tra cứu phạt nguội tại Việt Nam.

**Ví dụ lệnh thoại:**

- "Kiểm tra phạt nguội ô tô 30G-123.45."
- "Xe máy 29-T1 567.89 có bị phạt nguội không?"

**Ứng dụng thực tế:**

- Kiểm tra định kỳ xe của gia đình.
- Kiểm tra xe cũ trước khi mua để tránh các khoản phạt tồn đọng.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Ftraffic_fine_lookup_full_llm.yaml)

---

## Tự động Cảnh báo Phạt nguội

Nhận cảnh báo ngay khi có vi phạm giao thông mới được ghi nhận trên hệ thống của Cục CSGT cho xe của bạn.

**Lưu ý:** Tính năng này chỉ áp dụng cho hệ thống tra cứu phạt nguội tại Việt Nam.

**Tính năng nổi bật:**

- **Tự động kiểm tra:** Định kỳ quét hệ thống để phát hiện vi phạm mới.
- **Thông báo tức thì:** Gửi thông báo đến Home Assistant ngay khi có phạt nguội.
- **Hỗ trợ nhiều xe:** Dễ dàng cấu hình để theo dõi nhiều biển số xe cùng lúc.

**Ứng dụng thực tế:**

- Giúp bạn nắm được thông tin vi phạm sớm để xử lý kịp thời.
- Quản lý tình trạng phạt nguội cho tất cả phương tiện của gia đình một cách tự động.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Ftraffic_fine_notification.yaml)

---

## Đồng bộ Trạng thái Thiết bị

Đồng bộ trạng thái `on/off` giữa nhiều thiết bị, hoạt động tương tự như một công tắc cầu thang hai chiều ảo.

**Ứng dụng thực tế:**

- Một công tắc vật lý có thể điều khiển một bóng đèn thông minh không nối dây trực tiếp.
- Bật một đèn thì các đèn khác trong cùng khu vực cũng bật theo.

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Flink_multiple_devices.yaml)

---

## Các Blueprint đã lỗi thời

### Voice Assist - Hẹn giờ Bật/Tắt Thiết bị (Cũ)

**Sử dụng phiên bản mới [Voice Assist - Hẹn giờ & Lên lịch Thông minh](#voice-assist---hẹn-giờ--lên-lịch-thông-minh) để có nhiều tính năng hơn.**

Để sử dụng, bạn cần cài đặt **cả 2 blueprint**:

1. **Blueprint Điều khiển (LLM):**
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fdevice_control_timer_full_llm.yaml)
2. **Blueprint Công cụ Hẹn giờ:**
   [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fluuquangvu%2Ftutorials%2Fblob%2Fmain%2Fdevice_control_tool.yaml)

---

## Hướng dẫn Thêm

### [Tùy chỉnh chỉ dẫn hệ thống (system instruction) cho Voice Assist](/home_assistant_voice_instructions.md)

### [Phát video mới từ kênh YouTube yêu thích](/home_assistant_play_favorite_youtube_channel_videos.md)

### [Theo dõi các thiết bị mất kết nối (unavailable)](/home_assistant_unavailable_devices.md)

### [Tự động chuyển đổi giao diện (theme) sáng/tối](/home_assistant_ios_themes.md)

### [Hướng dẫn cài đặt tìm kiếm vị trí thiết bị](/home_assistant_device_location_lookup_guide.md)

---

**Nếu bạn thấy bộ sưu tập này hữu ích, đừng ngần ngại chia sẻ với cộng đồng Home Assistant nhé! Hãy theo dõi để cập nhật thêm nhiều blueprint độc đáo khác trong tương lai!**



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
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fsend_to_zalo_custom_bot_full_llm.yaml
)
## 🔗 Gửi tele có delete
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fsend_to_telegram_full_llm.yaml
)
## 🔗 Tạo ảnh có đính kèm ảnh
Go to Settings → Devices & Services → Helpers
Click "+ Create Helper"
Choose "Text"
Name it appropriately
Set a max length (e.g., 255)
Save it
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Fai_image_attrack.yaml
)
## 🔗 Tạo ảnh theo thời tiết
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
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2FAI_Weather_Image_Generator.yaml
)
## 🔗 Blueprint Phân tích (LLM):** Gửi ảnh chụp cho mô hình ngôn ngữ để phân tích và trả lời.
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTriTue2011%2FBlueprint%2Fmain%2Ffile_content_analyzer_full_llm.yaml
)
