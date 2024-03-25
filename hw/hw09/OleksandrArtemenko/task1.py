from random import randint


def guessing_game():
    max_tries = 10
    player_tries = 0
    low_range = 1
    high_range = 100
    game_continues = True
    unsuccessful_guesses = []

    print(f"Welcome to the guessing game. You have {max_tries} to guess the number from {low_range} to {high_range}.")
    number_to_guess = randint(low_range, high_range + 1)
    user_input = 0

    while player_tries < max_tries and game_continues:
        print(number_to_guess)

        if len(unsuccessful_guesses) != 0:
            print(f"Past guesses: {unsuccessful_guesses}.")

        try:
            user_input = int(input("Please, enter a number: "))
        except ValueError:
            print(f"Please, input a number from {low_range} to {high_range} in valid format.")
            continue

        if user_input not in range(low_range, high_range + 1) or not isinstance(user_input, int):
            print(f"Please, enter a valid number from {low_range} to {high_range}.")
        elif user_input < number_to_guess:
            player_tries += 1
            unsuccessful_guesses.append(user_input)
            if player_tries != 10:
                print(f"Number for guessing is higher than yours. You have {max_tries - player_tries} tries left.")
        elif user_input > number_to_guess:
            player_tries += 1
            unsuccessful_guesses.append(user_input)
            if player_tries != 10:
                print(f"Number for guessing is lower than yours. You have {max_tries - player_tries} tries left.")
        else:
            player_tries += 1
            print(f"Congratulations, you have guessed the right number in {player_tries} tries.")
            game_continues = False
            break

        if player_tries == 10:
            print(f"Unfortunately, you have not guessed the number. It was {number_to_guess}.")


play_again = True
while play_again:
    guessing_game()
    while True:
        play_more = input("Do you want to play again? Type 'yes' or 'no': ")
        match play_more:
            case "yes":
                break
            case "no":
                play_again = False
                break
            case _:
                print("Please, type 'yes' or 'no'.")
