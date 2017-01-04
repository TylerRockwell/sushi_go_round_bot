class Recipe:
    def __init__(self, name, ingredients, code):
        self.name = name
        self.ingredients = ingredients
        self.code = code

    def withCode(self, code):
        return self.code == code

    def lowIngredientList(self):
        return list(set(filter(lambda ingredient: ingredient.almostOut(), self.ingredients)))

    def anyIngredientMissing(self):
        return len(filter(lambda ingredient: ingredient.soldOut(), self.ingredients)) > 0
