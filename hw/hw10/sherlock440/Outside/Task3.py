class Human():
    people = [(), ()]  # in [0] index there will be a list men, in [1] there will be a list of women

    def __init__(self, name: str):
        self.name = name

    @classmethod
    def return_method(cls):
        return cls.people

class Man(Human):
    men = []

    def __init__(self, name: str):
        super().__init__(name)
        Man.men.append(self)

        Human.people.pop(0)
        Human.people.insert(0, tuple(Man.men))

    def __repr__(self):
        return f"Man({self.name})"

class Woman(Human):
    women = []

    def __init__(self, name: str):
        super().__init__(name)
        Woman.women.append(self)

        Human.people.pop(1)
        Human.people.insert(1, tuple(Woman.women))

    def __repr__(self):
        return f"Woman({self.name})"


adam = Man("Adam")
joe = Man("Joe")

eva = Woman("Eva")
liza = Woman("Liza")

print(Human.return_method())
