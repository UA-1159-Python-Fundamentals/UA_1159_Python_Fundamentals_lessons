class employee():
    """The employee class"""
    total_num_employers = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.__class__.total_num_employers += 1

    def __del__(self):
        self.__class__.total_num_employers -= 1

    def info(self):
        print(f"Name: {self.name}. Salary: {self.salary}")
    
    @classmethod
    def employers(cls):
        print(f"The total number of employers is {cls.total_num_employers}")


person1 = employee("Adam", 1000)
person2 = employee("Lucy", 2000)
person3 = employee("Jack", 1500)

person1.info()
person2.info()
person3.info()

employee.employers()

print(f"Inherited from: {employee.__class__.__base__}")
print(f"The class namespase: {employee.__class__.__dict__}")
print(f"The class name: {employee.__class__.__name__}")
print(f"The module name: {employee.__class__.__module__}")
print(f"The documentation: {employee.__class__.__doc__}")