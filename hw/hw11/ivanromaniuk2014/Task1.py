def is_age_even_or_odd(age: int) -> str:
    if age < 0:
        raise TypeError
    elif age == 0:
        return 'Welcome to our world Baby!'
    else:
        if age % 2 == 0:
            return 'Your age is even'
        else:
            return 'Your age is odd'

try:
    age = int(input('Please enter your age '))
    print(is_age_even_or_odd(age))
except ValueError:
    print('Please enter a number')
except TypeError:
    print('Please enter a positive number')



