import time
import pyautogui

time.sleep(1)
print(pyautogui.position())
time.sleep(2)
print(pyautogui.position())



for i in range(400):
    pyautogui.rightClick(1306, 414, 3)
    time.sleep(0.2)