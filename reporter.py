from detector import detect_failed_logins
from parser import parser_log

def print_report(suspicious_ips, threshold):
    print("SECURITY LOG ANALYSIS REPORT")
    print("Threshold:", threshold, "failed attempts")
    print("-----------------------------------")

    if len(suspicious_ips) == 0:
        print("No suspicious acitivity detected.")
        return

    for ip in suspicious_ips:
        count = suspicious_ips[ip]
        print(ip, "-", count, "failed login attempts")

def save_report(suspicious_ips, threshold, output_path):
    file = open(output_path, "w")

    file.write("SECURITY LOG ANALYSIS REPORT\n\n")
    file.write("Threshold: "+ str(threshold) + " failed attempts\n\n")
    print("-------------------------------------------\n")

    if len(suspicious_ips) == 0:
        print("No suspicious activity detected.\n")
    else:
        for ip in suspicious_ips:
            count = suspicious_ips[ip]
            file.write(ip + " - " + str(count) + " failed login attempts \n")

    file.close()
    print("Report saved to:", output_path, "\n")