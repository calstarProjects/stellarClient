import pyautogui

a, b = pyautogui.size()

for i in range(a if a < b else b):
    if not i == 0:
        if a % i == 0 and b % i == 0:
            print(a/i, b/i)