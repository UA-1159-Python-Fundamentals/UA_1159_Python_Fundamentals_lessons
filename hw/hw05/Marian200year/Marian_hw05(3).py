up_to_number = int(input("Please enter factorial number: "))

counter = 1
number = 1

while number <= up_to_number:
    counter = counter * number
    number += 1
print(counter)