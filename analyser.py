import re
import csv

print("--- Log Analysis Started ---\n")

log_pattern = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(SUCCESS|FAILED)"
failed_logins = {}

with open("server.log", "r") as file:
    for line in file:
        match = re.search(log_pattern, line)
        if match:
            ip_address = match.group(1)
            status = match.group(2)
            
            if status == "FAILED":
                if ip_address in failed_logins:
                    failed_logins[ip_address] += 1
                else:
                    failed_logins[ip_address] = 1

print("--- Security Report ---")
THRESHOLD = 3 

for ip, count in failed_logins.items():
    if count >= THRESHOLD:
        print(f"🚨 ALERT: Brute-force detected from IP {ip} ({count} failed attempts)")
    else:
        print(f"✅ IP {ip} had {count} failed attempt(s) (Under threshold)")

# --- NEW: Export to CSV ---
print("\nExporting findings to CSV...")

with open("security_report.csv", "w", newline="") as csv_file:
    # Set up  CSV writer
    writer = csv.writer(csv_file)
    
    # Write the header row
    writer.writerow(["IP Address", "Failed Attempts", "Threat Level"])
    
    # Loop through our dictionary again and save each IP into the file
    for ip, count in failed_logins.items():
        if count >= THRESHOLD:
            writer.writerow([ip, count, "Suspicious"])
        else:
            writer.writerow([ip, count, "Normal"])

print("Successfully saved to 'security_report.csv'!")