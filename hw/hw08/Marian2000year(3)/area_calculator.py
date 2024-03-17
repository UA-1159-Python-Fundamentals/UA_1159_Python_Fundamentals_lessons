from math import pi

def rectangle_area(length, width):
    print(f"The area of rectangle with {length} length and {width} width is {length*width}")


def triangle_area(height, base):
    print(f"The area of triangle with {height} length and {base} width is {height*base/2}")
    

def circle_area(radius):
    print(f"The area of circle with {radius} radius is {round(pi*pow(radius, 2), 2)}")


