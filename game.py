from food import *
from button import *
import controller as Controller

class Game:
    def __init__(self):
        self.coordinates = (0, 0)
        self.buttons = []
        self.generateButtons()

    def generateButtons(self):
        buttons = [
                        { 'name': 'Sound', 'coord': (302, 372) },
                        { 'name': 'Play', 'coord':  (311, 206) },
                        { 'name': 'Continue', 'coord':  (317, 393) },
                        { 'name': 'Skip', 'coord':  (579, 455) },
                  ]

        for button in buttons:
            self.buttons.append(Button(button['name'], button['coord']))

    def findButton(self, name):
        for button in self.buttons:
            if button.name == name: return button

    def start(self):
        Controller.clickOn(self) # Focus on browser
        for button in self.buttons:
           Controller.clickOn(button)
        Controller.clickOn(self.findButton('Continue'))

if __name__ == "__main__":
    g = Game()
    g.start()
