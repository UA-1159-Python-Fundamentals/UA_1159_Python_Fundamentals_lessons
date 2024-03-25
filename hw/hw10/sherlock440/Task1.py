class Polygon:
    def __init__(self, description: str = None, **sides: int | float):
        """
        :param description: Describes the figure if it's needed.
        :param sides: Keys should be in str format without quotes, values should be in int | float. Ex: z = (A=10, B=20)
        """
        self.sides = sides
        self.names = tuple([key for key in sides])
        self.sides_number = len(self.sides)
        self.description = description

    def __repr__(self):
        return f"({', '.join([f'{side}={length}' for side, length in self.sides.items()])})"

    def __str__(self):
        if self.description:
            # [Rectangle (A=10, B=20)]
            return f"[{self.description} ({', '.join([f'{side}={length}' for side, length in self.sides.items()])})]"
        else:
            # (A=10, B=20)
            return f"({', '.join([f'{side}={length}' for side, length in self.sides.items()])})"

    def remove_side(self, name: str):
        print(f"From {self} deleted a side named {name}")
        del self.sides[name]

    def add_sides(self, **sides: int | float):
        for key, length in sides.items():
            self.sides[key] = length

    def print(self):
        print(self.sides)


class Rectangle(Polygon):
    def __init__(self, **sides: int | float):
        super().__init__(description="Rectangle", **sides)

    def square(self) -> int|float:
        a = self.sides[self.names[0]]
        b = self.sides[self.names[1]]

        return a * b


abc = Polygon(A=1, B=2, C=3)
print(abc)

abc.remove_side("B")
print(abc)

abc.add_sides(D=4, E=5)
print(abc)

abcd = Rectangle(A=10, B=20)
print(abcd)

square = abcd.square()
print(square)
