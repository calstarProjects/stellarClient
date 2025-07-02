import pyautogui
import threading
import tkinter as tk


screenwidth, screenlength = pyautogui.size()

class gameScreen:
    def __init__(self, parent = None, title = 'Stellar Client Games', geometry = '800x600'):
        self.parent = parent
        self.window = None
        self.title = title
        self.geometry = geometry
    
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
            height=2
        )
        gameTwoButton.pack(side='left', fill='both', padx=(5, 0), expand=False)    
    def gameOne(self):
        from gameOne import initGameOne
        initGameOne()

    def onClose(self):
        if self.window:
            self.window.destroy()
            self.window = None
        

if __name__ == "__main__":
    app = gameScreen()
    app.show()
    app.window.mainloop()