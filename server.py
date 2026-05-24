class Server:
    def __init__(self):
        self.messages = []

    def relay_message(self, encrypted_packet):
        print("\n[Server] Relaying encrypted message...")
        self.messages.append(encrypted_packet)
        return encrypted_packet