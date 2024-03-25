# Tas10.1
# Task1
class Polygon:
    pass
class Rectangle(Polygon):
    def multi(self,x,y):
        return x * y
r=Rectangle()
print(r.multi(5,5))

# Task2
class Human:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hello, my name is {self.name}!"

    @classmethod
    def species(cls):
        return "I am a Homosapiens."

    @staticmethod
    def message():
        return "text"

person = Human("John")
print(person.greet())
print(Human.species())
print(Human.message())

# Task3
class Employee:
    """Employee"""
    total_employees = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    @classmethod
    def display_total_employees(cls):
        print(f"Total employees: {cls.total_employees}")

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

employee1 = Employee("andriy", 50000)
employee2 = Employee("olexiy", 60000)
employee3 = Employee("maks", 55000)

Employee.display_total_employees()

employee1.display_info()
employee2.display_info()
employee3.display_info()
base_classes = Employee.__base__
print("Base classes:", base_classes)

class_namespace = Employee.__dict__
print("Class namespace:", class_namespace)

class_name = Employee.__name__
print("Class name:", class_name)

module_name = Employee.__module__
print("Module name:", module_name)

doc_string = Employee.__doc__
print("Documentation string:", doc_string)