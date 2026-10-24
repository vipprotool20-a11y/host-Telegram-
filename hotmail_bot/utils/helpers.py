"""Shared text, time, and parsing helpers."""

from __future__ import annotations

import random
import string
from datetime import datetime, timedelta
from typing import List, Optional


def generate_key() -> str:
    segment1 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    segment2 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    segment3 = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"MAIL-{segment1}-{segment2}-{segment3}"


def parse_duration(duration_str: str) -> int:
    duration_str = duration_str.lower().strip()
    if duration_str.endswith("m"):
        return int(duration_str[:-1]) * 60
    if duration_str.endswith("h"):
        return int(duration_str[:-1]) * 3600
    if duration_str.endswith("d"):
        return int(duration_str[:-1]) * 86400
    if duration_str.endswith("w"):
        return int(duration_str[:-1]) * 604800
    if duration_str.endswith("mo"):
        return int(duration_str[:-2]) * 2592000
    if duration_str.endswith("y"):
        return int(duration_str[:-1]) * 31536000
    if duration_str == "lifetime":
        return 10 * 365 * 86400
    return int(duration_str) * 60


def format_expiry(expiry_str: str) -> str:
    if not expiry_str:
        return "N/A"
    try:
        expiry = datetime.fromisoformat(expiry_str)
        now = datetime.now()
        if expiry <= now:
            return "Expired"
        delta = expiry - now
        days = delta.days
        hours = delta.seconds // 3600
        minutes = (delta.seconds % 3600) // 60
        if days > 0:
            return f"{days}d {hours}h"
        if hours > 0:
            return f"{hours}h {minutes}m"
        return f"{minutes}m"
    except Exception:
        return "Invalid"


def esc(text: str) -> str:
    if not text:
        return ""
    special_chars = r"_*[]()~`>#+-=|{}.!-"
    return "".join(f"\\{c}" if c in special_chars else c for c in str(text))


def chunk_message(text: str, max_length: int = 4096) -> List[str]:
    if len(text) <= max_length:
        return [text]
    chunks: List[str] = []
    current = ""
    for line in text.split("\n"):
        if len(current) + len(line) + 1 > max_length:
            chunks.append(current)
            current = line
        else:
            current += "\n" + line if current else line
    if current:
        chunks.append(current)
    return chunks


def parse_combos(text: str) -> List[str]:
    combos: List[str] = []
    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        if "," in line:
            for combo in line.split(","):
                combo = combo.strip()
                if ":" in combo:
                    combos.append(combo)
        elif ":" in line:
            combos.append(line)
    return combos
