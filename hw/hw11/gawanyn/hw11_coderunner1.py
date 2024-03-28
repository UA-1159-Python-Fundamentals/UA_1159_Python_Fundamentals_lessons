from random import choices
from string import ascii_letters, digits

def check(login):
    try:
        str(login)

        if "-" in login or "id" in login:
            return True
        else:
            raise ValueError(f"incorrect login '{login}'")
    except:
        raise ValueError(f"incorrect login '{login}'")


letters_and_digits = choices(ascii_letters, k=5)
letters_and_digits.extend(choices(digits, k=5))

incorect_login = ''.join(letters_and_digits)
print(incorect_login)

try:
    if check(incorect_login):
        print("checked successfully")
except ValueError as e:
    print(str(e) == f"incorrect login '{incorect_login}'")
