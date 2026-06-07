import time

from projects.cybershield import dashboard
from monitoring import dashboard, logger

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
        old_count = len(self.messages)
        expired_count = old_count - len(self.messages)

        for _ in range(expired_count):
        dashboard.message_expired()

        logger.log_event(
            "MESSAGE_EXPIRED",
            "TTL message removed"
        )

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