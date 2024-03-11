#Task 1 

#list_integers_number = [i for i in range(100)]
#
#list_float_numbers = []
#
#for i in list_integers_number:
#    list_float_numbers.append(float(i))
#
#print(list_float_numbers)

#Task 2

#number_fib_length = int(input("Enter the Fibonacci length: "))
#sequence_fib = [0, 1]
#
#if number_fib_length == 1:
#    print(sequence_fib[0])
#elif number_fib_length == 2:
#    print(sequence_fib[1])
#elif number_fib_length <= 0:
#    print("The Fibonacci lenght must be greater than 0")
#
#else:
#    for i in range(1, number_fib_length - 1):
#        sequence_fib.append(sequence_fib[i - 1] + sequence_fib[i])
#    sequence_fib_str = ", ".join(map(str, sequence_fib))
#    print(sequence_fib_str)

#Task 3

#number_factorial_user = int(input("Enter the factorial number(n): "))
#number_factorial = 1
#
#if number_factorial_user == 0:
#    print(f"Factorial n = {number_factorial}")
#else:
#
#    for i in range(number_factorial_user):
#        number_factorial = number_factorial * (i + 1)
#    print(f"Factorial n = {number_factorial}")