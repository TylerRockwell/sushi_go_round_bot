from game_object import *
from button import *

class Phone:
    def __init__(self):
        self.coordinates = (566, 361)
        self.toppingButton = Button('Topping', (516, 275))
        self.riceButton = Button('Rice', (516, 296))
        self.orderButton = Button('Normal Order', (480, 293))

    def menuFor(food):
        if food.isRice():
            return self.riceButton
        else:
            return self.toppingButton
