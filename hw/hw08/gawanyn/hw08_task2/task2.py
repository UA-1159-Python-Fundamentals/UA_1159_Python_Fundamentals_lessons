password = input("Please enter the password: ")

if 6 <= len(password) <= 16:

    lowercase = False
    uppercase = False
    digit = False
    special_char = False

    for char in password:
        if char.islower():
            lowercase = True
        elif char.isupper():
            uppercase = True
        elif char.isdigit():
            digit = True
        elif char in "$#@":
            special_char = True

    if all([lowercase, uppercase, digit, special_char]):
        print("Pass valid")
    else:
        print("Pass invalid")
else:
    print("Pass length must be from 6 to 16")
        