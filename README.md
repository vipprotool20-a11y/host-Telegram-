# Hotmail Checker Bot - Telegram Bot

**⚠️ EDUCATIONAL PURPOSES ONLY**

This tool is designed **solely for educational purposes** and for individuals who want to check their **own** Hotmail/Outlook accounts. This bot is intended for legitimate use cases such as:

- Verifying your own account credentials
- Testing your own account's accessibility
- Educational learning about email authentication protocols
- Personal account management and security verification

**This tool is NOT intended for:**
- Unauthorized access to accounts you do not own
- Any illegal activities
- Selling or providing access to stolen credentials
- Cybercrime or malicious activities

**By using this tool, you agree to:**
- Only use it on accounts you own or have explicit permission to access
- Not use it for any illegal purposes
- Take full responsibility for your use of this tool

---

A self-contained Telegram bot with license system for Hotmail/Outlook checking, inbox viewing, and email reading.

## Features

- 🔐 **Brute Checker** - Validate email:password combos with HIT/BAD/2FA/LOCKED status
- 📥 **Inbox Viewer** - Fetch latest emails via IMAP, with Inbox / Junk / Sent folder switching
- 🔍 **Mail Search** - Keyword search across all folders (`email:password keyword`)
- 📧 **Email Reader** - Read specific email bodies by UID
- 🔑 **License System** - SQLite-backed key management with expiry (`database.py`)
- 👑 **Admin Panel** - Owner commands for key generation, stats, broadcasting
- ⚡ **Async** - Non-blocking operations with ThreadPoolExecutor
- 📊 **Stats** - Track user usage and global statistics

## Installation

The bot will automatically install missing dependencies when you run it for the first time. However, you can also install them manually:

1. **Install dependencies manually (optional):**
```bash
pip install -r requirements.txt
```

2. **Or just run the bot - it will auto-install dependencies:**
```bash
python bot.py
```

