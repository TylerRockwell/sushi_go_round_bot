class Recipe:
    def __init__(self, name, ingredients, code):
        self.name = name
        self.ingredients = ingredients
        self._code = code

    def with_code(self, code):
        return self._code == code

    def low_ingredient_list(self):
        return list(set(filter(lambda ingredient: ingredient.almost_out(), self.ingredients)))

    def any_ingredient_missing(self):
        return len(filter(lambda ingredient: ingredient.sold_out(), self.ingredients)) > 0
