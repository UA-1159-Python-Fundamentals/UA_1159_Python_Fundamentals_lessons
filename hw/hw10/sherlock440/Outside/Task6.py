import re

class Example():
    pass

def class_name_changer(cls, new_name: str):
    if re.match(r"^[A-Z][a-zA-Z0-9]*$", new_name):
        cls.__name__ = new_name
    else:
        raise AttributeError("New class name must start with an uppercase letter and contain only alphanumeric characters.")

print(Example.__name__)
class_name_changer(Example, "NonExample")
print(Example.__name__)

class_name_changer(Example, "BlaBlaBlaExample")
print(Example.__name__)

# class_name_changer(Example, "hahaExample")
# print(Example.__name__)
#
# class_name_changer(Example, "1NonExample")
# print(Example.__name__)