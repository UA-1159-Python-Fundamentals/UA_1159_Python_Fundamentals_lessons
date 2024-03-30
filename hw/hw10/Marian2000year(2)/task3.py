class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self, name):
        super().__init__(name)

class Woman(Human):
    def __init__(self, name):
        super().__init__(name)

def God():
    adam = Man("Adam")
    eve = Woman("Eve")
    return [adam, eve]


adam, eve = God()
print(adam.name) 
print(eve.name) 