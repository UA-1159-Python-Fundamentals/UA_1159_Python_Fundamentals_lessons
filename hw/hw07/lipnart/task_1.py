def lagest_number(num1, num2):
    """This function return lagest number of two numbers"""
    # l_num = lambda num1, num2: num1 if num1 > num2 else num2
    if num1 > num2:
        return num1
    else:
        return num2


print(lagest_number(10, 1))
print(lagest_number.__doc__)