import rumps
from config import REFRESH_TICK, monitor


class MenubarApp(rumps.App):
    def __init__(self, title):
        super(MenubarApp, self).__init__(title)
        self.monitor = monitor
        self.timer = rumps.Timer(self.update_stats, REFRESH_TICK)
        self.timer.start()

    def update_stats(self, _):
        self.title = self.monitor.get_format_string.format(
            cpu_icon=self.monitor.select_icon(self.monitor.cpu_usage),
            ram_icon=self.monitor.select_icon(self.monitor.ram_usage),
            disk_icon=self.monitor.select_icon(self.monitor.disk_usage),
            cpu_usage=self.monitor.cpu_usage,
            ram_usage=self.monitor.ram_usage,
            disk_usage=self.monitor.disk_usage,
        )
