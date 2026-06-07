from key_exchange import generate_keys, generate_shared_key
from kdf import derive_key
from monitoring import dashboard, logger

class SessionManager:

    def create_session(self):
        dashboard.session_created()

        logger.log_event(
        "SESSION_CREATED",
        "New ECDHE session established"
        )

        # Generate temporary ECDHE keys
        priv_a, pub_a = generate_keys()
        priv_b, pub_b = generate_keys()

        # Generate shared secrets
        shared_a = generate_shared_key(priv_a, pub_b)
        shared_b = generate_shared_key(priv_b, pub_a)

        # Derive AES session keys
        key_a = derive_key(shared_a)
        key_b = derive_key(shared_b)

        return key_a, key_b