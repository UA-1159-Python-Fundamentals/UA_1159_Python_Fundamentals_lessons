class Animal:
    def __init__(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs
    
    def make_sound(self):
        pass
    
class Mammal(Animal):
    def __init__(self, name, species, legs):
        super().__init__(name, species, legs)

    def give_birth(self):
        return "Giving birth"
    
    def make_sound(self):
        return "Roar"
    
class Bird(Animal):
    def __init__(self, name, species, legs):
        super().__init__(name, species, legs)

    def lay_eggs(self):
        return "Laying eggs"
    
    def make_sound(self):
        return "Squawk"
    
class Reptile(Animal):
    def __init__(self, name, species, legs):
        super().__init__(name, species, legs)

    def shed_skin(self):
        return "Shdding skin"
    
    def make_sound(self):
        return "Hiss"
    
lion = Mammal("Simba", "Lion", 4)
print(lion.name, lion.species, lion.legs)
print(lion.make_sound())
print(lion.give_birth())

parrot = Bird("Polly", "Parrot", 2)
print(parrot.name, parrot.species, parrot.legs)
print(parrot.make_sound())
print(parrot.lay_eggs())