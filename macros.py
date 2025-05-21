import tkinter.messagebox
import tkinter.simpledialog
import keyboard
import pyautogui
import math
import time
import tkinter

root = tkinter.Tk()
root.withdraw()
root.attributes('-topmost', True)
root.update()

def runMacroChoice():
    chosenMacro = ''
    key = ''

    def circle(itr):
        pyautogui.move(math.cos(itr/3)*50, math.sin(itr/3)*50)
    def autoClick():
        pyautogui.click()
    def autoKey():
        pyautogui.press(key)

    macroChoiceItr = 0
    macroChoices = ['autoClick', 'circle', 'autoKey', 'holdKey']
    while chosenMacro == '':
        if tkinter.messagebox.askyesno('Macro Choice', 'Would you like to do ' + macroChoices[macroChoiceItr%4]):
            chosenMacro = macroChoices[macroChoiceItr%4]
            tkinter.messagebox.showinfo('Macro Choice', 'You have chosen ' + chosenMacro)
        macroChoiceItr += 1

    match chosenMacro:
        case 'autoClick':
            pass
        case 'circle':
            pass
        case 'autoKey':
            tkinter.messagebox.askokcancel('Key Choice', 'After closing this box, press the key you with to autoKey')
            key = keyboard.read_key()
            pyautogui.press('backspace')
            tkinter.messagebox.askokcancel('Key Choice', 'You have chosen ' + key + ' as your key')
        case 'holdKey':
            tkinter.messagebox.askokcancel('Key Choice', 'After closing this box, press the key you with to holdKey')
            key = keyboard.read_key()
            pyautogui.press('backspace')
            tkinter.messagebox.askokcancel('Key Choice', 'You have chosen ' + key + ' as your key')

    desiredMins = None
    while desiredMins is None:
        desiredMins = int(tkinter.simpledialog.askinteger('Time Input', 'How many minutes? (under 60)', minvalue = 1, maxvalue = 59))
    tkinter.messagebox.showinfo('Ready', 'After closing this box, press the tab key to start')
    keyboard.wait('tab')
    startSecs = time.localtime().tm_sec
    desiredEndTime = time.localtime().tm_min + desiredMins % 60
    startTime = time.ctime(time.time())
    print('calced')
    
    iteration = 0
    while not keyboard.is_pressed('shift'):
        if keyboard.is_pressed('ctrl'):
            tkinter.messagebox.showwarning('WARNING', 'WARNING PAUSING FOR TOO LONG CAN GO PAST YOUR TIME GOAL AND RUN FOREVER \nHOLD SHIFT AND THEN CTRL TO FORCE QUIT \npress x to continue')
            keyboard.wait('x')
            pyautogui.press('backspace')
        if chosenMacro == 'holdKey':
            pyautogui.keyDown(key)
        print('start')
        while (not keyboard.is_pressed('ctrl')) and ((time.localtime().tm_sec != startSecs)):
            match chosenMacro:
                case 'autoClick':
                    autoClick()
                case 'circle':
                    circle(iteration)
                case 'autoKey':
                    autoKey()
                case 'holdKey':
                    pass
            iteration += 1
        if chosenMacro == 'holdKey':
                pyautogui.keyUp(key)
        print('looped')
        if ((time.localtime().tm_min == desiredEndTime) and (time.localtime().tm_sec == startSecs)):
            print('should be done')
            break
    tkinter.messagebox.showinfo('Task Finished', ('Desired Minutes = ' + str(desiredMins) + ', Start Seconds = ' + str(startSecs) + ', Desired End Time = ' + str(desiredEndTime) + ', Start Time ' + str(startTime) + ', End Time ' + str(time.ctime(time.time()))))
    print('boxed')