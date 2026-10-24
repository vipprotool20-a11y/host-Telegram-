"""
Configuration file for Hotmail Checker Bot
Fill in all the values below. Do not commit this file to version control.
"""

# =============================================================================
# === BOT CONFIGURATION =====================================================
# =============================================================================

BOT_CONFIG = {
    "BOT_TOKEN": "PUT_TOKEN_HERE",  # Get from @BotFather
    "OWNER_IDS": [123456789],  # Your Telegram user ID (get from @userinfobot)
    "OWNER_USERNAME": "@YourTG",  # Your Telegram username
    "OWNER_DISCORD": "",  # Your Discord server (leave empty if none)
    "BOT_NAME": "HotmailCheckerBot",
}

# =============================================================================
# === HOTMAIL CHECKER CONFIGURATION (from original file) ===================
# =============================================================================

# These values are used by the Hotmail checker from fucked_ORIGINAL_UNTOUCHED.py
# Fill them in if you have them, otherwise leave as empty strings

HOTMAIL_CONFIG = {
    "validate_url": "",  # Validation URL (if any)
    "tool_secret": "",  # Tool secret (if any)
    "api_secret": "",  # API secret (if any)
    "tg_url": "",  # Telegram webhook URL (if any)

    # --- Checker / proxy settings -------------------------------------------
    "proxy_file": "proxies.txt",  # Proxy list, one per line (ip:port, user:pass@ip:port, ip:port:user:pass, socks5://ip:port)
    "threads": 25,  # Default concurrent checks (overridable per user in the bot)
    "search_keywords": "",  # Optional: comma-separated keywords to match inside mail
}

# =============================================================================
# === PLACEHOLDER CHECK ======================================================
# =============================================================================

def has_placeholders():
    """Check if any configuration values are still placeholders."""
    placeholders = []

    # Check bot config
    if BOT_CONFIG["BOT_TOKEN"] == "PUT_TOKEN_HERE":
        placeholders.append("BOT_TOKEN")
    if BOT_CONFIG["OWNER_IDS"] == [123456789]:
        placeholders.append("OWNER_IDS")
    if BOT_CONFIG["OWNER_USERNAME"] == "@YourTG":
        placeholders.append("OWNER_USERNAME")
    # Discord is optional, so we don't check for it
    # if BOT_CONFIG["OWNER_DISCORD"] == "":
    #     placeholders.append("OWNER_DISCORD")

    return placeholders


def get_missing_config():
    """Return a formatted message about missing configuration."""
    missing = has_placeholders()
    if not missing:
        return None

    msg = "[!] Missing configuration values:\n\n"
    for item in missing:
        msg += f"  - {item}\n"
    msg += "\nPlease edit config.py and fill in all required values."
    return msg
