from random import randint

def guess_number():
    number_to_guess = randint(1, 100)
    attempts = 10

    while attempts > 0:
        guess = int(input("Вгадай цифру від 1 до 100: "))

        if guess < number_to_guess:
            print("Ваша цифра МЕНЬША, спробуйте ще")
        elif guess > number_to_guess:
            print("Ваша цифра БІЛЬША, спробуйте ще")
        else:
            print("Вітаю, ваша цифра вірна!")
            return
            break

        attempts -= 1
        print("Залишилось спроб:", attempts)

    print("У вас закінчились спроби. Цифра була:", number_to_guess)


guess_number()
