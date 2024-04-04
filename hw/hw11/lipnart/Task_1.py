def check_age(age):
    if age < 0:
        raise ValueError("Your age can't negative")
    elif age % 2 == 0:
        print("Your age is even")
    else:
        print("Your age is odd")
    
promts = int(input("Please, enter Your age: "))
check_age(promts)