class Customer:
    def __init__(self, plate, order, happiness):
        self.plate = plate
        self.order = order
        self.happiness = happiness

    def orderBox(self):
        return self.order.boundingBox

    def unhappy(self, colorValue):
        return not self.happiness.isPresent(colorValue)
