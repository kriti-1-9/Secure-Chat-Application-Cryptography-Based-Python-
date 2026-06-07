from datetime import datetime

class AuditLogger:

    def __init__(self):
        self.logs = []

    def log_event(self, event_type, description):

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        log_entry = {
            "timestamp": timestamp,
            "event_type": event_type,
            "description": description
        }

        self.logs.append(log_entry)

    def show_logs(self):

        print("\n========== AUDIT LOGS ==========\n")

        for log in self.logs:

            print(
                f"[{log['timestamp']}] "
                f"{log['event_type']} -> "
                f"{log['description']}"
            )