from signatures import generate_signing_keys, sign_message, verify_signature

# Generate keys
priv, pub = generate_signing_keys()

message = "Hello Secure World 🔐"

# Sign
signature = sign_message(priv, message)

# Verify
valid = verify_signature(pub, message, signature)

print("Signature valid:", valid)