
__all__ = ['checkker']

def check_letters(string):
    """The function takes string and returns True if there are at least one small and large letters"""

    small = False
    for i in string:
        if i in "abcdefghijklmnopqrstuvwxyz":
            small = True
            break

    large = False
    for i in string:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            large = True
            break

    if small == False:
        print("You need to add small character in your password")
    if large == False:
        print("You need to add large character in your password")

    return True if small == large == True else False


def check_numbers(string):
    """The function takes string and returns True if there are at least one number in this string"""

    numbers = False
    for i in string:
        if i in "0123456789":
            numbers = True
            break
    
    if numbers == False:
        print("You need to add some numbers in your password")

    return numbers

def check_symbols(string):
    """The function takes string and returns True if there are at least one of thease @#$ characters"""

    symbols = False
    for i in string:
        if i in "$#@":
            symbols = True
            break

    if symbols == False:
        print("You need to add @ or # or $ in your password")

    return symbols

def check_length(string):
    """The function takes string and returns True if length is more or equal 6 and less or equal 16"""

    if len(string) < 6 or len(string) > 16:
        print("Yor password must have 6 to 16 characters!!")

    return True if len(string)>=6 and len(string)<=16 else False

#the list of conditions if you need to add condition just define it above and append this list with it name
#your condition must takes string and returns True or False
checkker = [check_letters, check_numbers, check_symbols, check_length]