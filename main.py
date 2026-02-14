#!/usr/bin/env python3
"""
Ministry Tools - Lanzador Profesional
Version 1.0.0
"""

import os
import sys
import platform
import time
import subprocess
import shutil
import tempfile
import urllib.request

# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════

VERSION = "1.0.0"
APP_NAME = "Ministry Tools"

# ══════════════════════════════════════════════════════════════════════════════
# TERMINAL COLORS
# ══════════════════════════════════════════════════════════════════════════════

class Style:
    # Colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    # Bright colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

    # Formatting
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'


def init_terminal():
    """Initialize terminal settings (especially for Windows ANSI support)."""
    if platform.system() == 'Windows':
        os.system('')
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        except Exception:
            pass

init_terminal()

# ══════════════════════════════════════════════════════════════════════════════
# UTILITY
# ══════════════════════════════════════════════════════════════════════════════

def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def print_blank():
    print()

def get_os_info():
    system = platform.system()
    if system == 'Windows':
        return 'Windows', platform.release()
    elif system == 'Darwin':
        return 'macOS', platform.mac_ver()[0]
    elif system == 'Linux':
        return 'Linux', platform.release()
    return system, 'Unknown'

def display_system_info():
    os_name, os_version = get_os_info()
    python_version = platform.python_version()
    print(f"  {Style.DIM}{os_name} {os_version}  •  Python {python_version}{Style.RESET}")
    print_blank()

def display_header():
    clear()
    logo = f"""
{Style.BRIGHT_CYAN}
  ███╗   ███╗██╗███╗   ██╗██╗███████╗████████╗██████╗ ██╗   ██╗  ████████╗ ██████╗  ██████╗ ██╗     ███████╗
  ████╗ ████║██║████╗  ██║██║██╔════╝╚══██╔══╝██╔══██╗╚██╗ ██╔╝  ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
  ██╔████╔██║██║██╔██╗ ██║██║███████╗   ██║   ██████╔╝ ╚████╔╝      ██║   ██║   ██║██║   ██║██║     ███████╗
  ██║╚██╔╝██║██║██║╚██╗██║██║╚════██║   ██║   ██╔══██╗  ╚██╔╝       ██║   ██║   ██║██║   ██║██║     ╚════██║
  ██║ ╚═╝ ██║██║██║ ╚████║██║███████║   ██║   ██║  ██║   ██║        ██║   ╚██████╔╝╚██████╔╝███████╗███████║
  ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
{Style.RESET}
{Style.DIM}  Lanzador basico{Style.RESET}                                                           {Style.DIM}v{VERSION}{Style.RESET}
"""
    print(logo)

def display_menu():
    print(f"""
    {Style.BRIGHT_WHITE}MENU PRINCIPAL{Style.RESET}

    {Style.BRIGHT_GREEN}[1]{Style.RESET}  Test   {Style.DIM}Abrir yes.txt{Style.RESET}
    {Style.BRIGHT_GREEN}[2]{Style.RESET}  Check  {Style.DIM}Check for updates{Style.RESET}
    {Style.BRIGHT_GREEN}[3]{Style.RESET}  Exit
""")

def ensure_yes_file(path):
    """Create yes.txt if missing."""
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write("YES\n")

def open_file_default_app(path):
    """Open a file using the OS default associated app."""
    system = platform.system()
    try:
        if system == "Windows":
            os.startfile(path)  # type: ignore[attr-defined]
            return True
        elif system == "Darwin":
            subprocess.run(["open", path], check=False)
            return True
        else:
            subprocess.run(["xdg-open", path], check=False)
            return True
    except Exception:
        return False

# ══════════════════════════════════════════════════════════════════════════════
# ACTIONS
# ══════════════════════════════════════════════════════════════════════════════

def action_test():
    display_header()
    print(f"  {Style.BRIGHT_WHITE}TEST{Style.RESET}")
    print()

    yes_path = os.path.join(os.getcwd(), "yes.txt")
    ensure_yes_file(yes_path)

    print(f"  {Style.CYAN}Abriendo:{Style.RESET} {Style.DIM}{yes_path}{Style.RESET}")
    ok = open_file_default_app(yes_path)

    if ok:
        print(f"  {Style.BRIGHT_GREEN}✓{Style.RESET} Listo")
    else:
        print(f"  {Style.BRIGHT_RED}✗{Style.RESET} No se pudo abrir automaticamente.")
        print(f"  {Style.DIM}Abre manualmente el archivo en tu explorador.{Style.RESET}")

    print()
    input(f"  {Style.DIM}Presiona Enter para continuar...{Style.RESET}")

