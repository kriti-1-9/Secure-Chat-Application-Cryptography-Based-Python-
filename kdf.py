from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes

# Derive AES key from shared secret
def derive_key(shared_key):
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,  # 32 bytes = 256 bits
        salt=None,
        info=b'handshake data'
    ).derive(shared_key)

    return derived_key