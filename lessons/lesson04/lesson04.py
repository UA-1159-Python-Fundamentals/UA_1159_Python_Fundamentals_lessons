# a = 5
# b = 10
# c = 15
# print(a > b)
# a_str = "5"
# print(a == a_str)
# print(a > a_str)

# is_false = [0, False, None, [], (), {}, ""]


# # a = None
# b = int(input("a:"))
# if b > 10:
#     a = 25
# print(a)
# print(type(None))
# print (None== 0)
# print ([]== 0)
# print ([]== [])

# if len(my_list) > 0:
#     pass
# if my_list:
#     pass

# a = int(input("a:"))
# b = int(input("b:"))
# c = int(input("c:"))
# if a>b and b>c:
#     print("a>b>c")

# if a > b > c:
#     print("a>b>c")


# a = int(input("a:"))
# b = int(input("b:"))
# c = int(input("c:"))
# # if a>b and b<c:
#     print("a>b<c")

# if a > b < c:
#     print("a>b<c")

# if a > b or a > c:
#     print("a > b or a > c")

# print(1 > 3 or 1 > -1)

# a = 10 and 15 and "q" and "3a3"
# print(a)

# a = 10 and 15 and 0 and [] and "3a3"
# print(a)


# a = 0 or [] or "q" or "test" or ""
# print(a)

# a = 0 or None or "" or [] or {}
# print(a)


# print(10 and "" or 35 and "test")

# print((10 and "") or (35 and "test"))


# print(10 and ("" or 35) and "test")

# fail = validate1(phone) and validate1(phone) and validate1(phone)
# if not fail:
#     return response


# if not  validate1(phone):
#     fail = fail
# if not  validate2(phone)  :
#     fail = fail


# a = [1,2,3]
# b = [1,2,3]
# c = a

# print(a==b)
# print(a is b)
# print(a is c)
# print(id(a) ,id(c), id(a) == id(c))

# a = None
# b = None
# print(a is b)


# for i in range(270):
#     c = str(i)
#     c = int(c)
#     print(i, c, i is c)


# a = 7
# b = 12
# print(f"{a=} {b=}")
# a, b = b, a
# print(f"{a=} {b=}")
# b = a + b
# a = b - a
# b = b - a
# print(f"{a=} {b=}")


# l = [1, 2, 3, 4, 5, 6, "7"]
# print(7 in l)
# print("7" in l)
# print(3 in l)
# print("3" not in l)
# print("3333" not in "bchsdanc vhfdjncdsjbf27857t69854")
# print("3333" in "bchsdanc333333 vhfdjncdsjbf27857t69854")


# d = {1: "11", "2": 22}
# print(1 in d)
# print("11" in d)
# print(22 in d)
# print("2" in d)

# print((1, 2, 3) in [1, 2, 3, (1, 2, 3)])
# print(11 in [1, 2, 3, (11, 2, 3)])
# print(False in [1, 2, 3, (11, 2, 3)])
# print(False in [1, False, 3, (11, 2, 3)])


# a = 25

# if a > 10:
#     print("*"*10)
#     print(f"{a}>10")
#     print("*"*10)

# print("="*10)

# a = 5

# if a > 10:
#     print("*"*10)
#     print(f"{a}>10")
#     print("*"*10)

# print("="*10)

# a = int(input("a: "))

# if a > 10:
#     print("*"*10)
#     print(f"{a}>10")
#     print("*"*10)
# else:
#     print(">"*10)
#     print(f"\t{a}<10")
#     print("<"*10)

# print("="*10)

# age = int(input("age: "))
# if age < 12:
#     print('kid')
# elif age < 18:
#     print('teenager')
# elif age < 50:
#     print('adult')
# else:
#     print('you are not old')

# if age < 12:
#     print('kid')
# else:
#     if age < 18:
#         print('teenager')
#     else:
#         if age < 50:
#             print('adult')
#         else:
#             print('you are not old')


# weather = "raining"
# answer = "Open Your umbrella" if weather == "raining" else "Wear your cap"
# print(answer)

# weather = "sun"
# answer = "Open Your umbrella" if weather == "raining" else "Wear your cap"
# # answer = weather == "raining" ? "Open Your umbrella" : "Wear your cap" #other
# print(answer)


# weather = "raining"
# if weather == "raining":
#     answer = "Open Your umbrella"
# else:
#     answer = "Wear your cap"
# print(answer)

# status = int(input("set status code: "))

# match status:
#     case 400:
#         print("Bad request")
#     case 401 | 402 as code:
#         print(code, "Unauthorized")
#     case 403:
#         print("Forbidden")
#     case 404:
#         print("Not found")

#     case "_":
#         print("Not found")
        
#     case _:
#         print("Other error")
        
# if status == 400:
#         print("Bad request")
# elif status == 401:
#     print("Unauthorized")
# elif status == 403:
#     print("Forbidden")
# elif status == 404:
#     print("Not found")
# else:
#     print("Other error")



# values = "save"
# values = ("load", "http")
# values = ("save", "http", 15)
# values = ("save", "http", [1,2,3], 12, 15, 15)



# match values:
#     case "load", link:
#         print('"load", link', link)
#     case "save", link, filename:
#         print('"save", link, filename:', link, filename)
#     case "save", link, *filenames:
#         for filename in filenames:
#             print('case "save", link, *filenames:', link, filename)
#     case _:
#         print("case _:", values)

# a = 55
# # b = None
# if a > 10:
#     b = 15


# for i in "abc":
#     d = i

# print(b)
# print(d)

# a = [1,2,3]
# b = a[:]
# b = a.copy()

# b[1]=55
# print(a)

# def f():
#     """select *
    
    
    
#     docstring
#     """

# print(f.__doc__)
# help(f)


