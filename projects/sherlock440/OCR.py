import sys

import easyocr
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

reader = easyocr.Reader(['en', 'ru', 'uk'])  # ! In the first time it downloads some packages during some time — wait

def recognize_words(image_path: str) -> dict:
    result = reader.readtext(image_path)
    # [
    # ([[612, 114], [1074, 114], [1074, 286], [612, 286]], 'Hello', 0.9999672130473339),
    # ...
    # ]
    #
    # Returns list of tuples ——— [(),(),()]. Each of the tuples consists:
    # 1. list of 4 coordinates, each coordinate is [x, y] ——— [ [], [], [], [] ]
    # 2. string of the word ——— 'word'
    # 3. float of the model confident level

    if not result:
        print(f"Words are not found :(")
        sys.exit()

    recognized_words = {}

    for element in result:
        word = element[1]  # getting a recognized word

        word_dict = {
            'confident_level': element[-1],
            'corner_LU': element[0][0],
            'corner_RU': element[0][1],
            'corner_RD': element[0][2],
            'corner_LD': element[0][3],
        }

        recognized_words[word] = word_dict

    print("In the picture I found:")
    for element in recognized_words:
        print(f"— \033[33m{element}\033[0m")

    print()
    return recognized_words
