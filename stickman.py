#This script locates the image stickman.png in the region we give it and tell you if it can see it

from pyautogui import * 
import pyautogui 
import time 
import keyboard 
import random
import win32api, win32con
# , region=(150,175,350,600)
while 1:
    if pyautogui.locateOnScreen('20210518140945.png', region=(150,175,350,600),grayscale=True, confidence=0.994) != None:
        print("I can see it")
        time.sleep(0.5)

        f = pyautogui.locateOnScreen('222.png')
        print(f)

        x = pyautogui.locateCenterOnScreen('222.png', confidence=0.994)
        print(x)
    else:
        print("I am unable to see it")
        time.sleep(0.5)
