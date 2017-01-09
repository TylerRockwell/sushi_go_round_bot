from game_object import *
from button import *

class Food(GameObject):
    def __init__(self, name, foodType, coordinates, orderLocation, unavailablePixel = (109, 123, 127, 255), quantity = 0):
        self.name = name
        self.foodType = foodType
        self.orderButton = Button('Order', orderLocation)
        self.startingQuantity = quantity
        self.quantity = quantity
        self.unavailablePixel = unavailablePixel
        super(Food, self).__init__(name, coordinates)

    def availableForOrder(self, pixel):
        return not (pixel == self.unavailablePixel)

    def orderLocation(self):
        return self.orderButton.coordinates

    def consume(self):
        self.quantity -= 1

    def almostOut(self):
        # Temporary special case
        if self.name == 'Sake':
            return False
        return self.quantity < 5

    def soldOut(self):
        return self.quantity == 0

    def updateQuantity(self):
        self.quantity += self.startingQuantity
