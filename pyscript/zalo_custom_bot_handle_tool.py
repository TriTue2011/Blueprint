import asyncio
import mimetypes
import os
import secrets
from pathlib import Path
from typing import Any

import aiofiles
import aiohttp
from homeassistant.helpers import network

DIRECTORY = "/media/zalo"

_session: aiohttp.ClientSession | None = None


def _internal_url() -> str | None:
    """Return the internal Home Assistant URL, or None when it cannot be resolved."""
    try:
        return network.get_url(hass, allow_external=False)
    except network.NoURLAvailableError:
        return None


def _external_url() -> str | None:
    """Return the external HTTPS Home Assistant URL when configured and reachable."""
    try:
        return network.get_url(
            hass,
            allow_internal=False,
            allow_ip=False,
            require_ssl=True,
            require_standard_port=True,
        )
    except network.NoURLAvailableError:
        return None


async def _ensure_session() -> aiohttp.ClientSession:
    """Create or reuse a shared aiohttp session.

    Returns:
        An open `aiohttp.ClientSession` with a default timeout.
    """
    global _session
    if _session is None or _session.closed:
        _session = aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=60))
    return _session


async def _ensure_dir(path: str) -> None:
    """Ensure a directory exists, creating it if missing.

    Args:
        path: Directory path to create if it does not exist.
    """
    await asyncio.to_thread(os.makedirs, path, exist_ok=True)


async def _write_file(path: str, content: bytes) -> None:
    """Write bytes to a file asynchronously.

    Args:
        path: Destination file path.
        content: Raw bytes to write.
    """
    async with aiofiles.open(path, "wb") as f:
        await f.write(content)


async def _download_file(session: aiohttp.ClientSession, url: str) -> str | None:
    """Download a file from a given URL and save it under DIRECTORY.

    Args:
        session: Shared aiohttp session.
        url: Direct URL to the file to download.

    Returns:
        Full file path of the saved file, or None on failure.
    """
    async with session.get(url) as resp:
        resp.raise_for_status()
        content = await resp.read()
        content_type = resp.headers.get("Content-Type", "")
        ext = mimetypes.guess_extension(content_type.split(";")[0].strip()) or ""
        file_name = Path(url).name
        if not Path(file_name).suffix and ext:
            file_name += ext
        file_path = os.path.join(DIRECTORY, file_name)
        await _write_file(file_path, content)
        return file_path


@service(supports_response="only")
async def get_zalo_file_custom_bot(url: str) -> dict[str, Any]:
    """
    yaml
    name: Get Zalo File
    description: Download a file by direct URL and save it under Home Assistant media; returns a local path and file type.
    fields:
      url:
        name: URL
        description: Direct file URL (e.g., from a Zalo attachment).
        required: true
        selector:
          text:
    """
    if not url:
        return {"error": "Missing a required argument: url"}
    try:
        session = await _ensure_session()
        await _ensure_dir(DIRECTORY)

        file_path = await _download_file(session, url)
        if not file_path:
            return {"error": "Unable to download the file from Zalo."}

        mimetypes.add_type("text/plain", ".yaml")
        mime_type, encoding = mimetypes.guess_file_type(file_path)
        file_path = file_path.replace(
            "/media/", "local/"
        )  # Modify the media source to use a relative URI
        response: dict[str, Any] = {"file_path": file_path, "mime_type": mime_type}
        support_file_types = (
            "image/",
            "video/",
            "audio/",
            "text/",
            "application/pdf",
        )
        if mime_type and mime_type.startswith(support_file_types):
            response["supported"] = True
        else:
            response["supported"] = False
        return response
    except Exception as error:
        return {"error": f"An unexpected error occurred during processing: {error}"}


@service(supports_response="only")
def generate_webhook_id() -> dict[str, Any]:
    """
    yaml
    name: Generate Webhook ID
    description: Generate a unique URL-safe webhook ID and sample URLs.
    """
    webhook_id = secrets.token_urlsafe()
    internal_url = _internal_url()
    external_url = _external_url()
    response = {"webhook_id": webhook_id}
    if internal_url:
        response["sample_internal_url"] = f"{internal_url}/api/webhook/{webhook_id}"
    else:
        response["sample_internal_url"] = (
            "The internal Home Assistant URL is not found."
        )
    if external_url:
        response["sample_external_url"] = f"{external_url}/api/webhook/{webhook_id}"
    else:
        response["sample_external_url"] = (
            "The external Home Assistant URL is not found or incorrect."
        )
    return response
