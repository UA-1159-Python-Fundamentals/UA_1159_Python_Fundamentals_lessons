# Task1.
integer_list = [1, 2, 3, 4, 5]  # List with integer elements

float_list = []  # Empty list to store converted elements

for num in integer_list:
    float_num = float(num)  # Convert integer element to float
    float_list.append(float_num)  # Add converted float element to the new list

print(float_list)  # Print the list with float elements

# Task2.
n = int(input("Enter a number: "))  # Get the input number

fibonacci_sequence = [0, 1]  # Initialize the first two numbers

while fibonacci_sequence[-1] <= n:
    next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2]  # Calculate the next Fibonacci number
    fibonacci_sequence.append(next_num)  # Add the next number to the sequence

for num in fibonacci_sequence:
    if num <= n:
        print(num)

# Task3.
n = int(input("Enter a number: "))  # Get the input number

factorial = 1  # Initialize the factorial as 1

for i in range(1, n + 1):
    factorial *= i  # Multiply factorial by numbers from 1 to n

print(factorial)
