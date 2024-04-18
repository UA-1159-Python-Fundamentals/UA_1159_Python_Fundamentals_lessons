class Polygon:
    pass

class Rectangle(Polygon):

    def area_of_rectangle(self, a: int, b: int) -> int:
        self.a = a
        self.b = b
        return self.a * self.b


rectangle_one = Rectangle()

print(rectangle_one.area_of_rectangle(8, 10))
