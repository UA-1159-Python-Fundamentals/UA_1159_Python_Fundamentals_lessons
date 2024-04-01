# Task 1.

def process_age():
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    if age % 2 == 0:
        print("Your age is even.")
    else:
        print("Your age is odd.")


try:
    process_age()
except ValueError as e:
    print("Invalid input:", str(e))


# Task 2.
def analyze_number():
    try:
        number = int(input("Enter a number (1-7) to determine the day of the week: "))

        if number < 1 or number > 7:
            print("Invalid input: Number should be between 1 and 7.")
        else:
            days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            day = days_of_week[number - 1]
            print("The corresponding day of the week is:", day)

    except ValueError:
        print("Invalid input: Please enter a numerical value.")


analyze_number()
