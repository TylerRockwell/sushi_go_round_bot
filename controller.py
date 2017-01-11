import pyautogui
from time import sleep


class Controller:
    def __init__(self, x_offset, y_offset):
        self.x_offset = x_offset
        self.y_offset = y_offset

    def click_menu(self, obj):
        self.click_on(obj)
        sleep(.2)

    def click_on(self, obj):
        self._set_cursor_pos(obj.coordinates)
        self._left_click()
        sleep(.05)

    def drag_to(self, obj):
        position = self._offset_position(obj.coordinates)
        pyautogui.dragTo(position[0], position[1], 1)

    def _left_click(self):
        pyautogui.click()

    def _set_cursor_pos(self, coords=(0, 0)):
        position = self._offset_position(coords)
        pyautogui.moveTo(position[0], position[1])

    def _offset_position(self, coords):
        return [coords[0] + self.x_offset, coords[1] + self.y_offset]

    # Debug method
    def _get_cursor_pos(self):
        x, y = pyautogui.position()
        x -= self.xOffset
        y -= self.yOffset
        print x, y
