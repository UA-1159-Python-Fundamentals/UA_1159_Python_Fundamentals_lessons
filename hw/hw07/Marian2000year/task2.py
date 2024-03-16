from math import pi

def rectangle_area(length, width):
    return length*width

def triangle_area(height, base):
    return height*base/2

def circle_area(radius):
    return pi*radius**2

user_choice_are = str(input("What area you want to calculate: "))

match user_choice_are:

    case "rectangle":
        length = float(input("Please enter lenght of rectangle: "))
        width = float(input("Please enter width of rectangle: "))

        print(f"The area of rectangle with {length} length and {width} width is {rectangle_area(length, width)}")

    case "triangle":
        height = float(input("Please enter height of triangle: "))
        base = float(input("Please enter base of triangle: "))

        print(f"The area of triangle with {height} length and {base} width is {triangle_area(height, base)}")

    case "circle":
        radius = float(input("Please enter radius of circle: "))

        print(f"The area of circle with {radius} radius is {circle_area(radius).__round__(2)}")

    case _:
        print("Invalid choice")
