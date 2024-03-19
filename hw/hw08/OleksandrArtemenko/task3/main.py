import area_calculator_service as service


def main():
    program_runs = True
    while program_runs:
        user_choice = input("Please, choose a figure to calculate its area: rectangle, triangle or circle. Type 'exit' "
                            "to terminate the program.\n")
        match user_choice:
            case "rectangle":
                side1 = float(input("Please, enter side1 value: "))
                side2 = float(input("Please, enter side2 value: "))
                print(f"Area of the rectangle with {side1} and {side2} side sizes is "
                      f"{service.rectangle_area_calculator(side1, side2)}.")

            case "triangle":
                base = float(input("Please, enter base value: "))
                height = float(input("Please, enter height value: "))
                print(f"Area of the triangle with base {base} and height {height} is "
                      f"{service.triangle_area_calculator(base, height)}.")

            case "circle":
                radius = float(input("Please, enter radius value: "))
                print(f"Area of the circle with {radius} radius is {service.circle_area_calculator(radius)}.")

            case "exit":
                program_runs = False

            case _:
                print("Please, enter a valid command.")


main()
