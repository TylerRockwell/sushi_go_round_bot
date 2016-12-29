from game_object import *
from button import *

class Food(GameObject):
    def __init__(self, name, coordinates, orderLocation):
        self.orderButton = Button('Order', orderLocation)
        super(Food, self).__init__(name, coordinates)

    def isRice():
        return self.name == 'Rice'
