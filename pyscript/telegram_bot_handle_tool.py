import asyncio
import mimetypes
import os
import secrets
from typing import Any

import aiofiles
import aiohttp
from homeassistant.helpers import network

DIRECTORY = "/media/telegram"
TOKEN = pyscript.config.get("telegram_bot_token")

_session: aiohttp.ClientSession | None = None

if not TOKEN:
    raise ValueError("Telegram bot token is missing")

ACTIONS_CHAT: tuple[str, ...] = (
    "typing",
    "upload_photo",
    "record_video",
    "upload_video",
    "record_voice",
    "upload_voice",
    "upload_document",
    "choose_sticker",
    "find_location",
    "record_video_note",
    "upload_video_note",
)

PARSE_MODES: tuple[str, ...] = (
    "HTML",
    "MarkdownV2",
    "Markdown",
)


def _to_media_path(path: str) -> str:
    """Normalize Home Assistant media source path to /media/ prefix.

    Converts leading "local/" to "/media/". Leaves other paths unchanged.

    Args:
        path: Input file path from UI or config.

    Returns:
        Normalized path beginning with "/media/" when applicable.
    """
    if path.startswith("local/"):
        return "/media/" + path.removeprefix("local/")
    return path


def _to_local_path(path: str) -> str:
    """Convert a /media/ path to Home Assistant local/ media source path.

    Converts leading "/media/" to "local/". Leaves other paths unchanged.

    Args:
        path: Absolute media path.

    Returns:
        Path with leading "local/" when applicable.
    """
    if path.startswith("/media/"):
        return "local/" + path.removeprefix("/media/")
    return path


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


async def _get_file(session: aiohttp.ClientSession, file_id: str) -> str | None:
    """Resolve Telegram file path from a file_id.

    Args:
        session: Shared aiohttp session.
        file_id: Telegram file identifier.

    Returns:
        File path on Telegram's file server, or None.
    """
    url = f"https://api.telegram.org/bot{TOKEN}/getFile"
    async with session.post(url, json={"file_id": file_id}) as resp:
        resp.raise_for_status()
        data = await resp.json()
    return data.get("result", {}).get("file_path")


async def _download_file(
    session: aiohttp.ClientSession, file_path: str
) -> bytes | None:
    """Download a file from Telegram's file server.

    Args:
        session: Shared aiohttp session.
        file_path: Path returned by Telegram `getFile`.

    Returns:
        Raw bytes of the file content, or None.
    """
    url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    async with session.get(url) as resp:
        resp.raise_for_status()
        return await resp.read()


async def _send_message(
    session: aiohttp.ClientSession,
    chat_id: int | str,
    message: str,
    reply_to_message_id: int | None = None,
    message_thread_id: int | None = None,
    parse_mode: str | None = None,
) -> dict[str, Any]:
    """Send a text message to a Telegram chat.

    Args:
        session: Shared aiohttp session.
        chat_id: Target chat identifier.
        message: Message text (truncated to 4096 chars).
        reply_to_message_id: Optional message ID to reply to.
        message_thread_id: Optional thread (topic) ID in supergroups.
        parse_mode: Optional parse mode for formatting (HTML, MarkdownV2, Markdown).

    Returns:
        Telegram API JSON response as a dict.
    """
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": message[:4096]}
    if reply_to_message_id:
        payload["reply_to_message_id"] = reply_to_message_id
    if message_thread_id:
        payload["message_thread_id"] = message_thread_id
    if parse_mode:
        if parse_mode not in PARSE_MODES:
            raise ValueError(
                f"Unsupported parse_mode: {parse_mode}. Allowed: {', '.join(PARSE_MODES)}"
            )
        payload["parse_mode"] = parse_mode
    async with session.post(url, json=payload) as resp:
        resp.raise_for_status()
        return await resp.json()


