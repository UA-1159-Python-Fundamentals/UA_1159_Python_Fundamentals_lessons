import re

def valid_password(password):
    if len(password) < 6 or len(password) > 16:
        return False

    elif not any(char.islower() for char in password):
        return False

    elif not any(char.isupper() for char in password):
        return False

    elif not re.search("[$#@]", password):
        return False

    else:
        return True

password = input("enter your password: ")
if valid_password(password):
    print("Hello, your password is goed")
else:
    print("your password must include:"
          " min 6 max16 symbols, at least 1 lowercase "
          "and at least 1 uppercase letter, 1 number, "
          "at least 1 symbol $#@")

