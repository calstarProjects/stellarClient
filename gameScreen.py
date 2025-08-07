import pyautogui
import threading
import tkinter as tk

from SCWindow import SCWindow, runIfLocal

screenwidth, screenlength = pyautogui.size()

class gameScreen(SCWindow):
    def __init__(self, parent = None, title = 'Stellar Client Games', geometry = '800x600'):
        super().__init__(parent, title, geometry)
    
    def createCustomWidgets(self, mainFrame):
        gamesHeaderFrame = tk.Frame(mainFrame, bg='white')
        gamesHeaderFrame.pack(fill='x', pady=(0, 10))

        gamesHeader = tk.Label(
            gamesHeaderFrame,
            text='Games',
            font=(
                'Castellar',
                16,
                'bold'
            ),
            bg='white',
            fg='black'
        )
        gamesHeader.pack()

        gamesFrame = tk.Frame(mainFrame, bg='white')
        gamesFrame.pack(fill='both', expand=True)

        gameOneButton = tk.Button(
            gamesFrame,
            text='Bullet Hell Roguelike',
            font=(
                'Castellar',
                16
            ),
            bg='gray',
            fg='white',
            width=15,  # int(self.geometry[0:3])//3
            height=2,
            command=self.gameOne
        )
        gameOneButton.pack(side='left', fill='both', padx=(0, 5), expand=False)

        gameTwoButton = tk.Button(
            gamesFrame,
            text='Game Two',  # TODO: Update with actual game name
            font=(
                'Castellar',
                16
            ),
            bg='gray',
            fg='white',
            width=15, # int(self.geometry[0:3])//3
            height=2,
            command= lambda: print("Not implemented yet")
        )
        gameTwoButton.pack(side='left', fill='both', padx=(5, 0), expand=False)    

    def gameOne(self):
        from gameOne import initGameOne
        initGameOne()        

runIfLocal(gameScreen, __name__)