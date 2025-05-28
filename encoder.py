"""Encoding Function for the Stellar Client app
Basic key based encryption, uses tkinter to get input for the key and string

Returns a print statment and the encrypted/decrypted value

# Args:
    ##  Optional:
    ### - key -- The value that is used for encryption and decryption
    ### - encrypted/decrypted -- The acutal string to be modified

# Returns:
    ### - Encrypted/Decrypted
"""

import tkinter
import tkinter.messagebox
import tkinter.simpledialog
import pyperclip
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5 import QtCore


def encode(key: int = None, decrypted: str = None):    
    while key == None:
        key = tkinter.simpledialog.askinteger('Encryption Key', 'Please input your encryption key')
    while decrypted == None:
        decrypted = tkinter.simpledialog.askstring('Encryption String', 'Please input the string to encode')
    encrypted = ''

    for i in range(len(decrypted)):
        encrypted += chr(ord(decrypted[i]) - int(str(key)[i % len(str(key))]))

    tkinter.messagebox.showinfo('Encrypted', encrypted + ' will be copied to you clipboard')
    print(encrypted)
    pyperclip.copy(encrypted)
    return(encrypted)

def decode(key: int = None, encrypted: str = None):
    ### TODO ###
    # make it so the dialogues are pyqt aligned
    while key == None:
        key = tkinter.simpledialog.askinteger('Decryption Key', 'Please input your decryption key')
    while encrypted == None:
        encrypted = tkinter.simpledialog.askstring('Decryption String', 'Please input the string to decode')
    decrypted = ''

    for i in range(len(encrypted)):
        decrypted += chr(ord(encrypted[i]) + int(str(key)[i % len(str(key))]))

    tkinter.messagebox.showinfo('Decrypted', decrypted + ' will be copied to you clipboard')
    print(decrypted)
    pyperclip.copy(decrypted)
    return decrypted

class encodingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.loadUI()
        self.settings()
        self.buttonEvents()

    def loadUI(self):
        self.title = QLabel('Stellar Client')
        self.subtitle = QLabel('Your app for everything')
        self.encoderLabel = QLabel('Encoder/Decoder')
        self.encodeButton = QPushButton('encode')
        self.decodeButton = QPushButton('decode')
        self.title.setFont(QFont('Castellar', 45))
        self.subtitle.setFont(QFont('Castellar', 25))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.encoderLabel.setFont(QFont('Castellar', 20, 100))
        self.encoderLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.master = QBoxLayout(2)
        r1 = QBoxLayout(1)
        r2 = QBoxLayout(1)
        r3 = QBoxLayout(1)
        r4 = QBoxLayout(1)

        r1.addWidget(self.title)
        r2.addWidget(self.subtitle)
        r3.addWidget(self.encoderLabel)
        r4.addWidget(self.decodeButton)
        r4.addWidget(self.encodeButton)

        self.master.addLayout(r1, 20)
        self.master.addLayout(r2, 10)
        self.master.addLayout(r3, 20)
        self.master.addLayout(r4, 50)

        self.setLayout(self.master)
    
    def settings(self):
        self.setWindowTitle('Stellar Client')

    def buttonEvents(self):
        self.decodeButton.clicked.connect(self.decodeEvent)
        self.encodeButton.clicked.connect(self.encodeEvent)
    
    def decodeEvent(self):
        decode()
    
    def encodeEvent(self):
        encode()
    