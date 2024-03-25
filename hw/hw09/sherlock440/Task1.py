from random import randint

generated_number = randint(1, 100)

is_guessed = False
guessed_number = int(input("Let's pay your fortune, little child. I generated a number, and you have to guess it in 10 "
                           "attempts. If you don't guess, your father will go for a cigarettes and will have never "
                           "return back.\n\nYour guessed number: "))
attempt = 0
while attempt < 9:
    if guessed_number not in range(1, 101):
        attempt += 1
        print(f"It seems you haven't understood the rules, but I don't give a fuck, you have lost your"
              f" attempt №{attempt}")
        guessed_number = int(input("\nTry again: "))
        continue

    elif guessed_number < generated_number:
        attempt += 1
        print(f"You have fucked up, your number is SMALLER than mine. Your father has already put his cloth №{attempt} "
              f"— he has just {10 - attempt} clothes left")
        guessed_number = int(input("\nTry again: "))
    elif guessed_number > generated_number:
        attempt += 1
        print(f"You have fucked up, your number is GREATER than mine. Your father has already put his cloth №{attempt} "
              f"— he has just {10 - attempt} clothes left")
        guessed_number = int(input("\nTry again: "))
    elif guessed_number == generated_number:
        attempt += 1
        print(f"I bet you are a cheater, because you have guessed my number doing it on your attempt №{attempt}!")
        break

else:
    print("I am sorry to say that (not really), but your father has been gone for good")