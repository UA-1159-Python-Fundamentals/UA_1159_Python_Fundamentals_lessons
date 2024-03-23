from math import pow, pi

def calculate_area_rectangle(length, width):
    '''Function return area rectangle.'''
    return length*width

# print(calculate_area_rectangle(10, 5))

def calculate_area_triangle(a, h):
    '''Function return area triangle.
    a = side of a triangle.
    h = height of the triangle.'''
    return (a*h)/2

# print(calculate_area_triangle(10, 5))

def calculate_area_circle(r):
    '''Function return area circle.
    r = circle radius'''
    return pi*pow(r, 2)
# print(calculate_area_circle(2))