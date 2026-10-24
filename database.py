"""
Database layer for HotmailGodBot
================================

SQLite (via aiosqlite) persistence for licenses, users, and job stats.

Tables
------
users(user_id PK, username, first_seen, key, expiry, is_reseller)
keys(key PK, duration_seconds, created_by, created_at, used_by, used_at, revoked, multiuse)
jobs(user_id, feature, count, ts)

Every function here is `async` and opens its own short-lived connection, so the
layer is safe to call from concurrent asyncio tasks.
"""

import logging
from datetime import datetime
from typing import Optional, Dict, List

import aiosqlite

logger = logging.getLogger(__name__)

DB_PATH = "data.db"


async def init_db():
    """Initialize SQLite database with required tables."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                first_seen TEXT,
                key TEXT,
                expiry TEXT,
                is_reseller INTEGER DEFAULT 0
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS keys (
                key TEXT PRIMARY KEY,
                duration_seconds INTEGER,
                created_by INTEGER,
                created_at TEXT,
                used_by INTEGER,
                used_at TEXT,
                revoked INTEGER DEFAULT 0,
                multiuse INTEGER DEFAULT 0
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                user_id INTEGER,
                feature TEXT,
                count INTEGER,
                ts TEXT
            )
        """)
        await db.commit()
    logger.info("Database initialized")


async def get_user(user_id: int) -> Optional[Dict]:
    """Get user record from database."""
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "SELECT * FROM users WHERE user_id = ?", (user_id,)
        ) as cursor:
            row = await cursor.fetchone()
            return dict(row) if row else None


async def save_user(user_id: int, username: str, key: str, expiry: str, is_reseller: int = 0):
    """Save or update user record."""
    async with aiosqlite.connect(DB_PATH) as db:
        user = await get_user(user_id)
        if user:
            await db.execute(
                "UPDATE users SET username=?, key=?, expiry=?, is_reseller=? WHERE user_id=?",
                (username, key, expiry, is_reseller, user_id),
            )
        else:
            now = datetime.now().isoformat()
            await db.execute(
                "INSERT INTO users (user_id, username, first_seen, key, expiry, is_reseller) VALUES (?, ?, ?, ?, ?, ?)",
                (user_id, username, now, key, expiry, is_reseller),
            )
        await db.commit()


async def save_key(
    key: str,
    duration_seconds: int,
    created_by: int,
    multiuse: bool = False,
):
    """Save a new license key."""
    async with aiosqlite.connect(DB_PATH) as db:
        now = datetime.now().isoformat()
        await db.execute(
            "INSERT INTO keys (key, duration_seconds, created_by, created_at, multiuse) VALUES (?, ?, ?, ?, ?)",
            (key, duration_seconds, created_by, now, 1 if multiuse else 0),
        )
        await db.commit()


async def get_key(key_str: str) -> Optional[Dict]:
    """Get key record from database."""
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "SELECT * FROM keys WHERE key = ?", (key_str,)
        ) as cursor:
            row = await cursor.fetchone()
            return dict(row) if row else None


async def mark_key_used(key_str: str, user_id: int):
    """Mark a key as used by a user."""
    async with aiosqlite.connect(DB_PATH) as db:
        now = datetime.now().isoformat()
        await db.execute(
            "UPDATE keys SET used_by=?, used_at=? WHERE key=?",
            (user_id, now, key_str),
        )
        await db.commit()


async def revoke_key(key_str: str):
    """Revoke a license key."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE keys SET revoked=1 WHERE key=?", (key_str,))
        await db.commit()


async def extend_key(key_str: str, additional_seconds: int):
    """Extend a key's duration."""
    async with aiosqlite.connect(DB_PATH) as db:
        key = await get_key(key_str)
        if key:
            new_duration = key["duration_seconds"] + additional_seconds
            await db.execute(
                "UPDATE keys SET duration_seconds=? WHERE key=?",
                (new_duration, key_str),
            )
            await db.commit()


async def reset_user(user_id: int):
    """Reset a user's license."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE users SET key=?, expiry=? WHERE user_id=?", (None, None, user_id))
        await db.commit()


async def list_keys() -> List[Dict]:
    """List all keys."""
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("SELECT * FROM keys ORDER BY created_at DESC") as cursor:
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]


async def add_reseller(user_id: int):
    """Add reseller status to a user."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE users SET is_reseller=1 WHERE user_id=?", (user_id,))
        await db.commit()


async def log_job(user_id: int, feature: str, count: int):
    """Log a job execution for stats."""
    async with aiosqlite.connect(DB_PATH) as db:
        now = datetime.now().isoformat()
        await db.execute(
            "INSERT INTO jobs (user_id, feature, count, ts) VALUES (?, ?, ?, ?)",
            (user_id, feature, count, now),
        )
        await db.commit()


async def get_user_stats(user_id: int) -> Dict:
    """Get user's job statistics."""
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(
            "SELECT feature, SUM(count) as total, COUNT(*) as runs FROM jobs WHERE user_id=? GROUP BY feature",
            (user_id,),
        ) as cursor:
            rows = await cursor.fetchall()
            return {row[0]: {"total": row[1], "runs": row[2]} for row in rows}


async def get_global_stats() -> Dict:
    """Get global statistics."""
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT COUNT(*) FROM users") as cursor:
            total_users = (await cursor.fetchone())[0]
        async with db.execute("SELECT COUNT(*) FROM keys WHERE revoked=0") as cursor:
            active_keys = (await cursor.fetchone())[0]
        async with db.execute("SELECT COUNT(*) FROM keys WHERE used_by IS NOT NULL") as cursor:
            used_keys = (await cursor.fetchone())[0]
        async with db.execute("SELECT SUM(count) FROM jobs") as cursor:
            total_checks = (await cursor.fetchone())[0] or 0

        return {
            "total_users": total_users,
            "active_keys": active_keys,
            "used_keys": used_keys,
            "total_checks": total_checks,
        }
