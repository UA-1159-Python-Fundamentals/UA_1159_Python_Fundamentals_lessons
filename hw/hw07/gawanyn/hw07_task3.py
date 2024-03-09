def count_characters(s: str) -> dict:
    return {char: s.count(char) for char in set(s)}

# Приклад використання зі вхідним рядком "hello"
print(count_characters("hello"))  # Вивід: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
