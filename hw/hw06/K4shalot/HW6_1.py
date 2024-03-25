list = {1,2,3,4,5,6,7,8,9,10}
for x in list:
    if x % 2 == 0:
        print(x)
print("Numbers that can be divided by 3: ")        
for x in list:
    if x % 3 == 0:
        print(x)
print("Numbers that cant be divided by 3 or 2: ")
for x in list:
    if x % 2 != 0 and x % 3 != 0:
        print(x)