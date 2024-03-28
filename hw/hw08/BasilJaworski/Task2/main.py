
from validation import *

#User greeting
print()
print('Hello please enter your password for validation')

#Main loop
program = True
while program == True:
    user_input = input("Here:\t")
    print()

    if user_input == 'Q':
        break

    if check_validity(user_input) == True:
        print("Done! Your password is perfect!)")
        print("Enter Q to close program)")
    else:
        print("Change it. Or enter Q for end program")