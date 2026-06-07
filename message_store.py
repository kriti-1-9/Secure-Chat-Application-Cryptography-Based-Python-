import time

class MessageStore:

    def __init__(self):
        self.messages = []

    def add_message(self, sender, content, ttl):

        expiry_time = time.time() + ttl

        self.messages.append({
            "sender": sender,
            "content": content,
            "expires": expiry_time
        })

    def cleanup_expired_messages(self):

        current_time = time.time()

        self.messages = [
            msg
            for msg in self.messages
            if msg["expires"] > current_time
        ]

    def show_messages(self):

        self.cleanup_expired_messages()

        for msg in self.messages:
            print(f"{msg['sender']}: {msg['content']}")