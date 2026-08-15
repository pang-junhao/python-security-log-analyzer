## Opens file and prints out all the logs with for loop and returns ##
def parser_log(log):
    events = []
    with open(log, "r") as file:
        logs = file.readlines()

    for log in logs:
        log = log.strip()

        parts = log.split()

        try:
            date = parts[0]
            time = parts[1]
            event = parts[2]
            username = parts[3].split("user=")[1]
            ip_addresses = parts[4].split("ip=")[1]
        except(IndexError, ValueError):
            print("Skipping bad log:", log)
            continue

        events.append ({
            "date": date,
            "time": time,
            "event": event,
            "username": username,
            "ip": ip_addresses
        })

    return events