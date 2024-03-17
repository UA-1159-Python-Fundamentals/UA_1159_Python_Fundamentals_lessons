login = "First"
access = False

while access != True:
    if input("Please enter your login: ") == login:
        access = True
        print("Successful authorization!")
    else:
        print("Try again...")