import pyautogui
import threading
# from keylogger import keyLog, keyLogPrint
# from macros import runMacroChoice
# from encoder import encode, decode
# from gameOne import initGameOne
from macros import macroWidget
from encoder import encodingWidget
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5 import QtCore


screenwidth, screenlength = pyautogui.size()

class keyboardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.macroScreen = None
        self.encodeScreen = None
        self.loadUi()
        self.settings()
        self.buttonEvents()

    def loadUi(self):
        self.title = QLabel('Stellar Client')
        self.subtitle = QLabel('Your app for everything\n')
        self.keyboardLabel = QLabel('Keyboard Util')
        self.macrosButton = QPushButton('Macros')
        self.encodingButton = QPushButton('Encoding/Decoding')
        self.title.setFont(QFont('Castellar', 25))
        self.subtitle.setFont(QFont('Castellar', 15))
        self.keyboardLabel.setFont(QFont('Castellar', 20, 100))
        self.macrosButton.setFont(QFont('Castellar', 15))
        self.encodingButton.setFont(QFont('Castellar', 15))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.keyboardLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.master = QBoxLayout(2)
        r1 = QBoxLayout(1)
        r2 = QBoxLayout(1)
        r3 = QBoxLayout(1)
        r4 = QBoxLayout(1)

        r1.addWidget(self.title)
        r2.addWidget(self.subtitle)
        r3.addWidget(self.keyboardLabel)
        r4.addWidget(self.encodingButton)
        r4.addWidget(self.macrosButton)

        self.master.addLayout(r1, 20)
        self.master.addLayout(r2, 10)
        self.master.addLayout(r3, 20)
        self.master.addLayout(r4, 50)

        self.setLayout(self.master)
    
    def settings(self):
        self.setWindowTitle('Stellar Client Games')
    
    def buttonEvents(self):
        self.macrosButton.clicked.connect(self.macroButton)
        self.encodingButton.clicked.connect(self.encodeButton)

    def macroButton(self):
        if self.macroScreen == None:
            self.macroScreen = macroWidget()
        self.macroScreen.show()
    
    def encodeButton(self):
        if self.encodeScreen == None:
            self.macroScreen = encodingWidget()
        self.macroScreen.show()



# if __name__ in "__main__":
#     gameApp = QApplication([])
#     game = gameWidget()
#     game.show()
#     gameApp.exec_()