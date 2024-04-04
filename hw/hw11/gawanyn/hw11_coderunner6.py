def check_age(age):
    while age <= 0:
        raise ValueError("Incorrect age")

while True:    
    try:
        user_age = int(input())
        check_age(user_age)
        print(user_age)
        break
    except ValueError:
        pass

