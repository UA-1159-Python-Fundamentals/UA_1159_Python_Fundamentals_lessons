def calculate_rectangle_area(a, b):
    return a * b

def calculate_triangle_area(a, h):
    return 0.5 * a * h

def calculate_circle_area(r):
    PI = 3.14
    return PI * (r ** 2)

answer = input("Hello a young Math learner and cheater, area of what object you are lazy to calculate by yourself?\n\n"
               "Type only the number of the item:\n"
               "1. Rectangle (it's the hardest formula in Math, just warn you)\n"
               "2. Triangle (via height)\n"
               "3. Circle (I'll make you a present and will write one of arguments of the formula instead of you)\n"
               "==> ")
print()

match answer:
    case "1":
        a = float(input("Enter the height: "))
        b = float(input("Enter the wigth: "))

        print(f"The area = {calculate_rectangle_area(a, b)}")

    case "2":
        a = float(input("Enter the underneath: "))
        h = float(input("Enter the height: "))

        print(f"The area = {calculate_triangle_area(a, h)}")

    case "3":
        r = float(input("Enter the radius (don't get confused with a diameter): "))

        print(f"The area = {calculate_circle_area(r)}")