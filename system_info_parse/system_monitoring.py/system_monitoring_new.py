#This class will handle real time CPU and RAM (system) stat monitoring
import psutil
import cpuinfo
import platform

class StaticSystemMonitoring:

    def __init__(self):
        # """Initialize and fetch system details."""
        self.sys_architecture = platform.architecture()
        self.sys_pc_name = platform.node()
        self.sys_os = platform.platform()
        self.sys_basic_cpu = platform.processor()
        self.sys_cpuinfo = cpuinfo.get_cpu_info()
        self.sys_cpu_bits = self.sys_cpuinfo['bits']
        self.sys_total_ram = psutil.virtual_memory().total / 1024 / 1024 / 1024  # Convert to GB

    def get_system_info(self):
        # """Return system information as a dictionary."""
        return {
            "Architecture": self.sys_architecture,
            "Computer Name": self.sys_pc_name,
            "OS": self.sys_os,
            "Processor": self.sys_basic_cpu,
            "Full CPU Info": self.sys_cpuinfo['brand_raw'],
            "CPU Bits": self.sys_cpu_bits,
            "Total RAM (GB)": round(self.sys_total_ram, 2)
        }

    def display_system_info(self):
        # """Prints static system information."""
        info = self.get_system_info()
        print("\n=== Static System Information ===")
        for key, value in info.items():
            print(f"{key}: {value}")