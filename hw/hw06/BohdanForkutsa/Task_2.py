log = {"login1": "First"}
loop = True
while loop:

    enter_login = input("Enter login: ")
    if enter_login in log["login1"]:
        print("Hi")
        loop = False
    else:
        print("Error. Try again")
        continue