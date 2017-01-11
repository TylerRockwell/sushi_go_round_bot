from game_object import *
from button import *

class Phone:
    def __init__(self):
        self.coordinates = (566, 361)
        self.toppingButton = Button('Topping', (516, 275))
        self.riceButton = Button('Rice', (516, 296))
        self.sakeButton = Button('Sake', (507, 314))
        self.orderButton = Button('Normal Order', (480, 293))
        self.instantOrderButton = Button('Instant Order', (1, 1))
        self.hangUpButton = Button('Hang Up', (582, 337))

        self.foodMenus = [self.toppingButton, self.riceButton, self.sakeButton]

    def menuFor(self, food):
        return filter(lambda menu: menu.name == food.food_type, self.foodMenus)[0]
