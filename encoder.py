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
import tkinter.messagebox as tkmb
import tkinter.simpledialog as tksd
import pyperclip
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5 import QtCore


def encode(key: int = None, decrypted: str = None):    
    while key == None:
        key = tksd.askinteger('Encryption Key', 'Please input your encryption key')
    while decrypted == None:
        decrypted = tksd.askstring('Encryption String', 'Please input the string to encode')
    encrypted = ''

    for i in range(len(decrypted)):
        shift = int(str(key)[i % len(str(key))])
        encrypted += chr((ord(decrypted[i]) - shift) % 0x110000)

    # tkmb.showinfo('Encrypted', encrypted + ' will be copied to you clipboard')
    print(encrypted)
    # pyperclip.copy(encrypted)
    return(encrypted)

def decode(key: int = None, encrypted: str = None):
    ### TODO ###
    # make it so the dialogues are pyqt aligned
    while key == None:
        key = tksd.askinteger('Decryption Key', 'Please input your decryption key')
    while encrypted == None:
        encrypted = tksd.askstring('Decryption String', 'Please input the string to decode')
    decrypted = ''

    for i in range(len(encrypted)):
        shift = int(str(key)[i % len(str(key))])
        decrypted += chr((ord(encrypted[i]) + shift) % 0x110000)

    # tkmb.showinfo('Decrypted', decrypted + ' will be copied to you clipboard')
    print(decrypted)
    # pyperclip.copy(decrypted)
    return decrypted

class encodingWindow:
    def __init__(self, parent = None, title = 'Encoding/Decoding', geometry = "800x600"):
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

        statsHeaderFrame = tk.Frame(mainFrame, bg='white')
        statsHeaderFrame.pack(fill='x', pady=(0, 10))

        statsHeader = tk.Label(
            statsHeaderFrame,
            text='Encoder/Decoder',
            font=(
                'Castellar',
                16,
                'bold'
            ),
            bg='white',
            fg='black'
        )
        statsHeader.pack()

        contentFrame = tk.Frame(mainFrame, bg='white')
        contentFrame.pack(fill='x', pady=(0, 10))

        textLabel = tk.Label(
            contentFrame,
            text='Text input',
            font=(
                'Cascadia Code',
                14
            ),
            bg='gray',
            fg='black'
        )
        textLabel.pack(pady=(0, 10))

        self.textInput = tk.Text(
            contentFrame,
            font=(
                'Cascadia Code',
                12
            ),
            bg='gray',
            fg='black',
            height=2
        )
        self.textInput.pack(padx=int(self.geometry[0:3])/6, pady=(10, 0))

        keyLabel = tk.Label(
            contentFrame,
            text='Text input',
            font=(
                'Cascadia Code',
                14
            ),
            bg='gray',
            fg='black'
        )
        keyLabel.pack(pady=(0, 10))

        self.keyInput = tk.Text(
            contentFrame,
            font=(
                'Cascadia Code',
                12,
            ),
            bg='gray',
            fg='black',
            height=2
        )
        self.keyInput.pack(padx=int(self.geometry[0:3])/6, pady=(10, 10))

        buttonFrame = tk.Frame(contentFrame)
        buttonFrame.pack(fill=('y'), pady=(0, 10))

        encodeButton = tk.Button(
            buttonFrame,
            text='Encode',
            font=(
                'Cascadia Code',
                12
            ),
            fg='white',
            bg='black',
            command=self.encodeInputs
        )
        encodeButton.pack(padx=100, pady=(0, 10))
        encodeButton.bind()

        decodeButton = tk.Button(
            buttonFrame,
            text='Decode',
            font=(
                'Cascadia Code',
                12
            ),
            fg='white',
            bg='black',
            command=self.decodeInputs
        )
        decodeButton.pack(padx=100, pady=(0, 10))

        self.output = tk.Text(
            contentFrame,
            font=(
                'Cascadia Code',
                12,
            ),
            bg='gray',
            fg='black',
            height=2
        )
        self.output.pack(padx=int(self.geometry[0:3])/6, pady=(10, 10))
        self.output.config(state='disabled')

    def encodeInputs(self):
        text = self.textInput.get('1.0', tk.END).strip()
        key = self.keyInput.get('1.0', tk.END).strip()
        self.textInput.delete('1.0', tk.END)
        self.keyInput.delete('1.0', tk.END)
        self.output.config(state='normal')
        self.output.delete('1.0', tk.END)
        self.output.insert('1.0', encode(key, text))
        self.output.config(state='disabled')

    def decodeInputs(self):
        text = self.textInput.get('1.0', tk.END).strip()
        key = self.keyInput.get('1.0', tk.END).strip()
        self.textInput.delete('1.0', tk.END)
        self.keyInput.delete('1.0', tk.END)
        self.output.config(state='normal')
        self.output.delete('1.0', tk.END)
        self.output.insert('1.0', decode(key, text))
        self.output.config(state='disabled')
    
    def onClose(self):
        if self.window:
            self.window.destroy()
            self.window = None


if __name__ == '__main__':
    app = encodingWindow()
    app.show()
    app.window.mainloop()
