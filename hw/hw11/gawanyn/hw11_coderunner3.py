def check_odd_even(number):
    # enter your code
    try:
        if isinstance(number, int):
            if number % 2 == 0:
                return "Entered number is even"
            else:
                return "Entered number is odd"
        else:
            return "You entered not a number."    
    except ValueError:
        return "You entered not a number."