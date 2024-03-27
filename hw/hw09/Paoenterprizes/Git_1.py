import random

print('Гра "Вгадай число"\nчисло загадане у діапазоні від 1 до 40\nу вас 10 спроб'
      '')
answer = random.randint(1,40)
for i in range(1,11):
    option = int(input("Ввдіть свій варіант: "))
    if option == answer:
        print("Ви виграли!!!")
        print("Кількість спроб: ", i, " із 10")
        break
    elif option < answer:
        print("Ваш варіант меньший за загадане число")
    else: print("Ваш варіант більший за загадане число")
    print("Кількість спроб: ", i ," із 10")
    if i == 10:
        print ("ВИ ПРОГРАЛИ!!!")
print ("Гра завершена")