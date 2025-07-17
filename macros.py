import tkinter.messagebox as tkmb
import tkinter.simpledialog as tksd
import keyboard
import pyautogui
import math
import time
import tkinter as tk

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
    key = None
    match chosenMacro:
        case 'autoClick':
            pass
        case 'circle':
            pass
        case 'autoKey':
            tkmb.askokcancel('Key Choice', 'After closing this box, press the key you with to autoKey')
            key = keyboard.read_key()
            pyautogui.press('backspace')
            tkmb.askokcancel('Key Choice', 'You have chosen ' + key + ' as your key')
        case 'holdKey':
            tkmb.askokcancel('Key Choice', 'After closing this box, press the key you with to holdKey')
            key = keyboard.read_key()
            pyautogui.press('backspace')
            tkmb.askokcancel('Key Choice', 'You have chosen ' + key + ' as your key')
    if key != None:
        return key

def runMacro(chosenMacro: str, key: str = None):
    desiredMins = None
    while desiredMins is None:
        desiredMins = int(tksd.askinteger('Time Input', 'How many minutes? (under 60)', minvalue = 1, maxvalue = 59))
    tkmb.showinfo('Ready', 'After closing this box, press the tab key to start (also note that pressing ctrl will pause the macro and esc will end it)')
    keyboard.wait('tab')
    startSecs = time.localtime().tm_sec
    desiredEndTime = time.localtime().tm_min + desiredMins % 60
    startTime = time.ctime(time.time())
    print('calced')
    
    iteration = 0
    while not keyboard.is_pressed('esc'):
        if keyboard.is_pressed('ctrl'):
            tkmb.showwarning('WARNING', 'WARNING PAUSING FOR TOO LONG CAN GO PAST YOUR TIME GOAL AND RUN FOREVER \nHOLD ESC TO FORCE QUIT \npress x to continue')
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
    tkmb.showinfo('Task Finished', ('Desired Minutes = ' + str(desiredMins) + ', Start Seconds = ' + str(startSecs) + ', Desired End Time = ' + str(desiredEndTime) + ', Start Time ' + str(startTime) + ', End Time ' + str(time.ctime(time.time()))))
    print('boxed')

class macroWindow:
    def __init__(self, parent = None, title = 'Stellar Client Macros', geometry = "800x600"):
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

        encoderHeaderFrame = tk.Frame(mainFrame, bg='white')
        encoderHeaderFrame.pack(fill='y', padx=(0, 10))

        encoderHeader = tk.Label(
            encoderHeaderFrame,
            text='Macros',
            font=(
                'Castellar',
                16,
                'bold'
            ),
            bg='white',
            fg='black'
        )
        encoderHeader.pack()

        contentFrame = tk.Frame(mainFrame, bg='white')
        contentFrame.pack(padx=(0, 10))

        self.autoClickButton = tk.Button(
            contentFrame,
            text='Autoclick',
            font=(
                'arial',
                12
            ),
            bg='white',
            fg='grey',
            command=self.runAutoClick
        )
        self.autoClickButton.pack(padx=10, side='left', fill='both', expand=False)
        
        self.circleButton = tk.Button(
            contentFrame,
            text='Circle',
            font=(
                'arial',
                12
            ),
            bg='white',
            fg='grey',
            command=self.runCircle
        )
        self.circleButton.pack(padx=10, side='left', fill='both', expand=False)
        
        self.holdKeyButton = tk.Button(
            contentFrame,
            text='Hold Key',
            font=(
                'arial',
                12
            ),
            bg='white',
            fg='grey',
            command=self.runHoldKey
        )
        self.holdKeyButton.pack(padx=10, side='left', fill='both', expand=False)
        
        self.autoKeyButton = tk.Button(
            contentFrame,
            text='AutoKey',
            font=(
                'arial',
                12
            ),
            bg='white',
            fg='grey',
            command=self.runAutoKey
        )
        self.autoKeyButton.pack(padx=10, side='left', fill='both', expand=False)
        
    def runAutoClick(self):
        runMacro('autoClick', getInfo('autoClick'))
    def runCircle(self):
        runMacro('circle', getInfo('circle'))
    def runAutoKey(self):
        runMacro('autoKey', getInfo('autoKey'))
    def runHoldKey(self):
        runMacro('holdKey', getInfo('holdKey'))

    def onClose(self):
        if self.window:
            self.window.destroy()
            self.window = None

if __name__ == '__main__':
    window = macroWindow()
    window.show()
    if window.window:
        window.window.mainloop()