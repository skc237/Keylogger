# Python Keylogger with Encrypted DNS Tunneling Exfiltration

This repository contains a Python-based keylogger that captures keystrokes, encrypts the captured logs using AES encryption, and exfiltrates them via DNS tunneling. The keylogger is designed to work on both Windows and Linux platforms.

## Features

- **Keystroke Logging**: Captures keystrokes, including special key combinations.
- **Encryption**: Logs are encrypted using AES encryption before being saved locally.
- **DNS Tunneling**: Encrypted logs are exfiltrated using DNS tunneling with the `iodine` tool.
- **Cross-Platform**: Designed to work on both Windows and Linux systems.


## Installation

### Dependencies

- **Python 3.x**
- `pynput` library for capturing keyboard input.
- `cryptography` library for encryption and decryption.
- `iodine` for DNS tunneling.

Install dependencies using pip:
```bash
pip install pynput cryptography dnspython

Future works:
- **USB Execution**: The keylogger can be stored on a USB pendrive and automatically executed when plugged into a target machine.
- `dnspython` for DNS queries. enabling periodic exfiltration.
