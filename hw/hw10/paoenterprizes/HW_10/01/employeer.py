class Employeer:
    """To do"""
    total_emp = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employeer.counter +=1


    def calc_emp(self):
        print("Total employeer: "+ Employeer.total_emp)


    def info(self):
        print("Ім'я "+ self.name + "\t" + "заробітна плата " + self.salary)


print("Base: ", Employeer.__base__)
print("Dict: ", Employeer.__dict__)
print("Name: ", Employeer.__name__)
print("Module name: ", Employeer.__module__)
print("Documentation: ", Employeer.__doc__)


dict = {'a':1,'b':2,'c':2}
print(len(dict))