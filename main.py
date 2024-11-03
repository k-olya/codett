import psutil
import time
from datetime import datetime
import keyboard
import mouse

LOG_FILE = "vscode_time_log.txt"
PROCESS_NAME = "Code.exe"  # Process name for VS Code on Windows
AFK = False # Flag to check if the user is AFK

def log_time():
    # Log the current time if active and not AFK
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()}\n")

def is_vscode_running():
    # Check if VS Code is running
    for process in psutil.process_iter(['name']):
        if process.info['name'] == PROCESS_NAME:
            return True
    return False

def reset_afk_flag(_):
    global AFK
    AFK = False # Set the flag if there's any input

def main():
    global AFK

    # Attach handlers for keyboard and mouse
    keyboard.hook(reset_afk_flag)
    mouse.hook(reset_afk_flag)

    while True:
        if is_vscode_running() and not AFK:
            log_time()
        # Reset AFK flag for the next interval
        AFK = True
        time.sleep(300)  # Wait for 5 minutes (300 seconds)

if __name__ == "__main__":
    main()
