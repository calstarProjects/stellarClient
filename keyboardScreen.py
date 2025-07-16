from macros import macroWindow
from encoder import encodingWindow
from computerStats import computerStatsWindow
from keylogger import keyLog
from SCWindow import SCWindow, runIfLocal
import tkinter as tk

class keyboardWindow(SCWindow):
    def __init__(self):
        super().__init__(title='Stellar Client Keyboard Util', geometry="800x600")
    def __post_init__(self):
        self.macroWindow = None
        self.encodeWindow = None
        self.keylogWindow = None
        self.computerStatsWindow = None
        
    def createCustomWidgets(self, mainFrame):
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
            
        computerStatsButton = tk.Button(
            contentFrame,
            text='Computer Stats',
            font=(
                'Arial',
                12
            ),
            bg='gray',
            fg='black',
            command=self.computerStats
        )
        computerStatsButton.pack(side='left', fill='both', padx=10, expand=False)
            
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

    def computerStats(self):
        if self.computerStatsWindow == None:
            self.computerStatsWindow = computerStatsWindow(self.window)
        self.computerStatsWindow.show()    


runIfLocal(keyboardWindow, __name__)