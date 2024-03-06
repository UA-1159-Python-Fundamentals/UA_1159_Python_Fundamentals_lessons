#Task 1
#even_number = [ n for n in range(1, 11) if n % 2 == 0]
#print(even_number)
#odd_number = [ n for n in range(1, 11) if n % 3 == 0]
#print(odd_number)
#number_which_not_div_on_two_and_three = [ n for n in range(1, 11) if n % 2 != 0 and n % 3 != 0]
#print(number_which_not_div_on_two_and_three)

#Task 2

while True:
    user_login = input("Please enter your login: ")

    if user_login == "First":
        print(f"Welcome, diar {user_login}")
        break
    elif user_login != "First":
        print("Error 404, login not found.")

    
    