class Employee:
    total_employees = 0
    def __init__(self, salary, name):
        self.salary = salary
        self.name = name
        Employee.total_employees += 1
    @classmethod
    def display_total_employees(cls):
        print(f"Amount of employees: {cls.total_employees}")
    def display_info(self):
        print(f"Name: {self.name}, salary: {self.salary}")

employee1 = Employee("Kate", 50000)
employee2 = Employee("Alex", 60000)

Employee.display_total_employees()

employee1.display_info()
employee2.display_info()
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