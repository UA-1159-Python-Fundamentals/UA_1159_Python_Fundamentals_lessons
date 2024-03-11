def count_characters(s: str) -> dict:
    return {char: s.count(char) for char in set(s)}