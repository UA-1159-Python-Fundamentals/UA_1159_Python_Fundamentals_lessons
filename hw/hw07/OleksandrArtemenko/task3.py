def number_of_chars(word):
    """
    :param word: str
    :return: dict
    returns a dictionary with key as a character and value as its count in a word
    """
    return {char: word.count(char) for char in word}


# print(number_of_chars("hello"))
