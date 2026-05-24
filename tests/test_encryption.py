from encryption import generate_key, encrypt_message, decrypt_message

key = generate_key()

message = "Hello Kriti, this is a secret message!"

nonce, encrypted = encrypt_message(key, message)
print("Encrypted:", encrypted)

decrypted = decrypt_message(key, nonce, encrypted)
print("Decrypted:", decrypted)