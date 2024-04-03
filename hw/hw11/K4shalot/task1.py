def age_1(age):
    if age < 0:
        raise TypeError("negative")
    elif age % 2 == 0:
        print(f"age {age} is even")
    else:
        print(f"age {age} is odd")

age_1(int(input()))