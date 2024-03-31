# Task1 (https://www.codewars.com/kata/regular-ball-super-ball)

class Ball(object):

    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


# Task2 (https://www.codewars.com/kata/color-ghost)

import random


class Ghost(object):

    def __init__(self):
        self.color = random.choice(("white", "yellow", "purple", "red"))


# Task3 (https://www.codewars.com/kata/basic-subclasses-adam-and-eve)

def God():
    return [Man(), Woman()]


class Human:
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


# Task4 (https://www.codewars.com/kata/classy-classes)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"


# Task5 (https://www.codewars.com/kata/55c1d030da313ed05100005d)

import math


class Sphere(object):

    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round(4 / 3 * math.pi * math.pow(self.radius, 3), 5)

    def get_surface_area(self):
        return round(math.pi * math.pow(2 * self.radius, 2), 5)

    def get_density(self):
        return round(self.mass / (4 / 3 * math.pi * math.pow(self.radius, 3)), 5)


# Task6 (https://www.codewars.com/kata/55ddb0ea5a133623b6000043)

def class_name_changer(cls, new_name):
    if new_name.isalnum() and new_name[0].isupper():
        cls.__name__ = new_name
    else:
        raise ValueError
