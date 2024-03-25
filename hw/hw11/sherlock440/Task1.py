def is_even(age):
    if age < 0:
        raise TypeError("Your age can't be negative, who the hell are you?")

    elif age % 2 == 0:
        print(f"Your age {age} is even")
    else:
        print(f"Your age {age} is odd")

age = int(input("Enter your age, big boy: "))

is_even(age)