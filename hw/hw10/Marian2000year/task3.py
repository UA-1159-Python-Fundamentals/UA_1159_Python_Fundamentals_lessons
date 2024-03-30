class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def display_total_employees(self):
        print(f"Total number of employees: {Employee.total_employees}")

    def display_employee_info(self):
        print(f"Employee name: {self.name}, Salary: {self.salary}")


print("Base classes:", Employee.__base__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation bar:", Employee.__doc__)


if __name__ == "__main__":
    emp1 = Employee("Alice", 50000)
    emp2 = Employee("Bob", 60000)
    emp3 = Employee("Charlie", 70000)

    emp1.display_total_employees()
    emp2.display_employee_info()