div_2 = []
div_3 = []
not_div = []

for e in range(10):
    if e % 2 == 0:
        div_2.append(e)
        
    elif e % 3 == 0:
        div_3.append(e)
        
    else:
        not_div.append(e)

print(div_2)
print(div_3)
print(not_div)