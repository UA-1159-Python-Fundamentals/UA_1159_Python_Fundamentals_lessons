def count_characters(s: str) -> dict:
    result = {}
    for char in s:
        if char not in result:
            result[char] = s.count(char)
    return result

print(count_characters('hello'))