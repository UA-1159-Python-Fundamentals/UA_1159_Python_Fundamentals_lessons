# Task1
text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

text = text.replace(',', ' ')
text = text.replace('.', ' ')
text = text.replace('-', ' ')
text = text.replace('*', ' ')
text=text.split()
better_count=0
for word in text:
    if word =="better":
        better_count +=1
print("Кількісь слів: better -",better_count)
never_counter = text.count("never")
print("Кількісь слів: never -",never_counter)
is_counter=text.count("is")
print("Кількісь слів: is -",is_counter)


# Task2
digit = 7539
digit_str = str(digit)
str_ = '*'.join(digit_str)
result=eval(str_)
print(f"Добуток цифр числа:{digit} -",result)
digit_str = str(digit)
digit_list = list(digit_str)
digit_list.reverse()
digit_str = ''.join(digit_list)
digit_reversed = int(digit_str)
print(f"Число {digit} навпаки",digit_reversed)
digit_str = str(digit)
digit_list = list(digit_str)
digit_list.sort()
digit_str = ''.join(digit_list)
digit_sorted = int(digit_str)
print(f"Число {digit} в порядку зростання",digit_sorted)


# Task3
a = 5
b = 10
a, b = b, a
print("a =", a)
print("b =", b)