py_phi = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
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
better_num = py_phi.count('better')
never_num = py_phi.count('never')
is_num = py_phi.count('is')

print(f"Number of word 'better' in text is: {better_num}, Number of word 'never' in text is: {never_num}, Number of word 'is' in text is: {is_num}\n" ) 

print(f"Here is your uppercased text: {py_phi.upper()}\n")

print(f"Replaced symbols 'i' with '&': {py_phi.replace('i', '&')}\n")