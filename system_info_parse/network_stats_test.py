import psutil  

def get_network_usage():
    """Standalone function to fetch network I/O stats."""
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

if __name__ == "__main__":
    network_stats = get_network_usage()

    print("Network Usage Statistics:")
    print(f"Bytes Sent: {network_stats['bytes_sent'] / (1024 ** 2):.2f} MB")
    print(f"Bytes Received: {network_stats['bytes_received'] / (1024 ** 2):.2f} MB")
    print(f"Packets Sent: {network_stats['packets_sent']}")
    print(f"Packets Received: {network_stats['packets_recv']}")
    print(f"Input Errors: {network_stats['errin']}")
    print(f"Output Errors: {network_stats['errout']}")
    print(f"Dropped Input Packets: {network_stats['dropin']}")
    print(f"Dropped Output Packets: {network_stats['dropout']}")
