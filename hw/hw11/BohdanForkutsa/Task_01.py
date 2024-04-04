
def ages():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Your age is negative.")
        elif age % 2 == 1:
            print("Your age is odd.")
        elif age % 2 == 0:
            print("Your age is even.")
    except ValueError as error:
        print("Error", error)

    
ages()
ages()
ages()

