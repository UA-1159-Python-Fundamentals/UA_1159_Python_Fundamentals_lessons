try:
    week_num = int(input("Enter num."))
    week = ["monday", "thusday", "thursday", "wednesday", "friday", "seterday", "sunday"]

    if week_num <= 0 or week_num >= 8:
        raise ValueError("Your num not range 1-7!!!")
    elif type(week_num) is not int:
        raise ValueError("Your num not integer!!!")
    else:
        print(f"{week[week_num -1]}")
except ValueError as error:
    print("Error", error)
        