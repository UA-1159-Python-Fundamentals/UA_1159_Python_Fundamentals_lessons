import area_calculator

user_choice_are = str(input("What area you want to calculate: "))

match user_choice_are:

    case "rectangle":
        length = float(input("Please enter lenght of rectangle: "))
        width = float(input("Please enter width of rectangle: "))
        area_calculator.rectangle_area(length, width)
    case "triangle":
        height = float(input("Please enter height of triangle: "))
        base = float(input("Please enter base of triangle: "))
        area_calculator.triangle_area(height, base)
    case "circle":
        radius = float(input("Please enter radius of circle: "))
        area_calculator.circle_area(radius)
    case _:
        print("Invalid choice")