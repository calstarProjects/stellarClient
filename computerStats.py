import keyboard
import pyautogui
import time
import psutil
import datetime
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5 import QtCore


class compStatsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.loadUI()
        self.settings()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.periodic)
        self.timer.start(1 * 1000)

    def loadUI(self):
        self.installEventFilter(self)
        self.title = QLabel('Stellar Client')
        self.subtitle = QLabel('Your app for everything')
        self.statsLabel = QLabel('Stats')
        self.warning = QLabel("WARNING: This program WILL lag your computer, you may need to end it's task/use alt+4")
        self.stats = QLabel('')
        self.title.setFont(QFont('Castellar', 45))
        self.subtitle.setFont(QFont('Castellar', 25))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.statsLabel.setFont(QFont('Castellar', 20, 100))
        self.statsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.warning.setStyleSheet('color: red;')
        self.warning.setFont(QFont('Bahnschrift', 15, 200))
        self.warning.setAlignment(QtCore.Qt.AlignCenter)

        self.master = QBoxLayout(2)
        r1 = QBoxLayout(1)
        r2 = QBoxLayout(1)
        r3 = QBoxLayout(1)
        r4 = QBoxLayout(2)

        r1.addWidget(self.title)
        r2.addWidget(self.subtitle)
        r3.addWidget(self.statsLabel)
        r4.addWidget(self.warning)
        r4.addWidget(self.stats)

        self.master.addLayout(r1, 20)
        self.master.addLayout(r2, 10)
        self.master.addLayout(r3, 20)
        self.master.addLayout(r4, 50)

        self.setLayout(self.master)
    
    def settings(self):
        self.setWindowTitle('Stellar Client Computer Stats')

    def eventFilter(self, obj, event):
        """Input from the user with keypresses, called automatically"""

        # keypresses
        if obj == self and event.type() == QtCore.QEvent.KeyPress:
            # esc
            if event.key() in (QtCore.Qt.Key_Escape, QtCore.Qt.Key_Alt):
                if not (event.modifiers()):
                    # run the send message bit
                    self.destroy(True)
                    return True
        return super().eventFilter(obj, event)

    def periodic(self):
        startTime = time.time() * 100
        text = ''
        text += '-------Screen Stats-------\n'
        text += f'Screen Dimentions: {pyautogui.size()}\n'

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
            text += f'  PID: {proc['pid']}, Name: {proc['name']}, User: {proc['username']}, CPU: {proc['cpu_percent']:.2f}%, Memory: {proc['memory_info'].rss / (1024**2):.2f} MB\n'

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
        text += f'Time for cycle (in ms): {(time.time() * 100)-startTime}'

        self.stats.setText(text)
    
    def closeEvent(self, event):
        print("Window is closing. Terminating managed processes...")
        self.timer.stop() 
        print("QTimer stopped.")

        event.accept()



# if __name__ in "__main__":
#     app = QApplication([])
#     compStats = compStatsWidget()
#     compStats.show()
#     app.exec_()