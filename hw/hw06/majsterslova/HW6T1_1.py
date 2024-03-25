
x2 = []
x3 = []
r = []
for i in range(1, 11, 1):
    if i % 2 == 0:
        x2.append(int(i))
    if i % 3 == 0:
        x3.append(int(i))
    if i % 2 != 0 and i % 3 != 0:
        r.append(int(i))
print("Ділиться на 2 : ", x2)
print("Ділиться на 3 : ", x3)
print("Решта : " , r)    