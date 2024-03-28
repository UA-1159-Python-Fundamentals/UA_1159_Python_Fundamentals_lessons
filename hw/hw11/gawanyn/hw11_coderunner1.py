from random import choices
from string import ascii_letters, digits

def check(login):
  
    login = login.lower()
    role, id_part = "", ""
    separators = ["-id", "id", "-"]

    for separator in separators:
      parts = login.split(separator)
      if len(parts) == 2:
        role, id_part = parts
        break

    if role not in ("admin", "employee"):
      raise ValueError(f"incorrect login '{login}'")

    try:
      int(id_part)  # Check if the id part is a valid integer
    except ValueError:
      return f"incorrect login '{login}'"

    return True

letters_and_digits = choices(ascii_letters, k=5)
letters_and_digits.extend(choices(digits, k=5))

incorect_login = ''.join(letters_and_digits)
print(incorect_login)

try:
    if check(incorect_login):
        print("checked successfully")
except ValueError as e:
    print(str(e) == f"incorrect login '{incorect_login}'")
