from encryption import encrypt_message, decrypt_message
from signatures import sign_message, verify_signature
from monitoring import dashboard, logger

class Client:

    def __init__(self, name, aes_key, signing_private, signing_public):
        self.name = name
        self.aes_key = aes_key
        self.signing_private = signing_private
        self.signing_public = signing_public

    def send_message(self, plaintext):
        dashboard.message_sent()

        logger.log_event(
        "MESSAGE_SENT",
        f"{self.name} sent a message"
        )

        # Sign message
        signature = sign_message(self.signing_private, plaintext)

        # Encrypt message
        nonce, ciphertext = encrypt_message(self.aes_key, plaintext)

        packet = {
            "nonce": nonce,
            "ciphertext": ciphertext,
            "signature": signature,
            "sender": self.name
        }

        print(f"\n[{self.name}] Sending encrypted message...")
        return packet

    def receive_message(self, packet, sender_public_key):

        decrypted = decrypt_message(
            self.aes_key,
            packet["nonce"],
            packet["ciphertext"]
        )

        valid = verify_signature(
            sender_public_key,
            decrypted,
            packet["signature"]
        )

        if valid:
            print(f"\n[{self.name}] Verified message:")
            print("Message:", decrypted)
        else:
            print("\nSignature verification failed!")