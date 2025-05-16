import tkinter
import tkinter.messagebox
import tkinter.simpledialog

def encode():
    key = tkinter.simpledialog.askinteger('Encryption Key', 'Please input your encryption key')
    decryped = tkinter.simpledialog.askstring('Encryption String', 'Please input the string to encode')
    encrypted = ''

    for i in range(len(decryped)):
        encrypted += chr(ord(decryped[i]) + int(str(key)[i % len(str(key))]))

    tkinter.messagebox.showinfo('Encrypted', encrypted)
    print(encrypted)
def decode():
    key = tkinter.simpledialog.askinteger('Encryption Key', 'Please input your encryption key')
    encrypted = tkinter.simpledialog.askstring('Encryption String', 'Please input the string to encode')
    decrypted = ''

    for i in range(len(encrypted)):
        decrypted += chr(ord(encrypted[i]) + int(str(key)[i % len(str(key))]))

    tkinter.messagebox.showinfo('Decrypted', decrypted)
    print(decrypted)