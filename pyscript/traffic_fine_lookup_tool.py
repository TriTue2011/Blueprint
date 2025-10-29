import asyncio
import json
import re
import sqlite3
import ssl
import threading
import time
from io import BytesIO
from pathlib import Path

import aiohttp
import google.api_core.exceptions
from PIL import Image
from PIL import ImageOps
from bs4 import BeautifulSoup
from bs4.element import AttributeValueList
from typing_extensions import Any, Buffer, cast

TTL = 30  # Cache retention period (1-30 days)
RETRY_LIMIT = 3
GET_URL = "https://www.csgt.vn/"
POST_URL = "https://www.csgt.vn/?mod=contact&task=tracuu_post&ajax"
CAPTCHA_URL = "https://www.csgt.vn/lib/captcha/captcha.class.php"
GET_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,vi;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "DNT": "1",
    "Host": "www.csgt.vn",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0",
    "sec-ch-ua": '"Microsoft Edge";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}
POST_HEADERS = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,vi;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "DNT": "1",
    "Host": "www.csgt.vn",
    "Origin": "https://www.csgt.vn",
    "Pragma": "no-cache",
    "Referer": "https://www.csgt.vn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Microsoft Edge";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}

DB_PATH = Path("/config/cache.db")

GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_API_KEY = pyscript.config.get("gemini_api_key")

if not GEMINI_API_KEY:
    raise ValueError("You need to configure your Gemini API key")

if TTL < 1 or TTL > 30:
    raise ValueError("TTL must be between 1 and 30")

GEMINI_CLIENT: Any = None

SSL_CTX: ssl.SSLContext | None = None

_CACHE_READY = False
_CACHE_READY_LOCK = threading.Lock()

cache_max_age = TTL * 24 * 60 * 60
cache_min_age = cache_max_age - (
    2 * 60 * 60
)  # Only update cache when existing data is older than 2 hours


def _ensure_cache_db() -> None:
    """Create the cache database directory, SQLite file, and schema if they do not already exist."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.execute("PRAGMA synchronous=NORMAL;")
        conn.execute("PRAGMA temp_store=MEMORY;")
        conn.execute("PRAGMA busy_timeout=3000;")
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS cache_entries
            (
                key        TEXT PRIMARY KEY,
                value      TEXT    NOT NULL,
                expires_at INTEGER NOT NULL
            )
            """
        )
        conn.commit()


def _ensure_cache_db_once(force: bool = False) -> None:
    """Ensure the cache database exists, optionally forcing a rebuild."""
    global _CACHE_READY
    if force:
        _CACHE_READY = False
    if _CACHE_READY and DB_PATH.exists():
        return
    with _CACHE_READY_LOCK:
        if force:
            _CACHE_READY = False
        if not _CACHE_READY or not DB_PATH.exists():
            _ensure_cache_db()
            _CACHE_READY = True


def _reset_cache_ready() -> None:
    """Mark the cache database schema as stale so it will be recreated."""
    global _CACHE_READY
    with _CACHE_READY_LOCK:
        _CACHE_READY = False


async def _cache_prepare_db(force: bool = False) -> bool:
    """Ensure the cache database is ready for use."""
    await asyncio.to_thread(_ensure_cache_db_once, force)
    return True


def _cache_get_sync(key: str) -> tuple[str | None, int | None]:
    """Fetch a cache record synchronously, returning the value and remaining TTL."""
    for attempt in range(2):
        try:
            _ensure_cache_db_once(force=attempt == 1)
            now = int(time.time())
            with sqlite3.connect(DB_PATH) as conn:
                conn.row_factory = sqlite3.Row
                cur = conn.cursor()
                cur.execute("DELETE FROM cache_entries WHERE expires_at <= ?", (now,))
                conn.commit()
                cur.execute(
                    """
                    SELECT value, expires_at
                    FROM cache_entries
                    WHERE key = ?
                      AND expires_at > ?
                    """,
                    (key, now),
                )
                row = cur.fetchone()
            if not row:
                return None, None
            ttl_remaining = max(int(row["expires_at"]) - now, 0)
            return row["value"], ttl_remaining
        except sqlite3.OperationalError:
            _reset_cache_ready()
            if attempt == 0:
                continue
            raise
    return None, None


