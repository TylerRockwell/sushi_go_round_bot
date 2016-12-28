# Coordinates are based on 1920x1080 resolution
# with Chrome shifted to left half of screen

import pyautogui
import time

padding = { 'x': 20, 'y': 250 }
width = 639
height = 480

def leftClick():
    pyautogui.click()

def setCursorPos(coords = (0, 0)):
    pyautogui.moveTo(coords[0] + padding['x'], coords[1] + padding['y'])

def clickOn(obj):
    setCursorPos(obj.coordinates)
    leftClick()
    time.sleep(.1)

def getCursorPos():
    x, y = pyautogui.position()
    x -= padding['x']
    y -= padding['y']
    print x, y

def startGame():
    # Navigate through starting menus
    clickOn() # Focus game window
    clickOn((302, 372))
