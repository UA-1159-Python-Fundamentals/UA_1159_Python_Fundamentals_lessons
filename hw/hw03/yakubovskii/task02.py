num = input("Write a four-digit natural number:") 

# task_01
product = 1
for digit in str(num):
    product *= int(digit)
print(f"The product of digits is:{product}")

# task_02
print(f"Number in reverse order is:", num[::-1])

# task_03
print(f"Sorted {num} is: {sorted(num)}")


    
    