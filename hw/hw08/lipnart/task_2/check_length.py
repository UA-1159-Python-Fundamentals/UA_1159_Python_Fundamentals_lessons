def check_length(word):
    """Check minimum and maximum length of password"""
    if len(word) < 6:
        print("Your password is too short")
    elif len(word) > 16:
        print("Your password is too long")
    else:
        return True

check_length("passssssssss")