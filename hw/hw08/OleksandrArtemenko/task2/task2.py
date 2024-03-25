import re


def password_validator():
    validation_pattern = r"^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[$#@]).{6,16}$"
    password_input = input("Please, enter a password for validation: ")
    if re.fullmatch(validation_pattern, password_input):
        return True
    return False


print(password_validator())
