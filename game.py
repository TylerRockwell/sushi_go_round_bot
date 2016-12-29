from button import *
from food import *
from game_object import *
from phone import *
import controller as Controller

class Game:
    def __init__(self):
        self.coordinates = (0, 0)
        self.buildButtons()
        self.buildFood()
        self.buildPlates()
        self.mat = GameObject('Mat', (199, 380))
        self.phone = Phone()

    def buildButtons(self):
        self.soundButton = Button('Sound', (302, 372))
        self.playButton = Button('Play', (311, 206))
        self.continueButton = Button('Continue', (317, 393))
        self.skipButton = Button('Skip', (579, 455))

    def buildFood(self):
        self.rice = Food('Rice', (88, 338), (545, 280))
        self.shrimp = Food('Shrimp', (41, 330), (461, 210))
        self.nori = Food('Nori', (40, 393), (464, 269))
        self.roe = Food('Roe', (101, 388), (551, 275))
        self.salmon = Food('Salmon', (41, 453), (468, 331))
        self.unagi = Food('Unagi', (103, 442), (548, 211))

    def buildPlates(self):
        xCoordinates = [85, 189, 280, 387, 484, 581]
        self.plates = []
        for x in xCoordinates:
            self.plates.append(GameObject('Plate', (x, 204)))

    def buildRecipes(self):
        self.caliroll = Recipe([self.nori, self.rice, self.roe])
        self.gunkan = Recipe([self.nori, self.rice, self.roe, self.roe])
        self.onigiri = Recipe([self.rice, self.rice, self.nori])

    def prepareRecipe(recipe):
        for ingredient in recipe.ingredients:
            Controller.clickOn(ingredient)
        self.rollMat()

    def rollMat(self):
        Controller.clickOn(self.mat)

    def clearTables(self):
        for plate in self.plates:
            Controller.clickOn(plate)

    def restock(self, food):
        Controller.clickOn(self.phone)
        Controller.clickOn(self.phone.menuFor(food))
        Controller.clickOn(food.orderButton)
        Controller.clickOn(self.phone.orderButton)

    def start(self):
        Controller.clickMenu(self) # Focus on browser
        Controller.clickMenu(self.soundButton)
        Controller.clickMenu(self.playButton)
        Controller.clickMenu(self.continueButton)
        Controller.clickMenu(self.skipButton)
        Controller.clickMenu(self.continueButton)

if __name__ == "__main__":
    g = Game()
    g.start()
