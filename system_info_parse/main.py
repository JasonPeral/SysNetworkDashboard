import platform
import psutil
import cpuinfo
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

except KeyboardInterrupt:
    print("\nExiting...")

# Dont need this section anymore as we will have live info on CPU and RAM usage
#ram info 
# print(f"Total RAM: {sys_total_ram}GB")
# #Cpu usuge 
# print(f"CPU usage: {sys_cpu_usage}")