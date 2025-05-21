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

import tkinter
import tkinter.messagebox
import tkinter.simpledialog

def encode(key: int = None, decrypted: str = None):    
    if key == None:
        key = tkinter.simpledialog.askinteger('Encryption Key', 'Please input your encryption key')
    if decryped == None:
        decryped = tkinter.simpledialog.askstring('Encryption String', 'Please input the string to encode')
    encrypted = ''

    for i in range(len(decryped)):
        encrypted += chr(ord(decryped[i]) + int(str(key)[i % len(str(key))]))

    tkinter.messagebox.showinfo('Encrypted', encrypted)
    print(encrypted)
    return(encrypted)
def decode():
    key = tkinter.simpledialog.askinteger('Encryption Key', 'Please input your encryption key')
    encrypted = tkinter.simpledialog.askstring('Encryption String', 'Please input the string to encode')
    decrypted = ''

    for i in range(len(encrypted)):
        decrypted += chr(ord(encrypted[i]) + int(str(key)[i % len(str(key))]))

    tkinter.messagebox.showinfo('Decrypted', decrypted)
    print(decrypted)