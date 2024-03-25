login = str(input("Please enter your login: "))

while login != "First":
    login = str(input("Your login is invalid please enter another: "))
else: 
    print(f"Welcome, {login}")