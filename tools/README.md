# Hai trình soát chạy trước khi đẩy lên

Kho này có hai trình soát, và một workflow chạy cả hai mỗi lần push.

## `validate_blueprints.py` — schema và Jinja2

Nạp thẳng bộ schema thật của Home Assistant Core để soát từng file YAML, thay vì
chỉ kiểm tra cú pháp YAML suông. Nó bắt bốn nhóm lỗi:

- Sai schema blueprint (`AUTOMATION_BLUEPRINT_SCHEMA`, `BLUEPRINT_SCHEMA`).
- Sai định nghĩa selector (`homeassistant.helpers.selector.validate_selector`).
- Sai cú pháp Jinja2, kiểm bằng đúng engine template của Home Assistant nên nhận
  hết filter và test riêng của HA.
- Tham chiếu `!input` tới một input không hề được khai báo.

```bash
uv run --no-project --python 3.14 --with 'homeassistant>=2026.8.0' \
  python tools/validate_blueprints.py .
```

Home Assistant 2026.8 đòi Python 3.14, còn máy thường chưa có sẵn. Dùng
[`uv`](https://github.com/astral-sh/uv) thì nó tự tải cả hai, không cài gì vào máy.
Truyền một đường dẫn file thay cho `.` nếu chỉ muốn soát một blueprint.

## `check_readme.py` — README có khớp file thật không

Đọc chính các file YAML rồi đối chiếu với những gì README nói về chúng. Bắt đúng
loại sai lệch mà mắt người bỏ qua vì README quá dài:

- Bảng thông tin khai sai **Loại** so với `blueprint.domain` trong file.
- Bảng thông tin khai sai **HA tối thiểu** so với `homeassistant.min_version`.
- Nút Import trỏ vào một file không tồn tại.
- Có file YAML trong kho nhưng README không hề nhắc tới.
- Liên kết mục lục trỏ vào một tiêu đề không có thật — hay hỏng ở những tiêu đề
  có emoji kèm ký tự biến thể ẩn, vì neo GitHub sinh ra khác với trực giác.

Soát cả `README.md` lẫn `README.en.md`, hiểu nhãn của cả hai thứ tiếng.

```bash
python3 tools/check_readme.py .
```

Chỉ dùng thư viện chuẩn, không cần cài gì.

## Chạy tự động

[`.github/workflows/soat-blueprint.yaml`](/.github/workflows/soat-blueprint.yaml)
chạy cả hai trình soát mỗi lần push vào `main` và mỗi pull request. Riêng với
push vào `main`, trước khi soát nó còn đồng bộ `source_url` của mọi blueprint
theo đúng nhánh rồi commit lại kèm `[skip ci]`.

Thứ tự là có chủ đích: đồng bộ `source_url` **trước** rồi mới soát, để thứ được
commit là thứ đã qua kiểm tra. Làm ngược lại thì dòng `source_url` mới chưa ai
soát bao giờ.

`source_url` được chuẩn hoá về dạng `https://github.com/<kho>/blob/<nhánh>/<tệp>`.
Đó là dạng Home Assistant dùng, và [`scripts/blueprints_update.sh`](/scripts/blueprints_update.sh)
cũng tự đổi nó sang `raw.githubusercontent.com` lúc tải, nên hai bên khớp nhau.

## Nguồn

`validate_blueprints.py` lấy nguyên văn từ
[luuquangvu/tutorials](https://github.com/luuquangvu/tutorials/blob/main/tools/validate_blueprints.py)
(giấy phép MIT). Giữ nguyên bản để lần sau đồng bộ chỉ cần chép đè.
`check_readme.py` viết riêng cho kho này.
