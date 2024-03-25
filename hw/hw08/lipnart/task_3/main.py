from area_figure import *

key = True

while key:
    choice = int(
        input(
            "The area of ​​which figure you want to calculate? \n 1) Rectangle; \n 2) Triangle; \n 3) Circle. \n 4) End program. \n Enter here number of Your choice: "
        )
    )

    if choice == 4:
        key = False
        print("Thank you\n")
    elif choice == 1:
        a = int(input('Enter side "a": '))
        b = int(input('Enter side "b": '))
        ar = area_rectangle(a, b)
        print(f"Area of Your rectangle: {ar}\n")
    elif choice == 2:
        a = int(input('Enter side "a": '))
        h = int(input('Enter heigh of triangle "h": '))
        ar = area_triangle(a, h)
        print(f"Area of Your triangle: {ar}\n")
    elif choice == 3:
        r = int(input('Enter radius of cicle "r": '))
        ar = area_circle(r)
        print(f"Area of Your circle: {ar}\n")
    else:
        print("You have entered an incorrect number\n")
