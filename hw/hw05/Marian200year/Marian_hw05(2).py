up_to_number = int(input("Please enter number to which you want print Fibonacci numbers: "))

number1 = 0
number2 = 1

while number1 <= up_to_number:
    print(number1, end=" ")
    number1, number2 = number2, number1+number2