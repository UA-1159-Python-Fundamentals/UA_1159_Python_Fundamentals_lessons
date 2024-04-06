def dayOfWeek(dict_number_day):
    while True:
        try:
            number = int(input("Please enter a number: "))
            if number in dict_number_day:
                print(dict_number_day[number])
                break
            else:
                print("Sorry, invalid number! Please enter a number between 1 and 7.")
        except ValueError:
            print("Sorry, invalid input! Please enter an integer.")

number_day = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
    8: "Honday - Hello from K-Pax"
}

dayOfWeek(number_day)

