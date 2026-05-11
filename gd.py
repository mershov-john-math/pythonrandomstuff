import subprocess
import time
import signal
import sys
from random import choice
url = ["https://www.youtube.com/watch?v=D5uJOpItgNg","https://www.youtube.com/watch?v=Pb6KyewC_Vg","https://www.youtube.com/watch?v=afwK743PL2Y"
       ,"https://www.youtube.com/watch?v=zZ1L9JD6l0g", "https://www.youtube.com/watch?v=ZXHO4AN_49Q", "https://www.youtube.com/watch?v=Z5RufkDHsdM"]
num_windows = 10






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
        "open", "-na", "Google Chrome", "--args", "--new-window", choice(url),
    ])
    time.sleep(delay_between_windows)

while True:
    time.sleep(1)
