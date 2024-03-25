import random


def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 10

    while attempts > 0:
        guess = int(input("Guess the number (1-100): "))

        if guess < number_to_guess:
            print("The number is greater than your guess")
        elif guess > number_to_guess:
            print("The number is less than your guess")
        else:
            print("Congratulations! You guessed the number correctly!")
            return

        attempts -= 1
        print("Attempts left:", attempts)

    print("Sorry, you ran out of attempts. The number was:", number_to_guess)


guess_number()
