def is_tail(body, tail):
    if body.endswith(tail):
        return True
    else:
        return False

print(is_tail("hippo", 'o'))
print(is_tail("hippo", 'a'))
print(is_tail("hippo", 'po'))
print(is_tail("lion", 'o'))