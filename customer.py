class Customer:
    def __init__(self, name, plate, order, happiness):
        self.name = name
        self.plate = plate
        self.order = order
        self.happiness = happiness

    def order_box(self):
        return self.order.boundingBox

    def is_unhappy(self, colorValue):
        # Checks for empty happiness ball
        return self.happiness.isPresent(colorValue)

    def happiness_meter_location(self):
        return self.happiness.boundingBox
