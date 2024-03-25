def count_sheeps(sheep):
    counter = 0
    for count in sheep:
        if count is True:
            counter +=1
    return counter

print(count_sheeps([True,  True,  True,  False,
                  True,  True,  True,  True ,
                  True,  False, True,  False,
                  True,  False, False, True ,
                  True,  True,  True,  True ,
                  False, False, True,  True ]))