async def _send_photo(
    session: aiohttp.ClientSession,
    chat_id: int | str,
    file_path: str,
    caption: str | None = None,
    reply_to_message_id: int | None = None,
    message_thread_id: int | None = None,
    parse_mode: str | None = None,
) -> dict[str, Any]:
    """Upload and send a local photo via Telegram using multipart/form-data.

    Args:
        session: Shared aiohttp session.
        chat_id: Target chat identifier.
        file_path: Local filesystem path to the image.
        caption: Optional caption (Telegram limit ~1024 chars).
        reply_to_message_id: Optional message ID to reply to.
        message_thread_id: Optional thread (topic) ID in supergroups.
        parse_mode: Optional parse mode for caption (HTML, MarkdownV2, Markdown).

    Returns:
        Telegram API JSON response as a dict.
    """
    file_path = _to_media_path(file_path)

    file_exists = await asyncio.to_thread(os.path.isfile, file_path)
    if not file_exists:
        raise FileNotFoundError(f"File not found: {file_path}")

    async with aiofiles.open(file_path, "rb") as f:
        data = await f.read()

    filename = os.path.basename(file_path)
    mime_type, _ = mimetypes.guess_file_type(filename)
    content_type = mime_type or "application/octet-stream"

    form = aiohttp.FormData()
    form.add_field("chat_id", str(chat_id))
    if caption:
        form.add_field("caption", caption[:1024])
    if parse_mode:
        if parse_mode not in PARSE_MODES:
            raise ValueError(
                f"Unsupported parse_mode: {parse_mode}. Allowed: {', '.join(PARSE_MODES)}"
            )
        form.add_field("parse_mode", parse_mode)
    if reply_to_message_id:
        form.add_field("reply_to_message_id", str(reply_to_message_id))
    if message_thread_id:
        form.add_field("message_thread_id", str(message_thread_id))
    form.add_field(
        name="photo",
        value=data,
        filename=filename,
        content_type=content_type,
    )

    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    async with session.post(url, data=form) as resp:
        resp.raise_for_status()
        return await resp.json()


async def _get_webhook_info(session: aiohttp.ClientSession) -> dict[str, Any]:
    """Retrieve current Telegram bot webhook information.

    Args:
        session: Shared aiohttp session.

    Returns:
        Telegram API JSON response as a dict.
    """
    url = f"https://api.telegram.org/bot{TOKEN}/getWebhookInfo"
    async with session.get(url) as resp:
        resp.raise_for_status()
        return await resp.json()


async def _set_webhook(
    session: aiohttp.ClientSession, base_url: str, webhook_id: str
) -> dict[str, Any]:
    """Set the Telegram bot webhook URL.

    Args:
        session: Shared aiohttp session.
        base_url: Base external URL for Home Assistant.
        webhook_id: Unique webhook identifier path.

    Returns:
        Telegram API JSON response as a dict.
    """
    url = f"https://api.telegram.org/bot{TOKEN}/setWebhook"
    params = {
        "url": f"{base_url}/api/webhook/{webhook_id}",
        "drop_pending_updates": True,
    }
    async with session.post(url, json=params) as resp:
        resp.raise_for_status()
        return await resp.json()


async def _delete_webhook(session: aiohttp.ClientSession) -> dict[str, Any]:
    """Delete the Telegram bot webhook.

    Args:
        session: Shared aiohttp session.

    Returns:
        Telegram API JSON response as a dict.
    """
    url = f"https://api.telegram.org/bot{TOKEN}/deleteWebhook"
    params = {"drop_pending_updates": True}
    async with session.post(url, json=params) as resp:
        resp.raise_for_status()
        return await resp.json()


async def _get_updates(
    session: aiohttp.ClientSession, timeout: int = 30
) -> dict[str, Any]:
    """Fetch updates with long polling.

    Args:
        session: Shared aiohttp session.
        timeout: Long-poll timeout in seconds.

    Returns:
        Telegram API JSON response as a dict.
    """
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    params = {"timeout": timeout}
    async with session.post(url, json=params) as resp:
        resp.raise_for_status()
        return await resp.json()


async def _get_me(session: aiohttp.ClientSession) -> dict[str, Any]:
    """Get basic information about the bot.

    Args:
        session: Shared aiohttp session.

    Returns:
        Telegram API JSON response as a dict.
    """
    url = f"https://api.telegram.org/bot{TOKEN}/getMe"
    async with session.get(url) as resp:
        resp.raise_for_status()
        return await resp.json()


async def _send_chat_action(
    session: aiohttp.ClientSession,
    chat_id: int | str,
    message_thread_id: int | None = None,
    action: str = "typing",
) -> dict[str, Any]:
    """Send a chat action (e.g., typing) to a chat.

    Args:
        session: Shared aiohttp session.
        chat_id: Target chat identifier.
        message_thread_id: Optional topic/thread ID.
        action: One of: typing, upload_photo, record_video, upload_video, record_voice, upload_voice, upload_document, choose_sticker, find_location, record_video_note, upload_video_note.

    Returns:
        Telegram API JSON response as a dict.
    """
    if action not in ACTIONS_CHAT:
        raise ValueError(
            f"Unsupported chat action: {action}. Allowed: {', '.join(ACTIONS_CHAT)}"
        )
    url = f"https://api.telegram.org/bot{TOKEN}/sendChatAction"
    params = {
        "chat_id": chat_id,
        "action": action,
    }
    if message_thread_id:
        params["message_thread_id"] = message_thread_id
    async with session.post(url, json=params) as resp:
        resp.raise_for_status()
        return await resp.json()


