# Introduction

This README provides step-by-step instructions to set up and run a Python script designed for AES encryption and decryption. The script demonstrates secure key management and encryption practices using environmental variables and base64 encoding.

# Prerequisites

Before starting, ensure Python is installed on your system. If Python is not installed, download and install it from the official [Python Downloads](https://www.python.org/downloads/) page. This project also requires the following Python libraries:

- `pycryptodome`
- `python-dotenv`
- `qr-code`

These libraries can be installed via pip or pip3. The script is tested and confirmed to work with Python 3.6 and newer.

# Setup

## 1. Install Required Libraries

Open your terminal or command prompt and execute the following command to install the necessary libraries:

- `pip install pycryptodome python-dotenv qr-code`

If you are using a system where Python 3 is not the default Python interpreter (e.g., systems where python points to Python 2.x), you might need to use pip3 instead:

- `pip3 install pycryptodome python-dotenv`

## 2. Environment Configuration

Create a .env file in your project directory and specify your encryption key like so:

- `ENCRYPTION_KEY=your_encryption_key_here`

## 3. Running the Code

To run the script:
Execute by running the command:

- `python3 file_name.py`

# Understanding the Code

### Key Management

1. Upon execution, the script prompts the user to choose whether they want to input their own private key or prefer the script to generate a secure key for them:
2. If the user inputs their own key, the script will hash this key using SHA-256 to ensure it meets the security requirements for AES encryption.
3. If the user opts for a generated key, the script creates a random 256-bit key that is used for encryption.

### Key Conversion and Encryption

1. Regardless of the source of the key, the following steps are applied:

   ## Hashing: The raw key or user input is hashed using SHA-256 to generate a fixed-size 256-bit key.

   ## Base64 Encoding: The hashed key is then encoded in Base64. This step ensures that the key can be safely stored and transmitted if needed.

   ## Encryption: The script uses AES encryption to securely encrypt the data using the prepared key.

   ## Data Logging:

   a. Excel Log: All private keys, along with the date and time of their creation or usage, are saved in an Excel file (keys.xlsx). This file also logs the original text and its encrypted form for each operation.
   b. Text File Log: Encrypted data is also logged in a separate text file (encryption.txt), providing a backup and an alternative view of the data.

   ## Strength percentage

   We are providing infromation on how strong the private key is based on the length of the private key and has 3 outputs: Strong, Moderate and Weak.

   ## Confirmation message

   A confirmation message gets displayed in the end when the original text matches the decrypted text: "Encryption and decryption was successful".

# QR Code Implementation
1. The script now generates a QR code containing the private key.
2. This QR code can be scanned by authorized users to securely obtain the private key for decryption.

# This is git-hub repo
The codebase is available on GitHub: <a href="https://github.com/rk94407/private_key_encrypt"> private_key_encrypt </a>

Feel free to clone or fork the repository for your use. Contributions are welcome!
