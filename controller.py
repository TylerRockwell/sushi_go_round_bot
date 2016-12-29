# Coordinates are based on 1920x1080 resolution
# with Chrome shifted to left half of screen

import pyautogui
import pyscreenshot as ImageGrab
from time import sleep

padding = { 'x': 20, 'y': 250 }
width = 639
height = 480

def leftClick():
    pyautogui.click()

def setCursorPos(coords = (0, 0)):
    pyautogui.moveTo(coords[0] + padding['x'], coords[1] + padding['y'])

def clickMenu(obj):
    clickOn(obj)
    sleep(.1)

def clickOn(obj):
    setCursorPos(obj.coordinates)
    leftClick()
    sleep(.05)

def getCursorPos():
    x, y = pyautogui.position()
    x -= padding['x']
    y -= padding['y']
    print x, y

def screenGrab():
    box = (padding['x'], padding['y'], padding['x'] + width, padding['y'] + height)
    image = ImageGrab.grab(box, backend='mac_screencapture')
    return image
