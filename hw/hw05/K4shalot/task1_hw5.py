integer_list = [1,2,3,4,5,6,7,8,9,10]
print(integer_list)

for i in range(len(integer_list)):
    integer_list[i] = float(integer_list[i])

print(integer_list)