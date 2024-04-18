class Human:

    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f"Hello, {self.name}, welcome!"

    @classmethod
    def species(cls):
        return cls.species

    @staticmethod
    def mesaage():
        return "I`m a human"

Katya = Human("Katya")
print(Katya.greeting())
print(Human.species())
print(Katya.mesaage())
