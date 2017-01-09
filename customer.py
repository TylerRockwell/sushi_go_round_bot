class Customer:
    def __init__(self, name, plate, order, happiness):
        self.name = name
        self.plate = plate
        self.order = order
        self.happiness = happiness

    def orderBox(self):
        return self.order.boundingBox

    def isUnhappy(self, colorValue):
        # Checks for empty happiness ball
        return self.happiness.isPresent(colorValue)

    def happinessMeterLocation(self):
        return self.happiness.boundingBox
