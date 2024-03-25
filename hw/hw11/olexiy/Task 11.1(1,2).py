# ---------Task11---------
# Task1
def check_negative(x):
    if x<0:
        raise ValueError("Ваш вік відємний")
    elif x%2==0:
        print("Ваш вік парний")
    elif x%2==1:
        print("Ваш вік непарний")
def main():
    age=int(input("Введіть ваш вік:"))
    check_negative(age)
main()

# ----- Інший варіант розвязку через try..except --------

def check_negative():
    try:
        age=int(input("Введіть ваш вік:"))
        if age<0:
            raise ValueError("Вік не може бути відємним")
        elif age%2==0:
            print("Ваш вік парний")
        elif age % 2 == 1:
            print("Ваш вік непарний")
    except ValueError as err:
        print("Помилка",err)
check_negative()

# Task2
def day_of_week():
    week=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    try:
        input_day=int(input("Введіть порядковий номер вашого дня тижня: "))
        if 0 > input_day or input_day>7:
            raise ValueError("Таких днів не існує")
        elif type(input_day) is not int:
            raise ValueError("Це не число")
        else:
            print(f"{input_day} це {week[input_day-1]}")
    except ValueError as err:
        print("Error",err)
day_of_week()