class Employee:
    total_employee =0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employee += 1
    
    def display_employee_info(self):
        print(f'Name: {self.name}, Salary: {self.salary}')
    
    @classmethod
    def display_total_employees(cls):
        print(f'Total employees: {cls.total_employee}')

emp1 = Employee("Ivan", 5000)
emp2 = Employee("Mariia", 6000)
Employee.display_total_employees()
emp1.display_employee_info()
emp2.display_employee_info()

print(f'Base class: {Employee.__base__}')
print(f'Spase name of class: {Employee.__dict__}')
print(f'Name class: {Employee.__name__}')
print(f'Modul in wish of defened class: {Employee.__module__}')
print(f'Documants of class: {Employee.__doc__}')


    

    