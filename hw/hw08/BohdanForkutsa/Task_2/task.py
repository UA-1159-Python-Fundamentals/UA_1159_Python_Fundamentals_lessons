import re

def validation_pass(password):
    if not re.search("[a-z]", password):
        print("Error. You not use low register. Please, try again.")
        return False

    if not re.search("[A-Z]", password):
        print("Error. You not use up register. Please, try again.")
        return False
    
    if not re.search("[0-9]", password):
        print("Error. You not use number. Please, try again.")
        return False
    
    if not re.search("[@#$]", password):
        print("Error. You not use !@#$%. Please, try again.")
        return False
    
    if len(password) < 6 or len(password) > 16:
        print("Error. Your password need has 6 - 16 element. Please, try again.")
        return False
    
    return True

user_password = input("Please write a password: \n")

if validation_pass(user_password):
    print("Your password is valid.")


# print(validation_pass("@QWERTY1"))
# print(validation_pass("@qwerty1"))
# print(validation_pass("@Qwerty"))
# print(validation_pass("Qwerty"))
# print(validation_pass("@Qw1"))
# print(validation_pass("@Qwerty1"))

