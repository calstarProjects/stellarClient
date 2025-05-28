import pyautogui
import threading
# from keylogger import keyLog, keyLogPrint
# from macros import runMacroChoice
# from encoder import encode, decode
# from gameOne import initGameOne
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5 import QtCore


screenwidth, screenlength = pyautogui.size()

class gameWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.loadUi()
        self.settings()
        self.buttonEvents()

    def loadUi(self):
        self.title = QLabel('Stellar Client')
        self.subtitle = QLabel('Your app for everything\n')
        self.gamesLabel = QLabel('Games')
        self.gameOneButton = QPushButton('Bullet hell rougelike')
        self.gameTwoButton = QPushButton('Games')
        self.title.setFont(QFont('Castellar', 25))
        self.subtitle.setFont(QFont('Castellar', 15))
        self.gamesLabel.setFont(QFont('Castellar', 20, 100))
        self.gameOneButton.setFont(QFont('Castellar', 15))
        self.gameTwoButton.setFont(QFont('Castellar', 15))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.gamesLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.master = QBoxLayout(2)
        r1 = QBoxLayout(1)
        r2 = QBoxLayout(1)
        r3 = QBoxLayout(1)
        r4 = QBoxLayout(1)

        r1.addWidget(self.title)
        r2.addWidget(self.subtitle)
        r3.addWidget(self.gamesLabel)
        r4.addWidget(self.gameTwoButton)
        r4.addWidget(self.gameOneButton)

        self.master.addLayout(r1, 20)
        self.master.addLayout(r2, 10)
        self.master.addLayout(r3, 20)
        self.master.addLayout(r4, 50)

        self.setLayout(self.master)
    
    def settings(self):
        self.setWindowTitle('Stellar Client Games')
    
    def buttonEvents(self):
        self.gameOneButton.clicked.connect(self.gameOneRun)

    def gameOneRun(self):
        from gameOne import initGameOne
        initGameOne()
        self.refresh()

    def refresh(self):
        """Refresh the widget state after game completion."""
        # clear old layout
        old_layout = self.layout()
        if old_layout is not None:
            QWidget().setLayout(old_layout)  # detach & let GC clean

        self.loadUi()
        self.settings()
        self.buttonEvents()

# if __name__ in "__main__":
#     gameApp = QApplication([])
#     game = gameWidget()
#     game.show()
#     gameApp.exec_()