# SOC Threat Intelligence Platform 

An advanced Python-based cybersecurity tool that downloads real server logs, parses them for brute-force attacks, tracks the physical location of threat actors using live OSINT geolocation, and generates interactive threat maps and automated firewall remediation scripts.

# Overview
During a security incident, SOC analysts must parse server logs, identify threat actors, map their origins, and block them. This tool automates the entire incident response pipeline (SOAR). It pulls a real-world Linux server log dataset (Loghub), uses Regex to extract IPs associated with `authentication failure`, queries the IP-API to geolocate the hackers, visualizes the attack vectors on an interactive Folium map, and automatically generates a Bash script to drop the malicious IPs via `iptables`.

# Technical Skills Demonstrated
* **Security Orchestration (SOAR):** Automated generation of Linux firewall remediation scripts (`blocklist.sh`).
* **Data Visualization:** Using `folium` to generate interactive, dark-themed HTML threat maps plotting exact attacker coordinates.
* **API Integration:** Fetching live datasets and querying third-party OSINT JSON endpoints via `requests`.
* **Text Parsing & Regex:** Extracting specific IP data from unstructured system logs.

# The Output
When executed, the script automatically generates two files:
1. **`threat_map.html`:** A live, interactive global map plotting the ISP, location, and attack volume of every brute-force threat. 
2. **`blocklist.sh`:** An automated Bash script ready for execution on a Linux server to instantly ban the attackers.

## How to Run
Ensure you have the required libraries installed:
```bash
pip install requests folium
python analyser.py