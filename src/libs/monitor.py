import psutil


class Monitor:
    __STAT_KEYS = ['cpu', 'ram', 'disk']
    __FORMAT_STRING = \
        "CPU [{cpu_icon}] {cpu_usage}% | "\
        "RAM [{ram_icon}] {ram_usage}% | "\
        "DISK [{disk_icon}] {disk_usage}%"
    STATUS_OK = (30, "🟢")
    STATUS_WARN = (50, "🟡")
    STATUS_ALARM = (70, "🟠")
    STATUS_CRITICAL = (95, "🔴")

    def __init__(self):
        self.cpu = None
        self.ram = None
        self.disk = None

    def format(self, fmt=None):
        self.__FORMAT_STRING = fmt if fmt else self.__FORMAT_STRING

    @property
    def get_format_string(self):
        return self.__FORMAT_STRING

    @property
    def cpu_usage(self):
        return psutil.cpu_percent()

    @property
    def ram_usage(self):
        return psutil.virtual_memory().percent

    @property
    def disk_usage(self):
        return psutil.disk_usage("/").percent

    def select_icon(self, percent):
        ok_threshold, ok_icon = self.STATUS_OK
        warn_threshold, warn_icon = self.STATUS_WARN
        alarm_threshold, alarm_icon = self.STATUS_ALARM
        critical_threshold, critical_icon = self.STATUS_CRITICAL

        if percent <= ok_threshold:
            return ok_icon
        if percent > ok_threshold and percent <= warn_threshold:
            return warn_icon
        if percent > warn_threshold and percent <= alarm_threshold:
            return alarm_icon
        if percent > critical_threshold:
            return critical_icon
