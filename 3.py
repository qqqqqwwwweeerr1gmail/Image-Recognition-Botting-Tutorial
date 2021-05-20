



import os
import pyautogui as py


image_list = []

# Get list of all files in current directory
directory = os.listdir('TextDetection')

# Find files that end with .png or .jpg and add to image_list
for file in directory:
    if file.endswith('.png') or file.endswith('.jpg'):
        image_list.append(file)

# Loop through list to find all the images
for image in image_list:
    print(image)
    # print(py.locateOnScreen(image))
    print(py.locateOnScreen('D:\GitHub\Image-Recognition-Botting-Tutorial//TextDetection/'+image))
    print(py.locateOnScreen('TextDetection/222.png'))
    print(py.locateOnScreen('222.png'))







