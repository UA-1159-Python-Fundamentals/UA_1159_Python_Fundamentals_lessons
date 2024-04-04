from Game import Game
from time import sleep
from datetime import datetime
from BlackjackException import BlackjackException


if __name__ == "__main__":
    game_continues = True
    number_of_decks = None
    bankroll = None
    bet_size = None

    print("Welcome to the Blackjack game! Please, choose one of the following options: ")

    while not number_of_decks or not bankroll or not bet_size:
        try:
            number_of_decks = int(input("\nPlease, enter number of decks between 1 and 8 with which you want to play: "))
            bankroll = float(input("Please, enter your starting bank: "))
            bet_size = float(input("Please, enter size of your bet: "))
            game = Game(number_of_decks, bankroll, bet_size)
        except BlackjackException as e:
            print(e.description)
            print("Please, try again.")
            number_of_decks, bankroll, bet_size = (None, None, None)
        except Exception as e:
            # print(e)
            print("You have entered data in invalid format. Please, try again.")
            number_of_decks, bankroll, bet_size = (None, None, None)

    while game_continues:

        player_choice = None

        while not player_choice:
            sleep(game.TIME_DELAY)
            if game.player_bank == 0:
                game_continues = False
                print("Unfortunately, you have lost your balance.")
                break

            if game.player_bank < game.bet_amount:
                game.bet_amount = game.player_bank
                print(f"\nYour bet has been decreased to {game.bet_amount} because of low balance.")

            print(f"\nYour balance: {game.player_bank}. Your bet: {game.bet_amount}")
            print("Please, choose one of the following options: ")
            print("1. Proceed to the game")
            print("2. Change size of the bet")
            print("3. Increase bankroll")
            print("4. End the game")

            try:
                player_choice = int(input("Enter a number between 1 and 4 depending on your choice: "))

                match player_choice:
                    case 1:
                        game.game_round()
                    case 2:
                        game.bet_amount = float(input("Please, enter new size of your bet: "))
                        if game.bet_amount > game.player_bank:
                            game.bet_amount = game.player_bank
                            print(f"Bet size cannot be set at the level higher than size of your bankroll. "
                                  f"It has been set at the level of {game.bet_amount}")
                    case 3:
                        game.player_bank = float(input("Please, enter new size of your bankroll: "))
                    case 4:
                        game_continues = False
                        print("\nThank you for playing the game!")
                        print(f"Your initial balance was: {game.initial_bank}. "
                              f"Your final balance is: {game.player_bank}.")
                    case _:
                        print("Invalid choice. Please, enter a number between 1 and 4.")

            except Exception as e:
                print("Please, choose a valid option between 1 and 4")
                # print(e)
    else:
        with open("hand_history.txt", "a") as f:
            hand_history = {
                "time": str(datetime.now()),
                "decks played": game.number_of_decks,
                "hands played": game.hands,
                "starting bank": game.initial_bank,
                "closing bank": game.player_bank,
                "roi": f"{round((game.player_bank - game.initial_bank) / game.initial_bank * 100, 2)}%"
            }
            f.write(str(hand_history) + "\n")

