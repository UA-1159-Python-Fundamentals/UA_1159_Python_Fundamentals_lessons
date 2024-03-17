def check_character(word):
    """Check the character in password"""
    check_list = ["$", "#", "@"]
    for i in word:
        if i in check_list:
            return True
    else:
        print('Your password must contain special characters.\n For example: "@", "#", "$"')


check_character("The pass$")