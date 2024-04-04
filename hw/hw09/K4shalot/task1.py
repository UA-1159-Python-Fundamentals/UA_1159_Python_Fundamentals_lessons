from random import randint
attempts = 10
number = randint(0, 100)
while attempts > 0:
    guess = int(input("Guess a number between 0 and 100: "))
    
    if guess == number:
        print("Good!")
        break
    elif guess < number:
        print("too low.")
    else:
        print("too high.")
        
    attempts -= 1
    print("You have", attempts, "attempts left.")

if attempts == 0:
    print("try again")
