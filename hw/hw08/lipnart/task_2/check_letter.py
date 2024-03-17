import re

def check_lower_letter(word):
    if not re.search("[a-z]", word):
        print("Your password must contain at least 1 letter between [a-z]")
    else:
        return True
    

def check_upper_letter(word):
    if not re.search("[A-Z]", word):
        print("Your password must contain at least 1 letter between [A-Z]")
    else:
        return True
