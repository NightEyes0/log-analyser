import re

print("--- Log Analysis Started ---\n")

# THE REGEX PATTERN:
# \d{1,3} look for 1 to 3 numbers
# \.  look for a literal dot
# \s+ look for spaces
# (SUCCESS|FAILED) look for either of these exact words
log_pattern = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(SUCCESS|FAILED)"

# Open log file in read
with open("server.log", "r") as file:
    
    # Read the file 
    for line in file:
        
        # Check if the line matches our Regex pattern
        match = re.search(log_pattern, line)
        
        if match:
            # group(1) pulls out the first thing in parentheses (the IP)
            ip_address = match.group(1)
            # group(2) pulls out the second thing in parentheses (the Status)
            status = match.group(2)
            
            # The :<15 adds padding so the columns line up perfectly
            print(f"Found event -> IP: {ip_address:<15} | Status: {status}")