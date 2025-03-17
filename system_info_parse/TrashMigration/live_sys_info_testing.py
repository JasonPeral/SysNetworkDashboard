import psutil
import time

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

        time.sleep(1)  # Refresh every 1 second

except KeyboardInterrupt:
    print("\nExiting...")
