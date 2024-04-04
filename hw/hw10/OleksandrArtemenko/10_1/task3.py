class Employee:
    """
    Class that describes employee
    class attributes: employee_count(int) - counts all instances of class
    instance methods: employee_info - displays information about certain instance
    class methods:
    total_info_employees - displays total number of instances
    employee_class_info - displays different information about class
    """
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    @classmethod
    def total_info_employees(cls):
        print(f"Total number of employees: {cls.employee_count}.")

    def employee_info(self):
        print(f"Name: {self.name}, salary: {self.salary}.")

    @classmethod
    def employee_class_info(cls):
        print(f"Base classes: {cls.__base__}")
        print(f"Class namespace: {cls.__dict__}")
        print(f"Class name: {cls.__name__}")
        print(f"Module name: {cls.__module__}")
        print(f"Documentation bar: {cls.__doc__}")


# emp1 = Employee("Jack", 1000)
# emp2 = Employee("James", 2000)
# emp3 = Employee("John", 3000)
#
# Employee.total_info_employees()
# Employee.employee_class_info()
# emp1.employee_info()
# emp2.employee_info()
# emp3.employee_info()


