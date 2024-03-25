from math import pi
from math import pow

def area_of_rectangle(a, b):
    return a * b

def area_of_triangle(a, h):
    return 0.5 * a *h

def area_of_circle(r):
    return round(pi * pow(r, 2), 2)

__all__ = ['area_of_rectangle', 'area_of_triangle', 'area_of_circle']