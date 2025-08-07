# import keyboard
import pyautogui
import time
import psutil
import datetime
import tkinter as tk
from SCWindow import SCWindow, runIfLocal


class computerStatsWindow(SCWindow):
    def __init__(self, parent=None, title='Stellar Client Computer Stats', geometry="800x1200"):
        super().__init__(parent, title, geometry)

        self.size = pyautogui.size()
        self.timerJob = None
        self.isRunning = None

    def show(self):
        if self.window is not None and self.window.winfo_exists():
            self.window.lift()
            return
        
        self.isRunning = True
        self.createWindow()

    def createCustomWidgets(self, mainFrame):
        statsHeaderFrame = tk.Frame(mainFrame, bg='white')
        statsHeaderFrame.pack(fill='x', pady=(0, 10))

        self.statsHeader = tk.Label(
            statsHeaderFrame,
            text='Computer Stats',
            font=(
                'Castellar',
                16,
                'bold'
            ),
            bg='white',
            fg='black'
        )
        self.statsHeader.pack()


        contentFrame = tk.Frame(mainFrame, bg='white')
        contentFrame.pack(fill='x', pady=(0, 10))

        self.warningLabel = tk.Label(
            contentFrame,
            text="WARNING: This program WILL lag your computer, you may need to end it's task/use alt+4",
            font=(
                'Castellar',
                12,
                'bold'
            ),
            bg='white',
            fg='red',
            wraplength=700
        )
        self.warningLabel.pack()

        statsFrame = tk.Frame(contentFrame)
        statsFrame.pack(fill='both', expand=True)

        scrollbar = tk.Scrollbar(statsFrame)
        scrollbar.pack(side='right', fill='y')

        self.statsText = tk.Text(
            statsFrame,
            font=(
                'Cascadia Code',
                10,
            ),
            fg='gray',
            bg='white',
            yscrollcommand=scrollbar.set
        )
        self.statsText.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=self.statsText.yview)

        instructions = tk.Label(
            contentFrame,
            font=(
                'Cascadia Code',
                10,
            ),
            bg='gray',
            fg='black'
        )
        instructions.pack(pady=(10, 0))
        
    def periodic(self):
        if not self.isRunning or not self.window or not self.window.winfo_exists():
            return
        
        startTime = time.time() * 1000
        text = ''
        text += '-------Screen Stats-------\n'
        text += f'Screen Dimentions: {self.size}\n'

        text += '-------CPU-------\n'
        try:
            text += f'CPU Usage: {psutil.cpu_percent(None)}\n'
            text += f'CPU Usage per CPU: {psutil.cpu_percent(None, True)}\n'
        except:
            text += 'CPU info not avalible, '

        text += '-------RAM-------\n'
        memoryInfo = psutil.virtual_memory()
        text += f'Total RAM: {memoryInfo.total / (1024**3):.2f} GB\n'
        text += f'Used RAM: {memoryInfo.used / (1024**3):.2f} GB\n'
        text += f'Free RAM: {memoryInfo.free / (1024**3):.2f} GB\n'
        text += f'Available RAM: {memoryInfo.available / (1024**3):.2f} GB\n'
        text += f'Memory Usage Percentage: {memoryInfo.percent}%\n'

        text += '-------NETWORK-------\n'
        net_io = psutil.net_io_counters()
        text += f'Total Bytes Sent: {net_io.bytes_sent / (1024**2):.2f} MB\n'
        text += f'Total Bytes Received: {net_io.bytes_recv / (1024**2):.2f} MB\n'
        text += f'Total Packets Sent: {net_io.packets_sent}\n'
        text += f'Total Packets Received: {net_io.packets_recv}\n'

        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_info']):
            try:
                processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        processes.sort(key=lambda x: x['cpu_percent'], reverse=True)
        text += '-------PROCESSES-------\n'
        for proc in processes[:5]:
            text += f"  PID: {proc['pid']}, Name: {proc['name']}, User: {proc['username']}, CPU: {proc['cpu_percent']:.2f}%, Memory: {proc['memory_info'].rss / (1024**2):.2f} MB\n"

        text += '-------UPTIME-------\n'
        boot_time_timestamp = psutil.boot_time()
        boot_time_datetime = datetime.datetime.fromtimestamp(boot_time_timestamp)
        text += f'Boot Time: {boot_time_datetime.strftime('%Y-%m-%d %H:%M:%S')}\n'

        current_time = datetime.datetime.now()
        uptime = current_time - boot_time_datetime
        text += f'System Uptime: {uptime}\n'

        text += '-------TEMP-------\n'
        avgTemp = 0
        try:
            temps = psutil.sensors_temperatures()
            count = 0
            if temps:
                for name, entries in temps.items():
                    for entry in entries:
                        avgTemp += entry.current
                        count += 1
                if count > 0:
                    avgTemp /= count
                text += f'Avg temp: {avgTemp}\n'
            else:
                text += 'Temperature information not available on this system\n'
        except AttributeError:
            text += 'Temperature information not available on this system (requires `psutil` 5.x+ and supported hardware/OS)\n'

        text += '-------LAG-------\n'
        text += f'Time for cycle (in ms): {(time.time() * 1000)-startTime}'

        self.statsText.config(state='normal')
        self.statsText.delete('1.0', tk.END)
        self.statsText.insert('1.0', text)
        self.statsText.config(state='disabled')

        if self.isRunning and self.window and self.window.winfo_exists():
            self.timerJob = self.window.after(1000, self.periodic)
    
    def stopMonitor(self):
        self.isRunning = False
        if self.timerJob and self.window:
            self.window.after_cancel(self.timerJob)
            self.timerJob = None

        
runIfLocal(computerStatsWindow, __name__)