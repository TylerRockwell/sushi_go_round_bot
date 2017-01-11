from button import Button
from controller import Controller
from customer import Customer
from food import Food
from game_location import GameLocation
from game_object import GameObject
from phone import Phone
from recipe import Recipe
from time import sleep
from vision import Vision
# All coordinates are based on a Retina display at 1920x1200 resolution
# with Chrome shifted to left half of screen


class Game:
    x_offset = 20
    y_offset = 250
    width = 639
    height = 480
    # TODO: Organize/Standardize hardcoded pixel locations

    def __init__(self):
        print 'Starting a new game'
        self.coordinates = (0, 0)
        self.location = GameLocation(self.x_offset, self.y_offset, self.width, self.height)
        self.vision = Vision(self.location)
        self.controller = Controller(self.location)
        self.phone = Phone()
        self._build_buttons()
        self._reset_food()
        self._build_customers()
        self._build_recipes()
        self.mat = GameObject('Mat', (199, 380))

    def play(self):
        print 'Getting past menus'
        self._start()
        while True:
            self._deal_with_unhappy_customers()
            self._prepare_customer_orders()
            sleep(6)
            self._clear_tables()
            if self._is_level_complete():
                self.advance_level()

    def _reset_food(self):
        self._build_food()
        self._build_sake()

    def _start(self):
        self._focus()
        self.controller.clickOn(self.sound_button)
        self.controller.clickOn(self.play_button)
        self.controller.clickMenu(self.continue_button)
        self.controller.clickMenu(self.skip_button)
        self.controller.clickMenu(self.continue_button)

    def _deal_with_unhappy_customers(self):
        unhappy_customers = self._find_unhappy_customers()
        if len(unhappy_customers) == 0:
            print 'Everyone looks happy'

        for customer in unhappy_customers:
            print customer.name + ' is unhappy.'
            self._serve_sake(customer)

    def _get_customer_orders(self):
        print 'Gathering customer orders'
        orders = map(lambda customer: self.vision.analyze(customer.orderBox()), self.customers)
        # Reverse order to reduce last customer wait time
        orders.reverse()
        return orders

    def _prepare_customer_orders(self):
        for code in self.get_customer_orders:
            results = filter(lambda recipe: recipe.withCode(code), self.recipes)
            if results:
                self._prepare_recipe(results[0])

    def _clear_tables(self):
        print 'Clearing tables'
        for customer in self.customers:
            self.controller.clickOn(customer.plate)

    def _is_level_complete(self):
        return self.advanceButton.isPresent(self.vision.analyze(self.advanceButton.boundingBox))

    def _advance_level(self):
        print 'Level complete'
        sleep(15)
        # There are 2 continue buttons to start the next level
        for _ in xrange(2):
            print 'Advancing to next level'
            self.controller.clickOn(self.advanceButton)
            sleep(1)
        self.reset_food()

    def _focus(self):
        self.controller.clickOn(self)

    def _build_buttons(self):
        self.sound_button = Button('Sound', (302, 372), boundingBox=(499, 717, 768, 772))
        self.play_button = Button('Play', (311, 206), boundingBox=(448, 342, 825, 477))
        self.continue_button = Button('Continue', (317, 393))
        self.skip_button= Button('Skip', (579, 455))
        self.advanceButton = Button('Advance', boundingBox=(348, 714, 931, 797), colorSum=49559)

    def _build_food(self):
        # This list is getting long...perhaps there are other classes hiding here
        # name, type, location, orderButton location, unavailablePixel, startingQuantity
        self.rice = Food('Rice', 'Base', (88, 338), (516, 276), (118, 83, 85, 255), quantity=10)
        self.shrimp = Food('Shrimp', 'Topping', (41, 330), (461, 210), quantity=5)
        self.nori = Food('Nori', 'Topping', (40, 393), (464, 269), quantity=10)
        self.roe = Food('Roe', 'Topping', (101, 388), (551, 275), quantity=10)
        self.salmon = Food('Salmon', 'Topping', (41, 453), (468, 331), quantity=5)
        self.unagi = Food('Unagi', 'Topping', (103, 442), (548, 211), quantity=5)

    def _build_sake(self):
        self.sake = []
        locations = [(430, 370), (415, 342)]
        for location in locations:
            self.sake.append(
                    Food('Sake', 'Sake', location, (516, 273), (160, 160, 160, 255), quantity=1))

    def _build_customers(self):
        self.customers = []
        for position in xrange(6):
            plate = self._build_plate(position)
            order = self._build_order(position)
            happiness = self._build_happiness(position)

            self.customers.append(Customer('Customer ' + str(position), plate, order, happiness))

    def _build_plate(self, position):
        plate_coordinates = [85, 189, 280, 387, 484, 581]
        plate_location = (plate_coordinates[position], 204)
        plate = GameObject('Plate', plate_location)
        return plate

    def _build_order(self, position):
        order_coordinates = [51, 253, 455, 657, 859, 1061]
        order_width = 121
        order_y = 122
        order_height = 29
        order_box = (
                        order_coordinates[position],
                        order_y,
                        order_coordinates[position] + order_width,
                        order_y + order_height
                   )
        order = GameObject('Order Bubble', boundingBox=order_box)
        return order

    def _build_happiness(self, position):
        happiness_coordinates = [100, 302, 504, 706, 908, 1110]
        happiness_width = 11
        happiness_y = 216
        happiness_height = 7
        happiness_box = (
                            happiness_coordinates[position],
                            happiness_y,
                            happiness_coordinates[position] + happiness_width,
                            happiness_y + happiness_height
                       )
        happiness = GameObject('Happiness Indicator', boundingBox=happiness_box, colorSum=548)
        return happiness

    def _build_recipes(self):
        self.cali_roll = Recipe('California Roll', [self.nori, self.rice, self.roe], 4989)
        self.gunkan = Recipe('Gunkan', [self.nori, self.rice, self.roe, self.roe], 4352)
        self.onigiri = Recipe('Onigiri', [self.rice, self.rice, self.nori], 4345)
        self.salmon_roll = Recipe(
                                    'Salmon Roll',
                                    [self.rice, self.nori, self.salmon, self.salmon],
                                    4320
                                )
        self.shrimp_sushi = Recipe(
                                    'Shrimp Sushi',
                                    [self.rice, self.nori, self.shrimp, self.shrimp],
                                    4767
                                 )
        self.unagi_sushi = Recipe(
                                    'Unagi Sushi',
                                    [self.rice, self.nori, self.unagi, self.unagi],
                                    4568
                                )
        self.recipes = [
                            self.cali_roll,
                            self.gunkan,
                            self.onigiri,
                            self.salmon_roll,
                            self.shrimp_sushi,
                            self.unagi_sushi
                       ]

    def _prepare_recipe(self, recipe):
        if recipe.anyIngredientMissing():
            return
        print 'Preparing ' + recipe.name
        for ingredient in recipe.ingredients:
            self.controller.clickOn(ingredient)
            ingredient.consume()
        self._roll_mat()
        for ingredient in recipe.lowIngredientList():
            self.restock(ingredient)

    def _roll_mat(self):
        self.controller.clickOn(self.mat)
        sleep(1.5)

    def _restock(self, food, attempt=0):
        self.controller.clickMenu(self.phone)
        self.controller.clickMenu(self.phone.menuFor(food))
        # TODO: Clean this mess up
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
            if attempt < 3:
                self._restock(food, attempt+1)

    def _find_unhappy_customers(self):
        unhappy_customers = []
        for customer in self.customers:
            if customer.isUnhappy(self.vision.analyze(customer.happinessMeterLocation())):
                unhappy_customers.append(customer)

        return unhappy_customers

    def _serve_sake(self, customer):
        servable_sake = filter(lambda sake: sake.soldOut() is False, self.sake)
        if len(servable_sake) > 0:
            sake = servable_sake[0]
            print "Let's get " + customer.name + " drunk"
            self.controller.clickOn(sake)
            self.controller.dragTo(customer.plate)
            self.controller.clickOn(customer.plate)
            sake.consume()


if __name__ == "__main__":
    g = Game()
    g.play()
