class Employee:

    count_employee = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count_employee += 1

    @classmethod
    def print_count_employee(cls):
        return f"We have {cls.count_employee} employeers!!!"
    
    def info_employee(self):
        return f"Name: {self.name}, Salary: {self.salary}"
    
    @classmethod
    def info_class(cls):
        print(f"__base__:{cls.__base__}")
        print(f"__dict__:{cls.__dict__}")
        print(f"__name__:{cls.__name__}")
        print(f"__module__:{cls.__module__}")
        print(f"__doc__:{cls.__doc__}")
    
emplploy1 = Employee("Andrii", 10000)
emplploy2 = Employee("Bohdan", 20000)
emplploy3 = Employee("Andrii", 30000)

print(Employee.print_count_employee())

print(emplploy1.info_employee())
print(emplploy2.info_employee())
print(emplploy3.info_employee())

Employee.info_class()



