def chec_day():
    try:
        day = int(input('Enter your day of weeck '))
        if day < 0 or day >= 8:
            raise ValueError ('There is no such day ')
        if day == 1:
            print('Day is Monday')
        elif day == 2:
            print('Day is Tuesday')
        elif day == 3:
            print('Day is Vensday')
        elif day == 4:
            print('Day is Thursday')
        elif day == 5:
            print('Day is Friday')
        elif day == 6:
            print('Day is Saturday')
        elif day == 7:
            print('Day is Sunday')
    except ValueError as e:
        print(f'Error: {e}')

chec_day()
        