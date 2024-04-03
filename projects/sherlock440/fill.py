from other import name_to_bgr
from directories import fill_folder
import cv2


def fill_it(picture_path, words_to_replace, found_words, picture_name) -> str:
    image = cv2.imread(picture_path)

    for word in words_to_replace:
        color = input(f"\nWhat \033[33mcolor\033[0m use to fill over the word '\033[32m{word}\033[0m'? Write the \033[33mname\033[0m \033[34m=>\033[0m ")
        color_bgr = name_to_bgr(color)

        corner_LU, corner_RD = (tuple(found_words[word]['corner_LU']),
                                tuple(found_words[word]['corner_RD']))  # tuple is required for the cv2.rectangle

        cv2.rectangle(image, corner_LU, corner_RD, color_bgr, thickness=-1)

    # Creating new name for the picture that is being modifying
    name, extension = picture_name.rsplit('.', maxsplit=1)
    picture_modified_name = f"{name}-modified.{extension}"

    resulted_picture_path = str(fill_folder / picture_modified_name)
    cv2.imwrite(resulted_picture_path, image)

    return resulted_picture_path
