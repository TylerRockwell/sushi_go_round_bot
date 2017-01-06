from button import *
from controller import *
from customer import *
from food import *
from game_location import *
from game_object import *
from phone import *
from recipe import *
from time import sleep
from vision import *
# All coordinates are based on a Retina display at 1920x1200 resolution
# with Chrome shifted to left half of screen
class Game:
    xOffset = 20
    yOffset = 250
    width = 639
    height = 480

    def __init__(self):
        self.coordinates = (0, 0)
        self.location = GameLocation(self.xOffset, self.yOffset, self.width, self.height)
        self.vision = Vision(self.location)
        self.controller = Controller(self.location)
        self.buildButtons()
        self.buildFood()
        self.buildCustomers()
        self.buildRecipes()
        self.mat = GameObject('Mat', (199, 380))
        self.phone = Phone()

    def focus(self):
        self.controller.clickOn(self)

    def buildButtons(self):
        self.soundButton = Button('Sound', (302, 372), boundingBox = (499, 717, 768, 772))
        self.playButton = Button('Play', (311, 206), boundingBox = (448, 342, 825, 477))
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

    def buildCustomers(self):
        orderCoordinates = [51, 253, 455, 657, 859, 1061]
        orderWidth = 121
        plateCoordinates = [85, 189, 280, 387, 484, 581]
        self.customers = []
        for position in xrange(6):
            orderBox = (orderCoordinates[position], 122, orderCoordinates[position] + orderWidth, 151)
            plateLocation = (plateCoordinates[position], 204)

            plate = GameObject('Plate', plateLocation)
            order = GameObject('Order Bubble', boundingBox = orderBox)
            self.customers.append(Customer(plate, order))

    def buildRecipes(self):
        self.caliRoll = Recipe('California Roll', [self.nori, self.rice, self.roe], 4989)
        self.gunkan = Recipe('Gunkan', [self.nori, self.rice, self.roe, self.roe], 4352)
        self.onigiri = Recipe('Onigiri', [self.rice, self.rice, self.nori], 4345)
        self.salmonRoll = Recipe('Salmon Roll', [self.rice, self.nori, self.salmon, self.salmon], 4320)
        self.shrimpSushi = Recipe('Shrim Sushi', [self.rice, self.nori, self.shrimp, self.shrimp], 4767)
        self.unagiSushi = Recipe('Unagi Sushi', [self.rice, self.nori, self.unagi, self.unagi], 4568)
        self.recipes = [self.caliRoll, self.gunkan, self.onigiri, self.salmonRoll, self.shrimpSushi, self.unagiSushi]

    def prepareRecipe(self, recipe):
        if recipe.anyIngredientMissing():
            return
        print 'Preparing ' + recipe.name
        for ingredient in recipe.ingredients:
            self.controller.clickOn(ingredient)
            ingredient.consume()
        self.rollMat()
        for ingredient in recipe.lowIngredientList():
            self.restock(ingredient)

    def rollMat(self):
        self.controller.clickOn(self.mat)
        sleep(1.5)

    def clearTables(self):
        print 'Clearing tables'
        for customer in self.customers:
            self.controller.clickOn(customer.plate)

    def restock(self, food, attempt = 0):
        self.controller.clickMenu(self.phone)
        self.controller.clickMenu(self.phone.menuFor(food))
        #TODO: Clean this mess up
        location = tuple(map(lambda x: x*2, food.orderLocation()))
        pixel = self.vision.screenGrab().getpixel(location)
        print str(food.quantity) + ' ' + food.name + ' remaining. Trying to restock'
        if food.availableForOrder(pixel):
            print food.name + ' is available...Ordering'
            self.controller.clickMenu(food.orderButton)
            self.controller.clickMenu(self.phone.orderButton)
            food.updateQuantity()
        else:
            print food.name + ' is unavailable...Hanging up'
            self.controller.clickMenu(self.phone.hangUpButton)
            print 'Waiting for income...'
            sleep(3)
            if attempt < 3: self.restock(food, attempt + 1)

    def start(self):
        self.focus()
        self.controller.clickWithin(self.soundButton)
        self.controller.clickWithin(self.playButton)
        self.controller.clickMenu(self.continueButton)
        self.controller.clickMenu(self.skipButton)
        self.controller.clickMenu(self.continueButton)

    def getCustomerOrders(self):
        print 'Gathering customer orders'
        orders = map(lambda customer: self.vision.analyze(customer.orderBox()), self.customers)
        # Reverse order to reduce last customer wait time
        orders.reverse()
        return orders

    def prepareCustomerOrders(self, orders):
        for code in orders:
            results = filter(lambda recipe: recipe.withCode(code), self.recipes)
            if results: self.prepareRecipe(results[0])

    def isLevelComplete(self):
        return self.advanceButton.isPresent(self.vision.analyze(self.advanceButton.boundingBox))

    def advanceLevel(self):
        print 'Level complete'
        sleep(15)
        # There are 2 continue buttons to start the next level
        for _ in xrange(2):
            print 'Advancing to next level'
            self.controller.clickWithin(self.advanceButton)
            sleep(1)
        return Game() # TODO: Reset inventory properly

if __name__ == "__main__":
    print 'Starting a new game'
    g = Game()
    print 'Getting past menus'
    g.start()
    while True:
        orders = g.getCustomerOrders()
        g.prepareCustomerOrders(orders)
        sleep(6)
        g.clearTables()
        if g.isLevelComplete(): g = g.advanceLevel()
