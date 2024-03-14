def login_checker():
    while True:
        user_login = input("Enter your login is corect ")
        if user_login == "First":
            print("Welcome!")
        else:
            print("Error: Incorect login.")
login_checker()
    