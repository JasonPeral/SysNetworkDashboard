#This class will handle all log collection and filtering
# system_monitor/log_monitor.py
import subprocess
import json
import re
import time

class LogMonitor:
    """Class to fetch and filter system logs."""

    def __init__(self, log_duration="10m"):
        self.log_duration = log_duration  # Time frame for logs (e.g., "10m" = last 10 minutes)
        self.pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+[-+]\d{4}).*?\s(Error|Fault|Critical)\s+(.*?)$')

    def get_logs(self):
        """Fetch system logs and filter critical entries."""
        command = ["log", "show", "--style", "syslog", "--last", self.log_duration]

        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            log_entries = []

            for line in result.stdout.splitlines():
                match = self.pattern.search(line)
                if match:
                    timestamp, severity, message = match.groups()
                    log_entries.append({
                        "timestamp": timestamp,
                        "severity": severity,
                        "message": message.strip()
                    })

            if log_entries:
                with open('critical_logs.json', 'w') as f:
                    json.dump(log_entries, f, indent=4)
                print("[INFO] Critical logs saved to 'critical_logs.json'.")
            else:
                print("[INFO] No critical logs found.")

        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Failed to fetch logs: {e}")
        except Exception as e:
            print(f"[ERROR] Unexpected error: {e}")

    def start_periodic_logging(self, interval=10):
        """Runs get_logs() every 'interval' seconds."""
        try:
            while True:
                print("\n[INFO] Fetching system logs...")
                self.get_logs()
                print(f"[INFO] Waiting {interval} seconds before next check...")
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\n[INFO] Log monitoring stopped by user.")
