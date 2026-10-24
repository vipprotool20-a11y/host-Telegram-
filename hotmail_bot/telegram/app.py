"""Bot startup: logging, config, handler registration, polling."""

from __future__ import annotations

import asyncio
import importlib
import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

from telegram.ext import Application, JobQueue

from config import BOT_CONFIG, HOTMAIL_CONFIG, get_missing_config
from database import init_db
from hotmail_bot.async_workers import shutdown_executor
from hotmail_bot.core.checker import load_proxy_file
from hotmail_bot.core.loader import inject_hotmail_config
from hotmail_bot.telegram import runtime_handlers as rh

CONFIG = BOT_CONFIG
PROXY_FILE = HOTMAIL_CONFIG.get("proxy_file") or "proxies.txt"

log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        RotatingFileHandler(log_dir / "bot.log", maxBytes=5 * 1024 * 1024, backupCount=5),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

inject_hotmail_config(HOTMAIL_CONFIG)


def _wire_runtime_config() -> None:
    """Expose config/constants to the handler module."""
    rh.CONFIG = CONFIG
    rh.HOTMAIL_CONFIG = HOTMAIL_CONFIG
    rh.PROXY_FILE = PROXY_FILE
    rh.SEARCH_KEYWORDS = HOTMAIL_CONFIG.get("search_keywords") or ""
    rh.logger = logger


def register_handlers(application: Application) -> None:
    from telegram.ext import (
        CallbackQueryHandler,
        CommandHandler,
        MessageHandler,
        filters,
    )

    application.add_handler(CommandHandler("start", rh.start))
    application.add_handler(CommandHandler("owner", rh.owner_command))
    application.add_handler(CommandHandler("admin", rh.admin_panel))
    application.add_handler(CommandHandler("genkey", rh.genkey_command))
    application.add_handler(CommandHandler("listkeys", rh.listkeys_command))
    application.add_handler(CommandHandler("revoke", rh.revoke_command))
    application.add_handler(CommandHandler("extend", rh.extend_command))
    application.add_handler(CommandHandler("resetuser", rh.resetuser_command))
    application.add_handler(CommandHandler("stats", rh.stats_command))
    application.add_handler(CommandHandler("broadcast", rh.broadcast_command))
    application.add_handler(CommandHandler("addreseller", rh.addreseller_command))

    application.add_handler(CallbackQueryHandler(rh.handle_enter_key, pattern="^enter_key$"))
    application.add_handler(CallbackQueryHandler(rh.handle_admin_callback, pattern="^admin_"))
    application.add_handler(CallbackQueryHandler(rh.handle_admin_callback, pattern="^genkey_"))
    application.add_handler(CallbackQueryHandler(rh.handle_checker_settings, pattern="^ck_"))
    application.add_handler(CallbackQueryHandler(rh.handle_menu_callback, pattern="^menu_"))
    application.add_handler(CallbackQueryHandler(rh.handle_admin_callback, pattern="^admin_panel"))

    application.add_handler(MessageHandler(filters.Document.ALL, rh.handle_document))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, rh.handle_message))


async def main() -> None:
    _wire_runtime_config()

    missing = get_missing_config()
    if missing:
        print(missing.encode('utf-8', errors='replace').decode('utf-8'))
        print("\nPlease edit config.py and fill in all required values before running the bot.")
        input("\nPress Enter after you've filled in the config...")
        import config

        importlib.reload(config)
        global CONFIG
        CONFIG = config.BOT_CONFIG
        _wire_runtime_config()
        missing = config.get_missing_config()
        if missing:
            print("[-] Configuration still has placeholders. Please fill them in.")
            return

    await init_db()

    loaded = load_proxy_file(PROXY_FILE)
    if loaded:
        logger.info("Loaded %s proxies from %s (proxy mode available)", loaded, PROXY_FILE)
    else:
        logger.warning("No proxies in %s — upload proxies in bot or add file on disk", PROXY_FILE)

    application = Application.builder().token(CONFIG["BOT_TOKEN"]).build()

    try:
        job_queue: JobQueue = application.job_queue
        if job_queue is not None:
            job_queue.run_repeating(rh.check_expiry_job, interval=60, first=10)
            logger.info("JobQueue enabled - automatic expiry checks running")
        else:
            logger.warning('Install job queue: pip install "python-telegram-bot[job-queue]"')
    except Exception as exc:
        logger.warning("JobQueue setup failed: %s", exc)

    register_handlers(application)

    await application.initialize()
    await rh.notify_owner(application)

    logger.info("Bot started")
    await application.start()
    await application.updater.start_polling()

    try:
        await asyncio.Event().wait()
    except KeyboardInterrupt:
        logger.info("Shutting down...")
    finally:
        await application.updater.stop()
        await application.stop()
        await application.shutdown()
        shutdown_executor()
        logger.info("Bot stopped")


def run() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    run()
