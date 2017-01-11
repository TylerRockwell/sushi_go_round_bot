from numpy import array
from PIL import ImageOps
from PIL import Image  # Remove once all recipes have been coded
import pyscreenshot


class Vision:
    def __init__(self, game_location):
        self.game_location = game_location

    def analyze(self, box):
        image = self._screen_grab()
        # image = Image.open('screenshot.png') # Remove once all recipes have been coded
        order_image = image.crop(box)
        order_image = ImageOps.grayscale(order_image)
        value = array(order_image.getcolors()).sum()
        # print value
        return value

    def _screen_grab(self):
        box = self.game_window()
        image = pyscreenshot.grab(box, backend='mac_screencapture')
        return image

    def _game_window(self):
        window = (
                   self.game_location.xOffset,
                   self.game_location.yOffset,
                   self.game_location.offsetWidth(),
                   self.game_location.offsetHeight()
              )
        return window
