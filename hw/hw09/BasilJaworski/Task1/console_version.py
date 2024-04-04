from random import randint

guess = randint(1, 100)
attempt = 0

print("Hello I create a number, guess it!")
program = True
while program:
    number = int(input(">>"))

    if attempt == 10:
        print(f"Sorry you lose... it was {guess}")
        break

    if number == guess:
        print("Excellent!")
        break
    elif number < guess:
        print("Your number is less...")
    elif number > guess:
        print("Your number is bigger...")
    attempt += 1
    