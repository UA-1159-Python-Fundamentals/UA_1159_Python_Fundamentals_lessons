def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    else:
        return False
print(correct_tail("Fox", "x"))