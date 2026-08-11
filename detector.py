from parser import parser_log

def detect_failed_logins(events, threshold):

    failed_attempts = {}

    for event in events:

        if event["event"] == "LOGIN_FAILED":

            ip_addresses = event["ip"]

            if ip_addresses in failed_attempts:

                failed_attempts[ip_addresses] += 1

            else:

                failed_attempts[ip_addresses] = 1

    return failed_attempts