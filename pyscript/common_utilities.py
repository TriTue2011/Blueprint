import asyncio
import json
import sqlite3
import threading
import time
from pathlib import Path
from typing import Any

TTL = 300  # The Conversation ID retention period in Home Assistant is set to a fixed 5 minutes of idle time and cannot be modified.
DB_PATH = Path("/config/cache.db")

_CACHE_READY = False
_CACHE_READY_LOCK = threading.Lock()
_INDEX_LOCKS: dict[str, asyncio.Lock] = {}
_INDEX_LOCKS_GUARD = threading.Lock()


def _get_index_lock(key: str) -> asyncio.Lock:
    with _INDEX_LOCKS_GUARD:
        lock = _INDEX_LOCKS.get(key)
        if lock is None:
            lock = asyncio.Lock()
            _INDEX_LOCKS[key] = lock
        return lock


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


def _cache_prepare_db_sync(force: bool = False) -> bool:
    """Ensure the cache database is ready for use."""
    _ensure_cache_db_once(force=force)
    return True


def _cache_get_sync(key: str) -> str | None:
    """Retrieve the cached value for a key, pruning expired rows first."""
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
                    SELECT value
                    FROM cache_entries
                    WHERE key = ?
                      AND expires_at > ?
                    """,
                    (key, now),
                )
                row = cur.fetchone()
            return row["value"] if row else None
        except sqlite3.OperationalError:
            _reset_cache_ready()
            if attempt == 0:
                continue
            raise
    return None


def _cache_set_sync(key: str, value: str, ttl_seconds: int) -> bool:
    """Persist a cache entry with the provided TTL and prune expired records."""
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


def _cache_delete_sync(key: str) -> int:
    """Remove the cache entry identified by key if it exists."""
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


async def _cache_prepare_db(force: bool = False) -> bool:
    """Ensure the cache database is ready for use."""
    return await asyncio.to_thread(_cache_prepare_db_sync, force)


async def _cache_get(key: str) -> str | None:
    """Retrieve the cached value for a key, pruning expired rows first."""
    return await asyncio.to_thread(_cache_get_sync, key)


async def _cache_set(key: str, value: str, ttl_seconds: int) -> bool:
    """Persist a cache entry with the provided TTL and prune expired records."""
    return await asyncio.to_thread(_cache_set_sync, key, value, ttl_seconds)


async def _cache_delete(key: str) -> int:
    """Remove the cache entry identified by key if it exists."""
    return await asyncio.to_thread(_cache_delete_sync, key)


@time_trigger("startup")
async def initialize_cache_db() -> None:
    """Run once at startup to create the cache database and schema before services execute."""
    await _cache_prepare_db(force=True)


@service(supports_response="only")
async def memory_cache_get(key: str) -> dict[str, Any]:
    """
    yaml
    name: Memory Cache Get
    description: Fetch a cached value for a given key.
    fields:
      key:
        name: Key
        description: Identifier for the cached entry.
        required: true
        selector:
          text:
    """
    if not key:
        return {
            "status": "error",
            "op": "get",
            "error": "Missing a required argument: key",
        }
    try:
        raw_value = await _cache_get(key)
        if raw_value:
            value = json.loads(raw_value)
            return {
                "status": "ok",
                "op": "get",
                "key": key,
                "value": value,
            }
        return {
            "status": "error",
            "op": "get",
            "key": key,
            "error": "not_found",
        }
    except Exception as error:
        return {
            "status": "error",
            "op": "get",
            "key": key,
            "error": f"An unexpected error occurred during processing: {error}",
        }


@service(supports_response="only")
async def memory_cache_forget(key: str) -> dict[str, Any]:
    """
    yaml
    name: Memory Cache Forget
    description: Remove a cached entry if it exists.
    fields:
      key:
        name: Key
        description: Identifier for the cached entry.
        required: true
        selector:
          text:
    """
    if not key:
        return {
            "status": "error",
            "op": "forget",
            "error": "Missing a required argument: key",
        }
    try:
        deleted = await _cache_delete(key)
        return {
            "status": "ok",
            "op": "forget",
            "key": key,
            "deleted": deleted,
        }
    except Exception as error:
        return {
            "status": "error",
            "op": "forget",
            "key": key,
            "error": f"An unexpected error occurred during processing: {error}",
        }


@service(supports_response="only")
async def memory_cache_set(
    key: str,
    value: Any,
    ttl_seconds: int | None = None,
) -> dict[str, Any]:
    """
    yaml
    name: Memory Cache Set
    description: Store a value in cache for a given key.
    fields:
      key:
        name: Key
        description: Identifier for the cached entry.
        required: true
        selector:
          text:
      value:
        name: Value
        description: JSON-serializable value to cache for the provided key (string, number, list, dict, etc.).
        required: true
        selector:
          text:
      ttl_seconds:
        name: TTL Seconds
        description: Optional override for the entry's time to live (defaults to TTL constant).
        selector:
          number:
            min: 1
            max: 2592000
            mode: box
    """
    ttl = ttl_seconds if ttl_seconds is not None and ttl_seconds > 0 else TTL
    stored_value = json.dumps(value, ensure_ascii=False)
    try:
        success = await _cache_set(key, stored_value, ttl)
        if not success:
            return {
                "status": "error",
                "op": "set",
                "key": key,
                "value": value,
                "error": "cache_set returned False",
            }
        return {
            "status": "ok",
            "op": "set",
            "key": key,
            "value": value,
            "ttl": ttl,
        }
    except Exception as error:
        return {
            "status": "error",
            "op": "set",
            "key": key,
            "error": f"An unexpected error occurred during processing: {error}",
        }


@service(supports_response="only")
async def memory_cache_index_update(
    index_key: str,
    add: Any | None = None,
    remove: Any | None = None,
    replace: Any | None = None,
    ttl_seconds: int | None = None,
) -> dict[str, Any]:
    """
    yaml
    name: Memory Cache Index Update
    description: Atomically update a list index in cache by adding and/or removing identifiers.
    fields:
      index_key:
        name: Index key
        description: Cache key that stores the index list.
        required: true
        selector:
          text:
      add:
        name: IDs to add
        description: Optional list of identifiers to append when absent.
        selector:
          object:
      remove:
        name: IDs to remove
        description: Optional list of identifiers to remove from the index.
        selector:
          object:
      replace:
        name: Replace index
        description: Optional list that replaces the entire index before add/remove adjustments.
        selector:
          object:
      ttl_seconds:
        name: TTL Seconds
        description: Optional override for the index time to live (defaults to 30 days).
        selector:
          number:
            min: 1
            max: 2592000
            mode: box
    """
    cleaned_key = (index_key or "").strip()
    if not cleaned_key:
        return {
            "status": "error",
            "op": "index_update",
            "error": "Missing a required argument: index_key",
        }

    def _normalize(_value: Any) -> list[str]:
        if _value is None:
            return []
        if isinstance(_value, (str, int, float, bool)):
            seq = [_value]
        elif isinstance(_value, list):
            seq = _value
        elif isinstance(_value, tuple) or isinstance(_value, set):
            seq = list(_value)
        else:
            return []
        result: list[str] = []
        for _item in seq:
            normalized = str(_item).strip()
            if normalized:
                result.append(normalized)
        return result

    replace_list = _normalize(replace) if replace is not None else None
    add_list = _normalize(add)
    remove_list = _normalize(remove)

    if replace_list is None and not add_list and not remove_list:
        return {
            "status": "error",
            "op": "index_update",
            "key": cleaned_key,
            "error": "Nothing to add or remove",
        }

    ttl = ttl_seconds if ttl_seconds is not None and ttl_seconds > 0 else 2592000

    lock = _get_index_lock(cleaned_key)
    async with lock:
        try:
            entries: list[str] = []
            seen: set[str] = set()
            changed = False

            if replace_list is not None:
                for value in replace_list:
                    if value not in seen:
                        entries.append(value)
                        seen.add(value)
                changed = True
            else:
                existing_raw = await _cache_get(cleaned_key)
                if existing_raw:
                    try:
                        parsed = json.loads(existing_raw)
                        if isinstance(parsed, list):
                            for item in parsed:
                                value = str(item).strip()
                                if value and value not in seen:
                                    entries.append(value)
                                    seen.add(value)
                    except json.JSONDecodeError:
                        entries = []

            for value in add_list:
                if value not in seen:
                    entries.append(value)
                    seen.add(value)
                    changed = True

            if remove_list:
                remove_set = set(remove_list)
                filtered = [entry for entry in entries if entry not in remove_set]
                if len(filtered) != len(entries):
                    entries = filtered
                    changed = True

            stored_value = json.dumps(entries, ensure_ascii=False)
            success = await _cache_set(cleaned_key, stored_value, ttl)

            if not success:
                return {
                    "status": "error",
                    "op": "index_update",
                    "key": cleaned_key,
                    "error": "cache_set returned False",
                }

            return {
                "status": "ok",
                "op": "index_update",
                "key": cleaned_key,
                "ids": entries,
                "ttl": ttl,
                "changed": changed,
            }
        except Exception as error:
            return {
                "status": "error",
                "op": "index_update",
                "key": cleaned_key,
                "error": f"An unexpected error occurred during processing: {error}",
            }
