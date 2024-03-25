sheep_number = lambda sheep_list: sheep_list.count(True)

my_list = (
  [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
)


print(sheep_number(my_list))