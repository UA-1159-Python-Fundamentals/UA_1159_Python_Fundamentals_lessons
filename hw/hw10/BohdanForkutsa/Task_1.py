class Polygon():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area_rectangle(self, a, b):
        return a * b

class Rectangle(Polygon):
    pass


rectangle = Rectangle(10, 10)

print(rectangle.area_rectangle(rectangle.a, rectangle.b))