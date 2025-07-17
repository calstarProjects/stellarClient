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
from keyboardScreen import keyboardWindow
from encoder import encodingWindow
from gameScreen import gameScreen
import tkinter as tk

screenwidth, screenlength = pyautogui.size()

class stellarClientWindow:
    def __init__(self, parent = None, title = 'Stellar Client Homepage', geometry = '800x600'):
        # TODO: macro button, encode button, stat button, macroButton
        self.parent = parent
        self.window = None
        self.title = title
        self.geometry = geometry

        self.keyboardWindow = None
        self.gamesWindow = None
        self.WIPWindow = None
    def show(self):
        if self.window is not None and self.window.winfo_exists():
            self.window.lift()
            return
        
        self.createWindow()
    
    def createWindow(self):
        if self.parent:
            self.window = tk.Toplevel(self.parent)
        else:
            self.window = tk.Tk()
        
        self.window.title(self.title)
        self.window.geometry(self.geometry)
        self.window.protocol('WM_DELETE_WINDOW', self.onClose)
        self.window.deiconify()
        self.window.iconbitmap(r'util\stellarClientLogo.ico')
        icon = tk.PhotoImage(file=r'util\stellarClientLogo.png')
        self.window.iconphoto(True, icon)

        self.createWidgets()

    def createWidgets(self):
        mainFrame = tk.Frame(self.window, bg='white')
        mainFrame.pack(fill='both', expand=True, padx=10, pady=10)

        titleFrame = tk.Frame(mainFrame, bg='white')
        titleFrame.pack(fill='x', pady=(0, 10))

        self.titleLabel = tk.Label(
            titleFrame,
            text='Stellar Client',
            font=(
                'Castellar', 
                23, 
                'bold'
            ),
            bg='white',
            fg='black'
        )
        self.titleLabel.pack()


        subtitleFrame = tk.Frame(mainFrame, bg='white')
        subtitleFrame.pack(fill='x', pady=(0, 10))

        self.subtitleLabel = tk.Label(
            subtitleFrame,
            text='Your app for everything',
            font=(
                'Castellar', 
                18, 
                'bold'
            ),
            bg='white',
            fg='black'
        )
        self.subtitleLabel.pack()

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

    def onClose(self):
        if self.window:
            self.window.destroy()
            self.window = None


if __name__ in "__main__":
    mainWindow = stellarClientWindow()
    mainWindow.show()
    mainWindow.window.mainloop()