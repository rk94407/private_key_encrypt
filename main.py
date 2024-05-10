from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
from dotenv import load_dotenv
import base64

def encrypt_data(data, password):
    # Encrypt the data using AES encryption with a password.
    key = password.encode().ljust(32, b'\0')  # Ensures the key is 32 bytes
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))  # Ensure data is bytes
    return base64.b64encode(ciphertext), base64.b64encode(cipher.nonce), base64.b64encode(tag)

def decrypt_data(ciphertext, nonce, tag, password):
    # Decrypt the ciphertext using AES decryption with the password.
    key = password.encode().ljust(32, b'\0')  # Ensures the key is 32 bytes
    ciphertext = base64.b64decode(ciphertext)
    nonce = base64.b64decode(nonce)
    tag = base64.b64decode(tag)
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    try:
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        return plaintext.decode('utf-8')
    except ValueError:
        return "Decryption failed."

# Load environment variables from .env file
load_dotenv()

# Read data from the user
data = input("Please enter the text to encrypt: ")

# Encrypt the data with a password
password = os.getenv("ENCRYPTION_KEY", "default_secret")  # Default to 'default_secret' if not found
encrypted_data, nonce, tag = encrypt_data(data, password)

# Print encrypted data
print("Encrypted Data:", encrypted_data.decode())

# Decrypt the encrypted data
decrypted_data = decrypt_data(encrypted_data, nonce, tag, password)
print("Decrypted Data:", decrypted_data)
