class Employee():
    """
    This docstring is for the task where I have to call __doc__.
    "data_base" variable is for a class method "info_about_each".
    """
    number = 0
    data_base = {}

    def __init__(self, name: str, salary: int | float):
        self.name = name
        self.salary = salary
        Employee.data_base[name] = salary
        Employee.number += 1

    @classmethod
    def total_number(cls):
        return cls.number

    @classmethod
    def info_about_each(cls):
        return cls.data_base


john = Employee("John White", 100)
jimmy = Employee("Jimmy White", 100)
jeffrey = Employee("Jeffrey Black", 70)

print(Employee.total_number())
print(Employee.info_about_each())

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
