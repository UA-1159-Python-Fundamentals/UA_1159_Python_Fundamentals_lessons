class Human:
    name = None
    species = 'Homosapiense'

    def __init__(self, name: str) -> None:
        self.name = name

    def welcome_message(self) -> str:
        print(f"Hello, {self.name}!")

    @classmethod
    def inf_spiese(cls) -> str:
        return cls.species
    
    @staticmethod
    def arbitrary_mesage() -> str:
        return "Welcome to modernity!"

lima = Human("Lima")
lima.welcome_message()
print(Human.inf_spiese())
print(lima.arbitrary_mesage())
