import random

random_digit = random.randint(1000, 9999)  # 1234

stringed_digit = str(random_digit)  # '1234'
listed_digit = list(stringed_digit)  # ['1', '2', '3', '4']
joined_digit = ' * '.join(listed_digit)  # "1 * 2 * 3 * 4"
evaled_digit = eval(joined_digit)

print("\nTASK 1\n"
      f"The product of the digits of a number {random_digit} is: {evaled_digit}.\n"
      f"It would be funny to write it in a single line as: eval(' * '.join(list(str(random.randint(1000, 9999)))))")

print("\n\nTASK 2\n"
      f"It seems this task is for checking who was full of attention during your lesson, because there is no mentioning"
      f" of the tird parameter for slicing option in the presentation.\n"
      f"The answer is str(digit)[::-1]: {stringed_digit[::-1]}")

print("\n\nTASK 3\n"
      f"Okay, this is even more tricky because I have not found it neither in the presentation nor in my memory "
      f"(but yeah, we shouldn't believe my memory).\n"
      f"But we live in a cheating era so we can find the .sort() function out somewhere outside...\n...\n...\n"
      f"Okay, you've caught me. It seems that for .sort() all elements in a list should be integer, but idk how to "
      f"turn them into integer without cycles. So I have asked chatGPT and it suggested me to use sorted() function "
      f"that I have never seen. So, the result\n"
      f"The answer is: {random_digit} -> {''.join(sorted(list(str(random_digit))))}")