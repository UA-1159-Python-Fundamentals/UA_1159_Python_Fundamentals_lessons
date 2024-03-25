from check_character import *
from check_length import *
from check_letter import *
from check_number import *

key = True

while key:
    user_pass = str(input("Please enter Your password: "))
    if check_length(user_pass) and check_lower_letter(user_pass) and check_upper_letter(user_pass) and check_number(user_pass) and check_character(user_pass):
        print("Valid password")
        key = False
    else:
        print("Try again")