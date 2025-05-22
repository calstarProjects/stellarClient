from MainUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import keyboard
import threading
import pyautogui
import time

class messagingUIAPI(Ui_MainWindow):
    def __init__(self, mainWindow):
        super().__init__()
        self.setupUi(mainWindow)
        self.SendButton.clicked.connect(self.getMessageBox)
        self.messages = []
        self.appRunning = 1
    
    def getMessageBox(self):
        message = self.MessageArea.toPlainText()
        self.MessageArea.setPlainText('')
        self.messages.append(message)
    
    def feedMessageData(self):
        while self.appRunning == 1:
            if keyboard.is_pressed('enter'):
                self.getMessageBox()
                time.sleep(0.01)
            
                pyautogui.press('backspace')


if __name__ in "__main__":
    app = QtWidgets.QApplication([])
    mainWindow = QtWidgets.QMainWindow()
    window = messagingUIAPI(mainWindow)
    messagesThread = threading.Thread(target=window.feedMessageData)
    messagesThread.start()
    mainWindow.show()
    app.exec_()
    pyautogui.press('enter')

    window.appRunning = 0
    print(window.messages)