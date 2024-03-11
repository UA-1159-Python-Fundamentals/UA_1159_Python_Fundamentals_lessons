zen_of_python = """The Zen of Python, by Tim Peters
Beautiful is better than ugly.
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

zen_of_python_count_better = zen_of_python.lower().count("better")
zen_of_python_count_never = zen_of_python.lower().count("never")
zen_of_python_count_is = zen_of_python.lower().count("is")

print(f"Count of world 'better' is: {zen_of_python_count_better}")
print(f"count of world 'never' is: {zen_of_python_count_never}")
print(f"count of world 'is': {zen_of_python_count_is}")

zen_of_python = zen_of_python.upper()
print(zen_of_python)

i_to_change = zen_of_python.replace('i', '&')
print(i_to_change)



