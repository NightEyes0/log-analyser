import re
import requests

print("--- Advanced Log Analysis Started ---\n")

#  Download real server logs from the Loghub  dataset
log_url = "https://raw.githubusercontent.com/logpai/loghub/master/Linux/Linux_2k.log"
print("Downloading 2,000 real Linux server log lines...")
log_data = requests.get(log_url).text.splitlines()

#  Regex to find the Attacker's IP in an 'authentication failure' line
log_pattern = r"authentication failure;.*rhost=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
failed_logins = {}

print("Parsing logs for brute-force attacks...")
for line in log_data:
    match = re.search(log_pattern, line)
    if match:
        ip_address = match.group(1)
        
        # Count failures per IP
        if ip_address in failed_logins:
            failed_logins[ip_address] += 1
        else:
            failed_logins[ip_address] = 1

print("\n--- 🚨 THREAT INTELLIGENCE REPORT 🚨 ---")

#  Only track hackers who tried to break in 10 or more times
THRESHOLD = 10 

for ip, count in failed_logins.items():
    if count >= THRESHOLD:
        print(f"\n[!] Heavy Brute-Force Detected: {ip} ({count} failed attempts)")
        
        #OSINT Tracker (Where is the hacker located?)
        try:
            geo_data = requests.get(f"http://ip-api.com/json/{ip}").json()
            if geo_data['status'] == 'success':
                print(f"    -> Location: {geo_data['city']}, {geo_data['country']}")
                print(f"    -> ISP/Host: {geo_data['isp']}")
            else:
                print("    -> Location details hidden/unknown")
        except:
            print("    -> Threat tracking offline.")

print("\nReport generation complete.")