#Task 1
class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width])

    def calculate_area(self):
        length, width = self.sides
        return length * width


length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))
rectangle = Rectangle(length, width)

print("Area of the rectangle:", rectangle.calculate_area())

#Task 2
class Human:
    def __init__(self, name):
        self.name = name
    
    def welcome_message(self):
        return f"Welcome, {self.name}!"
    
    @classmethod
    def species_info(cls):
        return "This is a species of Homosapiens."
    
    @staticmethod
    def arbitrary_message():
        return "This is a static method returning an arbitrary message."
    
#Task 3

class Employee:

    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def display_employee_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def display_total_employees(cls):
        print(f"Total number of employees: {cls.total_employees}")

    @classmethod
    def get_class_info(cls):
        print(f"Base classes: {cls.__base__}")
        print(f"Class namespace: {cls.__dict__}")
        print(f"Class name: {cls.__name__}")
        print(f"Module name: {cls.__module__}")
        print(f"Documentation: {cls.__doc__}")

# Example usage:
employee1 = Employee("John", 50000)
employee2 = Employee("Alice", 60000)
employee3 = Employee("Max", 100000)

# Display information about each employee
employee1.display_employee_info()
employee2.display_employee_info()
employee3.display_employee_info()

# Display total number of employees
Employee.display_total_employees()

# Display class information
Employee.get_class_info()