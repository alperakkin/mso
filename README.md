# mso

## DEFINITION
Tracks your Mac's system resources  with this Python-powered menu bar application, providing real-time insights into CPU, memory, and disk.

![](https://github.com/alperakkin/mso/blob/main/resources/status_bar.png)



## QUICK START

### Configuration

The configuration options are defined in the file located at `src/config.py`.

You can customize the application's behavior and appearance using the following settings:

```python
# config.py

REFRESH_TICK = 5  # seconds

monitor = Monitor()

monitor.STATUS_OK = (30, "🟢")
monitor.STATUS_WARN = (55, "🟡")
monitor.STATUS_ALARM = (75, "🟠")
monitor.STATUS_CRITICAL = (95, "🔴")


monitor.format("{cpu_icon} CPU:  {cpu_usage}% | "
               "{ram_icon} RAM:  {ram_usage}% | "
               "{disk_icon} DISK: {disk_usage}% ")

```


- **`REFRESH_TICK`**:
  Determines the update frequency of the system resource metrics displayed in the menu bar.
  - Default: `5` seconds

- **Status Thresholds**:
  Define the thresholds for system resource usage levels and their corresponding status icons:


  - **`STATUS_OK`**: Usage below `30%`, represented by the 🟢 icon.
  - **`STATUS_WARN`**: Usage between `30%` and `55%`, represented by the 🟡 icon.
  - **`STATUS_ALARM`**: Usage between `55%` and `75%`, represented by the 🟠 icon.
  - **`STATUS_CRITICAL`**: Usage above `75%`, represented by the 🔴 icon.

  You can replace these icons with any emoji or custom icon of your choice. For example:

- **Icon Customization**:
    You can modify the icons for CPU, RAM, and disk usage by adjusting the predefined status thresholds (like STATUS_OK, STATUS_WARN, etc.). For example:

```python
monitor.STATUS_OK = (30, "🚀")  # Change CPU OK status icon to rocket
monitor.STATUS_WARN = (55, "⚡️")  # Change CPU warning status icon to high voltage

```


- **Predefined Values**:
{cpu_icon}: The icon representing CPU usage (e.g., 🟢, 🟡, 🟠, 🔴).
{cpu_usage}: The actual CPU usage as a percentage (e.g., 35%).
{ram_icon}: The icon representing RAM usage (similar to CPU icons).
{ram_usage}: The actual RAM usage as a percentage.
{disk_icon}: The icon representing disk usage.
{disk_usage}: The actual disk usage as a percentage.

- **Display Format**:
  Customize the display of the metrics in the menu bar using the `format()` method. By default:
  ```python
  "{cpu_icon} CPU:  {cpu_usage}% | {ram_icon} RAM:  {ram_usage}% | {disk_icon} DISK: {disk_usage}% "
  ```

![](https://github.com/alperakkin/mso/blob/main/resources/colors.png)

  Another example:
  ```python
  "{cpu_icon} CPU:  {cpu_usage}% |  RAM:  {ram_usage}% | System Monitor "
  ```
![](https://github.com/alperakkin/mso/blob/main/resources/another-example.png)


### Running the Application in the Background (nohup)

You can run the application in the background, independent of your terminal session, using `nohup`. This is useful for keeping the application running even after you close the terminal. Here's how to do it:

1. Open a terminal and navigate to your project directory.

2. Run the application using `nohup` and send the output to a file (e.g., `output.log`):
   ```bash
   nohup python3 src/main.py > /dev/null 2>&1 &
   ```
3. The application now runs in the background, and all output is discarded.

4. To stop the application, find its process ID (PID) using the ps command:
```bash
ps aux | grep python
```

By using nohup, the application continues to run even if you close the terminal or disconnect from the system, and no output will be saved or displayed.

