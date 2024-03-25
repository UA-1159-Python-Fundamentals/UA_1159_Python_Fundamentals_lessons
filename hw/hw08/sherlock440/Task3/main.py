from calculate import *

answer = input(f"If you also feel deja vu that we have already done a similar task, write the number of a figure in the"
               f" following list to find the area\n"
               "1. Rectangle (it's the hardest formula in Math, just warn you)\n"
               "2. Triangle (via height)\n"
               "3. Circle (I'll make you a present and will write one of arguments of the formula instead of you)\n"
               "==> ")

match answer:
    case "1":
        a = float(input("Enter the height: "))
        b = float(input("Enter the width: "))

        print(f"The area = {calculate_rectangle_area(a, b)}")

    case "2":
        a = float(input("Enter the underneath: "))
        h = float(input("Enter the height: "))

        print(f"The area = {calculate_triangle_area(a, h)}")

    case "3":
        r = float(input("Enter the radius (don't get confused with a diameter): "))

        print(f"The area = {calculate_circle_area(r)}")
