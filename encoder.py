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
from SCWindow import SCWindow, runIfLocal
# Reminder: pyperclip can be used for copypaste

def encode(key: int = None, decrypted: str = None):    
    while key == None:
        key = tksd.askinteger('Encryption Key', 'Please input your encryption key')
    while decrypted == None:
        decrypted = tksd.askstring('Encryption String', 'Please input the string to encode')
    encrypted = ''

    for i in range(len(decrypted)):
        shift = int(str(key)[i % len(str(key))])
        encrypted += chr((ord(decrypted[i]) - shift) % 0x110000)

    print(encrypted)
    return(encrypted)

def decode(key: int = None, encrypted: str = None):
    while key == None:
        key = tksd.askinteger('Decryption Key', 'Please input your decryption key')
    while encrypted == None:
        encrypted = tksd.askstring('Decryption String', 'Please input the string to decode')
    decrypted = ''

    for i in range(len(encrypted)):
        shift = int(str(key)[i % len(str(key))])
        decrypted += chr((ord(encrypted[i]) + shift) % 0x110000)

    print(decrypted)
    return decrypted

class encodingWindow(SCWindow):
    def __init__(self, parent=None, title='Stellar Client Encryption', geometry="800x600"):
        super().__init__(parent, title, geometry)
    def createCustomWidgets(self, mainFrame):
        encoderHeaderFrame = tk.Frame(mainFrame, bg='white')
        encoderHeaderFrame.pack(fill='x', pady=(0, 10))

        encoderHeader = tk.Label(
            encoderHeaderFrame,
            text='Encoder/Decoder',
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
            text='Key input',
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
            height=1,
            width=8,

        )
        self.keyInput.tag_configure("centre", justify='center')
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
            height=2,
        )
        self.output.pack(padx=int(self.geometry[0:3])/6, pady=(10, 10), expand=False)
        self.output.config(state='disabled')

    def periodic(self):
        self.keyInput.tag_add("centre", "1.0", tk.END)
        self.window.after(1, self.periodic)

    def encodeInputs(self):
        text = self.textInput.get('1.0', tk.END).strip()
        key = self.keyInput.get('1.0', tk.END).strip()
        try:
            key = int(key) if key else None
        except ValueError:
            tkmb.showerror("Invalid Key", "Key must be a valid integer")
            return
        self.textInput.delete('1.0', tk.END)
        self.keyInput.delete('1.0', tk.END)
        self.output.config(state='normal')
        self.output.delete('1.0', tk.END)
        self.output.insert('1.0', encode(key, text))
        self.output.config(state='disabled')
    def decodeInputs(self):
        text = self.textInput.get('1.0', tk.END).strip()
        key = self.keyInput.get('1.0', tk.END).strip()
        try:
            key = int(key) if key else None
        except ValueError:
            tkmb.showerror("Invalid Key", "Key must be a valid integer")
            return
        self.textInput.delete('1.0', tk.END)
        self.keyInput.delete('1.0', tk.END)
        self.output.config(state='normal')
        self.output.delete('1.0', tk.END)
        self.output.insert('1.0', decode(key, text))
        self.output.config(state='disabled')    


runIfLocal(encodingWindow, __name__)