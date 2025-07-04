from gameScreen import gameScreen
from macros import macroWindow
from encoder import encodingWindow
from computerStats import computerStatsWindow
from keylogger import keyLog
import tkinter as tk

class keyboardWindow:
    def __init__(self, parent = None, title = 'Stellar Client Keyboard Util', geometry = '800x600'):
        # TODO: macro button, encode button, stat button, macroButton
        self.parent = parent
        self.window = None
        self.title = title
        self.geometry = geometry

        self.macroWindow = None
        self.encodeWindow = None
        self.keylogWindow = None
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

        keyboardUtilHeaderFrame = tk.Frame(mainFrame, bg='white')
        keyboardUtilHeaderFrame.pack(fill='x', pady=(0, 10))

        keyboardUtilHeader = tk.Label(
            keyboardUtilHeaderFrame,
            text='Keyboard Util',
            font=(
                'Castellar',
                16,
                'bold'
            ),
            bg='white',
            fg='black'
        )
        keyboardUtilHeader.pack(expand=True)

        contentFrame = tk.Frame(mainFrame)
        contentFrame.pack(pady=(0, 10))

        macroButton = tk.Button(
            contentFrame,
            text='Macros',
            font=(
                'Arial',
                12
            ),
            bg='gray',
            fg='black',
            command=self.macro
        )
        macroButton.pack(side='left', fill='both', padx=10, expand=False)

        encodeButton = tk.Button(
            contentFrame,
            text='Encoding',
            font=(
                'Arial',
                12
            ),
            bg='gray',
            fg='black',
            command=self.encoder
        )
        encodeButton.pack(side='left', fill='both', padx=10, expand=False)
    
        keyLogButton = tk.Button(
            contentFrame,
            text='Keylogger',
            font=(
                'Arial',
                12
            ),
            bg='gray',
            fg='black',
            command=self.keylog
        )
        keyLogButton.pack(side='left', fill='both', padx=10, expand=False)
    
    def macro(self):
        if self.macroWindow == None:
            self.macroWindow = macroWindow(self.window)
        self.macroWindow.show()
    
    def encoder(self):
        if self.encodeWindow == None:
            self.encodeWindow = encodingWindow(self.window)
        self.encodeWindow.show()
    
    def keylog(self):
        keyLog('ctrl')
    
    def onClose(self):
        if self.window:
            self.window.destroy()
            self.window = None




if __name__ == "__main__":
    app = keyboardWindow()
    app.show()
    app.window.mainloop()
