class Human:
    def __init__(self, name):
        self.name = name

    def say_hallo(self):
        print(f'Hallo, {self.name}!')
    
    @classmethod
    def species(cls):
        return "In is Homo saoiens"
    
    @staticmethod
    def arbitrary_message():
        return "It is message from static method"
    
person = Human('Vasyl')
person.say_hallo()
print(Human.species())
print(Human.arbitrary_message())
