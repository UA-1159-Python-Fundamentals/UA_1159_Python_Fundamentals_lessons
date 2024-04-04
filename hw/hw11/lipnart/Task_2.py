def check_day(number):
    week = {
        "1": "Monday",
        "2": "Tuesday",
        "3": "Wednesday",
        "4": "Thursday",
        "5": "Friday",
        "6": "Saturday",
        "7": "Sunday",
    }

    for i in week:
        if i == number:
            print(f"{number} : {week[i]}")
        elif not number.isdigit():
            raise ValueError("It's not a number")
        elif int(number) < 0 or int(number) > 8:
            raise ValueError("Entered Your number is not a number of the week")


check_day(input("Enter number the day of the week: "))
