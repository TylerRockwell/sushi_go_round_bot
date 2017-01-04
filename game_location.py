class GameLocation:
    def __init__(self, xOffset, yOffset, width, height):
        self.xOffset = xOffset
        self.yOffset = yOffset
        self.width = width
        self.height = height

    def offsetWidth(self):
        return self.xOffset + self.width

    def offsetHeight(self):
        return self.yOffset + self.height
