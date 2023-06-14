import subprocess
import sys
import os
import psutil

from sys import platform

cmd = "sudo apt update && sudo apt upgrade -y && sudo apt install python3 -y && sudo apt install python3-pip -y"
mvenv = "sudo mv .env_example .env"

if psutil.LINUX:
    if os.access('install.py', os.W_OK):
        os.system(cmd)
        subprocess.check_call([sys.executable, "-m", "pip3", "install", "-r", "requirements.txt"])
        os.system(mvenv)
        print("\n\n\nDone! Use python3 userbot.py to start your personal userbot.\n\nScript made with ❤ by @OgDeltwin")
    else:
        print("Some permissions are missing. Retry with chmod +x install.py")
else:
    print("This script can't run with your OS. Please run this script on OS with APT as package manager.")
