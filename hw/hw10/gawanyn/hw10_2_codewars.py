#Task 1 Ball-super-ball

class Ball(object):
    # your code goes here
    def __init__ (self, ball_type = "regular"):
        self.ball_type = ball_type

#Task 2 Color-ghost
        
import random

class Ghost(object):
    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        self.color = colors[random.randint(0, len(colors) - 1)]

#Task 3 Basic-subclasses-Adam-and-Eve
        
class Human:
    def __init__(self, name):
        self.name = name
        
class Man(Human):
    def __init__(self, name):
        super().__init__(name)
        
class Woman(Human):
    def __init__(self, name):
        super().__init__(name)
        
class God:
    def __init__(self):
        self.paradise = self.create()

    def create(self):
        adam = Man("Adam")
        eve = Woman("Eve")
        return [adam, eve]
    
    def __getitem__(self, index):
        return self.paradise[index]
    
    def __len__(self):
        return len(self.paradise)
    
#Task 4 Classy-classes
    
class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"

#Task 5 Building Spheres

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
        volume = (4/3) * math.pi * self.radius ** 3
        return round(volume, 5)
    
    def get_surface_area(self):
        surface_area = 4 * math.pi * self.radius ** 2
        return round(surface_area, 5)
    
    def get_density(self):
        density = self.mass / self.get_volume()
        return round(density, 5)
    
#Task 6 Dynamic Classes
    
def class_name_changer(cls, new_name):
    if not new_name[0].isupper() or not new_name.isalnum():
        raise ValueError("New class name must start with an uppercase letter and contain only alphanumeric characters.")

    cls.__name__ = new_name