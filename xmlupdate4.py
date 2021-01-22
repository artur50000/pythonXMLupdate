import os
import shutil
import pyautogui
import time
import cv2
import keyboard


def im(image):

    path = path_to_image + image

    buttontolocation = pyautogui.locateOnScreen(path, confidence=0.7)

    buttontopoint = pyautogui.center(buttontolocation)

    pyautogui.moveTo(buttontopoint)


def delete():
    keyboard.press_and_release('shift+f10')

    for i in range(0, 6):
        keyboard.press_and_release('down')

    keyboard.press_and_release('right')

    keyboard.press_and_release('enter')


time.sleep(2)

file = path_to_excel_file + "updateVictory.xlsm"
os.startfile(file)


time.sleep(15)
im('data.png')

pyautogui.click(button='left')

time.sleep(2)
im('refreshall.png')

pyautogui.click(button='left')

time.sleep(25)

for i in range(0, 4):
    keyboard.press_and_release('left')


delete()

for i in range(0, 7):
    keyboard.press_and_release('up')

for i in range(0, 5):
    keyboard.press_and_release('right')


for i in range(0, 3):
    delete()

for i in range(0, 5):
    keyboard.press_and_release('left')

keyboard.write("Release date")
keyboard.press_and_release('right')
keyboard.write("Product")
keyboard.press_and_release('right')
keyboard.write("Component")
keyboard.press_and_release('right')
keyboard.write("GA Release")
keyboard.press_and_release('right')
keyboard.write("Component name")
keyboard.press_and_release('right')

im('select.png')
time.sleep(2)
pyautogui.click(button='left')

keyboard.press_and_release('left')
keyboard.press_and_release('enter')

im('home.png')
time.sleep(2)
pyautogui.click(button='left')

time.sleep(2)
im('format.png')
time.sleep(2)
pyautogui.click(button='left')

for i in range(0, 4):
    keyboard.press_and_release('down')

keyboard.press_and_release('enter')
