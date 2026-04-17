"""
Weather Image Generator — PyScript
File: /config/pyscript/weather_image.py
"""
import base64
import json
from pathlib import Path

INVOKE_URL    = "https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux.2-klein-4b"
DEBUG_JSON    = "/config/media/weather/debug_response.json"
DEFAULT_W     = 1344
DEFAULT_H     = 768
DEFAULT_STEPS = 4


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
        with urllib.request.urlopen(req, timeout=120) as resp:
            return resp.status, resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8")


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
def generate_weather_image(
    prompt      = "a beautiful sky",
    output_path = "/config/media/weather/weather_current.png",
    steps       = DEFAULT_STEPS,
    width       = DEFAULT_W,
    height      = DEFAULT_H,
):
    api_key = pyscript.config.get("nvidia_api_key", "")
    if not api_key:
        log.error("weather_image: Thiếu nvidia_api_key trong pyscript config")
        return

    log.info(f"weather_image: Bắt đầu | steps={steps} {width}x{height} | '{prompt[:60]}'")

    payload_bytes = json.dumps({
        "prompt": prompt,
        "width":  int(width),
        "height": int(height),
        "seed":   0,
        "steps":  int(steps),
    }).encode("utf-8")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept":        "application/json",
        "Content-Type":  "application/json",
    }

    status, body_text = _http_post(INVOKE_URL, headers, payload_bytes)

    if status != 200:
        log.error(f"weather_image: HTTP {status} — {body_text[:300]}")
        return

    body = json.loads(body_text)

    try:
        _save_text(DEBUG_JSON, json.dumps(body, ensure_ascii=False, indent=2))
    except Exception as e:
        log.warning(f"weather_image: Không lưu debug JSON: {e}")

    b64 = body.get("artifacts", [{}])[0].get("base64", "")
    if not b64:
        log.error(f"weather_image: Không có ảnh: {str(body)[:300]}")
        return

    _save_file(output_path, base64.b64decode(b64))
    log.info(f"weather_image: ✅ Ảnh đã lưu → {output_path}")