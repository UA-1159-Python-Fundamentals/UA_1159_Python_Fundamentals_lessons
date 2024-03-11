#Task1
import random
list=[random.randint(0,10) for _ in range(10)]
print(list)
for i in range(len(list)):
   list[i]=float(list[i])
print(list)


#Task2
n = int(input("Введіть порядковий номер числа Фібоначчі: "))
sequence_number=n+1
if n < 0:
     result = 0
     print("Введенно відємне число")
elif n == 0:
     result = 0
     print(f"Число Фібоначчі за порядковим номером {n}: {result}")
elif n == 1:
     result = 1
     print(f"Число Фібоначчі за порядковим номером {n}: {result}")
elif n == 2:
     result = 1
     print(f"Число Фібоначчі за порядковим номером {n}: {result}")
else:
    a, b = 0, 1
    for i in range(2, sequence_number):
        a, b = b, a + b
    result = b
    print(f"Число Фібоначчі за порядковим номером {n}: {result}")

#Task3
factorial=1
n = int(input("Введіть число для обчислення факторіалу:"))
for i in range(n):
    factorial *= n-i
print(f"Факторіал числа:{n} -",factorial)



