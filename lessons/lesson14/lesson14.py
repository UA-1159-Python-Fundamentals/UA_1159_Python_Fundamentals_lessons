file = open("lessons\lesson14\data\\text.txt")



# print(file)
# print(file.read())
# print(">"*20)
# print(file.read())

# for i in dir(file):
#     print(i)
# print(file.tell())
# print(file.readline())
# print(file.tell())
# print(file.readlines())
# print(file.tell())
# file.seek(0)
# print(file.tell())
# print(len(file.readline()))
# # file.seek(763)
# print(file.tell())
# print(file.readline())
# file.close()
# file = open("lessons\lesson14\data\\text3.txt", "a")
# file.write("text")
# file.writelines(["text1","\n1","\n2","\n3"])
# file.close()
try:
    file = open("lessons\\lesson14\\data\\text.txt", "br")



    print(file.read())
finally:
    file.close()

with open("lessons\\lesson14\\data\\text.txt", "r") as file:
    for line in file:
        print(line)
        import time
        time.sleep(3)
a = 1




