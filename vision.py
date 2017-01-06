from numpy import *
from PIL import ImageOps
from PIL import Image # Remove once all recipes have been coded
import pyscreenshot

class Vision:
    def __init__(self, gameLocation):
        self.gameLocation = gameLocation

    def screenGrab(self):
        box = self.gameWindow()
        image = pyscreenshot.grab(box, backend='mac_screencapture')
        return image

    def gameWindow(self):
        window = (
                   self.gameLocation.xOffset,
                   self.gameLocation.yOffset,
                   self.gameLocation.offsetWidth(),
                   self.gameLocation.offsetHeight()
              )
        return window

    def analyze(self, box):
        image = self.screenGrab()
        # image = Image.open('screenshot.png') # Remove once all recipes have been coded
        orderImage = image.crop(box)
        orderImage = ImageOps.grayscale(orderImage)
        value = array(orderImage.getcolors()).sum()
        # print value
        return value
