# a = 1
# print(type(a), a)
# a = "1"
# print(type(a), a)
# a = [1]
# print(type(a), a)
# a = True
# print(type(a), a)

# bool = True
# bool = False
# i = 10**4298
# print(i)
# i = -10000000000
# import sys
# sys.set_int_max_str_digits(10_000)
# i = 10**10000
# print(i)
# i = 10**10_005
# print(i)

# f = 10.5
# print(f)
# f = .5
# print(f)
# f = 5.
# print(f)


# s = "text"
# print(id(s))
# s = "text1"
# print(id(s))
# s = "text"
# print(id(s))


# l = [1,2,3]
# print(id(l), l)
# l.append(1)
# print(id(l), l)
# l.append(1)
# print(id(l), l)

# l.insert(2, 999)
# print(id(l), l)

# a = 10
# b = a + 12
# print(a, b)
# a = -10
# b = a + 12
# print(a, b)
# a = [10, 1,2]
# b = a
# print(a, b)
# b.append(22)
# print(a, b)


# a = 1
# print(type(a), a, type(a) is int)
# a = "1"
# print(type(a), a, type(a) is str)
# a = [1]
# print(type(a), a, type(a) is str,  type(a) is list)
# a = True
# print(type(a), a, type(a) is str, type(a) is bool)

# a = 1 + 2 + 3 + 5 + 6 + 7 + 8 + 9
# print(a)
# a = 1 + 2 + 3 \
#     + 5 + 6 \
#     + 7 + 8 + 9
# print(a)
# a = (1 + 2 + 3
#     + 5 + 6
#     + 7 + 8 + 9)
# print(a)
# a = [1 + 2 + 3
#     + 5 + 6
#     + 7 + 8 + 9]
# print(a)
# a = {1 + 2 + 3
#     + 5 + 6
#     + 7 + 8 + 9}
# print(a)

# l = [1+5+8+9, "sdhvsh" + "sadsad"]
# print(l, type(l))
# print(l[0], type(l[0]))
# print(l[1], type(l[1]))


# a = 1
# b=2
# a, b = 1, 2
# PI = 3.14
# print(PI)

# PI = "mytest"
# print(PI)

# a = 10
# print(a)
# a = 10_0_0
# print(a)
# a = 0b10 # 0..1
# print(a)
# a = 0o10 # 0..7
# print(a)
# a = 0x10 # 0..9a..f
# print(a)
# a = 33
# print(a)
# print(bin(a))
# print(oct(a))
# print(hex(a))


# f = 10.0
# print(f)
# f = .01
# print(f)
# f = 10.
# print(f)
# f = 235e-2
# print(f)

# print((-1)**(0.5))
# print((-1)**(1/3))

# l = [1, 2, "text", 1, 2, "text"]
# t = (1, 2, 3, 1, 2, "text")
# s = {1, 2, "text", 1, 2, "text"}
# d = {
#     "key1": "value1",
#     10: "value2",
#     (1, 2, 3): "value3",
# }
# print(l)
# print(t)
# print(s)
# print(d)
# text = "asfasdsfdaadfdsafsafdasfdfadasf"
# print(set(text))

# l = []
# for e in text:
#     if e not in l:
#         l.append(e)
# print(l)

# s = {1,2,3,1,2,3,1,2,3, (1,2,3), 1,2,3, (1,2,3),(3,1,2), 1,2,3, }
# print(s)

# l = [i for i in range(100000)]
# l = []
# for i in range(100000):
#     l.append(i)


# print(l.__sizeof__())
# t = tuple(l)
# print(t.__sizeof__())

# text = "asfasdsfdaadfdsafsafdasfdfadasf"
# for i in range(len(text)):
#     print(i, text[i])
# s = {1,2,3,1,2,3,1,2,3, (1,2,3), 1,2,3, (1,2,3),(3,1,2), 1,2,3, }
# print(list(s))
# print(list(s))
# print(list(s))
# print(list(s))
# print(list(s))

# l = list(s)
# l[0] = 99
# print(l)
# l[1] = list("test")
# print(l)
# print(l[1])
# l[1][2]="test"
# print(l)

# print(int("123"))
# print(int("1101010", 2))
# print(int("1101010", 3))
# # print(int("1101010", 37))
# print(int("zx36", 36))

# s = "10+25+36"
# print(eval(s))
# a = 12
# s = "10+25+36+a"
# print(eval(s))

# d = dict([(1,1),(2,"2"),(3,[1,2,3]),(4,5416)])
# print(d)

# for i in range(100):
#     print(f"{i}-{chr(i)}")
# for i in "uisaefjnv ddhvb":
#     print(f"{i}-{ord(i)}")


# s = "jbdskjvbfd"
# s = """line_01
# line_02
# """
# s = '''line_01
# line_02
# '''

# print(s)
# # "\n" newline
# # "\t" tab
# for i in "uisaefjnv ddhvb":
#     print(f"{i}\t{ord(i)}")
# print("new\"A\\")

# name = "John"
# age = 23
# template = "%s is %d years old."
# print(template % (name, age))

# template = "{} is {} years old."
# print(template.format(name, age))

# template = "{name_temp} is {age_temp} years old."
# print(template.format(age_temp=age, name_temp=name ))

# print(f"{name} is {age} years old.")

# text = 'programiz'

# print(text[0])
# # print(text[666]) #error
# print(text[len(text)-1])
# print(text[-1])
# print(text[4:9])
# print(text[0:5])

# print(text[4:])
# print(text[:5])
# print(text[:])
# print(text[::2])
# print(text[::3])
# print(text[::-1])

# text = list('programiz')

# print(text[0])
# # print(text[666]) #error
# print(text[len(text)-1])
# print(text[-1])
# print(text[4:9])
# print(text[0:5])

# print(text[4:])
# print(text[:5])
# print(text[:])
# print(text[::2])
# print(text[::3])
# print(text[::-1])


text = "this will split. all WoRdS iNtO a list."

print(text.capitalize())
print(text.upper())
print(text.lower())
print(text.replace("ll", "1986"))
print(text.split())
print(text.split("ll"))
print("=>".join(["1","2","3","4"]))

a = 10
bc = "text"
t = f"=>{a} => {bc.upper()}"
print(t)

a = None

b = None
print(id(a))
print(id(b))