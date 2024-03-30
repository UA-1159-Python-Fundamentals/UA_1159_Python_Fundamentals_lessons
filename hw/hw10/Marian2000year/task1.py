class Polygon:
    def __init__(self, num_of_sides, length_of_side):
        self.num_of_sides = num_of_sides
        self.length_of_side = length_of_side

    
class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4, [length, width, length, width])

    def area(self):
        return self.length_of_side[0] * self.length_of_side[1]


if __name__ == "__main__":
    rectangle = Rectangle(40, 5)
    print("Area of the rectangle:", rectangle.area())