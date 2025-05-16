import keyboard
import pyautogui
import time
print('Press Ctrl-C to quit.')
try:
    print
    while not keyboard.is_pressed('ctrl'):
        if keyboard.is_pressed('e'):
            time.sleep(0.1)
            keyboard.press('backspace')
            print('\n')
            exit()
        else:
            X, Y = pyautogui.position()
            positionStr = 'X: ' + str(X).rjust(4) + ' Y: ' + str(Y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
