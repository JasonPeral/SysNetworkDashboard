import psutil 
import subprocess
import json 
import re
import time

#class based structure to modularize the code

class SystemMonitor:
    def __init__(self, log_duration="10m", log_file="critical_logs.json"):
        #duration setting for parsing logs and saving those logs to files
        self.log_duration = log_duration
        self.log_file = log_file

    
    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=1)
    
    def get_memory_usage(self):
        memory = psutil.virtual_memory()
        return {
            "Total": memory.total,
            "Currently Available": memory.available,
            "Used": memory.used,
            "Percentage": memory.percent
        }
    
    def get_disk_usage(self):
        disk = psutil.disk_usage('/')
        return {
            "total": disk.total,
            "used": disk.used,
            "free": disk.free,
            "percentage": disk.percent
        }
    
    def fetch_critical_logs(self):
        """Fetch critical system logs using subprocess."""
        command = [
            #"sudo",
            "log", "show",
            "--style", "syslog",
            "--last", self.log_duration
        ]

        # Regex to match Error, Fault, or Critical logs
        pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+[-+]\d{4}).*?\s(Error|Fault|Critical)\s+(.*?)$')

        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            log_entries = []

            for line in result.stdout.splitlines():
                match = pattern.search(line)
                if match:
                    timestamp, severity, message = match.groups()
                    log_entries.append({
                        "timestamp": timestamp,
                        "severity": severity,
                        "message": message.strip()
                    })

            if log_entries:
                with open(self.log_file, 'w') as f:
                    json.dump(log_entries, f, indent=4)
                print(f"Critical logs saved to {self.log_file}.")
            else:
                print("No critical logs found.")

        except subprocess.CalledProcessError as e:
            print(f"Error executing log command: {e}")

    def display_system_status(self):
        cpu = self.get_cpu_usage()
        memory = self.get_memory_usage()
        disk = self.get_disk_usage()

        print(f"\n--- System Status ---")
        print(f"CPU Usage: {cpu}%")
        print(f"Memory Usage: {memory['Used'] / (1024 ** 3):.2f} GB / {memory['Total'] / (1024 ** 3):.2f} GB ({memory['Percentage']}%)")
        print(f"Disk Usage: {disk['used'] / (1024 ** 3):.2f} GB / {disk['total'] / (1024 ** 3):.2f} GB ({disk['percentage']}%)")

    def start_monitoring(self, interval=60):
        try:
            while True:
                self.display_system_status()
                self.fetch_critical_logs()
                print("\n--- Waiting for next check ---\n")
                time.sleep(interval)  
        except KeyboardInterrupt:
            print("\nMonitoring stopped.")


if __name__ == "__main__":  # Added program entry point
    monitor = SystemMonitor()
    monitor.start_monitoring(interval=60)
