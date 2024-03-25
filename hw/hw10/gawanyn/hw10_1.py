class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width])  # Вказуємо довжину та ширину як сторони

    def calculate_area(self):
        length, width = self.sides
        return length * width

    def calculate_square(self):
        return self.calculate_area()

# Приклад використання
length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))
rectangle = Rectangle(length, width)

print("Area of the rectangle:", rectangle.calculate_area())
print("Square of the rectangle:", rectangle.calculate_square())
