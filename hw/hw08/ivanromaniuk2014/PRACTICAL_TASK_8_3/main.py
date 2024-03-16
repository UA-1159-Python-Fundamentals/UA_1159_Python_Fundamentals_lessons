from function_of_area import area_of_circle, area_of_rectangle, area_of_triangle

while True:
    choose = input("The area of ​​which geometric figure do you want to get?\n 1. triangle\n 2. rectan\n 3. circle\n 4. exit\n - Your choose: ")

    if choose not in "1234":
        print("Error. You can choose only 1, 2, 3 or 4")

    match choose:
        case "1":
            height = float(input("Enter the Height of the triangle\n - "))
            print(f"Area of triangle = {area_of_triangle (height, base)}\n")
        case "2":
            side_one = float(input("Enter the value of the first side\n - "))
            side_two = float(input("Enter the value of the second side\n - "))
            print(f"Area of rectagle = {area_of_rectangle(side_one, side_two)}\n")
        case "3":
            r = float(input("Enter the radius of circle\n - "))
            print(f"Area of circle = {area_of_circle(r)}\n")
        case "4":
            break
