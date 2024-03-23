import math
class Sphere():
    def __init__(self, radius: int | float, mass: int | float):
        self.r = radius
        self.mass = mass

    def get_radius(self):
        return self.r

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round(4 / 3 * math.pi * (self.r ** 3), 5)

    def get_surface_area(self):
        return round(4 * math.pi * (self.r ** 2), 5)

    def get_density(self):
        return round(self.mass / Sphere.get_volume(self), 5)


ball = Sphere(2,50)
print(ball.get_radius())
print(ball.get_mass())
print(ball.get_volume())
print(ball.get_surface_area())
print(ball.get_density())