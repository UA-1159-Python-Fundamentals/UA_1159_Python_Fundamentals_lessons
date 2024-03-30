class Human:
    def __init__(self, name):
        self.name = name

    def display_welcome_message(self):
        print(f"Hello, {self.name}! Welcome.")

    @classmethod
    def species(cls):
        return "Homosapiens"

    @staticmethod
    def arbitrary_message():
        return "This is a static message. Humans are amazing!"


if __name__ == "__main__":
    person = Human("John")
    person.display_welcome_message()

    print("Species:", Human.species())

    print("Arbitrary Message:", Human.arbitrary_message())