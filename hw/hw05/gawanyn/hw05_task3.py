n = int(input("Enter number: "))

list = [_ for _ in range(1, n+1)]

print(list)

product = 1

for i in list:
    product *= i

print(product)