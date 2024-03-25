def number_classifier(num1, num2):
    even_numbers_divisible_by_two = [num for num in range(num1, num2 + 1) if num % 2 == 0]
    odd_numbers_divisible_by_three = [num for num in range(num1, num2 + 1) if num % 2 != 0 and num % 3 == 0]
    non_divisible_by_two_and_three = [num for num in range(num1, num2 + 1) if num % 2 != 0 and num % 3 != 0]
    print(f"List of even numbers, divisible by two: {even_numbers_divisible_by_two}")
    print(f"List of odd numbers, divisible by three: {odd_numbers_divisible_by_three}")
    print(f"List of numbers that are not divisible by two and three: {non_divisible_by_two_and_three}")


number_classifier(1, 10)  # 1 to 10 inclusive
