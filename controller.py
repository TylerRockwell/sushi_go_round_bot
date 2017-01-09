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

    def dragTo(self, obj):
        pyautogui.dragTo(obj.coordinates[0] + self.gameLocation.xOffset, obj.coordinates[1] + self.gameLocation.yOffset, 1)

    # Debug method
    def getCursorPos(self):
        x, y = pyautogui.position()
        x -= self.gameLocation.xOffset
        y -= self.gameLocation.yOffset
        print x, y

