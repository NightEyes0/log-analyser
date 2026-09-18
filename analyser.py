import re

print("--- Log Analysis Started ---\n")

log_pattern = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(SUCCESS|FAILED)"

# A dictionary to keep track of failed logins per IP
failed_logins = {}

with open("server.log", "r") as file:
    for line in file:
        match = re.search(log_pattern, line)
        
        if match:
            ip_address = match.group(1)
            status = match.group(2)
            
            # If the login failed, add it to our tracking dictionary
            if status == "FAILED":
                if ip_address in failed_logins:
                    failed_logins[ip_address] += 1
                else:
                    failed_logins[ip_address] = 1

# Security Logic 
print("--- Security Report ---")

# If an IP fails 3 or more times, flag it as a brute-force attack
THRESHOLD = 3 

for ip, count in failed_logins.items():
    if count >= THRESHOLD:
        print(f"🚨 ALERT: Brute-force detected from IP {ip} ({count} failed attempts)")
    else:
        print(f"✅ IP {ip} had {count} failed attempt(s) (Under threshold)")

print("\nAnalysis complete.")