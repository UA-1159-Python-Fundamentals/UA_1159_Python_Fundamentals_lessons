# Task1.
philosophy = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

# Find the number of occurrences of specific words
better_count = philosophy.count("better")
never_count = philosophy.count("never")
is_count = philosophy.count("is")

print("Occurrences of 'better':", better_count)
print("Occurrences of 'never':", never_count)
print("Occurrences of 'is':", is_count)

# Convert the text to uppercase
uppercase_text = philosophy.upper()
print(uppercase_text)

# Replace 'i' with 'g'
replaced_text = philosophy.replace("i", "g")
print(replaced_text)

# Task2.
number = int(input("Enter a four-digit number: "))

# Find the product of the digits
product = 1
digits = []
temp_number = number

while temp_number > 0:
    digit = temp_number % 10
    product *= digit
    digits.append(digit)
    temp_number //= 10

# Reverse the number
reversed_number = int("".join(str(digit) for digit in digits[::-1]))

# Sort the digits in ascending order
sorted_digits = sorted(digits)

print("Product of the digits:", product)
print("Reversed number:", reversed_number)
print("Digits in ascending order:", sorted_digits)

# Task3.
a = 5
b = 10

print("Before swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)
