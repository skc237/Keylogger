import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def generate_key():
    return os.urandom(32)  # Generate a 256-bit key for AES

def save_key(key):
    key_path = 'syskey.bin'
    with open(key_path, 'wb') as key_file:
        key_file.write(key)

def load_key():
    key_path = 'syskey.bin'
    with open(key_path, 'rb') as key_file:
        return key_file.read()


# Generate and store the key if it's not already present
if not os.path.exists('syskey.bin'):
    key = generate_key()
    save_key(key)
else:
    key = load_key()



def encrypt_log(log_data):
    backend = default_backend()
    iv = os.urandom(16)  # Initialization vector
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()

    # Pad the log data to be a multiple of block size
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(log_data) + padder.finalize()

    # Encrypt the data
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return iv + encrypted_data