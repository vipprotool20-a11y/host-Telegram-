"""Inbox search and email viewer using OAuth + OWA from the original script."""

from __future__ import annotations

import re
from html.parser import HTMLParser
from typing import List, Optional

from hotmail_bot.core.loader import hotmail_module

_oauth_login = hotmail_module.oauth_login
_find_items = hotmail_module.find_items
_get_item = hotmail_module.get_item
_owa_request = hotmail_module.owa_request
_make_session = hotmail_module.make_session

FOLDER_IDS = ("inbox", "junkemail", "sentitems")


class _HTMLTextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._parts: List[str] = []

    def handle_data(self, data: str) -> None:
        if data.strip():
            self._parts.append(data.strip())

    def get_text(self) -> str:
        return "\n".join(self._parts)


def html_to_plain(html: str) -> str:
    if not html:
        return ""
    if "<" not in html:
        return html.strip()
    parser = _HTMLTextExtractor()
    try:
        parser.feed(html)
        text = parser.get_text()
    except Exception:
        text = re.sub(r"<[^>]+>", " ", html)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def _normalize_item_id(raw_id) -> tuple[str, str]:
    """Fix original search_messages bug when ItemId is a dict."""
    if isinstance(raw_id, dict):
        return str(raw_id.get("Id") or ""), str(raw_id.get("ChangeKey") or "")
    return str(raw_id or ""), ""


def _format_items(items: list, limit: int) -> list[dict]:
    result = []
    for item in items[:limit]:
        uid, _ck = _normalize_item_id(item.get("Id", item.get("ItemId", "")))
        if not uid and item.get("Id"):
            uid = str(item.get("Id", ""))
        result.append(
            {
                "uid": uid,
                "from": item.get("from", ""),
                "subject": item.get("subject", ""),
                "date": item.get("date", ""),
                "snippet": (item.get("preview") or "")[:200],
            }
        )
    return result


def get_inbox(
    email: str, password: str, limit: int = 10, folder: str = "inbox"
) -> list[dict]:
    token, cid, _error = _oauth_login(email, password)
    if not token:
        return []
    items, _total = _find_items(email, token, cid, folder=folder, limit=limit)
    return _format_items(items, limit)


def search_inbox(email: str, password: str, query: str, limit: int = 15) -> list[dict]:
    token, cid, _error = _oauth_login(email, password)
    if not token:
        return []
    items, _total = _find_items(email, token, cid, query=query, limit=limit)
    return _format_items(items, limit)


def search_inbox_folders(
    email: str,
    password: str,
    query: str,
    folders: tuple[str, ...] = FOLDER_IDS,
    limit_per_folder: int = 10,
) -> list[dict]:
    """Search within Inbox, Junk, and Sent separately (folder-scoped find)."""
    token, cid, _error = _oauth_login(email, password)
    if not token:
        return []

    combined: list[dict] = []
    q = query.lower()
    for folder in folders:
        items, _total = _find_items(
            email, token, cid, folder=folder, limit=limit_per_folder * 3
        )
        for item in items:
            hay = " ".join(
                [
                    item.get("subject") or "",
                    item.get("preview") or "",
                    item.get("from") or "",
                ]
            ).lower()
            if q in hay:
                row = _format_items([item], 1)[0]
                row["folder"] = folder
                combined.append(row)
            if len(combined) >= limit_per_folder * len(folders):
                break
    return combined[: limit_per_folder * len(folders)]


def _get_item_metadata(email: str, msg_id: str, token: str, cid: str) -> dict:
    payload = {
        "__type": "GetItemJsonRequest:#Exchange",
        "Header": _make_session(),
        "Body": {
            "__type": "GetItemRequest:#Exchange",
            "ItemShape": {
                "__type": "ItemResponseShape:#Exchange",
                "BaseShape": "Default",
                "AdditionalProperties": [
                    {"__type": "PropertyUri:#Exchange", "FieldURI": "Subject"},
                    {"__type": "PropertyUri:#Exchange", "FieldURI": "DateTimeReceived"},
                    {"__type": "PropertyUri:#Exchange", "FieldURI": "From"},
                    {"__type": "PropertyUri:#Exchange", "FieldURI": "ToRecipients"},
                ],
            },
            "ItemIds": [{"__type": "ItemId:#Exchange", "Id": msg_id}],
        },
    }
    meta = {"from": "", "to": "", "subject": "", "date": ""}
    try:
        resp = _owa_request(email, token, cid, "GetItem", payload, None, 20)
        if resp.status_code != 200:
            return meta
        data = resp.json()
        items = (
            data.get("Body", {})
            .get("ResponseMessages", {})
            .get("Items", [{}])[0]
            .get("Items", [])
        )
        if not items:
            return meta
        msg = items[0]
        from_mb = (msg.get("From") or {}).get("Mailbox", {}) or {}
        name = from_mb.get("Name", "")
        addr = from_mb.get("EmailAddress", "")
        meta["from"] = f"{name} <{addr}>" if addr else name
        meta["subject"] = msg.get("Subject", "(No Subject)")
        meta["date"] = msg.get("DateTimeReceived", "")
        recipients = msg.get("ToRecipients") or []
        to_parts = []
        for rcpt in recipients:
            mb = rcpt.get("Mailbox", rcpt) if isinstance(rcpt, dict) else {}
            if isinstance(mb, dict):
                rname = mb.get("Name", "")
                raddr = mb.get("EmailAddress", "")
                to_parts.append(f"{rname} <{raddr}>" if raddr else rname)
        meta["to"] = ", ".join(to_parts) if to_parts else email
    except Exception:
        pass
    return meta


def read_email(email: str, password: str, uid: str) -> dict:
    empty = {
        "from": "",
        "to": "",
        "subject": "",
        "date": "",
        "body": "",
        "body_plain": "",
        "error": "",
    }
    try:
        token, cid, error = _oauth_login(email, password)
        if not token:
            empty["body"] = error or "Failed to authenticate"
            empty["error"] = empty["body"]
            return empty

        meta = _get_item_metadata(email, uid, token, cid)
        body_html = _get_item(email, uid, token, cid) or ""
        body_plain = html_to_plain(body_html)

        return {
            "from": meta["from"],
            "to": meta["to"] or email,
            "subject": meta["subject"],
            "date": meta["date"],
            "body": body_plain or body_html,
            "body_plain": body_plain,
            "body_html": body_html,
            "error": "",
        }
    except Exception as e:
        empty["body"] = f"Error: {e}"
        empty["error"] = str(e)
        return empty
