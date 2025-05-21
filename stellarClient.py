"""This is the main program that runs the Stellar Client

Functions: 

- Keyboard manipulation:
    - Autoclickers, other macros, keylogger if you want to?

- Games:
    - For now, just a rougelike game

In Progress:

- Messaging
- More Games    

"""


import sys
import pyautogui
from keylogger import keyLog, keyLogPrint
from macros import runMacroChoice
from encoder import encode, decode
from gameScreen import *
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5 import QtCore

screenwidth, screenlength = pyautogui.size()

class stellarClientWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.loadUi()
        self.settings()
        self.gamesWindow = None
        self.buttonEvents()

    def loadUi(self):
        self.title = QLabel('Stellar Client')
        self.subtitle = QLabel('Your app for everything')
        self.applicationsLabel = QLabel('Applications')
        self.keyboardUtilButton = QPushButton('Keyboard Util')
        self.gamesButton = QPushButton('Games')
        self.title.setFont(QFont('Castellar', 45))
        self.subtitle.setFont(QFont('Castellar', 25))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.applicationsLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.master = QBoxLayout(2)
        r1 = QBoxLayout(1)
        r2 = QBoxLayout(1)
        r3 = QBoxLayout(1)
        r4 = QBoxLayout(1)

        r1.addWidget(self.title)
        r2.addWidget(self.subtitle)
        r3.addWidget(self.applicationsLabel)
        r4.addWidget(self.gamesButton)
        r4.addWidget(self.keyboardUtilButton)

        self.master.addLayout(r1, 20)
        self.master.addLayout(r2, 10)
        self.master.addLayout(r3, 20)
        self.master.addLayout(r4, 50)

        self.setLayout(self.master)
    
    def settings(self):
        self.setWindowTitle('Stellar Client')

    def buttonEvents(self):
        self.gamesButton.clicked.connect(self.gameButton)
        self.keyboardUtilButton.clicked.connect(self.keyboardButton)
    
    def gameButton(self):
        if self.gamesWindow == None:
            self.gamesWindow = gameWidget()
        self.gamesWindow.show()

    def keyboardButton(self):
        pass


if __name__ in "__main__":
    app = QApplication([])
    main = stellarClientWidget()
    main.show()
    app.exec_()