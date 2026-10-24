"""Load fucked_ORIGINAL_UNTOUCHED.py and inject HOTMAIL_CONFIG overrides."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Any

_ORIGINAL_FILENAME = "fucked_ORIGINAL_UNTOUCHED.py"


def _load_hotmail_module() -> Any:
    root = Path(__file__).resolve().parents[2]
    original_path = root / _ORIGINAL_FILENAME
    if not original_path.is_file():
        raise FileNotFoundError(
            f"Missing {_ORIGINAL_FILENAME} in {root}. Place the original checker script there."
        )

    spec = importlib.util.spec_from_file_location("hotmail_checker", str(original_path))
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load {_ORIGINAL_FILENAME}")

    module = importlib.util.module_from_spec(spec)
    sys.modules["hotmail_checker"] = module
    spec.loader.exec_module(module)
    return module


hotmail_module = _load_hotmail_module()


def inject_hotmail_config(hotmail_config: dict) -> None:
    """Apply non-empty HOTMAIL_CONFIG values onto the loaded checker module."""
    for key in ("validate_url", "tool_secret", "api_secret", "tg_url"):
        value = hotmail_config.get(key)
        if value:
            setattr(hotmail_module, key, value)
