import tkinter.messagebox
import tkinter.simpledialog
import keyboard
import pyautogui
import math
import time
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
import tkinter

def circle(itr: int):
    pyautogui.move(math.cos(itr/3)*50, math.sin(itr/3)*50)
def autoClick():
    pyautogui.click()
def autoKey(key: str):
    keyboard.press_and_release(key)
def holdKey(key: str, stop: bool = False):
    if not stop:
        if not keyboard.is_pressed(key):
            keyboard.press(key)
    else:
        keyboard.release(key)
        
def getInfo(chosenMacro):
    match chosenMacro:
        case 'autoClick':
            pass
        case 'circle':
            pass
        case 'autoKey':
            tkinter.messagebox.askokcancel('Key Choice', 'After closing this box, press the key you with to autoKey')
            key = keyboard.read_key()
            pyautogui.press('backspace')
            tkinter.messagebox.askokcancel('Key Choice', 'You have chosen ' + key + ' as your key')
        case 'holdKey':
            tkinter.messagebox.askokcancel('Key Choice', 'After closing this box, press the key you with to holdKey')
            key = keyboard.read_key()
            pyautogui.press('backspace')
            tkinter.messagebox.askokcancel('Key Choice', 'You have chosen ' + key + ' as your key')

def runMacro(chosenMacro: str, key: str = None):
    desiredMins = None
    while desiredMins is None:
        desiredMins = int(tkinter.simpledialog.askinteger('Time Input', 'How many minutes? (under 60)', minvalue = 1, maxvalue = 59))
    tkinter.messagebox.showinfo('Ready', 'After closing this box, press the tab key to start (also note that pressing ctrl will pause the macro and esc will end it)')
    keyboard.wait('tab')
    startSecs = time.localtime().tm_sec
    desiredEndTime = time.localtime().tm_min + desiredMins % 60
    startTime = time.ctime(time.time())
    print('calced')
    
    iteration = 0
    while not keyboard.is_pressed('esc'):
        if keyboard.is_pressed('ctrl'):
            tkinter.messagebox.showwarning('WARNING', 'WARNING PAUSING FOR TOO LONG CAN GO PAST YOUR TIME GOAL AND RUN FOREVER \nHOLD SHIFT AND THEN CTRL TO FORCE QUIT \npress x to continue')
            keyboard.wait('x')
            pyautogui.press('backspace')
        if chosenMacro == 'holdKey':
            pyautogui.keyDown(key)
        print('start')
        while (not keyboard.is_pressed('ctrl')) and ((time.localtime().tm_sec != startSecs)) and (not keyboard.is_pressed('esc')):
            match chosenMacro:
                case 'autoClick':
                    autoClick()
                case 'circle':
                    circle(iteration)
                case 'autoKey':
                    autoKey(key)
                case 'holdKey':
                    holdKey(key)
            iteration += 1
        if chosenMacro == 'holdKey':
            holdKey(key, True)
        print('looped')
        if ((time.localtime().tm_min == desiredEndTime) and (time.localtime().tm_sec == startSecs)):
            print('should be done')
            break
    tkinter.messagebox.showinfo('Task Finished', ('Desired Minutes = ' + str(desiredMins) + ', Start Seconds = ' + str(startSecs) + ', Desired End Time = ' + str(desiredEndTime) + ', Start Time ' + str(startTime) + ', End Time ' + str(time.ctime(time.time()))))
    print('boxed')

class macroWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.loadUI()
        self.buttons()

    def loadUI(self):
        self.title = QLabel('Stellar Client')
        self.subtitle = QLabel('Your app for everything')
        self.macrosLabel = QLabel('Macros')
        self.autoClickButton = QPushButton('Autoclick')
        self.circleButton = QPushButton('Circle')
        self.autoKeyButton = QPushButton('Autokey')
        self.holdKeyButton = QPushButton('Hold Key')
        self.title.setFont(QFont('Castellar', 45))
        self.subtitle.setFont(QFont('Castellar', 15))
        self.macrosLabel.setFont(QFont('Castellar', 20, 100))
        self.autoClickButton.setFont(QFont('Castellar', 15))
        self.circleButton.setFont(QFont('Castellar', 15))
        self.autoKeyButton.setFont(QFont('Castellar', 15))
        self.holdKeyButton.setFont(QFont('Castellar', 15))

        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.macrosLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.master = QBoxLayout(2)

        r1 = QBoxLayout(1)
        r2 = QBoxLayout(1)
        r3 = QBoxLayout(1)
        r4 = QBoxLayout(1)

        r1.addWidget(self.title)
        r2.addWidget(self.subtitle)
        r3.addWidget(self.macrosLabel)
        r4.addWidget(self.autoClickButton)
        r4.addWidget(self.circleButton)
        r4.addWidget(self.autoKeyButton)
        r4.addWidget(self.holdKeyButton)

        self.master.addLayout(r1, 20)
        self.master.addLayout(r2, 10)
        self.master.addLayout(r3, 20)
        self.master.addLayout(r4, 50)

        self.setLayout(self.master)

    def buttons(self):
        self.autoClickButton.clicked.connect(self.runAutoClick)
        self.circleButton.clicked.connect(self.runCircle)
        self.autoKeyButton.clicked.connect(self.runAutoKey)
        self.holdKeyButton.clicked.connect(self.runHoldKey)

    def runAutoClick(self):
        getInfo('autoClick')
        runMacro('autoClick')
    def runCircle(self):
        getInfo('circle')
        runMacro('circle')
    def runAutoKey(self):
        getInfo('autoKey')
        runMacro('autoKey')
    def runHoldKey(self):
        getInfo('holdKey')
        runMacro('holdKey')