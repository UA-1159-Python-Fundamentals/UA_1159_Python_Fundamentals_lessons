class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.sides = [0 for i in range(num_sides)]

    def input_side(self):
        self.sides = [float(input(f'Enter side width {i+1}:')) for i in range(self.num_sides)] 

    def disp_side(self):
        for i in range(self.num_sides):
            print(f'Side {i+1} have width {self.sides[i]}')


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def finde_area(self):
        return self.sides[0] * self.sides[1]

rect = Rectangle()
rect.input_side()
rect.disp_side()
area = rect.finde_area()
print(f'Area rectangle: {area}')



