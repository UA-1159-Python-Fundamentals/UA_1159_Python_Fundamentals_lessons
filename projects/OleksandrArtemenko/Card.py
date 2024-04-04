class Card:

    dict_img = {"hearts": 9829, "spades": 9824, "clubs": 9827, "diamonds": 9830}

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value}{chr(self.dict_img[self.suit])}"


# if __name__ == "__main__":
#     card = Card("9", "hearts")
#     print(card)


