def divide(numerator, denominator):
    # enter your code
    try:
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError
        
        if denominator == 0:
            raise ZeroDivisionError
        
        result = round(numerator / denominator, 2)
        return (f"Result is {result}")
    except ValueError:
        return ("Value Error! You did not enter a number!")
    except ZeroDivisionError:
        return (f"Oops, {numerator}/{denominator}, division by zero is error!!!")

print(divide(8, 4))
print(divide(8, 0))
print(divide("9", 3))