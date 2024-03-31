def massage():
    return "agu agu"


class Human:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("hello " + self.name)

    def species(self):
        print(self.name +" is homosapiens")