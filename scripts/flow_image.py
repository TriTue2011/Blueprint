"""
Google Flow Image Generator — PyScript
File: /config/pyscript/flow_image.py
"""
import json

# Giá trị mặc định — dùng khi không truyền tham số từ blueprint
DEFAULT_FLOW_URL   = ""    # bắt buộc truyền api_url từ blueprint (không đặt địa chỉ riêng ở đây)
DEFAULT_PROJECT_ID = ""    # bắt buộc truyền project_id từ blueprint
DEBUG_JSON         = "/config/media/flow/debug_response.json"


@pyscript_executor
def _http_post(url, headers, payload_bytes):
    import urllib.request
    import urllib.error
    req = urllib.request.Request(
        url,
        data=payload_bytes,
        headers=headers,
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


@pyscript_executor
def _save_file(path_str, data_bytes):
    from pathlib import Path
    p = Path(path_str)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(data_bytes)


@pyscript_executor
def _save_text(path_str, text):
    from pathlib import Path
    p = Path(path_str)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)


@service
def generate_flow_image(
    prompt      = "a beautiful sky",
    output_path = "/config/www/flow_latest.jpg",
    project_id  = "",
    api_url     = "",
):
    api_key = pyscript.config.get("flow_api_key", "")
    if not api_key:
        log.error("flow_image: Thiếu flow_api_key trong pyscript config")
        return

    # Dùng giá trị truyền vào, fallback về mặc định
    pid = project_id if project_id and project_id.strip() else DEFAULT_PROJECT_ID
    url = api_url if api_url and api_url.strip() else DEFAULT_FLOW_URL

    if not pid or not url:
        log.error("flow_image: Thiếu project_id hoặc api_url (hãy điền ở blueprint)")
        return

    log.info(f"flow_image: Bắt đầu | url={url} | project={pid} | '{prompt[:80]}'")

    payload_bytes = json.dumps({
        "project_id":    pid,
        "prompt":        prompt,
        "return_binary": True,
    }).encode("utf-8")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type":  "application/json",
    }

    status, body_bytes = _http_post(url, headers, payload_bytes)

    if status != 200:
        err_text = body_bytes.decode("utf-8", errors="replace") if isinstance(body_bytes, bytes) else str(body_bytes)
        log.error(f"flow_image: HTTP {status} — {err_text[:300]}")
        try:
            _save_text(DEBUG_JSON, err_text)
        except Exception:
            pass
        return

    # Kiểm tra có phải ảnh JPEG thật không (magic bytes FF D8)
    if isinstance(body_bytes, bytes) and body_bytes[:2] != b'\xff\xd8':
        err_text = body_bytes.decode("utf-8", errors="replace")
        log.error(f"flow_image: Không phải ảnh JPEG — {err_text[:300]}")
        try:
            _save_text(DEBUG_JSON, err_text)
        except Exception:
            pass
        return

    _save_file(output_path, body_bytes)
    log.info(f"flow_image: ✅ Ảnh đã lưu → {output_path} ({len(body_bytes) // 1024}KB)")