py_philosophy = """The Zen of Python, by Tim Peters

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

count_better = py_philosophy.count("better")
count_never = py_philosophy.count("never")
count_is = py_philosophy.count("is")
py_philosophy_upper = py_philosophy.upper()
py_philosophy_replaced_i_lower = py_philosophy.replace("i", "&")
py_philosophy_replaced_i_all = py_philosophy.translate(str.maketrans({"i": "&", "I": "&"}))

print(f"Count of word 'better': {count_better}, count of word 'never': {count_never}, count of word 'is': {count_is}\n"
      + "\n" + "*" * 100 + "\n")
print(py_philosophy_upper + "\n" + "*" * 100 + "\n")
print(py_philosophy_replaced_i_lower + "\n" + "*" * 100 + "\n")
print(py_philosophy_replaced_i_all + "\n" + "*" * 100 + "\n")
