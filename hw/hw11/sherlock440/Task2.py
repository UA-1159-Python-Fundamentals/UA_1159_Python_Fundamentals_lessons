def what_is_the_day(day):
    match day:
        case "1": print("Monday")
        case "2": print("Tuesday")
        case "3": print("Wednesday")
        case "4": print("Thursday")
        case "5": print("Friday")
        case "6": print("Saturday")
        case "7": print("Sunday")
        case _: raise TypeError("You need more days in week to learn Python, yeah? (I hope you typped a number bigger "
                                "than 7, because in any other cases my question has no sense)")

what_is_the_day(input("Enter a number of the day, sweet pie: "))