def _internal_url() -> str | None:
    """Return the internal Home Assistant URL, if available.

    Returns:
        Internal URL string or None when unavailable.
    """
    try:
        return network.get_url(hass, allow_external=False)
    except network.NoURLAvailableError:
        return None


def _external_url() -> str | None:
    """Return the external HTTPS Home Assistant URL, if available.

    Returns:
        External URL string or None when unavailable.
    """
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


@service(supports_response="only")
async def send_telegram_message(
    chat_id: str,
    message: str,
    reply_to_message_id: int | None = None,
    message_thread_id: int | None = None,
    parse_mode: str | None = None,
) -> dict[str, Any]:
    """
    yaml
    name: Send Telegram Message
    description: Send a plain text message to a Telegram chat.
    fields:
      chat_id:
        name: Chat ID
        description: ID of the conversation (user or group).
        required: true
        selector:
          text:
      message:
        name: Message
        description: Message text.
        example: Hello from Home Assistant
        required: true
        selector:
          text:
      reply_to_message_id:
        name: Reply To Message ID
        description: Message ID to reply to.
        selector:
          number:
            min: 1
            step: 1
      message_thread_id:
        name: Message Thread ID
        description: Topic/thread ID (forum topics in supergroups).
        selector:
          number:
            min: 1
            step: 1
      parse_mode:
        name: Parse Mode
        description: Format entities in the message using the selected parse mode.
        selector:
          select:
            mode: dropdown
            options:
              - HTML
              - MarkdownV2
              - Markdown
    """
    if not all([chat_id, message]):
        return {"error": "Missing one or more required arguments: chat_id, message"}
    if parse_mode and parse_mode not in PARSE_MODES:
        return {
            "error": f"Unsupported parse_mode: {parse_mode}. Allowed: {', '.join(PARSE_MODES)}"
        }
    try:
        session = await _ensure_session()
        response = await _send_message(
            session,
            chat_id,
            message,
            reply_to_message_id=reply_to_message_id,
            message_thread_id=message_thread_id,
            parse_mode=parse_mode,
        )
        if not response:
            return {"error": "Failed to send message"}
        return response
    except Exception as error:
        return {"error": f"An unexpected error occurred during processing: {error}"}


@service(supports_response="only")
async def get_telegram_file(file_id: str) -> dict[str, Any]:
    """
    yaml
    name: Get Telegram File
    description: Download a file by Telegram file_id; saves under media and returns a local path and type.
    fields:
      file_id:
        name: File ID
        description: Telegram file_id of the media to download.
        required: true
        selector:
          text:
    """
    if not file_id:
        return {"error": "Missing a required argument: file_id"}
    try:
        session = await _ensure_session()
        await _ensure_dir(DIRECTORY)

        online_file_path = await _get_file(session, file_id)
        if not online_file_path:
            return {"error": "Unable to retrieve the file_path from Telegram."}

        content = await _download_file(session, online_file_path)
        if not content:
            return {"error": "Unable to download the file from Telegram."}

        file_name = os.path.basename(online_file_path)
        file_path = os.path.join(DIRECTORY, file_name)
        await _write_file(file_path, content)
        mimetypes.add_type("text/plain", ".yaml")
        mime_type, _ = mimetypes.guess_file_type(file_name)
        file_path = _to_local_path(file_path)
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
async def get_telegram_webhook() -> dict[str, Any]:
    """
    yaml
    name: Get Telegram Bot Webhook
    description: Retrieve current webhook configuration and status.
    """
    try:
        session = await _ensure_session()
        return await _get_webhook_info(session)
    except Exception as error:
        return {"error": f"An unexpected error occurred during processing: {error}"}


@service(supports_response="only")
async def set_telegram_webhook(webhook_id: str | None = None) -> dict[str, Any]:
    """
    yaml
    name: Set Telegram Bot Webhook
    description: Configure the HTTPS webhook endpoint for your Telegram bot.
    fields:
      webhook_id:
        name: Webhook ID
        description: Optional custom path suffix for /api/webhook; leave empty to auto-generate.
        selector:
          text:
    """
    try:
        if not webhook_id:
            webhook_id = secrets.token_urlsafe()
        external_url = _external_url()
        if not external_url:
            return {
                "error": "The external Home Assistant URL is not found or incorrect."
            }
        session = await _ensure_session()
        response = await _set_webhook(session, external_url, webhook_id)
        if isinstance(response, dict) and response.get("ok"):
            response["webhook_id"] = webhook_id
        return response
    except Exception as error:
        return {"error": f"An unexpected error occurred during processing: {error}"}


