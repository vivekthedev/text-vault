import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def create_password_key(password):
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=b"", iterations=10000)
    key = base64.urlsafe_b64encode(kdf.derive(bytes(str(password), "UTF-8"))).decode(
        "UTF-8"
    )
    return key


def get_fernet(key):
    return Fernet(key)


def encrypt_text(password, text):
    key = create_password_key(password)
    return get_fernet(key).encrypt(bytes(str(text), "UTF-8")).decode("UTF-8")


def decrypt_text(password, text):
    key = create_password_key(password)
    return get_fernet(key).decrypt(bytes(str(text), "UTF-8")).decode("UTF-8")
