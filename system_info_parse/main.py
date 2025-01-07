import platform
import psutil
import cpuinfo


#moving hardcoded dependency calls into variables for later use with dashboard
sys_architecture = platform.architecture()
sys_pc_name = platform.node()
sys_os = platform.platform
sys_basic_cpu = platform.processor()
sys_cpuinfo = cpuinfo.get_cpu_info()
sys_cpu_bits = sys_cpuinfo['bits']
sys_total_ram = psutil.virtual_memory().total/1024/1024/1024
sys_cpu_usage = psutil.cpu_percent(5)

#information on the architecture of our machine 
print(f"Architecture: {sys_architecture}")
print(f"Computer Name: {sys_pc_name}")
print(f"OS: {sys_os}")

#less detailed info on cpu
print(f"Processor: {sys_basic_cpu}")

print(f"Full CPU info: {sys_cpuinfo['brand_raw']}")

#Apple does not display cpu hz information. Opting to run bits key
print(f"Bits: {sys_cpu_bits}")

#To see what keys are available to parse in .get_cpu_info
# print(my_cpuinfo.keys())

#ram info 
print(f"Total RAM: {sys_total_ram}GB")
#Cpu usuge 
print(f"CPU usage: {sys_cpu_usage}")