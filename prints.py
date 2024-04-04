import pyautogui

location = None
while location is None:
    pyautogui.screenshot('../Epic7 Garden/heart.png', region=(1249, 738, 1327-1249, 777-738))
    location = pyautogui.locateOnScreen('heart.png', confidence=.95)
print(location)
