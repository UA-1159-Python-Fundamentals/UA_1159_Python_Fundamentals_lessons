import random

counter = 1
number_to_guess = random.randint(1, 100)
entered_number = int(input("Please enter number (10 attempts): "))
print(number_to_guess)

while counter < 10:
    if entered_number == number_to_guess:
        print("Winner winner chicken dinner")
        break
    elif entered_number > number_to_guess:
        counter +=1
        entered_number = int(input(f"Your number is too high. Enter lower (attempt № {counter})"))

    elif entered_number < number_to_guess:
        counter +=1
        entered_number = int(input(f"Your number is too low. Enter higher (attempt № {counter})"))
else:
    print("Sorry. You have use maximum attempts")