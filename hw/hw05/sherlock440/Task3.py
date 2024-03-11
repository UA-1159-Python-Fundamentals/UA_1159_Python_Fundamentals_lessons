n = int(input("Enter you number, sweet child. Type right this way, I'm at your service with a smile —> "))


range_list = range(1, n+1)

str_range_list = []
for element in range_list:
    str_range_list.append(str(element))

range_str = " * ".join(str_range_list)
result = eval(range_str)

print(f"\n{n}! = {range_str} = {result}")