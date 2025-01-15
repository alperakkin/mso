from libs.monitor import Monitor

REFRESH_TICK = 30  # seconds

monitor = Monitor()

monitor.STATUS_OK = (30, "🟢")
monitor.STATUS_WARN = (55, "🟡")
monitor.STATUS_ALARM = (75, "🟠")
monitor.STATUS_CRITICAL = (95, "🔴")


monitor.format("CPU [{cpu_icon}] {cpu_usage} | "
               "RAM [{ram_icon}] {ram_usage} | "
               "DISK [{disk_icon}] {disk_usage} ")
