#Task_1
class Ball(object):
    def __init__(self, ball_type="regular") -> None:
        self.ball_type = ball_type

#Task_2
from random import choice
class Ghost(object):
    def __init__(self):
        self.color = choice(("white", "yellow", "purple", "red"))

#Task_3
class Human():
    pass
class Man(Human):
    pass
class Woman(Human):
    pass
def God():
    adam = Man()
    eve = Woman()
    return(adam, eve)

#Task_4
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"

#Task_5
from math import pi
class Sphere(object):
    
    PI = pi
    
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        
    def get_mass(self):
        return self.mass    
    
    def get_radius(self):
        return self.radius
    
    def get_volume(self):
        return round(4 / 3 * Sphere.PI * self.radius ** 3, 5)
    
    def get_density(self):
        return round(self.mass / (4 / 3 * Sphere.PI * self.radius ** 3), 5)
    
    def get_surface_area(self):
        return round(4 * Sphere.PI * self.radius ** 2, 5)
 
#Task_6  
def class_name_changer(cls, new_name):
    if new_name[0].isupper() and new_name.isalnum():
        cls.__name__ = new_name
    else:
        raise ValueError("valid name")
    return cls
    
 