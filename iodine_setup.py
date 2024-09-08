    # iodine_setup.py
import subprocess
import os

def check_iodine_installed():
    try:
        subprocess.run(["iodine", "-help"], check=True)
        return True
    except FileNotFoundError:
        return False

def install_iodine():
    if os.name == 'nt':
        # Handle Windows iodine installation
        print("Please manually install iodine on Windows.")
    else:
        subprocess.run(["sudo", "apt-get", "install", "iodine", "-y"])
