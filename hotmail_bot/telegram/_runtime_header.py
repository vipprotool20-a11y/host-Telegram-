"""Telegram command and callback handlers."""

from __future__ import annotations

import asyncio
import logging
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional

import aiosqlite
from telegram import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    Update,
)
from telegram.constants import ParseMode
from telegram.error import BadRequest, TelegramError
from telegram.ext import Application, ContextTypes

from database import (
    DB_PATH,
    add_reseller,
    extend_key,
    get_global_stats,
    get_key,
    get_user,
    get_user_stats,
    list_keys,
    log_job,
    mark_key_used,
    reset_user,
    revoke_key,
    save_key,
    save_user,
)
from hotmail_bot.async_workers import (
    async_check_hotmail,
    async_get_inbox,
    async_read_email,
    async_search_folders,
    async_search_inbox,
)
from hotmail_bot.core.checker import (
    activate_proxies_for_user,
    get_checker_settings as _get_checker_settings,
    is_awaiting_proxy_upload,
    mark_awaiting_proxy_upload,
    proxy_count,
    set_user_proxy_file,
    user_proxy_count,
)
from hotmail_bot.state import (
    checker_results,
    clear_job,
    enqueue_job,
    get_queued_job,
    inbox_folder,
    proxy_batch_lock,
    user_jobs,
)
from hotmail_bot.utils.helpers import (
    chunk_message,
    esc,
    format_expiry,
    generate_key,
    parse_combos,
    parse_duration,
)

logger = logging.getLogger(__name__)

CONFIG: dict = {}
HOTMAIL_CONFIG: dict = {}
PROXY_FILE = "proxies.txt"
SEARCH_KEYWORDS = ""


def get_checker_settings(user_id: int) -> Dict:
    return _get_checker_settings(user_id, HOTMAIL_CONFIG)


def is_owner(user_id: int) -> bool:
    return user_id in CONFIG["OWNER_IDS"]


async def check_license(user_id: int) -> tuple[bool, Optional[Dict]]:
    user = await get_user(user_id)
    if not user or not user["key"] or not user["expiry"]:
        return (False, user)
    try:
        expiry = datetime.fromisoformat(user["expiry"])
        if datetime.now() > expiry:
            return (False, user)
    except Exception:
        return (False, user)
    return (True, user)


INBOX_FOLDERS = {
    "inbox": "📥 Inbox",
    "junkemail": "🚫 Junk",
    "sentitems": "📤 Sent",
}


def get_inbox_folder(user_id: int) -> str:
    return inbox_folder.get(user_id, "inbox")


def set_inbox_folder(user_id: int, folder: str) -> None:
    if folder in INBOX_FOLDERS:
        inbox_folder[user_id] = folder
