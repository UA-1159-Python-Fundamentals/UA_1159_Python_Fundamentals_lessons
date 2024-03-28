import functions

def inter_greeding():
    """The function for user greading. Once at the start ot the program"""

    print()
    print("Hello this is a program for calculate area!")
    print("You can choose one of the available figures")   

def inter_select():
    """The function reminds user how to navigate"""

    print("Enter 1 --> Rectangle")
    print("Enter 2 --> Triangle")
    print("Enter 3 --> Circle")
    print("Enter 0 --> End program")

def user_input():
    """The function validates user choise"""

    entered = input("Select\t>>>")
    if entered in ["1", "2", "3", "0"]:
        return entered
    else:
        print()
        print("Chose correct number!")
        user_input

def calc(s):
    """The function for calculate area"""

    global program

    if s == "0":
        program = False
        print("Good bye")
        return None
    elif s == "1":
        print("Your choise is Rectangle")
        length = int(input("Please enter the length:"))
        width = int(input("Please enter the width:"))
        return functions.calc_area_rec(length, width)
    elif s == "2":
        print("Your choise is Triangle")
        base = int(input("Please enter the base:"))
        height = int(input("Please enter the height:"))
        return functions.calc_area_tri(base, height)
    elif s == "3":
        print("Your choise is Circle")
        radius = int(input("Please enter the radius:"))
        return functions.calc_area_cir(radius)
    else:
        pass


program = True
inter_greeding()

while program == True:
    inter_select()
    entered = user_input()
    print("The area is:\t", calc(entered))
    print()