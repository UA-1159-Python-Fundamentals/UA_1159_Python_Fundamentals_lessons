def count_characters(s: str) -> dict:
    '''This function calculate the numbers of characters included in  given string'''
    result = {}
    for char in s:
        if char not in result:
            result[char] = s.count(char)
    return result

print(count_characters('hello'))