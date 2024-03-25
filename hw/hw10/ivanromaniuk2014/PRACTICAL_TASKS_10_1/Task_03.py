class Employee:
    """
    A class that represents an employee.

    Attributes:
        name (str): The name of the employee.
        salary (int): The salary of the employee.
        quantity_employeers (int): The total number of employees.

    Methods:
        __init__(self, name: str, salary: int): Initializes the employee with the given name and salary.
        calculate_quantity_of_employers(cls) -> int: Returns the total number of employees.
        display_employeer(self) -> str: Returns a string with the name and salary of the employee.
    """

    quantity_employeers = 0

    def __init__(self, name: str, salary: int):
        """
        Initializes the employee with the given name and salary.

        Args:
            name (str): The name of the employee.
            salary (int): The salary of the employee.
        """
        self.name = name
        self.salary = salary
        Employee.quantity_employeers += 1

    @classmethod
    def calculate_quantity_of_employers(cls) -> int:
        """
        Returns the total number of employees.

        Returns:
            int: The total number of employees.
        """
        return cls.quantity_employeers

    def display_employeer(self) -> str:
        """
        Returns a string with the name and salary of the employee.

        Returns:
            str: A string with the name and salary of the employee.
        """
        return f"The name of the employee: {self.name}, his selary: {self.salary}"

vasia = Employee("Vasia", 5000)
ivan = Employee("Ivan", 10000)
igor = Employee("Igor", 100)

print(Employee.calculate_quantity_of_employers())
print(Employee.display_employeer(igor))


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
