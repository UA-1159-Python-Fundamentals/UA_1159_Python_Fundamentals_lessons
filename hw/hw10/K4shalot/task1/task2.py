class Human:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hello, my name is {self.name}!"

    @classmethod
    def species(cls):
        return "I am a Homosapiens."

    @staticmethod
    def message():
        return "text"

person = Human("John")
print(person.greet())
print(Human.species())
print(Human.message())

class Human:
    def __init__(self, name):
        self.name = name