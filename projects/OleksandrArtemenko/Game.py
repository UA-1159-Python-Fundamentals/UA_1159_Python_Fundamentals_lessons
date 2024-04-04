from Deck import Deck
from Card import Card
from time import sleep
from BlackjackException import BlackjackException
import os


class Game:
    TIME_DELAY = 2
    scores = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10
    }

    def __init__(self, number_of_decks, player_bank, bet_amount):
        self.number_of_decks = number_of_decks
        self.deck = Deck(self.number_of_decks)
        self.deck.shuffle()
        self.initial_size = len(self.deck)
        self.player_bank = player_bank
        self.initial_bank = player_bank
        self.bet_amount = bet_amount
        self.player_hand = []
        self.dealer_hand = []
        self.hands = 0

        if self.player_bank < 0:
            raise BlackjackException("Bankroll cannot be less than zero")

        if self.bet_amount > self.player_bank or self.bet_amount < 0:
            raise BlackjackException("Size of the bet cannot exceed size of the player's bank or be less than zero")

    def refresh_deck(self):
        if len(self.deck) < 0.3 * self.initial_size:
            self.deck = Deck(self.number_of_decks)
            self.deck.shuffle()

    def refresh_hands(self):
        self.player_hand.clear()
        self.dealer_hand.clear()

    def deal_starting_hand(self):
        self.deck.deal_card(2, self.player_hand)
        self.deck.deal_card(2, self.dealer_hand)

    def deal_player_card(self):
        self.deck.deal_card(1, self.player_hand)

    def deal_dealer_card(self):
        self.deck.deal_card(1, self.dealer_hand)

    def display_hand_player_turn(self):
        sleep(self.TIME_DELAY)
        os.system("cls")
        print()
        print("*" * 30)
        print(f"Dealer's hand: {self.dealer_hand[0]}")
        print("Player's hand: ", end="")
        for card in self.player_hand:
            print(card, end=" ")
        print(f"\nPlayer's score: {self.calculate_score(self.player_hand)}")
        print("*" * 30)
        print()

    def display_hand_dealer_turn(self):
        sleep(self.TIME_DELAY)
        os.system("cls")
        print()
        print("*" * 30)
        print("Dealer's hand: ", end="")
        for card in self.dealer_hand:
            print(card, end=" ")
        print(f"\nDealer's score: {self.calculate_score(self.dealer_hand)}")
        print()
        print("Player's hand: ", end="")
        for card in self.player_hand:
            print(card, end=" ")
        print(f"\nPlayer's score: {self.calculate_score(self.player_hand)}")
        print("*"*30)
        print()

    def calculate_score(self, hand):
        score = 0
        for card in hand:
            if card.value != "A":
                score += self.scores[card.value]
        for card in hand:
            if card.value == "A" and score > 10:
                score += 1
            elif card.value == "A":
                score += 11
        return score

    def dealer_turn(self):
        if self.calculate_score(self.player_hand) <= 21:
            self.display_hand_dealer_turn()
            while self.calculate_score(self.dealer_hand) < 17:
                self.deal_dealer_card()
                self.display_hand_dealer_turn()

    def round_over(self):

        if self.calculate_score(self.player_hand) > 21:
            self.display_hand_dealer_turn()
            self.player_bank -= self.bet_amount
            print(f"Dealer wins! Current bank: {max(self.player_bank, 0)}")
        elif self.calculate_score(self.dealer_hand) > 21:
            self.display_hand_dealer_turn()
            self.player_bank += self.bet_amount
            print(f"Player wins! Current bank: {self.player_bank}")
        elif self.calculate_score(self.player_hand) < self.calculate_score(self.dealer_hand):
            self.display_hand_dealer_turn()
            self.player_bank -= self.bet_amount
            print(f"Dealer wins! Current bank: {max(self.player_bank, 0)}")
        elif self.calculate_score(self.player_hand) > self.calculate_score(self.dealer_hand):
            self.display_hand_dealer_turn()
            self.player_bank += self.bet_amount
            print(f"Player wins! Current bank: {self.player_bank}")
        else:
            self.display_hand_dealer_turn()
            print(f"It is a push! Current bank: {self.player_bank}")
        self.refresh_hands()
        self.hands += 1

    def ask_player_choice(self):
        player_choice = input("Please, choose your next turn: hit, stand or double\n")
        return player_choice

    def game_round(self):
        self.refresh_deck()
        player_choice = None
        self.deal_starting_hand()
        if self.calculate_score(self.player_hand) == 21:
            self.round_over()
            print("\nIt's a blackjack!")
            return

        while self.calculate_score(self.player_hand) < 21:

            while not player_choice:
                self.display_hand_player_turn()
                player_choice = self.ask_player_choice()
                match player_choice:
                    case "hit":
                        self.deal_player_card()
                        player_choice = None
                        if self.calculate_score(self.player_hand) == 21:
                            self.display_hand_player_turn()
                            self.dealer_turn()
                            self.round_over()
                            return
                        elif self.calculate_score(self.player_hand) > 21:
                            self.display_hand_player_turn()
                            self.round_over()
                            return
                    case "stand":
                        self.dealer_turn()
                        self.round_over()
                        return
                    case "double":
                        if self.bet_amount * 2 <= self.player_bank:
                            self.bet_amount *= 2
                            self.deal_player_card()
                            self.display_hand_player_turn()
                            self.dealer_turn()
                            self.round_over()
                            self.bet_amount /= 2
                            return
                        else:
                            player_choice = None
                            print(f"Bet cannot be doubled because of low balance. Current balance: {self.player_bank},"
                                  f" current bet: {self.bet_amount}")
                    case _:
                        player_choice = None
                        print("Invalid choice. You should choose hit, stand or double.")

        # self.round_over()
        # return


# if __name__ == "__main__":
#     new_game = Game(2, 1000, 100)
#     new_game.game_round()


