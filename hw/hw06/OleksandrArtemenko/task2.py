def login_check():
    while True:
        user_input = input("Please, enter login: ")
        if user_input == "First":
            print(f"Welcome, {user_input}")
            break
        else:
            print(f"Login '{user_input}' is incorrect. Please, try again.")


login_check()
