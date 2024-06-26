class InputError(Exception):
    def __init__(self, data):
        self.data = data

def check(text):
    if not isinstance(text, str):
        raise InputError("Type text error")
    elif len(text) < 3:
        raise InputError("Short text error")
    elif len(text) > 15:
        raise InputError("Long text error")
    else:
        return True

# Example usage
def test_input(text):
    try:
        print(check(text))
    except InputError as e:
        print(e.data)

# Test cases
test_input("")  # Short text error
test_input("Hello world")  # True
test_input("Long text that can not be placed in some document")  # Long text error
test_input({})  # Type text error
