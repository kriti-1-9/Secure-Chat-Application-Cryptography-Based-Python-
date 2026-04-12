from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

# Generate signing keys
def generate_signing_keys():
    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    return private_key, public_key

# Sign message
def sign_message(private_key, message):
    signature = private_key.sign(message.encode())
    return signature

# Verify signature
def verify_signature(public_key, message, signature):
    try:
        public_key.verify(signature, message.encode())
        return True
    except:
        return False