number = input("Please enter number: ")

print(f"\n- Your number is: {number}")
print(f"\n- Number in reverse order is:" ,number[::-1])

number = list(number)
product = 1

for i in range(len(number)):
    if int(number[i]) != 0:
        product *= int(number[i])

print(f"\n- Product of digits in your number is (without ZERO): {product}")

sorted_number = '-'.join(sorted(number))
print(f"\n- Your number with sorted digits in ascending order: {sorted_number}\n")



