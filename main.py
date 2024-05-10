from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import os
from dotenv import load_dotenv
import base64


def generate_private_key():
    # Generate a random private key.
    private_key = get_random_bytes(16)  # Using 16 bytes (128 bits) for AES encryption
    return private_key


def encrypt_private_key(private_key, password):
    # Encrypt the private key using AES encryption with a password.
    cipher = AES.new(password.encode(), AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(private_key)
    return ciphertext, cipher.nonce, tag


def decrypt_private_key(ciphertext, nonce, tag, password):
    # Decrypt the ciphertext using AES decryption with the password.
    cipher = AES.new(password.encode(), AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext
    except ValueError:
        return "Decryption failed."


# Generate private key
private_key = generate_private_key()

# Load environment variables from .env file
load_dotenv()

# Encrypt private key with a password
password = os.environ.get("ENCRYPTION_KEY")
ciphertext, nonce, tag = encrypt_private_key(private_key, password)

# Print encrypted private key
print("Encrypted Private Key:", base64.b64encode(ciphertext))

# Decrypt the encrypted private key
decrypted_private_key = decrypt_private_key(ciphertext, nonce, tag, password)
print("Decrypted Private Key:", decrypted_private_key)