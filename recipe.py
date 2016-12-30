class Recipe:
    def __init__(self, name, ingredients, code):
        self.name = name
        self.ingredients = ingredients
        self.code = code

    def withCode(self, code):
        return self.code == code
