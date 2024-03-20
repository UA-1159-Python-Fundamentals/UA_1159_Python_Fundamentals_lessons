a = "hello"

def counter(string):
    dic = {}
    for el in string:
        dic[el] = string.count(el)
    
    return dic
print(counter(a))

