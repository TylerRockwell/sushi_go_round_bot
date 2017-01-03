class GameObject(object):
    def __init__(self, name, coordinates = (), boundingBox = (), colorSum = 0):
        self.name = name
        self.coordinates = coordinates
        self.boundingBox = boundingBox
        self.colorSum = colorSum

    def isPresent(self, colorValue):
        return colorValue == self.colorSum