@service(supports_response="only")
async def delete_telegram_webhook() -> dict[str, Any]:
    """
    yaml
    name: Delete Telegram Bot Webhook
    description: Remove the webhook configuration and stop webhook delivery.
    """
    try:
        session = await _ensure_session()
        return await _delete_webhook(session)
    except Exception as error:
        return {"error": f"An unexpected error occurred during processing: {error}"}


@service(supports_response="only")
async def get_telegram_updates(timeout: int = 30) -> dict[str, Any]:
    """
    yaml
    name: Get Telegram Updates
    description: Tool for getting Telegram message updates.
    fields:
      timeout:
        name: Timeout
        description: Time to wait for a response from the Telegram.
        selector:
          number:
            min: 30
            max: 60
            step: 1
        default: 30
    """
    try:
        session = await _ensure_session()
        return await _get_updates(session, timeout=timeout)
    except Exception as error:
        return {"error": f"An unexpected error occurred during processing: {error}"}


@service(supports_response="only")
async def get_telegram_bot_info() -> dict[str, Any]:
    """
    yaml
    name: Get Telegram Bot Information
    description: Tool for getting Telegram bot basic information.
    """
    try:
        session = await _ensure_session()
        return await _get_me(session)
    except Exception as error:
        return {"error": f"An unexpected error occurred during processing: {error}"}


@service(supports_response="only")
async def send_telegram_chat_action(
    chat_id: str,
    message_thread_id: int | None = None,
    action: str = "typing",
) -> dict[str, Any]:
    """
    yaml
    name: Send Telegram Chat Action
    description: Send a chat action to a Telegram chat (e.g., typing, upload_photo).
    fields:
      chat_id:
        name: Chat ID
        description: The unique identifier of the target chat where the chat action will be sent.
        required: true
        selector:
          text:
      message_thread_id:
        name: Message Thread ID
        description: The unique identifier of the specific message thread (topic) where the chat action will be sent.
        selector:
          number:
            min: 1
            step: 1
      action:
        name: Action
        description: Chat action to broadcast.
        selector:
          select:
            mode: dropdown
            options:
              - typing
              - upload_photo
              - record_video
              - upload_video
              - record_voice
              - upload_voice
              - upload_document
              - choose_sticker
              - find_location
              - record_video_note
              - upload_video_note
        default: typing
    """
    if not chat_id:
        return {"error": "Missing a required argument: chat_id"}
    if action not in ACTIONS_CHAT:
        return {
            "error": f"Unsupported chat action: {action}. Allowed: {', '.join(ACTIONS_CHAT)}"
        }
    try:
        session = await _ensure_session()
        response = await _send_chat_action(
            session,
            chat_id,
            message_thread_id,
            action=action,
        )
        if not response:
            return {"error": "Failed to send message"}
        return response
    except Exception as error:
        return {"error": f"An unexpected error occurred during processing: {error}"}


@service(supports_response="only")
async def send_telegram_photo(
    chat_id: str,
    file_path: str,
    caption: str | None = None,
    reply_to_message_id: int | None = None,
    message_thread_id: int | None = None,
    parse_mode: str | None = None,
) -> dict[str, Any]:
    """
    yaml
    name: Send Telegram Photo
    description: Send a local image by uploading via multipart/form-data.
    fields:
      chat_id:
        name: Chat ID
        description: ID of the conversation (user or group).
        required: true
        selector:
          text:
      file_path:
        name: File Path
        description: Local image path under /media or local/.
        required: true
        selector:
          text:
      caption:
        name: Caption
        description: Optional text shown under the photo.
        selector:
          text:
      parse_mode:
        name: Parse Mode
        description: Format entities in the caption using the selected parse mode.
        selector:
          select:
            mode: dropdown
            options:
              - HTML
              - MarkdownV2
              - Markdown
      reply_to_message_id:
        name: Reply To Message ID
        description: The unique identifier of the original message you want to reply to.
        selector:
          number:
            min: 1
            step: 1
      message_thread_id:
        name: Message Thread ID
        description: The unique identifier of the specific message thread (topic) where the photo will be sent.
        selector:
          number:
            min: 1
            step: 1
    """
    if not all([chat_id, file_path]):
        return {"error": "Missing one or more required arguments: chat_id, file_path"}
    if parse_mode and parse_mode not in PARSE_MODES:
        return {
            "error": f"Unsupported parse_mode: {parse_mode}. Allowed: {', '.join(PARSE_MODES)}"
        }
    try:
        session = await _ensure_session()
        response = await _send_photo(
            session,
            chat_id,
            file_path,
            caption=caption,
            reply_to_message_id=reply_to_message_id,
            message_thread_id=message_thread_id,
            parse_mode=parse_mode,
        )
        if not response:
            return {"error": "Failed to send photo"}
        return response
    except Exception as error:
        return {"error": f"An unexpected error occurred during processing: {error}"}
