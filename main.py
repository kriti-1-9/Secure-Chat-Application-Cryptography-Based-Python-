from key_exchange import generate_keys, generate_shared_key
from kdf import derive_key
from signatures import generate_signing_keys

from client import Client
from server import Server

# =========================
# Key Exchange
# =========================

# User A keys
priv_a, pub_a = generate_keys()

# User B keys
priv_b, pub_b = generate_keys()

from session_manager import SessionManager

# Create session manager
session = SessionManager()

# Generate temporary session keys
key_a, key_b = session.create_session()

# =========================
# Signature Keys
# =========================

sign_priv_a, sign_pub_a = generate_signing_keys()
sign_priv_b, sign_pub_b = generate_signing_keys()

# =========================
# Create Clients
# =========================

alice = Client(
    "Alice",
    key_a,
    sign_priv_a,
    sign_pub_a
)

bob = Client(
    "Bob",
    key_b,
    sign_priv_b,
    sign_pub_b
)

# =========================
# Create Server
# =========================

server = Server()

# =========================
# Communication
# =========================

packet = alice.send_message("Hello Bob 🔐")

forwarded_packet = server.relay_message(packet)

bob.receive_message(forwarded_packet, sign_pub_a)

print("\n--- NEW SESSION CREATED ---")

# Rotate session keys
key_a, key_b = session.create_session()

alice.aes_key = key_a
bob.aes_key = key_b

packet2 = alice.send_message("New secure session 🔄")

forwarded_packet2 = server.relay_message(packet2)

bob.receive_message(forwarded_packet2, sign_pub_a)

from monitoring import dashboard, logger

dashboard.show_dashboard()

logger.show_logs()