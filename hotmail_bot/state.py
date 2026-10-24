"""In-memory session state for Telegram users."""

from __future__ import annotations

import asyncio
from typing import Any, Dict, Optional

user_jobs: Dict[int, Dict[str, Any]] = {}
checker_results: Dict[int, Dict[str, Any]] = {}
inbox_folder: Dict[int, str] = {}

# Serialize proxy-mode checker batches (shared global proxy pool in original module)
proxy_batch_lock = asyncio.Lock()


async def enqueue_job(user_id: int, feature: str, *_ignored) -> bool:
    if user_id not in user_jobs:
        user_jobs[user_id] = {"feature": feature, "progress_msg": None, "queue": []}
        return True
    user_jobs[user_id]["queue"].append(feature)
    return False


async def get_queued_job(user_id: int) -> Optional[str]:
    if user_id in user_jobs and user_jobs[user_id]["queue"]:
        return user_jobs[user_id]["queue"].pop(0)
    return None


async def clear_job(user_id: int) -> None:
    user_jobs.pop(user_id, None)
