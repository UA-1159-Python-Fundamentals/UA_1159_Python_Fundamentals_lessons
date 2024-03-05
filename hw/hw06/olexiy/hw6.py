# Task6.1
even=0
even_list=[]
odd=0
odd_list=[]
notdivsible=0
notdivsible_list=[]
for i in range(1,11):
    if i % 2==0:
        even +=1
        even_list.append(i)
    if i % 3==0:
        odd+=1
        odd_list.append(i)
    if i % 2!=0 and i % 3 !=0:
        notdivsible+=1
        notdivsible_list.append(i)
print("Кількість парних чисел: ",even)
print("Парні числа у заданому діапазоні: ",even_list)
print("Кількість чисел, які діляться на 3: ",odd)
print("Числа які діляться на 3 у заданому діапазоні: ", odd_list)
print("Кількість чисел, які не діляться а ні на 2, а ні на 3: ",notdivsible)
print("Числа які не діляться а ні на 2, а ні на 3",notdivsible_list)


# Task6.2
while True:
    login=input("Eneter your login: ")
    if login =='First':
        print("Your login correct!")
        break
    else:
        print("Your login isnt correct!")
