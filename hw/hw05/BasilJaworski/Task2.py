n = int(input("Please Enter Int number from 1 to infinity: "))

fibo_list = [0, 1, 1]
max_fibo = 1
counter = 3
while True:
    max_fibo = fibo_list[counter - 2] + fibo_list[counter - 1]
    if max_fibo > n:
        break
    fibo_list.append(max_fibo)
    counter += 1

print(fibo_list)