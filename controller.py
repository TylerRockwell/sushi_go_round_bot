# Coordinates are based on 1920x1080 resolution
# with Chrome shifted to left half of screen

from PIL import ImageOps
# from PIL import Image # Remove once all recipes have been coded
from numpy import *
import pyautogui
import pyscreenshot as ImageGrab
from time import sleep

# TODO: Move padding logic to paddable module
padding = { 'x': 20, 'y': 250 }
width = 639
height = 480

def leftClick():
    pyautogui.click()

def setCursorPos(coords = (0, 0)):
    pyautogui.moveTo(coords[0] + padding['x'], coords[1] + padding['y'])

def clickMenu(obj):
    clickOn(obj)
    sleep(.2)

def clickOn(obj):
    setCursorPos(obj.coordinates)
    leftClick()
    sleep(.05)

def clickWithin(obj):
    # bounding box should be in the form (x1, y1, x2, y2)
    box = retinaAdjustment(obj.boundingBox)
    setCursorPos(tuple(box[:2]))
    leftClick()
    sleep(.05)

def retinaAdjustment(box):
    return tuple(map(lambda n: n/2, box))

def getCursorPos():
    x, y = pyautogui.position()
    x -= padding['x']
    y -= padding['y']
    print x, y

# TODO: Move this screenshotting code out of this module
def screenGrab():
    box = (padding['x'], padding['y'], padding['x'] + width, padding['y'] + height)
    image = ImageGrab.grab(box, backend='mac_screencapture')
    return image

def rgbSum(box):
    image = screenGrab()
    # image = Image.open('screenshot.png') # Remove once all recipes have been coded
    orderImage = image.crop(box)
    orderImage = ImageOps.grayscale(orderImage)
    value = array(orderImage.getcolors()).sum()
    # print value
    return value

def getCustomerOrder(seatPosition):
    seatCoordinates = [51, 253, 455, 657, 859, 1061]
    x = seatCoordinates[seatPosition]
    box = (x, 122, x + 121, 151)
    return rgbSum(box)

def getAllOrders():
    orders = []
    for seat in xrange(6):
        orders.append(getCustomerOrder(seat))
    return orders
