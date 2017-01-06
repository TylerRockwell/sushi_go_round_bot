class GameObject(object):
    def __init__(self, name, coordinates = (), boundingBox = (), colorSum = 0):
        self.name = name
        self.coordinates = coordinates # TODO: Do away with this and use boundingBox for all elements
        self.boundingBox = boundingBox
        self.colorSum = colorSum

    def isPresent(self, colorValue):
        return colorValue == self.colorSum
