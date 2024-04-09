class Human():
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Hello {self.name}! Welcome to our party!")

    @classmethod
    def specie(cls):
        return "Homosapiens"
    
    @staticmethod
    def arbitrary():
        return "Your AD can be here for only 9.99$ per month!"


persone = Human("Gustavo")

persone.welcome()

print(f"This persone is {persone.specie()}")
print(f"I have a beautifull message for you: {persone.arbitrary()}")