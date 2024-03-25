class Polygon:
    pass

class Rectangle(Polygon):

    def area_of_rectangle(self, a: int, b: int) -> int:
        return a * b
    
rectangle_one = Rectangle()

print(rectangle_one.area_of_rectangle(5, 6))




