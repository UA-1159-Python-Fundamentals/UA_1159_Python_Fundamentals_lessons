class Human:
    pass


class Man(Human):
    massage = "First object are a man"


class Woman(Human):
    pass


def God():
    return (Man(), Woman())
