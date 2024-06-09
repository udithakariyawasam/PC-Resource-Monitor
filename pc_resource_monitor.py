import psutil
import time

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

def monitor_resources():
    print("Monitoring PC Resources (Press Ctrl+C to stop)")
    print("{:<10} {:<10} {:<10}".format("CPU (%)", "Memory (%)", "Disk (%)"))
    try:
        while True:
            cpu_usage = get_cpu_usage()
            memory_usage = get_memory_usage()
            disk_usage = get_disk_usage()
            print("{:<10} {:<10} {:<10}".format(cpu_usage, memory_usage, disk_usage))
            time.sleep(1)  # Update every second
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    monitor_resources()
