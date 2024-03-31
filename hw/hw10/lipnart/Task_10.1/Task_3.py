class Employee:
    counter = 0

    def __init__(self, name: str, salary: int) -> None:
        self.name = name
        self.salary = salary
        Employee.counter += 1

    @classmethod
    def numb_employees(cls) -> int:
        return f"Total number of employees: {cls.counter}"

    def inf_employee(self) -> str:
        print(f"The name of employee is {self.name}, his salary {self.salary}")


oleg = Employee("Oleg", 500)
oliver = Employee("Oliver", 700)
mark = Employee("Mark", 400)

Employee.inf_employee(oleg)
Employee.inf_employee(oliver)
Employee.inf_employee(mark)
print(Employee.numb_employees())


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
