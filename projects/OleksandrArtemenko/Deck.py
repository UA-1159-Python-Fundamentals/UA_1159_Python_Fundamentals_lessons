from Card import Card
from random import shuffle
from BlackjackException import BlackjackException


class Deck:

    def __init__(self, number_of_standard_decks):
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.suits = ["hearts", "spades", "clubs", "diamonds"]

        if number_of_standard_decks in range(1, 9):
            self.number_of_standard_decks = number_of_standard_decks
        else:
            raise BlackjackException("The amount of decks must be in range between 1 and 8")

        self.deck = [Card(value, suit) for value in self.values for suit in self.suits] * self.number_of_standard_decks

    def __repr__(self):
        return str(self.deck) + f"\nA deck of {len(self.deck)} cards."

    def __len__(self):
        return len(self.deck)

    def shuffle(self):
        shuffle(self.deck)

    def deal_card(self, number, hand=None):
        if hand is None:
            hand = []
        for _ in range(number):
            card = self.deck[0]
            hand.append(card)
            self.deck.remove(card)
        return hand


# if __name__ == "__main__":
#
#     new_deck = Deck(3)
#     print(new_deck.number_of_standard_decks)
#     print(new_deck)
#     new_deck.shuffle()
#     print(new_deck)
#     pl_hand = new_deck.deal_card(2)
#     print(pl_hand)
#     print(new_deck)
#     new_deck.deal_card(1, pl_hand)
#     print(pl_hand)
#     print(new_deck)
#     new_deck.deal_card(1, pl_hand)
#     print(pl_hand)
#     print(new_deck)
#     print(len(new_deck))

