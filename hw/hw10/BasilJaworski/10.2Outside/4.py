class Person:
    def __init__(self, name, age):
        self.__name = str(name)
        self.__age = int(age)
        
    @property
    def info(self):
        return f"{self.__name}s age is {str(self.__age)}"