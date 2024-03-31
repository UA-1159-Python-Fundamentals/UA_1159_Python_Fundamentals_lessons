class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f"Welcome, {self.name}."

    @classmethod
    def info_species(cls, self=""):
        return f"{self.name + " of human type" if isinstance(self, Human) else "Human"} is a species of {cls.species}."

    @staticmethod
    def say_phrase():
        return "Hello"


# person = Human("Jack")
# print(person.welcome())
# print(Human.info_species())
# print(Human.info_species(person))
# print(person.info_species())
# print(Human.say_phrase())