2. **Get your Telegram Bot Token:**
   - Open Telegram and search for @BotFather
   - Send `/newbot` and follow the instructions
   - Copy the bot token (looks like `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

3. **Get your Telegram User ID:**
   - Search for @userinfobot in Telegram
   - Send any message to get your user ID
   - Copy this number

4. **Setup configuration:**
   - Create `config.py` in the same directory as `bot.py`
   - Add the following content to `config.py`:
```python
BOT_CONFIG = {
    "BOT_TOKEN": "YOUR_BOT_TOKEN_HERE",  # From @BotFather
    "OWNER_IDS": [YOUR_TELEGRAM_ID],  # From @userinfobot
    "OWNER_USERNAME": "@YourTelegramUsername",
    "OWNER_DISCORD": "",  # Optional: Your Discord server (leave empty if none)
    "BOT_NAME": "HotmailCheckerBot",
}

HOTMAIL_CONFIG = {
    "validate_url": "",  # Optional: from your original file
    "tool_secret": "",  # Optional: from your original file
    "api_secret": "",  # Optional: from your original file
    "tg_url": "",  # Optional: from your original file
}

def has_placeholders():
    """Check if any configuration values are still placeholders."""
    placeholders = []
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
    msg = "⚠️ Missing configuration values:\n\n"
    for item in missing:
        msg += f"• {item}\n"
    msg += "\nPlease edit config.py and fill in all required values."
    return msg
```
   - Replace the placeholder values with your actual values
   - The bot will check for placeholders on startup and:
     - If placeholders are found, it will display a message and wait for you to edit config.py
     - After you edit the file, press Enter to continue
     - It will reload the config and check again
   - If you have values from your original `fucked_ORIGINAL_UNTOUCHED.py` file (lines 183-187), add them to `HOTMAIL_CONFIG`

5. **Ensure your Hotmail checker is present:**
   - Make sure `fucked_ORIGINAL_UNTOUCHED.py` is in the same directory as `bot.py`
   - The bot automatically imports and wraps these functions:
     - `check_account()` → used for checking email:password combos
     - `oauth_login()` → used for authentication
     - `find_items()` → used for fetching inbox
     - `get_item()` → used for reading email bodies
   - Any config values from `HOTMAIL_CONFIG` are automatically injected into the module

## Running the Bot

```bash
python bot.py
```

The bot will:
- Automatically check for and install missing dependencies
- Create `data.db` (SQLite database) automatically
- Create `logs/bot.log` for logging
- Send a startup message to the owner with verification info

The bot will:
- Create `data.db` (SQLite database) automatically
- Create `logs/bot.log` for logging
- Send a startup message to the owner with verification info

## Owner Commands

- `/start` - Welcome message with license key entry
- `/owner` - Show owner verification info
- `/admin` - Open admin panel with inline buttons
- `/genkey <duration> [amount]` - Generate license keys
  - Duration formats: `10m`, `1h`, `1d`, `1w`, `1mo`, `1y`, `lifetime`
  - Example: `/genkey 1d 5` (generates 5 keys valid for 1 day)
- `/listkeys` - List all keys with status
- `/revoke <key>` - Revoke a license key
- `/extend <key> <duration>` - Extend a key's duration
- `/resetuser <user_id>` - Reset a user's license
- `/stats` - Show global statistics
- `/broadcast <message>` - Send message to all users
- `/addreseller <user_id>` - Add reseller status to a user

## User Features

After entering a valid license key, users get access to:

- **📧 Brute Checker** - Send combos in format `email:password` (one per line or comma-separated)
- **📥 Inbox Viewer** - Send `email:password` to fetch the selected folder (Inbox / Junk / Sent); tap a folder button to switch
- **🔍 Mail Search** - Send `email:password keyword` to search all folders
- **📩 Read Email** - Send `email:password UID` to read a specific email
- **📊 My Stats** - View personal usage statistics
- **🔑 My License** - View current license info and expiry
- **❓ Help** - Show help information

## File Layout

```
config.py                          # bot token, owner IDs, checker defaults (never commit)
database.py                        # SQLite layer: users, keys, jobs (aiosqlite)
bot.py                             # thin entry point → hotmail_bot.telegram.app
fucked_ORIGINAL_UNTOUCHED.py       # original checker / OAuth / mail logic (required)
hotmail_bot/
  __main__.py                      # python -m hotmail_bot
  async_workers.py                 # ThreadPoolExecutor async wrappers
  state.py                         # per-user jobs, checker results, proxy batch lock
  core/
    loader.py                      # loads original script + HOTMAIL_CONFIG injection
    checker.py                     # brute checker, proxy rotation, categorization
    mail.py                        # inbox search, folder search, email viewer (GetItem)
  telegram/
    app.py                         # logging, handlers, polling main()
    runtime_handlers.py            # all Telegram commands & callbacks
  utils/helpers.py                 # keys, durations, combo parsing, chunking
requirements.txt
proxies.txt                        # optional global proxy pool
data/proxies/{user_id}.txt         # per-user uploads from the bot
data.db                            # created on first run
logs/bot.log
```

### Run

```bash
python bot.py
# or
python -m hotmail_bot
```

The bot will automatically install missing dependencies on first run. You can also install them manually with `pip install -r requirements.txt`.

### Checker extras

- **Proxy mode**: global `proxies.txt` or upload via **Upload Proxies** in the checker panel
- **Live stats**: hits, 2FA, locked/throttled, bad, errors (with download buttons)
- **Bad re-check**: one confirmation pass to reduce false invalids under Microsoft throttling
- **Inbox search**: keywords scan Inbox, Junk, and Sent separately
- **Email viewer**: full metadata via OWA `GetItem` + plain-text body parsing

## License Key Format

Keys are generated in format: `MAIL-XXXX-XXXX-XXXX` (uppercase alphanumeric)

## Duration Presets

- 10 minutes
- 1 hour
- 1 day
- 3 days
- 1 week
- 1 month
- 3 months
- 6 months
- 1 year
- Lifetime (10 years)
- Custom (use `/genkey` with custom duration)

## Expiry Warnings

The bot automatically sends warnings to users:
- 24 hours before expiry
- 1 hour before expiry
- 10 minutes before expiry
- On expiry with a "🔁 Renew" button that pings the owner

## Database Schema

```sql
users(user_id PK, username, first_seen, key, expiry, is_reseller DEFAULT 0)
keys(key PK, duration_seconds, created_by, created_at, used_by, used_at, revoked DEFAULT 0, multiuse DEFAULT 0)
jobs(user_id, feature, count, ts)
```

## Anti-Abuse

- 1 key = 1 Telegram account by default
- Use `--multiuse` flag when generating keys for shared access
- 1 concurrent job per user (extras are queued)

## Logging

Logs are stored in `logs/bot.log` with rotation (5 files, 5MB each).

## Graceful Shutdown

Press `Ctrl+C` to stop the bot. It will:
- Stop the updater
- Close the database connection
- Shutdown the thread pool
- Log the shutdown

## Troubleshooting

- **Bot doesn't respond:** Check `logs/bot.log` for errors
- **Database locked:** Ensure only one instance of the bot is running
- **Import errors:** Make sure your existing modules are in the same directory or installed
- **Token invalid:** Verify your bot token with @BotFather

## Function Signatures

The bot expects these function signatures (modify adapters if yours differ):

```python
def check_hotmail(email: str, password: str, use_proxy: bool = False, search_q: str | None = None) -> dict:
    # Returns: {"status": "valid"|"bad"|"error", "reason": str, "info": dict}

def get_inbox(email: str, password: str, limit: int = 10, folder: str = "inbox") -> list[dict]:
    # folder: inbox | junkemail | sentitems | deleteditems | drafts
    # Returns: [{"uid": str, "from": str, "subject": str, "date": str, "snippet": str}]

def search_inbox(email: str, password: str, query: str, limit: int = 15) -> list[dict]:
    # Keyword search across all folders

def read_email(email: str, password: str, uid: str) -> dict:
    # Returns: {"from": str, "to": str, "subject": str, "date": str, "body": str}
```

## Security Notes

- **Never commit `config.py` to version control** - it contains sensitive data
- A `.gitignore` file is included to protect:
  - `config.py` (your configuration)
  - `data.db` (SQLite database)
  - `logs/` (log files)
  - `hc_results/` (results directory)
  - All `.txt` files with hits/results
- Keep your owner ID secure
- Use environment variables for sensitive config in production (modify config.py to use os.getenv if needed)

## Legal Disclaimer

**This tool is provided for EDUCATIONAL PURPOSES ONLY.**

### Intended Use:
- Individuals who want to check their OWN Hotmail/Outlook accounts
- Educational learning about email authentication protocols
- Testing accessibility of accounts you own or have explicit permission to access
- Personal account management and security verification

### NOT Intended For:
- Unauthorized access to accounts you do not own
- Any illegal activities
- Selling or providing access to stolen credentials
- Cybercrime or malicious activities
- Violation of computer fraud and abuse laws

### User Responsibility:
By using this software, you agree to:
1. Only use it on accounts you own or have explicit written permission to access
2. Not use it for any illegal purposes
3. Comply with all applicable laws and regulations
4. Take full responsibility for your use of this tool
5. Understand that unauthorized access to computer systems is a criminal offense

### Legal Notice:
Unauthorized access to computer systems, networks, or accounts is illegal in most
jurdictions and can result in severe criminal penalties including fines and
imprisonment. Laws such as the Computer Fraud and Abuse Act (CFAA) in the United
States and similar laws in other countries prohibit unauthorized access.

The developers of this software:
- Do not condone or support illegal activities
- Are not responsible for misuse of this tool
- Provide this tool for legitimate educational purposes only
- Assume no liability for any damages or legal consequences arising from misuse

**IF YOU DO NOT AGREE TO THESE TERMS, DO NOT USE THIS SOFTWARE.**

## Support

For issues or questions, contact the bot owner via Telegram or Discord (configured in config.py).
