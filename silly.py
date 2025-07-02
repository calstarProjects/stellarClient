import pyautogui

a, b = pyautogui.size()

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        print(a // i, b // i)