# Task10.2
# Task1
class Ball:
    def __init__(self,type="regular"):
        self.type =type
    def type_of_ball(self):
        print(f"{self.type}")
ball1=Ball()
ball1.type_of_ball()

# Task2
import random
class Ghost:
    def __init__(self):
        self.colors=["yellow","red","purple","white"]
        self.color=random.choice(self.colors)
ghost1=Ghost()
print(ghost1.color)

# Task3
class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def creation():
    adam = Man()
    eve = Woman()
    return [adam, eve]

adam, eve = creation()
print(adam)
print(eve)

# Task4
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_info(self):
        print(f"{self.name} is {self.age}")
person1=Person("ivan",34)
person1.get_info()

# Task5
from math import pi
class Sphere:
    def __init__(self,radius,mass):
        self.radius=radius
        self.mass=mass
    def radius_sphere(self):
        print(self.radius)
    def mass_sphere(self):
        print(self.mass)
    def volume_sphere(self):
        return round((4/3)*pi*self.radius**3,5)
    def surface_area(self):
        return round(4*pi*self.radius**2,5)
    def density(self):
        v=self.volume_sphere()
        return self.mass/v


sphere1=Sphere(4,6)
sphere1.radius_sphere()
sphere1.mass_sphere()
print(sphere1.volume_sphere())
print(sphere1.surface_area())
print(sphere1.density())

# Task6
def change_class_name(cls, new_name):
    if not new_name[0].isupper() or not new_name.isalnum():
        raise ValueError("New class name must start with an uppercase letter and contain only alphanumeric characters")
    new_class = type(new_name,(cls,),{})
    return new_class

class MyClass:
    pass

UsefulClass = change_class_name(MyClass, "UsefulClass")

SecondUsefulClass = change_class_name(UsefulClass, "SecondUsefulClass")
print(SecondUsefulClass.__name__)
