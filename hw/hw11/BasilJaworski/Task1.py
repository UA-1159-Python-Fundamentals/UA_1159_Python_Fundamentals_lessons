class NegativeAge(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return "The number is less than 0!"

def check_age(age):
    """The function to check is the age positive and is the age even or odd"""

    try:
        even = int(age)
        if even<0:
            return NegativeAge("Error")
        even = even%2
    except:
        return "Error! Thats not a number"
    else:
        return f"Your age '{age}' is even!" if even==0 else f"Your age '{age}' is odd!"



while True:
    user_age = input("Please enter your age here: ")
    quit() if user_age == "q" else print(check_age(user_age))