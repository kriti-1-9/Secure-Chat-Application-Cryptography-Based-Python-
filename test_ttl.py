from message_store import MessageStore
import time

store = MessageStore()

store.add_message(
    "Alice",
    "This message self-destructs",
    5
)

print("Messages immediately:")
store.show_messages()

time.sleep(6)

print("\nMessages after 6 seconds:")
store.show_messages()