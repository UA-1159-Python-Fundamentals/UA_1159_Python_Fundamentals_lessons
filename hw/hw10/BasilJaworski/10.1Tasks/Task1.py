class Poligon():
    def __init__(self, num_of_sides):
        self.num_of_sides = num_of_sides
        self.sides = [0 for i in range(num_of_sides)]

    def enter_sides(self):
        """The entering sizes function"""
        self.sides = [float(input(f"Enter the side #{i+1}:")) for i in range(self.num_of_sides)]

    def return_sides(self):
        """The displaying sizes function"""
        for i in range(self.num_of_sides):
            print(f"Side {i+1} equal: {self.sides[i]}")


class Rectangle(Poligon):
    def __init__(self):
        Poligon.__init__(self, 2)

    def find_area(self):
        """The finding area function"""
        print(f"The area of your rect is: {self.sides[0]*self.sides[1]}!")


m = Rectangle()
m.enter_sides()
m.find_area()