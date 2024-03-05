num = int(input("Write a four-digit natural number:"))
num = list

product = 1


if num < 9999 or num > 1000:
    print(f"The product of digits is:{product}")
    print(f"Number in reverse order is:", num[::-1])
    print(f"Sorted {num} is: {sorted(num)}")
for digit in str(num):
    product *= int(digit)
else:
    print(f"\t Wrong {num}. Try again.")
 

