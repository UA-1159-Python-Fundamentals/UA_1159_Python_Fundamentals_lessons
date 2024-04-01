# I.
class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


# II.
import random


class Ghost:
    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        self.color = random.choice(colors)


# III.
class Human:
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


def God():
    adam = Man()
    eve = Woman()
    return adam, eve


# IV.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"


# V.
class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = (4 / 3) * 3.14159 * (self.radius ** 3)
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * 3.14159 * (self.radius ** 2)
        return round(surface_area, 5)

    def get_density(self):
        density = self.mass / self.get_volume()
        return round(density, 5)


# VI.
def class_name_changer(cls, new_name):
    if not new_name[0].isupper() or not new_name.isalnum():
        raise ValueError("Invalid class name")

    cls.__name__ = new_name

    return cls
