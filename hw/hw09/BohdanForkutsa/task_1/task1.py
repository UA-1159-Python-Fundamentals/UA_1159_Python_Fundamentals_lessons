from random import randint

computer_num = randint(1, 100)

count = 10

while count >= 0:
    
    user_num = int(input("Будь ласка, введіть число: \n"))

    if computer_num == user_num:
        print(f"Вітаю!!! Ти знайшов число! Залишилось {count} спроб.")
        break
    elif user_num < computer_num:
        count -= 1
        print(f"Твоє число менше, спробуй щераз. Залишилось {count} спроб.")
    elif user_num > computer_num:
        count -= 1
        print(f"Твоє число більше, спробуй щераз. Залишилось {count} спроб.")
    elif user_num < 1 or user_num > 100:
        count -= 1
        print(f"Потрібно ввести число від 1 до 100. Залишилось {count} спроб.")

    if count == 0:
        print("\nGG")