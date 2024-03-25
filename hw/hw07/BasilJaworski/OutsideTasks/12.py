"""Is this my tail?"""
def correct_tail(body, tail):
    body_l = list(body)
    return True if body_l[-1] == tail else False