async def _cache_get(key: str) -> tuple[str | None, int | None]:
    """Return the cached JSON payload for a key and its remaining TTL in seconds."""
    return await asyncio.to_thread(_cache_get_sync, key)


def _cache_set_sync(key: str, value: str, ttl_seconds: int) -> bool:
    """Store or update a cache record synchronously with retry on schema loss."""
    for attempt in range(2):
        try:
            _ensure_cache_db_once(force=attempt == 1)
            now = int(time.time())
            expires_at = now + ttl_seconds
            with sqlite3.connect(DB_PATH) as conn:
                cur = conn.cursor()
                cur.execute("DELETE FROM cache_entries WHERE expires_at <= ?", (now,))
                cur.execute(
                    """
                    INSERT INTO cache_entries (key, value, expires_at)
                    VALUES (?, ?, ?)
                    ON CONFLICT(key) DO UPDATE SET value      = excluded.value,
                                                   expires_at = excluded.expires_at
                    """,
                    (key, value, expires_at),
                )
                conn.commit()
            return True
        except sqlite3.OperationalError:
            _reset_cache_ready()
            if attempt == 0:
                continue
            raise
    return False


async def _cache_set(key: str, value: str, ttl_seconds: int) -> bool:
    """Persist a cache entry with the provided TTL and prune expired records."""
    return await asyncio.to_thread(_cache_set_sync, key, value, ttl_seconds)


def _cache_delete_sync(key: str) -> int:
    """Remove a cache record synchronously and return the rowcount."""
    for attempt in range(2):
        try:
            _ensure_cache_db_once(force=attempt == 1)
            with sqlite3.connect(DB_PATH) as conn:
                cur = conn.cursor()
                cur.execute("DELETE FROM cache_entries WHERE key = ?", (key,))
                deleted = cur.rowcount if cur.rowcount is not None else 0
                conn.commit()
            return max(deleted, 0)
        except sqlite3.OperationalError:
            _reset_cache_ready()
            if attempt == 0:
                continue
            raise
    return 0


async def _cache_delete(key: str) -> int:
    """Remove the cache entry identified by key if it exists."""
    return await asyncio.to_thread(_cache_delete_sync, key)


@pyscript_compile
def _build_ssl_ctx() -> ssl.SSLContext:
    """Build an SSL context compatible with target site requirements.

    Configures ciphers and TLS minimum version explicitly to improve
    compatibility when connecting via aiohttp.

    Returns:
        An initialized `ssl.SSLContext` instance.
    """
    ctx = ssl.create_default_context()
    ctx.set_ciphers(
        "@SECLEVEL=0:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA:ECDHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:DES-CBC3-SHA"
    )
    ctx.minimum_version = ssl.TLSVersion.TLSv1_2
    return ctx


@pyscript_compile
def _build_gemini_client() -> Any:
    """Create a Gemini client using the configured API key.

    Returns:
        Google GenAI client instance.
    """
    import google.genai as genai

    return genai.Client(api_key=GEMINI_API_KEY)


async def _ensure_ssl_ctx() -> None:
    """Ensure the global SSL context is built once in a thread.

    Safe to call multiple times; only initializes when missing.
    """
    global SSL_CTX
    if SSL_CTX is None:
        SSL_CTX = await asyncio.to_thread(_build_ssl_ctx)


async def _ensure_gemini_client() -> None:
    """Ensure the global Gemini client is initialized once in a thread.

    Safe to call multiple times; only initializes when missing.
    """
    global GEMINI_CLIENT
    if GEMINI_CLIENT is None:
        GEMINI_CLIENT = await asyncio.to_thread(_build_gemini_client)


