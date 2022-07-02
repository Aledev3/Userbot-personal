import subprocess
import sys
import os

cmd = "sudo apt update && sudo apt upgrade && sudo apt install python3 && sudo apt install python3-pip"
mvenv = "sudo mv .env_example .env"
 
if os.access('install.py', os.W_OK):
    os.system(cmd)
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    os.system(mvenv)
    print("Done!")
else:
    print("Some permissions are missing. Try chmod +x install.py")
