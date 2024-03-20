
def large_number(num1, num2):
    """Hi. Function return the largest number."""
    
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return print("num1 = num2")

print(large_number(5, 5))
print(large_number(6, 5))
print(large_number(5, 6))