@pyscript_compile
def _extract_violations_from_html(content: str, url: str) -> dict[str, Any]:
    """Parse violations from the result HTML page.

    Args:
        content: HTML content returned by csgt.vn for a lookup.
        url: Final detail URL used to fetch the result page.

    Returns:
        A dict with status (success/error), source URL, message, and details.
    """
    soup = BeautifulSoup(content, "html.parser")
    violations = []
    body_print = soup.find("div", id="bodyPrint123")

    if not body_print:
        return {
            "status": "error",
            "url": url,
            "message": "Không tìm thấy dữ liệu vi phạm",
            "detail": "",
        }

    sections = body_print.find_all(recursive=False)
    current_violation = {}
    for element in sections:
        if "form-group" in element.get("class", AttributeValueList()):
            if not current_violation:
                current_violation = {
                    "Biển kiểm soát": "",
                    "Màu biển": "",
                    "Loại phương tiện": "",
                    "Thời gian vi phạm": "",
                    "Địa điểm vi phạm": "",
                    "Hành vi vi phạm": "",
                    "Trạng thái": "",
                    "Đơn vị phát hiện vi phạm": "",
                    "Nơi giải quyết vụ việc": [],
                }

            label = element.find("label", class_="control-label")
            value = element.find("div", class_="col-md-9")
            if label and value:
                key = label.get_text(strip=True).replace(":", "")
                val = value.get_text(strip=True)
                if key in current_violation:
                    if key != "Nơi giải quyết vụ việc":
                        current_violation[key] = val

            text = element.get_text(strip=True)
            if text and re.match(r"[1-9]\. |Địa chỉ:|Số điện thoại liên hệ:", text):
                current_violation["Nơi giải quyết vụ việc"].append(text)

        elif element.name == "hr":
            if current_violation:
                violations.append(current_violation)
                current_violation = {}

    if current_violation:
        violations.append(current_violation)

    if not violations:
        return {
            "status": "success",
            "url": url,
            "message": "Không có vi phạm giao thông",
            "detail": "",
        }

    return {
        "status": "success",
        "url": url,
        "message": f"Có {len(violations)} vi phạm giao thông",
        "detail": violations,
    }


async def _get_captcha(
    ss: aiohttp.ClientSession, url: str
) -> tuple[BytesIO, None] | tuple[None, str]:
    """Download the CAPTCHA image.

    Args:
        ss: An aiohttp session.
        url: CAPTCHA endpoint URL.

    Returns:
        (BytesIO, None) on success or (None, error_message) on failure.
    """
    try:
        async with ss.get(url, timeout=aiohttp.ClientTimeout(total=60)) as response:
            response.raise_for_status()
            content = await response.read()
            return BytesIO(cast(Buffer, content)), None
    except asyncio.TimeoutError as error:
        return None, f"TimeoutError during retrieve CAPTCHA image: {error}"
    except aiohttp.ClientError as error:
        return None, f"ClientError during retrieve CAPTCHA image: {error}"
    except Exception as error:
        return None, f"An unexpected error during retrieve CAPTCHA image: {error}"


@pyscript_compile
def _process_captcha(
    image: str | BytesIO, threshold: int = 180, factor: int = 8, padding: int = 35
) -> Image.Image:
    """Preprocess CAPTCHA for better OCR.

    Applies grayscale, contrast, binarization, scaling, background removal,
    and crop around glyphs.

    Args:
        image: File path or BytesIO of the CAPTCHA image.
        threshold: Binarization threshold (0-255).
        factor: Scale multiplier for upscaling.
        padding: Padding applied when cropping around glyphs.

    Returns:
        A Pillow Image prepared for OCR.
    """
    img = Image.open(image)
    img = img.convert("L")
    img = ImageOps.autocontrast(img, cutoff=2)
    table = [0] * threshold + [255] * (256 - threshold)
    img = img.point(table)
    img = img.resize(
        (img.width * factor, img.height * factor), resample=Image.Resampling.BOX
    )
    img = img.convert("RGBA")
    for x in range(img.width):
        for y in range(img.height):
            (r, g, b, a) = img.getpixel((x, y))
            if (r, g, b) == (255, 255, 255):
                img.putpixel((x, y), (r, g, b, 0))
    bbox = img.getbbox()
    if bbox:
        (left, upper, right, lower) = bbox
        left = max(0, left - padding)
        upper = max(0, upper - padding)
        right = min(img.width, right + padding)
        lower = min(img.height, lower + padding)
        img = img.crop((left, upper, right, lower))
    img = img.convert("L")
    return img