def action_check():
    display_header()
    print(f"  {Style.BRIGHT_WHITE}CHECK FOR UPDATES{Style.RESET}")
    print()

    # Configuration
    GDRIVE_FILE_ID = "1JkAlS277xgF-sqf6DJq0Pv4oo2VuM-gI"
    GITHUB_REPO = "https://github.com/ImMaxSchaeffer/Updater-Test"
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    local_version_path = os.path.join(current_dir, "version.txt")

    # Read local version
    try:
        with open(local_version_path, "r", encoding="utf-8") as f:
            local_version = f.read().strip()
        print(f"  {Style.CYAN}Local version:{Style.RESET} {local_version}")
    except FileNotFoundError:
        local_version = "0.0.0"
        print(f"  {Style.YELLOW}!{Style.RESET} No local version.txt found, assuming {local_version}")

    # Fetch remote version from Google Drive
    print(f"  {Style.DIM}Checking for updates...{Style.RESET}")
    gdrive_url = f"https://drive.google.com/uc?export=download&id={GDRIVE_FILE_ID}"
    
    try:
        with urllib.request.urlopen(gdrive_url, timeout=10) as response:
            remote_version = response.read().decode("utf-8").strip()
        print(f"  {Style.CYAN}Remote version:{Style.RESET} {remote_version}")
    except Exception as e:
        print(f"  {Style.BRIGHT_RED}✗{Style.RESET} Failed to fetch remote version: {e}")
        print()
        input(f"  {Style.DIM}Presiona Enter para continuar...{Style.RESET}")
        return

    # Compare versions (simple string comparison works for semantic versioning)
    def version_tuple(v):
        return tuple(map(int, v.split('.')))

    try:
        local_v = version_tuple(local_version)
        remote_v = version_tuple(remote_version)
    except ValueError:
        print(f"  {Style.BRIGHT_RED}✗{Style.RESET} Invalid version format")
        print()
        input(f"  {Style.DIM}Presiona Enter para continuar...{Style.RESET}")
        return

    if remote_v > local_v:
        print()
        print(f"  {Style.BRIGHT_GREEN}✓{Style.RESET} Update available! ({local_version} → {remote_version})")
        print(f"  {Style.DIM}Downloading update from GitHub...{Style.RESET}")
        
        # Clone repo to temp directory
        temp_dir = tempfile.mkdtemp()
        clone_path = os.path.join(temp_dir, "repo")
        
        try:
            # Clone the repository
            result = subprocess.run(
                ["git", "clone", "--depth", "1", GITHUB_REPO, clone_path],
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if result.returncode != 0:
                print(f"  {Style.BRIGHT_RED}✗{Style.RESET} Git clone failed: {result.stderr}")
                shutil.rmtree(temp_dir, ignore_errors=True)
                print()
                input(f"  {Style.DIM}Presiona Enter para continuar...{Style.RESET}")
                return

            print(f"  {Style.DIM}Updating files...{Style.RESET}")
            
            # Copy all files from cloned repo to current directory (replacing old ones)
            for item in os.listdir(clone_path):
                if item == ".git":
                    continue  # Skip .git folder
                
                src = os.path.join(clone_path, item)
                dst = os.path.join(current_dir, item)
                
                if os.path.isdir(src):
                    if os.path.exists(dst):
                        shutil.rmtree(dst)
                    shutil.copytree(src, dst)
                else:
                    shutil.copy2(src, dst)

            print(f"  {Style.BRIGHT_GREEN}✓{Style.RESET} Update complete! Files have been replaced.")
            print(f"  {Style.YELLOW}!{Style.RESET} Please restart the application to use the new version.")
            
        except subprocess.TimeoutExpired:
            print(f"  {Style.BRIGHT_RED}✗{Style.RESET} Git clone timed out")
        except Exception as e:
            print(f"  {Style.BRIGHT_RED}✗{Style.RESET} Update failed: {e}")
        finally:
            # Clean up temp directory
            shutil.rmtree(temp_dir, ignore_errors=True)
    else:
        print()
        print(f"  {Style.BRIGHT_GREEN}✓{Style.RESET} You are already on the latest version!")

    print()
    input(f"  {Style.DIM}Presiona Enter para continuar...{Style.RESET}")

# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

def main():
    try:
        while True:
            display_header()
            display_system_info()
            display_menu()

            choice = input(f"  {Style.CYAN}Selecciona:{Style.RESET} ").strip()

            if choice == "1":
                action_test()
            elif choice == "2":
                action_check()
            elif choice == "3":
                clear()
                print()
                print(f"  {Style.CYAN}Adios.{Style.RESET}")
                print()
                sys.exit(0)
            else:
                print(f"  {Style.RED}Opcion invalida.{Style.RESET}")
                time.sleep(1)

    except KeyboardInterrupt:
        clear()
        print()
        print(f"  {Style.YELLOW}Terminado.{Style.RESET}")
        print()
        sys.exit(0)

if __name__ == "__main__":
    main()
