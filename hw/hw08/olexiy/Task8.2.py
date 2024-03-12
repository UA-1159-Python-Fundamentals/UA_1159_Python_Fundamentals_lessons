# Task 8.2
import re
def password_check(password):
    validation_counter=0
    if 6 <= len(password) <= 16:
        print("Validation 1")
        validation_counter+=1
    else:
        print("Password error 1")
    if re.search(r'[#@$]', password):
        print("Validation 2")
        validation_counter += 1
    else:
        print("Password error 2")
    if re.search(r'[a-z]',password):
        print("Validation 3")
        validation_counter += 1
    else:
        print("Password error 3")
    if re.search(r'[A-Z]',password):
        print("Validation 4")
        validation_counter += 1
    else:
        print("Password error 4")
    if validation_counter==4:
        return "All validations passed"
    else:
        return "Your password bad"
password=input("Enter your password: ")
print(password_check(password))

