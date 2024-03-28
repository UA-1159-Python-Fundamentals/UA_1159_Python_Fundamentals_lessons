class MyError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def check_positive(number):
    try:
        number = float(number)
        if number > 0:
            return f"You input positive number: {number}"
        elif number < 0:
            raise MyError (f"You input negative number: {number}. Try again.")
        else:
            raise ValueError
    except ValueError:
        return "Error type: ValueError!"
    except MyError as me:
        return me
    
print(isinstance(check_positive("-235"), MyError))
