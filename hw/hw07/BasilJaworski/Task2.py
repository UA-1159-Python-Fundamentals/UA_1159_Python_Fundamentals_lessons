def area_rec(length, width):
    """The function takes length and width and returns the area of rectangle"""
    return length * width

def area_tri(base, height):
    """The function takes base and height and returns the area of triangle"""
    return (base * height)/2

def area_cir(radius):
    """The function takes a radius and returns the area of circle"""
    return 3.14 * radius**2

def load_screen():
    """The function for display info about this program """
    print()
    print("Hi there!")
    print("This program will calculate area for you")
    print("You can choose one of the available figures, just enter the number below")

def choose_screen():
    """The function reminds user how to navigate"""
    print("For Rectangle\tEnter -> 1")
    print("For Triangle\tEnter -> 2")
    print("For Circle\tEnter -> 3")
    print("For Exit\tEnter -> 0")

def entered_data():
    """The function for entering data then calculating and returns results"""
    
    global program
    figure = input("Waiting for your choise: ")

    if figure == "1":
        print("So you choose the Rectangle area!")
        length = int(input("What is the length of the Rectangle: \t"))
        width = int(input("What is the width of the Rectangle: \t"))
        return f"The area is: {area_rec(length, width)}"
    
    elif figure == "2":
        print("So you choose the Triangle area!")
        base = int(input("What is the base of the Triangle: \t"))
        height = int(input("What is the height of the Triangle: \t"))
        return f"The area is: {area_tri(base, height)}"
    
    elif figure == "3":
        print("So you choose the Circle area!")
        radius = int(input("What is the radius of the Circle: \t"))
        return f"The area is: {area_cir(radius)}"
    
    elif figure == "0":
        program = False
        return "Good bye)"
    
    else:
        return "Try again:)"


program = True

load_screen()

while program == True:
    choose_screen()
    print(entered_data())
    print()