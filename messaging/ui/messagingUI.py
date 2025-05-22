from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QBoxLayout, QWidget, QTextEdit
from PyQt5.QtGui import QFont
from PyQt5 import QtCore

class messageUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.settings()

    def initUI(self):
        self.title = QLabel('Stellar Client')
        self.subtitle = QLabel('Your app for everything')
        self.chatLabel = QLabel('Messaging')
        self.messageLog = QLabel('None')
        self.inputBox = QTextEdit('Write Text Here')
        self.title.setFont(QFont('Castellar', 45))
        self.subtitle.setFont(QFont('Castellar', 25))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.chatLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.master = QBoxLayout(2)
        r1 = QBoxLayout(1)
        r2 = QBoxLayout(1)
        r3 = QBoxLayout(1)
        r4 = QBoxLayout(1)

        r1.addWidget(self.title)
        r2.addWidget(self.subtitle)
        r3.addWidget(self.chatLabel)
        r4.addWidget(self.inputBox)
        r4.addWidget(self.messageLog)

        self.master.addLayout(r1, 20)
        self.master.addLayout(r2, 10)
        self.master.addLayout(r3, 20)
        self.master.addLayout(r4, 50)

        self.setLayout(self.master)
    
    def settings(self):
        self.setWindowTitle('Stellar Client')

    def getMessageBoxText(self):
        message = self.inputBox.toPlainText()
        self.inputBox.setPlainText('')
        return message
    
    def setMessagesText(self, text):
        self.messageLog.setText(text)
        return self.messageLog.text()

if __name__ in "__main__":
    app = QApplication([])
    messageWidget = messageUI()
    messageWidget.show()
    app.exec_()