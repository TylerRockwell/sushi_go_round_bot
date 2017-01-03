from button import *
from food import *
from game_object import *
from phone import *
from recipe import *
import controller as Controller
from time import sleep

class Game:
    def __init__(self):
        self.coordinates = (0, 0)
        self.buildButtons()
        self.buildFood()
        self.buildPlates()
        self.buildRecipes()
        self.mat = GameObject('Mat', (199, 380))
        self.phone = Phone()

    def focus(self):
        Controller.clickOn(self)

    def buildButtons(self):
        self.soundButton = Button('Sound', (302, 372))
        self.playButton = Button('Play', (311, 206))
        self.continueButton = Button('Continue', (317, 393))
        self.skipButton = Button('Skip', (579, 455))
        self.advanceButton = Button('Advance', boundingBox = (348, 714, 931, 797), colorSum = 49559)

    def buildFood(self):
        # name, location, orderButton location, unavailablePixel, startingQuantity
        self.rice =   Food('Rice',      (88, 338),  (516, 276), unavailablePixel = (118, 83, 85, 255), quantity = 10)
        self.shrimp = Food('Shrimp',    (41, 330),  (461, 210), quantity = 5)
        self.nori =   Food('Nori',      (40, 393),  (464, 269), quantity = 10)
        self.roe =    Food('Roe',       (101, 388), (551, 275), quantity = 10)
        self.salmon = Food('Salmon',    (41, 453),  (468, 331), quantity = 5)
        self.unagi =  Food('Unagi',     (103, 442), (548, 211), quantity = 5)

    def buildPlates(self):
        xCoordinates = [85, 189, 280, 387, 484, 581]
        self.plates = []
        for x in xCoordinates:
            self.plates.append(GameObject('Plate', (x, 204)))

    def buildRecipes(self):
        self.caliroll = Recipe('California Roll', [self.nori, self.rice, self.roe], 4989)
        self.gunkan = Recipe('Gunkan', [self.nori, self.rice, self.roe, self.roe], 4352)
        self.onigiri = Recipe('Onigiri', [self.rice, self.rice, self.nori], 4345)
        self.recipes = [self.caliroll, self.gunkan, self.onigiri]

    def prepareRecipe(self, recipe):
        print 'Preparing ' + recipe.name
        for ingredient in recipe.ingredients:
            Controller.clickOn(ingredient)
            ingredient.consume()
        self.rollMat()
        lowIngredients = list(set(filter(lambda x: x.almostOut(), recipe.ingredients)))
        for ingredient in lowIngredients:
            self.restock(ingredient)

    def rollMat(self):
        Controller.clickOn(self.mat)
        sleep(1.5)

    def clearTables(self):
        print 'Clearing tables'
        for plate in self.plates:
            Controller.clickOn(plate)

    def restock(self, food):
        Controller.clickMenu(self.phone)
        Controller.clickMenu(self.phone.menuFor(food))
        #TODO: Clean this mess up
        location = tuple(map(lambda x: x*2, food.orderLocation()))
        pixel = Controller.screenGrab().getpixel(location)
        if food.availableForOrder(pixel):
            print food.name + ' is available...Ordering'
            Controller.clickMenu(food.orderButton)
            Controller.clickMenu(self.phone.orderButton)
            food.updateQuantity()
        else:
            print food.name + ' is unavailable...Hanging up'
            Controller.clickMenu(self.phone.hangUpButton)
            sleep(3)
            self.restock(food)

    def start(self):
        self.focus()
        # Controller.clickMenu(self.soundButton)
        Controller.clickMenu(self.playButton)
        Controller.clickMenu(self.continueButton)
        Controller.clickMenu(self.skipButton)
        Controller.clickMenu(self.continueButton)

    def getCustomerOrders(self):
        print 'Gathering customer orders'
        return Controller.getAllOrders()

    def prepareCustomerOrders(self, orders):
        for code in orders:
            results = filter(lambda recipe: recipe.withCode(code), self.recipes)
            if results: self.prepareRecipe(results[0])

    def isLevelComplete(self):
        return self.advanceButton.isPresent(self.colorAverage(self.advanceButton.boundingBox))

    def colorAverage(self, box):
        return Controller.rgbSum(box)

if __name__ == "__main__":
    print 'Starting a new game'
    g = Game()
    print 'Getting past menus'
    g.start()
    won = False
    while not won:
        orders = g.getCustomerOrders()
        g.prepareCustomerOrders(orders)
        g.clearTables()
        sleep(3)
        g.clearTables()
        sleep(3)
        won = g.isLevelComplete()