async def _solve_captcha(
    image: Image.Image, retry_count: int = 1
) -> tuple[str, None] | tuple[None, str]:
    """Solve CAPTCHA using Gemini with optional retries.

    Args:
        image: Preprocessed CAPTCHA image.
        retry_count: Current retry attempt counter.

    Returns:
        (solution_text, None) on success or (None, error_message) on failure.
    """
    prompt = "Extract exactly six consecutive lowercase letters (a-z) and digits (0-9) from this image, no spaces, and output only these characters."
    await _ensure_gemini_client()

    def _solve_captcha_sync(_prompt: str, _image: Image.Image) -> Any:
        return GEMINI_CLIENT.models.generate_content(
            model=GEMINI_MODEL, contents=[_prompt, _image]
        )

    try:
        response = await asyncio.to_thread(_solve_captcha_sync, prompt, image)
        if (
            response.candidates
            and response.candidates[0].content
            and response.candidates[0].content.parts
            and response.candidates[0].content.parts[0].text
        ):
            generated_text = response.candidates[0].content.parts[0].text.strip()
            return generated_text, None
        else:
            reason = (
                response.candidates[0].finish_reason
                if response.candidates
                else "Unknown"
            )
            return None, f"CAPTCHA solving was not successful for reason: {reason}"
    except google.api_core.exceptions.ResourceExhausted as error:
        if retry_count < RETRY_LIMIT:
            print(
                f"Quota exceeded. Retrying in 30 seconds... (Attempt {retry_count}/{RETRY_LIMIT}): {error}"
            )
            await asyncio.sleep(30)
            return await _solve_captcha(image, retry_count + 1)
        else:
            return (
                None,
                f"Quota exhausted and retry limit ({retry_count}/{RETRY_LIMIT}) reached: {error}",
            )
    except AttributeError as error:
        return (
            None,
            f"Possibly incorrect field in the response. Check for proper API handling: {error}",
        )
    except Exception as error:
        return None, f"An unexpected error occurred during CAPTCHA solving: {error}"


async def _check_license_plate(
    license_plate: str, vehicle_type: int, retry_count: int = 1
) -> dict[str, Any]:
    """End-to-end lookup flow against csgt.vn with caching and retries.

    Performs: fetch landing page -> get CAPTCHA -> preprocess -> solve ->
    submit form -> fetch result detail -> parse violations. Caches successful
    results via the shared SQLite cache outside of this function.

    Args:
        license_plate: VN plate number (uppercase, validated by caller).
        vehicle_type: 1=Car, 2=Motorbike, 3=Electric Bicycle.
        retry_count: Current retry attempt counter.

    Returns:
        Parsed response dict with status and details, or error.
    """
    await _ensure_ssl_ctx()
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=SSL_CTX)) as ss:
        try:
            async with ss.get(
                GET_URL, headers=GET_HEADERS, timeout=aiohttp.ClientTimeout(total=60)
            ) as response_1st:
                response_1st.raise_for_status()
                image, error = await _get_captcha(ss, CAPTCHA_URL)

                if not image:
                    return {"error": f"Unable to retrieve CAPTCHA image: {error}"}

                image_filtered = _process_captcha(image)
                captcha, error = await _solve_captcha(image_filtered)

                if not captcha:
                    return {"error": f"CAPTCHA solving was not successful: {error}"}

                captcha = re.sub(r"[^a-zA-Z0-9]", "", captcha).lower()

                data = f"BienKS={license_plate}&Xe={vehicle_type}&captcha={captcha}&ipClient=9.9.9.91&cUrl=1"

                async with ss.post(
                    url=POST_URL,
                    headers=POST_HEADERS,
                    data=data,
                    timeout=aiohttp.ClientTimeout(total=60),
                ) as response_2nd:
                    response_2nd.raise_for_status()
                    response_2nd_json = await response_2nd.json(
                        content_type="text/html"
                    )
                    url = response_2nd_json.get("href")

                    if not url:
                        if retry_count < RETRY_LIMIT:
                            print(
                                f"Retrying in 30 seconds... (Attempt {retry_count}/{RETRY_LIMIT})"
                            )
                            await asyncio.sleep(30)
                            return await _check_license_plate(
                                license_plate, vehicle_type, retry_count + 1
                            )
                        else:
                            return {
                                "error": f"Retry limit ({retry_count}/{RETRY_LIMIT}) reached"
                            }

                    async with ss.get(
                        url=url, timeout=aiohttp.ClientTimeout(total=60)
                    ) as response_3rd:
                        response_3rd.raise_for_status()
                        text_content = await response_3rd.text()
                        response = _extract_violations_from_html(text_content, url)

                        if response and response.get("status") == "success":
                            await _cache_set(
                                f"{license_plate}-{vehicle_type}",
                                json.dumps(response, ensure_ascii=False),
                                cache_max_age,
                            )
                        return response

        except Exception as error:
            if retry_count < RETRY_LIMIT:
                print(
                    f"Retrying in 30 seconds... (Attempt {retry_count}/{RETRY_LIMIT}): {error}"
                )
                await asyncio.sleep(30)
                return await _check_license_plate(
                    license_plate, vehicle_type, retry_count + 1
                )
            else:
                return {
                    "error": f"Retry limit ({retry_count}/{RETRY_LIMIT}) reached: {error}"
                }


