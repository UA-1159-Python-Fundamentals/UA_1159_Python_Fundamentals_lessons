from math import pi, pow


def rectangle_area_calculator(side1, side2):
    return round(side1 * side2, 2)


def triangle_area_calculator(base, height):
    return round(0.5 * base * height, 2)


def circle_area_calculator(radius):
    return round(pi * pow(radius, 2), 2)
