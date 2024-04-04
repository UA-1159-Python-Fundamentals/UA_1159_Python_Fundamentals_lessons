class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"{self.name}s age is {self.age}"

    def getInfo(self):
        return f"{self.name}s age is {self.age}"
    

john = Person("John", 34)
print(john.info)           
print(john.getInfo())