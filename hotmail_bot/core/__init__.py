from hotmail_bot.core.loader import hotmail_module
from hotmail_bot.core.checker import (
    check_hotmail,
    load_proxy_file,
    proxy_count,
    get_checker_settings,
    set_user_proxy_file,
    user_proxy_count,
    activate_proxies_for_user,
    categorize_check_result,
)
from hotmail_bot.core.mail import get_inbox, search_inbox, read_email, search_inbox_folders

__all__ = [
    "hotmail_module",
    "check_hotmail",
    "load_proxy_file",
    "proxy_count",
    "get_checker_settings",
    "set_user_proxy_file",
    "user_proxy_count",
    "activate_proxies_for_user",
    "categorize_check_result",
    "get_inbox",
    "search_inbox",
    "read_email",
    "search_inbox_folders",
]
