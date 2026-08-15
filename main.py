from parser import parser_log
from detector import detect_failed_logins
from reporter import print_report, save_report

## Set log_file destination ##
log_file = "logs/auth.log"
report_file = "reports/report.txt"
threshold = 5

# Call parser_log function and retrieve value as events #
events = parser_log(log_file)

# Call detect_failed_logins and retrieve value as suspicious_ips #
suspicious_ips = detect_failed_logins(events, threshold)

# Show results and saves them into a report file #
print_report(suspicious_ips, threshold)
save_report(suspicious_ips, threshold, report_file)