@time_trigger("startup")
async def build_cached_ctx() -> None:
    """Run once at HA startup / Pyscript reload."""
    await _cache_prepare_db(force=True)
    await _ensure_ssl_ctx()
    await _ensure_gemini_client()


@service(supports_response="only")
async def traffic_fine_lookup_tool(
    license_plate: str, vehicle_type: int, bypass_caching: bool = False
) -> dict[str, Any]:
    """
    yaml
    name: Traffic Fine Lookup Tool
    description: Check Vietnam traffic fine status on csgt.vn and return parsed results.
    fields:
      license_plate:
        name: License Plate
        description: Vietnam license plate without spaces or dashes.
        example: 29A99999
        required: true
        selector:
          text:
      vehicle_type:
        name: Vehicle Type
        description: Vehicle classification expected by csgt.vn (1=Car, 2=Motorbike, 3=Electric Bicycle).
        example: "1"
        required: true
        selector:
          select:
            options:
              - label: Car
                value: "1"
              - label: Motorbike
                value: "2"
              - label: Electric Bicycle
                value: "3"
        default: "1"
      bypass_caching:
        name: Bypass Caching
        description: Ignore cached data and fetch fresh results (useful for debugging).
        example: false
        selector:
          boolean:
    """
    try:
        license_plate = str(license_plate).upper()
        vehicle_type = int(vehicle_type)

        if vehicle_type == 1:
            pattern = r"^\d{2}[A-Z]{1,2}\d{4,5}$"
        else:
            pattern = r"^\d{2}[A-Z1-9]{2}\d{4,5}$"
        if not (license_plate and re.match(pattern, license_plate)):
            return {"error": "The license plate number is invalid"}

        if vehicle_type not in [1, 2, 3]:
            return {"error": "The type of vehicle is invalid"}

        cache_key = f"{license_plate}-{vehicle_type}"
        if bool(bypass_caching):
            await _cache_delete(cache_key)
            return await _check_license_plate(license_plate, vehicle_type)

        cached_value, ttl = await _cache_get(cache_key)
        if cached_value is not None:
            if ttl is not None and ttl < cache_min_age:
                task.create(_check_license_plate, license_plate, vehicle_type)
            return json.loads(cached_value)
        return await _check_license_plate(license_plate, vehicle_type)
    except Exception as error:
        return {"error": f"An unexpected error occurred during processing: {error}"}
