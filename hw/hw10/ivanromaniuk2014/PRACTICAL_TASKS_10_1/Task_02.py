class Human:

    species = "Homosapiens"
    def __init__(self, name:str) -> None:
        self.name = name
    def greeting (self) -> str:
        print(f"Hello {self.name}. I am glad to see you")

    @classmethod
    def species_info(cls) -> str:
        return cls.species
    
    @staticmethod
    def arbitrary_message() -> str:
        return "I am a human"
    

vasia = Human("Vasil")
vasia.greeting()
print(Human.species_info())
print(vasia.arbitrary_message())