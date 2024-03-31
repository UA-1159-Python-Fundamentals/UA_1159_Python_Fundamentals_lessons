class Polygon:
    pass


class Rectangle(Polygon):

    def sqare_rectangle(self, a: int, b: int) -> int:
        sqare = a * b

        return sqare


rect_1 = Rectangle()

print(rect_1.sqare_rectangle(2, 3))
