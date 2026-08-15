from parser import parser_log
from detector import detect_failed_logins

## Set log_file destination ##
log_file = "logs/auth.log"

# Call parser_log function and retrieve value as events #
events = parser_log(log_file)

# Call detect_failed_logins and retrieve value as detect #
detect = detect_failed_logins(events, "5")