class SecurityDashboard:

    def __init__(self):

        self.total_users = 0
        self.successful_logins = 0
        self.failed_logins = 0
        self.blocked_accounts = 0

        self.active_sessions = 0

        self.messages_sent = 0
        self.messages_expired = 0

    # ---------------------
    # User Metrics
    # ---------------------

    def user_registered(self):
        self.total_users += 1

    def login_success(self):
        self.successful_logins += 1

    def login_failure(self):
        self.failed_logins += 1

    def account_blocked(self):
        self.blocked_accounts += 1

    # ---------------------
    # Session Metrics
    # ---------------------

    def session_created(self):
        self.active_sessions += 1

    # ---------------------
    # Message Metrics
    # ---------------------

    def message_sent(self):
        self.messages_sent += 1

    def message_expired(self):
        self.messages_expired += 1

    # ---------------------
    # Display Dashboard
    # ---------------------

    def show_dashboard(self):

        print("\n========== SECURITY DASHBOARD ==========")

        print(f"Registered Users     : {self.total_users}")
        print(f"Successful Logins    : {self.successful_logins}")
        print(f"Failed Logins        : {self.failed_logins}")
        print(f"Blocked Accounts     : {self.blocked_accounts}")

        print(f"Active Sessions      : {self.active_sessions}")

        print(f"Messages Sent        : {self.messages_sent}")
        print(f"Messages Expired     : {self.messages_expired}")

        print("========================================")