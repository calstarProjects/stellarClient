import tkinter as tk

class SCWindow:
    """The base Stellar Client Window Object/Class
    Functions*:

    - __init__:
        - Initialize function

    - show:
        - Makes the window create/lift itself
    
    - createWindow: 
        - Makes the self.window object
    
    - createWidgets:
        - Makes basic Stellar Client Header

    - createCustomWidgets:
        - Customizable extra tk window objects
    
    - periodic:
        - Periodic function called repeatedly
        - In initialization, you can set the loop rate in ms

    - onStart:
        - Start function that runs when the window is initalised

    - onClose:
        - Close function that runs when the window is closed by the user

    *None of these need be called by you to run the application (except occasionally self.periodicLoop to start the periodic function if it has stopped)
    When making a custom window, you can alter the __init__ function and the createCustomWidgets like so
    
    def __init__(self, parent=None, title='<Your Window's Name Here>', geometry="800x600", periodicRate = 1, <extra inputs>):
        super().__init__(parent, title, geometry, periodicRate)

        self.<extra traits> = <extra inputs>
        
    def createCustomWidgets(self, mainFrame):
        extraHeaderFrame = tk.Frame(mainFrame, bg='white')
        extraHeaderFrame.pack(fill='x', pady=(0, 10))

        extraHeader = tk.Label(
            extraHeaderFrame,
            text='EXTRA',
            bg='white',
            fg='black'
        )
        extraHeader.pack(expand=True)
    """

    def __init__(self, parent = None, title = 'Stellar Client', geometry = "800x600", periodicRate = 1):
        self.parent = parent
        self.window = None
        self.title = title
        self.geometry = geometry
        self.periodicRate = periodicRate


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
        self.createCustomWidgets(mainFrame)
    
    def createCustomWidgets(self, mainFrame):
        pass

    def periodic(self):
        pass

    def periodicLoop(self):
        self.window.after(self.periodicRate, self.periodic)
        self.window.after(self.periodicRate, self.periodicLoop)
    
    def onStart(self):
        pass

    def onClose(self):
        if self.window:
            self.window.destroy()
            self.window = None


def runIfLocal(window: type[SCWindow], name:str):
    if name == '__main__':
        app = window()
        app.show()
        app.periodicLoop()
        app.onStart()
        app.window.mainloop()

runIfLocal(SCWindow, __name__)