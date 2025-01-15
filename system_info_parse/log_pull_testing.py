import subprocess
import json
import re
import time

def get_logs():
    #First I will define the log command to fetch my logs
    command = [
        #adding sudo as the logs are not parsing
        #"sudo", #got rid of sudo and still successfully pulled logs
        "log", "show",
        "--style", "syslog",
        "--last", "10m" #I will modify the time frame as needed
    ]
    #Matching logs based on logs show output on my system
    pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+[-+]\d{4}).*?\s(Error|Fault|Critical)\s+(.*?)$')


    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        log_entries = []

        # Iterating over each line and search for matching log entries
        for line in result.stdout.splitlines():
            match = pattern.search(line)
            if match:
                timestamp, severity, message = match.groups()
                log_entries.append({
                    "timestamp": timestamp,
                    "severity": severity,
                    "message": message.strip()
                })

        #Checking if any logs were found as I had this problem previously
        if log_entries:
            # Savinf to JSON for later use
            with open('critical_logs.json', 'w') as f:
                json.dump(log_entries, f, indent=4)
            
            print("Critical logs have been saved to 'critical_logs.json'.")
        else:
            print("No critical logs found.")
    
    except subprocess.CalledProcessError as e:
        print(f"Error executing log command: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def start_periodic_logging(interval=60):
    """Run get_logs() every 'interval' seconds."""
    try:
        while True:
            print("\n[INFO] Fetching system logs...")
            get_logs()
            print(f"[INFO] Waiting {interval} seconds before the next check...")
            time.sleep(interval)  #Argument that will depict what intervals we want to update the log 
    except KeyboardInterrupt:
        print("\n[INFO] Log monitoring stopped by user.")

start_periodic_logging(10)