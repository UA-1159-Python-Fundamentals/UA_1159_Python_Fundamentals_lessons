import re

def is_valid(password):
    a_z = re.findall(r'[a-z]', password)
    if a_z:
        print(f"✅ You password contains at least 1 symbol between [a-z]. Here is the list: {a_z}")
    else:
        print("❌ Your password must contain at least 1 symbol between [a-z]")

    A_Z = re.findall(r'[A-Z]', password)
    if A_Z:
        print(f"✅ You password contains at least 1 symbol between [A-Z]. Here is the list: {A_Z}")
    else:
        print("❌ Your password must contain at least 1 symbol between [A-Z]")

    number = re.findall(r'[0-9]', password)
    if number:
        print(f"✅ You password contains at least 1 symbol between [0-9]. Here is the list: {number}")
    else:
        print("❌ Your password must contain at least 1 symbol between [0-9]")

    character = re.findall(r'\$|#|@', password)
    if character:
        print(f"✅ You password contains at least 1 symbol between [$#@]. Here is the list: {character}")
    else:
        print("❌ Your password must contain at least 1 symbol between [$#@]")

    length = 6 <= len(password) <= 16
    if length:
        print(f"✅ You password has an acceptable length — {len(password)}")
    else:
        print(f"❌ The length of your password is {len(password)}, but it must be not less than 6 and not more than 16")



    if a_z and A_Z and number and character and length:
        print(f"\nYour password {'*'*(len(password))} is valid")
        return True
    else:
        print(f"\nYou have fucked up with your password {'*'*(len(password))}")
        return False



password = input("Type your password, honey: ")
is_valid(password)