class Human():
    
    species = "Homosapiens"
    
    def __init__(self, name):
        self.name = name
        print(f"--- Welcome, {self.name}!!!---")

    @classmethod
    def what_this_is_species(cls):
        return f"This is {cls.species}!!!"

    @staticmethod
    def text():
        return "Довільний текст."    
    


a = Human("Bohdan")
print(Human.what_this_is_species())
print(Human.text())