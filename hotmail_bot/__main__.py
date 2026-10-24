"""python -m hotmail_bot"""

import subprocess
import sys
from pathlib import Path


def check_and_install_dependencies():
    """Check if required dependencies are installed, install if missing."""
    requirements_file = Path(__file__).parent.parent / "requirements.txt"

    if not requirements_file.exists():
        print("⚠️ requirements.txt not found. Skipping dependency check.")
        return

    # Read requirements
    with open(requirements_file) as f:
        requirements = f.read().strip().split('\n')
        requirements = [r.strip() for r in requirements if r.strip() and not r.startswith('#')]

    # Check if each package is installed
    missing_packages = []
    for req in requirements:
        # Extract package name (everything before version specifiers)
        pkg_name = req.split('>=')[0].split('==')[0].split('~=')[0].split('[')[0].strip()

        # Map package names to their import names
        import_map = {
            'python-telegram-bot': 'telegram',
            'aiosqlite': 'aiosqlite',
            'requests': 'requests',
        }

        import_name = import_map.get(pkg_name, pkg_name.replace('-', '_'))

        try:
            __import__(import_name)
        except ImportError:
            missing_packages.append(req)

    if missing_packages:
        print("[*] Installing missing dependencies...")
        print(f"Missing packages: {', '.join(missing_packages)}")
        print("This may take a moment...\n")

        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "-r", str(requirements_file)],
                stdout=subprocess.DEVNULL if '--quiet' in sys.argv else None
            )
            print("[+] Dependencies installed successfully!\n")
        except subprocess.CalledProcessError as e:
            print(f"[-] Failed to install dependencies: {e}")
            print("Please run: pip install -r requirements.txt")
            sys.exit(1)
    else:
        print("[+] All dependencies are already installed.\n")


check_and_install_dependencies()
from hotmail_bot.telegram.app import run
run()
