class NegativeAgeException(Exception):
    pass


def check_age(age):
    if age < 0:
        raise NegativeAgeException("age must not be negative")
    return "Your age is even" if age % 2 == 0 else "Your age is odd"


def main():
    try:
        user_input = int(input("Please, enter your age: "))
        print(check_age(user_input))
    except NegativeAgeException as e:
        print(f"NegativeAgeException raised, {e}")
    except ValueError as e:
        print(f"ValueError raised, {e}")


main()
