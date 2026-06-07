from audit_logger import AuditLogger

logger = AuditLogger()

logger.log_event(
    "LOGIN_SUCCESS",
    "User kriti authenticated"
)

logger.log_event(
    "SESSION_CREATED",
    "ECDHE session established"
)

logger.log_event(
    "MESSAGE_EXPIRED",
    "TTL message deleted"
)

logger.show_logs()