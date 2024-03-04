n = int(input("Input a number in order for me to create a Fuckinacci numbers till your number: "))
while 0 > n:
    print(f"Your input is boring, come on, increase the number, the size does matter\n")
    n = int(input("Input a number in order for me to create a Fuckinacci numbers till your number: "))
else:
    print("Finally, attaboy!")


fuckinacci_list = [0, 1]

while fuckinacci_list[-1] < n:
    new_element = fuckinacci_list[-1] + fuckinacci_list[-2]
    fuckinacci_list.append(new_element)
else:
    if fuckinacci_list[-1] > n:
        fuckinacci_list.pop()
    print(f"\nHere we go, I hope you have got off on knowing that I would spend 20 mins for this task, but it was"
          f"rather interesting.\n\nThe order:\n{fuckinacci_list}")