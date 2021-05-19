from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


#
# while 1:
#     if pyautogui.locateOnScreen('20210518140945.png', grayscale=True, confidence=0.8) != None:
#         print("I can see it")
#         time.sleep(0.5)
#
#         # click()
#         pyautogui.click('20210518140945.png')
#
#     else:
#         print("I am unable to see it")
#         time.sleep(0.5)
#
#     break

pyautogui.click('./20210518140945.png')