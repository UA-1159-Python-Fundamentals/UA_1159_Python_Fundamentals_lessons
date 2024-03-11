is_tail = lambda body, tail: True if body.endswith(tail) else False

print(is_tail("hippo", 'o'))
print(is_tail("hippo", 'a'))
print(is_tail("hippo", 'po'))
print(is_tail("lion", 'o'))