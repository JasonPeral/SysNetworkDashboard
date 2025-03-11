# system_monitor/utils.py
import os

def clear_screen():
    """Clears the console screen (cross-platform)."""
    os.system('cls' if os.name == 'nt' else 'clear')
