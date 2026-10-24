"""Thread-pool wrappers for blocking Hotmail I/O."""

from __future__ import annotations

import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import Optional

from hotmail_bot.core.checker import check_hotmail
from hotmail_bot.core.mail import get_inbox, read_email, search_inbox, search_inbox_folders

executor = ThreadPoolExecutor(max_workers=10)


async def async_check_hotmail(
    email: str,
    password: str,
    pool: Optional[ThreadPoolExecutor] = None,
    use_proxy: bool = False,
    search_q: Optional[str] = None,
) -> dict:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(
        pool or executor,
        check_hotmail,
        email,
        password,
        use_proxy,
        search_q,
    )


async def async_get_inbox(
    email: str, password: str, limit: int = 10, folder: str = "inbox"
) -> list:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(executor, get_inbox, email, password, limit, folder)


async def async_search_inbox(email: str, password: str, query: str, limit: int = 15) -> list:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(executor, search_inbox, email, password, query, limit)


async def async_search_folders(email: str, password: str, query: str, limit: int = 15) -> list:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(
        executor, search_inbox_folders, email, password, query, limit
    )


async def async_read_email(email: str, password: str, uid: str) -> dict:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(executor, read_email, email, password, uid)


def shutdown_executor() -> None:
    executor.shutdown(wait=True)
