import psutil

def get_network_usage(self):
    net_io = psutil.net_io_counters()
    return {
        "bytes_sent": net_io.bytes_sent,
        "bytes_received": net_io.bytes_recv,
        "packets_sent": net_io.packets_sent,
        "packets_recv": net_io.packets_recv,
        "errin": net_io.errin,
        "errout": net_io.errout,
        "dropin": net_io.dropin,
        "dropout": net_io.dropout
    }

network = self.get_network_usage()
# print(f"Network I/O: Sent: {network['bytes_sent'] / (1024 ** 2):.2f} MB | Received: {network['bytes_received'] / (1024 ** 2):.2f} MB")
# print(f"Packets: Sent: {network['packets_sent']}, Received: {network['packets_recv']}")
