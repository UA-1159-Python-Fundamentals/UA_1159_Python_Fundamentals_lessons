number = int(1234)
number_str = str(number)

#Products of digits

product_of_digits = 1

for digit in str(number):
    product_of_digits *= int(digit)

print("Product is:", product_of_digits)

#Reverse number

reverse_number = int(number_str[::-1])
print("Reverse number is:", reverse_number)

#Sorted digits

sorted_digits = sorted(number_str, reverse = True)
sorted_number = int(''.join(sorted_digits))

print("Sorted number is:", sorted_number)




