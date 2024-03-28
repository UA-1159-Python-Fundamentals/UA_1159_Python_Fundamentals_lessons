
from .val_conditions import *

def check_validity(string):
    """The function takes string and checks all conditions, 
    you can modify the condition list in val_condition module. 
    Returns True if all conditions is True"""

    for i in checkker:
        if i(string) != True:
            return False
    return True