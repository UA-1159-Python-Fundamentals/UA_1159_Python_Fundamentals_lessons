zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
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
Namespaces are one honking great idea -- let's do more of those!
"""

better_num = zen.find('better')
never_num = zen.find('never')
is_num = zen.find("is")

# Or I could do aforementioned statements literally inside the following f-string
print("\nTASK 1\n"
      f"Number of 'better' word in text is: {better_num}.\n"
      f"Number of 'never' word in text is: {never_num}.\n"
      f"Number of 'is' word in text is: {is_num}.\n")

print(f"\n\nTASK 2\n"
      f"\nHere is your all-uppercased text, you crazy weirdo:\n{zen.upper()}\n\n")

print(f"\n\nTASK 3\n"
      f"\nHere is your little insurrection, you tricky dude:\n\n{zen.replace('i', '&')}")