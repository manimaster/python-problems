from cryptography.fernet import Fernet

class CryptoFernet:
    def __init__(self):
        """
        Initializes a Fernet instance with a key.
        If you want to use a previously generated key, set it using set_key() method.
        """
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def set_key(self, key):
        """
        Set a previously generated key.
        """
        self.key = key
        self.cipher = Fernet(self.key)

    def get_key(self):
        """
        Returns the current key.
        """
        return self.key

    def encrypt(self, message):
        """
        Encrypts a message.
        """
        encoded_message = message.encode()
        encrypted_message = self.cipher.encrypt(encoded_message)
        return encrypted_message

    def decrypt(self, encrypted_message):
        """
        Decrypts an encrypted message.
        """
        decrypted_message = self.cipher.decrypt(encrypted_message)
        return decrypted_message.decode()

# Example Usage:
crypto = CryptoFernet()

# Encryption
msg = "Hello, World!"
encrypted_msg = crypto.encrypt(msg)
print("Encrypted:", encrypted_msg)

# Decryption
decrypted_msg = crypto.decrypt(encrypted_msg)
print("Decrypted:", decrypted_msg)
