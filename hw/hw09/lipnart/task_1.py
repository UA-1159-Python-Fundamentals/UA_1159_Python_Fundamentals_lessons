import random

user_name = input("Hello! What is your name? \n")

number = random.randint(1, 100)

count_attempts = 0

while True:
    guess_number = int(input("Enter your number from range: 1 to 100: \n"))
    count_attempts += 1
    if guess_number == number:
        print(f"Good job, {user_name}! You are winner!")
        print(f"You spend {count_attempts} attempts")
        break
    elif 1 <= guess_number <= 100 and guess_number < number:
        print("Your number is less! Try again!")
    elif 1 <= guess_number <= 100 and guess_number > number:
        print("Your number is more! Try again!")
    else:
        print("Your number is not in range 1 to 40! Try again!")

    if count_attempts == 10:
        print("You lose!")
        break
