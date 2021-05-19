
from pyautogui import *
import pyautogui


x, y = pyautogui.position()  # current mouse x and y

print(pyautogui.position())

pyautogui.size()  # current screen resolution width and height
print(pyautogui.size())

pyautogui.onScreen(x, y)  # True if x & y are within the screen.
print(pyautogui.onScreen(x, y))

a = pyautogui.locateOnScreen('./20210518140945.png', grayscale=True, confidence=0.8)
print(a)
b = pyautogui.locateAllOnScreen('./20210518140945.png', confidence=0.8)
print(b)
for i in pyautogui.locateAllOnScreen('./20210518140945.png', confidence=0.8):
    print('a')
    print(i)
    click(i.left+10, i.top+10)
    break



# if pyautogui.locateOnScreen('20210518140945.png', region=(150, 175, 350, 600), grayscale=True,
#                             confidence=0.994) != None:
#     print("I can see it")
#     time.sleep(0.5)
#
#     f = pyautogui.locateOnScreen('222.png')
#     print(f)
#
#     x = pyautogui.locateCenterOnScreen('222.png', confidence=0.994)
#     print(x)

c = list(pyautogui.locateAllOnScreen('./20210518140945.png'))
print(c)

# click(a.left,a.top)