import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def load_key():
    key_path = 'syskey.bin'
    with open(key_path, 'rb') as key_file:
        return key_file.read()
    
def decrypt_log(encrypted_data, key):
    backend = default_backend()
    iv = encrypted_data[:16]  # Extract IV from the beginning
    encrypted_data = encrypted_data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()

    # Decrypt the data
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Unpad the decrypted data
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(decrypted_data) + unpadder.finalize()


# Decrypt the logger file
def decrypt_file(file_path):
    key = load_key()

    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    decrypted_log = decrypt_log(encrypted_data, key)
    return decrypted_log

# Decrypt and print logs
if __name__ == "__main__":
    decrypted_logs = decrypt_file("logger.txt")
    print("Decrypted Logs:\n", decrypted_logs)