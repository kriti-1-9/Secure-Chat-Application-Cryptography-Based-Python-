import bcrypt
import time

class AuthSystem:

    def __init__(self):

        # Simulated database
        self.users = {}

        # Failed login tracking
        self.failed_attempts = {}

        # Block duration (seconds)
        self.block_time = 30

    # =========================
    # Register User
    # =========================
    def register(self, username, password):

        hashed = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        )

        self.users[username] = hashed

        print(f"[+] User '{username}' registered successfully.")

    # =========================
    # Login User
    # =========================
    def login(self, username, password):

        current_time = time.time()

        # Check if blocked
        if username in self.failed_attempts:

            attempts, last_attempt = self.failed_attempts[username]

            if attempts >= 3:

                if current_time - last_attempt < self.block_time:
                    print("[!] Account temporarily blocked.")
                    return False
                else:
                    # Reset after block expires
                    self.failed_attempts[username] = [0, current_time]

        # User exists?
        if username not in self.users:
            print("[!] User not found.")
            return False

        stored_hash = self.users[username]

        # Verify password
        if bcrypt.checkpw(password.encode(), stored_hash):

            print("[+] Login successful.")

            # Reset failed attempts
            self.failed_attempts[username] = [0, current_time]

            return True

        else:

            print("[!] Invalid password.")

            # Track failed attempts
            if username not in self.failed_attempts:
                self.failed_attempts[username] = [1, current_time]
            else:
                self.failed_attempts[username][0] += 1
                self.failed_attempts[username][1] = current_time

            return False