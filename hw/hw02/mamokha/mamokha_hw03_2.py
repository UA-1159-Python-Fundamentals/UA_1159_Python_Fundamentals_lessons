KManokhaHW03# task2

number = int(9876)
number_str = str(number)

#product

product = 1

for digit in str(number):
    product *= int(digit)

print("Product is:", product)

#reverse

reverse_number = int(number_str[::-1])
print("Reverse number is:", reverse_number)

#sorted

sorted_digits = sorted(number_str, reverse = True)
sorted_number = int(''.join(sorted_digits))

print("Sorted number is:", sorted_number)
