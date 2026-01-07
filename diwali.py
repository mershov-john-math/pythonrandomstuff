import subprocess
import time
import signal
import sys

url = "https://www.youtube.com/watch?v=pWphVkRzhtY"
num_windows = 10000






delay_between_windows = 0

def close_all_windows(signal_received=None, frame=None):
    print("\nClosing all Chrome windows via AppleScript...")
    subprocess.run([
        "osascript", "-e",
        'tell application "Google Chrome" to close windows'
    ])
    sys.exit(0)

signal.signal(signal.SIGINT, close_all_windows)

for i in range(num_windows):
    subprocess.Popen([
        "open", "-na", "Google Chrome", "--args", "--new-window", url
    ])
    time.sleep(delay_between_windows)

while True:
    time.sleep(1)
