from libs.monitor import Monitor

REFRESH_TICK = 5  # seconds

monitor = Monitor()

monitor.STATUS_OK = (30, "🟢")
monitor.STATUS_WARN = (55, "🟡")
monitor.STATUS_ALARM = (75, "🟠")
monitor.STATUS_CRITICAL = (95, "🔴")


monitor.format("{cpu_icon} CPU:  {cpu_usage}% | "
               "{ram_icon} RAM:  {ram_usage}% | "
               "{disk_icon} DISK: {disk_usage}% ")
