class Customer:
    def __init__(self, plate, order):
        self.plate = plate
        self.order = order

    def orderBox(self):
        return self.order.boundingBox
