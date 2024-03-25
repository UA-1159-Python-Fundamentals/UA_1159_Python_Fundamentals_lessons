import random

number = random.randint(1, 100)

#print(number)

count = 0

while count < 10:

    user_number = int(input("--Try to guess the number--: \n"))

    if user_number == number:
        print("Greetings, your answer is correct")
        break
    elif user_number > number:
        print("Try again, your answer is more than a number")
    elif user_number < number:
        print("Try again, your answer is less than a number")
    count += 1
else:
    print("Your attempts are over")