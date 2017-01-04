import pyautogui
from time import sleep

class Controller:
    def __init__(self, gameLocation):
        self.gameLocation = gameLocation

    def leftClick(self):
        pyautogui.click()

    def setCursorPos(self, coords = (0, 0)):
        pyautogui.moveTo(coords[0] + self.gameLocation.xOffset, coords[1] + self.gameLocation.yOffset)

    def clickMenu(self, obj):
        self.clickOn(obj)
        sleep(.2)

    def clickOn(self, obj):
        self.setCursorPos(obj.coordinates)
        self.leftClick()
        sleep(.05)

    def clickWithin(self, obj):
        # bounding box should be in the form (x1, y1, x2, y2)
        box = self.retinaAdjustment(obj.boundingBox)
        self.setCursorPos(tuple(box[:2]))
        self.leftClick()
        sleep(.05)

    def retinaAdjustment(self, box):
        return tuple(map(lambda n: n/2, box))

    # Debug method
    def getCursorPos(self):
        x, y = pyautogui.position()
        x -= self.gameLocation.xOffset
        y -= self.gameLocation.yOffset
        print x, y

