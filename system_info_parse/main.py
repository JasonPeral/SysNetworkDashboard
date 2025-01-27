import platform
import psutil
import cpuinfo
import time
import subprocess
import json
import re
import time

#moving hardcoded dependency calls into variables for later use with dashboard
sys_architecture = platform.architecture()
sys_pc_name = platform.node()
sys_os = platform.platform
sys_basic_cpu = platform.processor()
sys_cpuinfo = cpuinfo.get_cpu_info()
sys_cpu_bits = sys_cpuinfo['bits']
sys_total_ram = psutil.virtual_memory().total/1024/1024/1024
sys_cpu_usage = psutil.cpu_percent(5)

#To see what keys are available to parse in .get_cpu_info
# print(my_cpuinfo.keys())
#information on the architecture of our machine 
print(f"Architecture: {sys_architecture}")
print(f"Computer Name: {sys_pc_name}")
print(f"OS: {sys_os}")
#less detailed info on cpu
print(f"Processor: {sys_basic_cpu}")
print(f"Full CPU info: {sys_cpuinfo['brand_raw']}")
#Apple does not display cpu hz information. Opting to run bits key
print(f"Bits: {sys_cpu_bits}")


try:
    while True:
        # To have this as constantly refreshing we will put this into a while loop
        # where here we will grab CPU and RAM info
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_info = psutil.virtual_memory()
        ram_usage = ram_info.percent
        available_ram = ram_info.available / (1024 ** 2)  # Converting to MB
        total_ram = ram_info.total / (1024 ** 2)  # Convert to MB

        # Clear the screen (platform-independent)
        print("\033[H\033[J", end="")  # Clear the terminal screen
        print("Live System Monitoring")
        print("----------------------")
        print(f"CPU Usage: {cpu_usage}%")
        print(f"RAM Usage: {ram_usage}%")
        print(f"Available RAM: {available_ram:.2f} MB / {total_ram:.2f} MB")

        print("----------------------")
        print("Static System Monitoring")
        print(f"Architecture: {sys_architecture}")
        print(f"Computer Name: {sys_pc_name}")
        print(f"OS: {sys_os}")
        #less detailed info on cpu
        print(f"Processor: {sys_basic_cpu}")
        print(f"Full CPU info: {sys_cpuinfo['brand_raw']}")
        #Apple does not display cpu hz information. Opting to run bits key
        print(f"Bits: {sys_cpu_bits}")

        time.sleep(1)  # Refresh every 1 second
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

except KeyboardInterrupt:
    print("\nExiting...")
