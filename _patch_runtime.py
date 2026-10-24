from pathlib import Path

p = Path(r"C:\Users\rizzw\Downloads\hm\hotmail_bot\telegram\runtime_handlers.py")
body = p.read_text(encoding="utf-8")
marker = "# =============================================================================\n# === MAIN ==================================================================="
if marker in body:
    body = body.split(marker)[0].rstrip() + "\n"

header = Path(r"C:\Users\rizzw\Downloads\hm\hotmail_bot\telegram\_runtime_header.py").read_text(encoding="utf-8")
p.write_text(header + "\n" + body.lstrip(), encoding="utf-8")
print("patched", p.stat().st_size)
