import psutil
import time
from system_monitoring.utils import clear_screen  # Utility function for screen clearing

class LiveMonitor:
    """Class for monitoring live system performance (CPU & RAM usage)."""

    def __init__(self, interval=1):
        self.interval = interval  # Refresh rate in seconds

    def monitor(self):
        """Continuously monitors CPU and RAM usage."""
        try:
            while True:
                cpu_usage = psutil.cpu_percent(interval=1)
                ram_info = psutil.virtual_memory()
                ram_usage = ram_info.percent
                available_ram = ram_info.available / (1024 ** 2)  # Convert to MB
                total_ram = ram_info.total / (1024 ** 2)  # Convert to MB

                clear_screen()  # Clears the console
                print("Live System Monitoring")
                print("----------------------")
                print(f"CPU Usage: {cpu_usage}%")
                print(f"RAM Usage: {ram_usage}%")
                print(f"Available RAM: {available_ram:.2f} MB / {total_ram:.2f} MB")

                time.sleep(self.interval)
        except KeyboardInterrupt:
            print("\n[INFO] Live monitoring stopped by user.")
