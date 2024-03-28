from math import pow
from math import pi as PI

def calc_area_rec(length, width):
    """The function takes length an width of the rectangle and returns area"""
    return length * width

def calc_area_tri(base, height):
    """The function takes base and height of the triangle and returns area"""
    return base * height * 0.5

def calc_area_cir(radius):
    """The function takes radius of the circle and returns area"""
    return PI * pow(radius, 2)
