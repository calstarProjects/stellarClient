from SCWindow import SCWindow, runIfLocal
from weather import weatherWindow
from news import newsWindow
import tkinter as tk

class worldInfo(SCWindow):
    def __init__(self, parent = None, title = 'Stellar Client Games', geometry = '800x400'):
        super().__init__(parent, title, geometry)
        self.weatherWindow = None
        self.newsWindow = None
    
    def createCustomWidgets(self, mainFrame):
        gamesHeaderFrame = tk.Frame(mainFrame, bg='white')
        gamesHeaderFrame.pack(fill='x', pady=(0, 10))

        gamesHeader = tk.Label(
            gamesHeaderFrame,
            text='World Info',
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
            text='Weather',
            font=(
                'Castellar',
                16
            ),
            bg='gray',
            fg='white',
            width=15,  # int(self.geometry[0:3])//3
            height=2,
            command=self.weather
        )
        gameOneButton.pack(side='left', fill='both', padx=(0, 5), expand=False)

        gameTwoButton = tk.Button(
            gamesFrame,
            text='News',  # TODO: Update with actual game name
            font=(
                'Castellar',
                16
            ),
            bg='gray',
            fg='white',
            width=15, # int(self.geometry[0:3])//3
            height=2,
            command= self.news
        )
        gameTwoButton.pack(side='left', fill='both', padx=(5, 0), expand=False)    

    def weather(self):
        if self.weatherWindow == None:
            self.weatherWindow = weatherWindow(self.window)
        self.weatherWindow.show()
        
    def news(self):
        if self.newsWindow == None:
            self.newsWindow = newsWindow(self.window)
        self.newsWindow.show()              

runIfLocal(worldInfo, __name__)