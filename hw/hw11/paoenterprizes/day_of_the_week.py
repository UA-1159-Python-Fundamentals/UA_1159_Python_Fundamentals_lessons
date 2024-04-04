day = input("Введіть число для розрахування дня тижня: ")
week = ("Понеділок","Вівторок","Середа","Четверг","П'ятниця","Субота","Неділя")
def day_of_the_week(day):
    if day.isdigit():
        return week[(int(day)%7)-1]
    else: return "Помилка введене значення не є числом"
print(day_of_the_week(day))