def count_sheeps(sheep):
    s=0
    for i in sheep:
        if i == True:
            s = s + 1
    return s
array1 = [True,  True,  True,  False,
                  True,  True,  True,  True ,
                  True,  False, True,  False,
                  True,  False, False, True ,
                  True,  True,  True,  True ,
                  False, False, True,  True ];

print(count_sheeps(array1))