# name = "Liubomyr"

# for i in name:
#     print(i)

# i = 0

# while i < len(name):
#     print(i, name[i])
#     i += 1

# i = int(input("number:"))
# s = 0
# while i < 10:
#     print(f"{s}+{i}=", end="")
#     s += i
#     print(s)
#     i = int(input("number:"))
# print(s)


# data = "text"
# for i in data:
#     print(i)

# data = [1, 2, 3, "text"]
# for i in data:
#     print(i)

# data = {11, 21, 31, "text"}
# for i in data:
#     print(i)

# data = {
#     1: 2,
#     3: "text"
# }
# for i in data:
#     print(i, data[i])
# print(data.items())
# a, b = (1 ,2)
# for key, value in data.items():
#     print(key, value)

# name = "Liubomyr"

# for i in name:
#     print(i)

# r = range(5)
# print(r, list(r))
# r = range(-5, 5)
# print(r, list(r))
# r = range(-5, 5, 3)
# print(r, list(r))
# # r = range(-5, 5, 0.5)
# # print(r, list(r))

# for i in range(len(name)):
#     print(f"name[{i}]={name[i]}")

# print(list(enumerate(name)))
# for index, value in enumerate(name):
#     print(f"name[{index}]={value}")

# print(i)
# print(dir())
# print(list(enumerate(name)))
# for index, value in enumerate(name):
#     print(f"name[{index}]={value}")
#     a = 1
#     b=2
# print(dir())
# # print(dir(int))
# print(__builtins__)
# del a
# print(dir())

# s = 0
# for i in range(100):
#     print(i, end="\t")
#     if s >20:
#         print()
#         break
#     print(f"{s}+{i}=", end="")
#     s += i
#     print(s)
# print("sum=", s)

# s = 0
# i = 0
# while i < 100:
#     print(i, end="\t")
#     if s >20:
#         print()
#         break
#     print(f"{s}+{i}=", end="")
#     s += i
#     i += 1
#     print(s)
# print("sum=", s)

# s = 0
# for i in range(100):
#     print(i, end="\t")
#     if i %2:
#         print()
#         continue
#     print(f"{s}+{i}=", end="")
#     s+=i
#     print(s)

# for i in range(5):
#     print(i)
#     if i ==2:
#         break

# for i in range(5):
#     if i == 2:
#         continue
#     print(i)

# for i in range(5):
#     # if 1 < i <3:
#     if i in range(1, 3):
#         continue
#     print(i)


# for i in range(5):
#     print(i)
# else:
#     print("end_for")

# print("end")

# for i in range(5):
#     print(i)
#     if i ==2:
#         break
# else:
#     print("end_for")

# print("end")

# for i in range(5):
#     print(i)
#     if i ==2:
#         continue
# else:
#     print("end_for")

# print("end")


from random import randint

# l = []
# for i in range(10):
#     l.append(randint(-2, 100))
# print(l)

# n = False
# for element in l:
#     if element < 0:
#         n = True

# if not n:
#     print("good", l)



# for element in l:
#     if element < 0:
#         break
# else:
#     print("good")



# count = 0
# while count < 10:
#     l = []
#     for i in range(10):
#         l.append(randint(-2, 100))
#     print(l, end="")




#     for element in l:
#         if element < 0:
#             break
#     else:
#         count +=1
#         print(" is good")
#     print()



# p = []
# while len(p) < 10:
#     l = []
#     for i in range(10):
#         l.append(randint(-2, 100))

#     for element in l:
#         if element < 0:
#             break
#     else:
#         p.append(l)
# for row in p:
#     print(row)


# for i in range(2):
#     print("i:", i)
#     for j in range(2):
#         print("j:", "\t", j)
#         for k in range(2):
#             print("k:", "\t\t", k)



print(1, 2, 3, 4, 455)
print(1, 2, 3, 4, 455, sep=" => ")

print(1, 2, 3, 4, 455, sep=" => ", end="_*_")
print("text")
print("text")



from random import randint

l = []
for i in range(10):
    l.append(randint(-2, 100))
print(l)

N = 10
matrix = []
for i in range(N):
    l = []
    for i in range(N):
        l.append(randint(0, 100))
    matrix.append(l)

print(matrix)

for i in range(N):
    for j in range(N):
        print(matrix[i][j], end="\t")
    print()
