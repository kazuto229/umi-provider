from cryptography.fernet import Fernet

class TokenStore:

    def __init__(self, key):
        self.fernet = Fernet(key)

    def encrypt(self, value):
        return self.fernet.encrypt(value.encode())

    def decrypt(self, value):
        return self.fernet.decrypt(value).decode()