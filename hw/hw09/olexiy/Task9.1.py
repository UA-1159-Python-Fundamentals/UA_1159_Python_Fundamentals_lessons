# Task9.1
from random import randint
guessed_number=randint(1,100)
print(guessed_number)
attempt=10
while attempt!=0:
    user_input = int(input("Вгадайте число від 1 до 100,у вас 10 спроб: "))
    if 1<=user_input<=100:
        if user_input==guessed_number:
            print("Ви вгадали число!!!")
            break
        elif user_input>guessed_number:
            attempt-=1
            print(f"Ви не вгадали ,ваше число більше за загадане у вас ще {attempt} спроб ")

        else:
            attempt-=1
            print(f"Ви не вгадали ,ваше число менше за загадане у вас ще {attempt} спроб ")

    else:
        print("Введіть число в заданому діапазоні")
if attempt==0:
    print(f"Ви програли,загадане число було {guessed_number}")

