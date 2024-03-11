# Task1

even_divisible_by_2 = []
odd_divisible_by_3 = []
not_divisible_by_2_or_3 = []

for num in range(1, 11):
    if num % 2 == 0:
        even_divisible_by_2.append(num)
    if num % 2 != 0 and num % 3 == 0:
        odd_divisible_by_3.append(num)
    if num % 2 != 0 and num % 3 != 0:
        not_divisible_by_2_or_3.append(num)

print("Even numbers divisible by 2:", even_divisible_by_2)
print("Odd numbers divisible by 3:", odd_divisible_by_3)
print("Numbers not divisible by 2 and 3:", not_divisible_by_2_or_3)

# Task2

while True:
    login = input("Enter login: ")

    if login == "First":
        print("Welcome, user!")
        break  # Exit the loop if the login is correct

    print("Error: Invalid login. Please try again.")

print("End of program")
