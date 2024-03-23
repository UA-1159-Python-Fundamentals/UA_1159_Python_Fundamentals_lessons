class Person():
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age
        self.__info = f"{self.__name}s age is {self.__age}"

    @property
    def info(self):
        return self.__info


john = Person("John", 34)

print(john.info)
