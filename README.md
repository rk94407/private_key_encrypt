# 1. Introduction:

This document provides step-by-step instructions for running the encryption code and understanding its functionality.

# 2. Prerequisites:

Python installed on your system.
Installation of required libraries: <b> "pycryptodome" <b> and <b> "python-dotenv" <b>.

# 3. Setup:

### 1. 
Install required libraries using pip: <b> pip install pycryptodome python-dotenv <b>

### 2.
Create a .env file in the project directory and add the following line with your desired encryption key: <b> ENCRYPTION_KEY=your_encryption_key_here <b>

# 4. Running the Code:

1. Open a terminal or command prompt.
2. Navigate to the directory containing the Python script (encryption_code.py).
3. Run the script using the following command: <b> python main.py <b>

# 5. Understanding the Code:

The code generates a random private key using AES encryption.
It loads the encryption key from the .env file.
The private key is encrypted using AES encryption with the provided key.
The encrypted private key is printed to the console.
The encrypted private key is decrypted using the same key, and the decrypted private key is printed to the console.

# 6. Important Note:

Ensure that the .env file is securely managed and not shared with unauthorized users.
Keep the encryption key confidential to maintain data security.

# 7. Conclusion:

By following these steps, you can successfully run the encryption code, encrypt and decrypt private keys using AES encryption, and understand the underlying functionality of the script.