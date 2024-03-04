num = input("Please enter here a four-digit natural number: ")
if num.isdigit():
    a, b, c, d = num[0], num[1], num[2], num[3]
    a, b, c, d = int(a), int(b), int(c), int(d)
    prod = a*b*c*d
    print(f"The product of the digits of this number is {prod}")

    num_rev = list(reversed(num))
    num_rev = "".join(num_rev)
    print(f"Look your number in reverse order: {num_rev}")

    num_sort = sorted(num)
    num_sort = "".join(num_sort)
    print(f"Your number is sorted in ascending order: {num_sort}")

else:
    print("You enter not digit.")