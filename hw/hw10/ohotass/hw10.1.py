# Task 1.
class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def get_area(self):
        pass


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4)  # Call the superclass constructor with 4 sides
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width


# Example usage
rectangle = Rectangle(5, 8)
area = rectangle.get_area()
print("Area of the rectangle:", area)


# Task 2.
class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def display_welcome_message(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message."


# Example usage
person1 = Human("Oksana")
person1.display_welcome_message()
print("Species:", Human.get_species())
print("Arbitrary message:", Human.arbitrary_message())


# Task 3.

class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    @classmethod
    def print_total_employees(cls):
        print("Total employees:", cls.total_employees)

    def display_employee_info(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


# Example usage
employee1 = Employee("Taras", 5000)
employee2 = Employee("Ivan", 6000)
employee3 = Employee("Bohdan", 5500)

Employee.print_total_employees()

employee1.display_employee_info()
employee2.display_employee_info()
employee3.display_employee_info()
print("Base classes:", Employee.__base__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)
