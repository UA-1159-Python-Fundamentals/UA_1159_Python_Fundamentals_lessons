def check_number(word):
    """Chek numbers in password"""
    for i in word:
        if i.isdigit():
            return True
    else:
        pass
        print("Your password must contain at least 1 number.")


check_number("dfxcgvhj4567")