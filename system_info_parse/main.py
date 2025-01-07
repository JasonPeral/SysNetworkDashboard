import platform
import psutil
import cpuinfo

#information on the architecture of our machine 
print(f"Architecture: {platform.architecture()}")
print(f"Computer Name: {platform.node()}")
print(f"OS: {platform.platform}")

#less detailed info on cpu
print(f"Processor: {platform.processor()}")

my_cpuinfo = cpuinfo.get_cpu_info();
print(f"Full CPU info: {my_cpuinfo['brand_raw']}")

#Apple does not display cpu hz information. Opting to run bits key
print(f"Bits: {my_cpuinfo['bits']}")

#To see what keys are available to parse in .get_cpu_info
# print(my_cpuinfo.keys())

#ram info 
print(f"Total RAM: {psutil.virtual_memory().total/1024/1024/1024}GB")
#Cpu usuge 
print(f"CPU usage: {psutil.cpu_percent(5)}")