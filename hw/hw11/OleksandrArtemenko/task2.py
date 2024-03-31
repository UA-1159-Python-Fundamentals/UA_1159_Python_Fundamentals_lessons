class DayOfWeekException(Exception):
    pass


def get_day_of_week(number):
    weekdays_dict = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
    if type(number) is int and number not in range(1, 8):
        raise DayOfWeekException("weekday with such number does not exist, it should be from 1 to 7")
    return weekdays_dict[number]


def main():
    try:
        user_input = int(input("Please, input number of a weekday: "))
        return get_day_of_week(user_input)
    except DayOfWeekException as e:
        return f"DayOfWeekException raised, {e}"
    except ValueError as e:
        return f"ValueError raised, {e}"


print(main())
