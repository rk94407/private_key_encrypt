# 1. Introduction:

This document provides step-by-step instructions for running the encryption code and understanding its functionality.

# 2. Prerequisites:

Python installed on your system.
Installation of required libraries: <b> "pycryptodome" <b> and <b> "python-dotenv" <b>.

# 3. Setup:

1. Install required libraries using pip: <b> pip3 install pycryptodome python-dotenv <b> (Depends on the version you have, if you have latest version of python then you have to use pip3 otherwise just pip)

2. Create a .env file in the project directory and add the following line with your desired encryption key: <b> ENCRYPTION_KEY=your_encryption_key_here <b>

# 4. Running the Code:

1. Open a terminal or command prompt.
2. Navigate to the directory containing the Python script (encryption_code.py).
3. Run the script using the following command: <b> python3 main.py <b> (Depends on the version you have, if you have latest version of python then you have to use python3 otherwise just python)

# 5. Understanding the Code:

The code generates a random private key using AES encryption.
It loads the encryption key from the .env file.
The private key is encrypted using AES encryption with the provided key.
The encrypted private key is printed to the console.
The encrypted private key is decrypted using the same key, and the decrypted private key is printed to the console.