from key_exchange import generate_keys, generate_shared_key
from kdf import derive_key
from encryption import encrypt_message, decrypt_message

# Step 1: Generate key pairs
priv_a, pub_a = generate_keys()
priv_b, pub_b = generate_keys()

# Step 2: Generate shared secret
shared_a = generate_shared_key(priv_a, pub_b)
shared_b = generate_shared_key(priv_b, pub_a)

# Step 3: Derive AES key
key_a = derive_key(shared_a)
key_b = derive_key(shared_b)

# Step 4: Encrypt message
message = "Hello Secure World!"
nonce, encrypted = encrypt_message(key_a, message)

# Step 5: Decrypt message
decrypted = decrypt_message(key_b, nonce, encrypted)

print("Original:", message)
print("Decrypted:", decrypted)