# Task1
def find_largest_number(a, b):
    """
    Returns the largest number of two numbers.

    Args:
        a (float or int): The first number.
        b (float or int): The second number.

    Returns:
        float or int: The largest number between a and b.

    Examples:
        >>> find_largest_number(3, 7)
        7
        >>> find_largest_number(-5, 0)
        0
        >>> find_largest_number(10.5, 10.5)
        10.5
    """
    return max(a, b)


docstring = find_largest_number.__doc__
print(docstring)

# Task2
from os import name
import math


def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width


def calculate_triangle_area(base, height):
    """Calculate the area of a triangle."""
    return 0.5 * base * height


def calculate_circle_area(radius):
    """Calculate the area of a circle."""
    return math.pi * radius ** 2


def main():
    print("Choose a shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = calculate_rectangle_area(length, width)
        print("The area of the rectangle is:", area)
    elif choice == "2":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = calculate_triangle_area(base, height)
        print("The area of the triangle is:", area)
    elif choice == "3":
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(radius)
        print("The area of the circle is:", area)
    else:
        print("Invalid choice!")


if name == "__main__":
    main()


# Task3
def count_characters(string):
    """Calculate the number of characters in a given string."""
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


input_string = "hello"
output = count_characters(input_string)
print(output)
