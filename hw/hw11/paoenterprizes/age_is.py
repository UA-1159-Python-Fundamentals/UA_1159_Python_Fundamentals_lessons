age = int(input("Введіть свій вік: "))
def age_is(age):
    if age > 0:
        if age % 2 == 0:
            print("Ваш вік парний")
        else:print("Ваш вік непарний")
    else:print("Помилка невірно набраний вік")

age_is(age)