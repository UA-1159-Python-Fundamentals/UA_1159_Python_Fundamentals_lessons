def four_digit_ops(num):
    product = 1
    for digit in str(num):
        product *= int(digit)

    print(f"The product of digits in {num} is: {product}")
    print(f"Reverse number of {num} is: {str(num)[::-1]}")
    print(f"Sorted {num} in the ascending order is: {"".join(sorted(str(num)))}")


four_digit_ops(6345)
