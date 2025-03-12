# main.py
from system_monitoring_static import StaticSystemMonitor
from system_live_monitoring import LiveMonitor
from log_processor_new import LogMonitor
import threading

def main():
    """Initialize and start system monitoring."""
    print("[INFO] Starting System Monitoring Dashboard...\n")

    # Initialize monitors
    static_monitor = StaticSystemMonitor()
    live_monitor = LiveMonitor(interval=1)
    log_monitor = LogMonitor(log_duration="10m")

    # Display static system information
    static_monitor.display_system_info()

    # Run live system monitoring and log monitoring in separate threads
    live_thread = threading.Thread(target=live_monitor.monitor)
    log_thread = threading.Thread(target=log_monitor.start_periodic_logging, args=(10,))

    live_thread.start()
    log_thread.start()

    live_thread.join()
    log_thread.join()

if __name__ == "__main__":
    main()
