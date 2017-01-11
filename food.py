from game_object import *
from button import *

class Food(GameObject):
    def __init__(self, name, food_type, coordinates, order_location, unavailable_pixel = (109, 123, 127, 255), quantity = 0):
        self.name = name
        self.food_type = food_type  # Make these 'types' separate classes
        self.order_button = Button('Order', order_location)
        self._starting_quantity = quantity
        self.quantity = self._starting_quantity
        self._unavailable_pixel = unavailable_pixel
        super(Food, self).__init__(name, coordinates)

    def available_for_order(self, pixel):
        return not (pixel == self.unavailable_pixel)

    def order_location(self):
        return self.order_button.coordinates

    def consume(self):
        self.quantity -= 1

    def almost_out(self):
        # Temporary special case, will be resolved upon creation of Sake class
        if self.name == 'Sake':
            return False
        return self.quantity < 5

    def sold_out(self):
        return self.quantity == 0

    def update_quantity(self):
        self.quantity += self._starting_quantity
