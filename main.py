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
    {Style.BRIGHT_GREEN}[2]{Style.RESET}  Check  {Style.DIM}Placeholder{Style.RESET}
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
    print(f"  {Style.BRIGHT_WHITE}CHECK{Style.RESET}")
    print()
    print(f"  {Style.BRIGHT_YELLOW}!{Style.RESET} Placeholder: aqui va tu logica real despues.")
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
