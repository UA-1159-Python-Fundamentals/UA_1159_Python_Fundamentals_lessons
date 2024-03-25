def correct_tail(body, tail):
    body = str(body)
    if body[len(body)-1] == tail:
        return True
    else:
        return False

print((correct_tail("Fox", "x")))