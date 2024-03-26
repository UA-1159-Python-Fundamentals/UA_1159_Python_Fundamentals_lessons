dict_of_days = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}

try:
    key = int(input('Please enter a number from 1 to 7: '))
    print(f'Your number "{key}" corresponds to the day of the week {dict_of_days[key]}')
except ValueError:
    print('You must enter a number')
except KeyError:
    print('You must enter a number only from 1 to 7')
