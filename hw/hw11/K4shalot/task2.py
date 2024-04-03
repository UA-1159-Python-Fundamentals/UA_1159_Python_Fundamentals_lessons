def day_of_week(day):
    if day == ("1"):
        print("Monday")
    elif day == ("2"):
        print("Tuesday")
    elif day == ("3"):
        print("Wednesday")
    elif day == ("4"):
        print("Thursday")
    elif day == ("5"):
        print("Friday")
    elif day == ("6"):
        print("saturday")
    elif day == ("7"):
        print("sunday")
    else:
        raise TypeError("Number must be beetwen 1 and 7")

day_of_week(input())