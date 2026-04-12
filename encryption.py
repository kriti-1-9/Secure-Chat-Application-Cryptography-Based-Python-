from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

# Generate a random 256-bit key
def generate_key():
    return AESGCM.generate_key(bit_length=256)

# Encrypt message
def encrypt_message(key, plaintext):
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)  # unique per message
    ciphertext = aesgcm.encrypt(nonce, plaintext.encode(), None)
    return nonce, ciphertext

# Decrypt message
def decrypt_message(key, nonce, ciphertext):
    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)
    return plaintext.decode()