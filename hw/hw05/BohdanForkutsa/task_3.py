def factorial(n):

    result = n 

    if n == 0 or n == 1:
        result = 1
    else:
        for i in range(2, n):
            result *= i
    
    return result

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))