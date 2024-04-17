def chec_age():
    try:
        age = int(input('Enter your age '))
        if age < 0:
            raise ValueError ('Age cenot be nagative ')
        if age % 2 == 0:
            print("Your age is even")
        else:
            print("Your age is odd")
    except ValueError as e:
        print(f'Error: {e}')

chec_age()