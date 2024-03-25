while True:
    login = input("your_login: ")
    if login == "First":
        print("success, Welcome back")
        break
    elif login != "First":
        print("Error:your login not correct, try again")