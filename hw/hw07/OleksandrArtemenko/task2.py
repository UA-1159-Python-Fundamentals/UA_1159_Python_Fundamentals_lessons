import math


def rectangle_area(side1, side2):
    """
    :param side1: float
    :param side2: float
    :return: float
    calculates area of the rectangle (rounded to 2 decimal places), using sizes of two sides as input
    """
    return round(side1 * side2, 2)


def triangle_area(side1, side2, side3):
    """
    :param side1: float
    :param side2: float
    :param side3: float
    :return: float
    calculates area of the rectangle (rounded to 2 decimal places), using sizes of three sides as input, validates
    existence of a triangle (returns None if does not exist)
    """
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        return round(0.5 * (side1 + side2 + side3), 2)
    return None


def circle_area(radius):
    """
    :param radius: float
    :return: float
    calculates area of the circle (rounded to 2 decimal places), using radius as input
    """
    return round(math.pi * math.pow(radius, 2), 2)


def main():
    program_runs = True
    while program_runs:
        function_choice = input("Please, choose a figure to calculate its area - rectangle, triangle of circle. "
                                "If you want to exit the program, type 'exit'.\n")
        match function_choice:
            case "rectangle":
                side1 = float(input("Please, input side1: "))
                side2 = float(input("Please, input side2: "))
                print(f"Area of a rectangle with sides of size {side1} and {side2} is {rectangle_area(side1, side2)}.")

            case "triangle":
                side1 = float(input("Please, input side1: "))
                side2 = float(input("Please, input side2: "))
                side3 = float(input("Please, input side3: "))
                area = triangle_area(side1, side2, side3)
                if area is not None:
                    print(f"Area of a triangle with sides of size {side1}, {side2} and {side3} is "
                          f"{triangle_area(side1, side2, side3)}.")
                else:
                    print(f"Triangle with sides of size {side1}, {side2} and {side3} cannot exist.")

            case "circle":
                radius = float(input("Please, input radius: "))
                print(f"Area of a circle with radius of {radius} is {circle_area(radius)}.")

            case "exit":
                program_runs = False

            case _:
                print("Please, input valid choice of a figure.")


main()
