"""This is the main program that runs the Stellar Client

Functions: 

- Keyboard manipulation:
    - Autoclickers, other macros, keylogger if you want to?

- Games:
    - For now, just a roguelike game

In Progress:

- Messaging
- More Games
"""


import sys
import pyautogui
from keyboardScreen import keyboardWindow
from encoder import encodingWindow
from gameScreen import gameScreen
from SCWindow import SCWindow, runIfLocal
import tkinter as tk

screenwidth, screenlength = pyautogui.size()

class stellarClientWindow(SCWindow):
    """The main window object for the Stellar Client Project
    
    Holds links to all other Stellar Client Apps"""
    def __init__(self, parent = None, title = 'Stellar Client Homepage', geometry = "800x600"):
        super().__init__(parent, title, geometry)

        self.keyboardWindow = None
        self.gamesWindow = None
        self.WIPWindow = None
    
    def createCustomWidgets(self, mainFrame):
        contentFrame= tk.Frame(mainFrame, bg='grey')
        contentFrame.pack(pady=10)

        self.keyboardButton = tk.Button(
            contentFrame,
            text='Keyboard Util',
            font=(
                'Castellar',
                14
            ),
            bg='light grey',
            fg='black',
            command=self.keyboard
        )
        self.keyboardButton.pack(padx=10, pady=10, side='left', fill='both', expand=False)

        self.gamesButton = tk.Button(
            contentFrame,
            text='Games',
            font=(
                'Castellar',
                14
            ),
            bg='light grey',
            fg='black',
            command=self.games
        )
        self.gamesButton.pack(padx=10, pady=10, side='left', fill='both', expand=False)

        self.WIPButton = tk.Button(
            contentFrame,
            text='WIP',
            font=(
                'Castellar',
                14
            ),
            bg='light grey',
            fg='black',
            command=self.wip
        )
        self.WIPButton.pack(padx=10, pady=10, side='left', fill='both', expand=False)
    
    def keyboard(self):
        if self.keyboardWindow == None:
            self.keyboardWindow = keyboardWindow(self.window)
        self.keyboardWindow.show()

    def games(self):
        if self.gamesWindow == None:
            self.gamesWindow = gameScreen(self.window)
        self.gamesWindow.show()

    def wip(self):
        if self.WIPButton == None:
            pass # self.keyboardWindow = keyboardWindow(self.window)
        # self.keyboardWindow.show()

runIfLocal(stellarClientWindow, __name__)