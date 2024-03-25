import math


def calculate_rectangle_area(a, b):
    return a * b


def calculate_triangle_area(a, h):
    return 0.5 * a * h


def calculate_circle_area(r):
    return math.pi * math.pow(r, 2)


def main():
    print("Which figure's area would you like to calculate?")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        side_a = float(input("Enter the length of side a: "))
        side_b = float(input("Enter the length of side b: "))
        area = calculate_rectangle_area(side_a, side_b)
        print("The area of the rectangle is:", area)
    elif choice == 2:
        base = float(input("Enter the length of the base: "))
        height = float(input("Enter the height: "))
        area = calculate_triangle_area(base, height)
        print("The area of the triangle is:", area)
    elif choice == 3:
        radius = float(input("Enter the radius: "))
        area = calculate_circle_area(radius)
        print("The area of the circle is:", area)
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
