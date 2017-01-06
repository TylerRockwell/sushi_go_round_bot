class GameObject(object):
    def __init__(self, name, coordinates = (), boundingBox = (), colorSum = 0):
        self.name = name
        self.coordinates = coordinates
        self.boundingBox = boundingBox
        self.colorSum = colorSum

        if len(self.coordinates) == 0: self.setCoordinates()

    def isPresent(self, colorValue):
        return colorValue == self.colorSum

    def setCoordinates(self):
        self.coordinates = self.clickablePoint()

    def clickablePoint(self):
        gameCoordinates = self.retinaAdjustedBox()
        return tuple(gameCoordinates[:2])

    def retinaAdjustedBox(self):
        return tuple(map(lambda n: n/2, self.boundingBox))
