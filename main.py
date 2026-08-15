from parser import parser_log
from detector import detect_failed_logins

## Set log_file destination ##
log_file = "logs/auth.log"
threshold = 5

# Call parser_log function and retrieve value as events #
events = parser_log(log_file)

# Call detect_failed_logins and retrieve value as suspicious_ips #
suspicious_ips = detect_failed_logins(events, threshold)