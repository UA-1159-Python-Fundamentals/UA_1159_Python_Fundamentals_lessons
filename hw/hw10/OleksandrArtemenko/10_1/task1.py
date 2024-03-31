class Polygon:

    def __init__(self, *args):
        self.sides = []
        for arg in args:
            if type(arg) in (int, float):
                self.sides.append(arg)

    def __str__(self):
        return f"This is a {len(self.sides)}-sided polygon."


class Rectangle(Polygon):

    def __init__(self, *args):
        super().__init__(*args)
        if len(self.sides) != 2:
            raise ValueError("You are passing values with which it is impossible to create a rectangle")

    def __str__(self):
        return "This is a rectangle."

    def calculate_area(self):
        return self.sides[0] * self.sides[1]


# pol = Polygon(1, 2, 3, 4, 5)
# print(pol)
# rec = Rectangle(3, 4)
# print(rec)
# print(rec.calculate_area())
