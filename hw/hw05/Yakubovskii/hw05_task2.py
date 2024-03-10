n = int(input("Write a fibonacci number: "))
f = 0
a = 1
# while f > 21:
#     f += a
#     break
# print(f)
while f <= n:
    print(f, end=" ")
    f, a = a, a + f