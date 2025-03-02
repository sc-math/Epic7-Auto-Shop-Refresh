import pyautogui
import time

location = None
time.sleep(1)
x1 = pyautogui.position()
print(x1)

time.sleep(2)
x2 = pyautogui.position()
print(x2)

while location is None:
    pyautogui.screenshot('mystic.png', region=(x1.x, x1.y, x2.x - x1.x, x2.y - x1.y))
    location = pyautogui.locateOnScreen('mystic.png', confidence=.95)
print(location)
