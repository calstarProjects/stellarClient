import tkinter as tk

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

import tkinter as tk

class SCWindow:
    def __init__(self, parent = None, title = 'Stellar Client', geometry = "800x600"):
        self.parent = parent
        self.window = None
        self.title = title
        self.geometry = geometry
        self.__post_init__()

    def __post_init__(self):
        pass

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
        self.window.after(1, self.periodic)

    def onClose(self):
        if self.window:
            self.window.destroy()
            self.window = None


def runIfLocal(window:SCWindow, name:str):
    if name == '__main__':
        app = window()
        app.show()
        app.periodic()
        app.window.mainloop()
