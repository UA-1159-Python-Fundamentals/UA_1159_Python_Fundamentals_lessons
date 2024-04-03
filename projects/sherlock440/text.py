from other import choose_a_font, choose_a_font_size, choose_font_color, is_daddy_pleased, print_cyan
import sys
from PIL import Image, ImageDraw, ImageFont
from directories import fonts_folder, text_folder
from pathlib import Path


def write_text(picture_name, picture_path, words_to_replace, found_words):
    # Uploading the image
    image = Image.open(picture_path)

    # Creating a temporary copy of the image in order to have an ability to return changes if they are not liked by user
    name, extension = picture_path.rsplit('.', maxsplit=1)
    temp_path = f"{name}_temp.{extension}"
    image.save(temp_path)

    for word in words_to_replace:
        print(f"Let's put a new word instead of '\033[32m{word}\033[0m'!\n")

        is_result_OK = False
        while not is_result_OK:  # in the end we ask a user if he wants to rewrite text again
            image = Image.open(temp_path)
            # Making an object for drawing
            draw = ImageDraw.Draw(image)


            # * Choosing a font
            # Iterating a fonts' folder to ask a user which to choose
            files_dict = {number + 1: file.name for number, file in enumerate(fonts_folder.iterdir())}

            if not files_dict:
                print(f"There are no fonts in your {fonts_folder} :(")
                sys.exit()

            elif len(files_dict) == 1:
                print(f"I found only one font, you lazy prick, so let's work with it :(")
                font_path = f"{fonts_folder}/{files_dict[1]}"

                font_name = files_dict[1]  # we will need it later

            else:  # if there are more than 1 font
                message = ""
                for number, file in files_dict.items():
                    message += f"\033[33m{number}\033[0m. {file}\n"

                font_number = choose_a_font(message, len(files_dict))

                font_path = f"{fonts_folder}/{files_dict[font_number]}"

                font_name = files_dict[font_number]  # we will need it later

            # * Choosing a font size, color and inscription
            font_size = choose_a_font_size()
            font = ImageFont.truetype(font_path, font_size)

            font_color = choose_font_color()

            print_cyan("\n\nEnter a text and check it out then")
            text = input("Enter a \033[33mtext\033[0m to put it \033[34m=>\033[0m ")

            # * Calculating a center position of inserting the text
            # Getting coordinates of the center point where initial word was
            corner_LU, corner_RD = ((found_words[word]['corner_LU']),
                                    (found_words[word]['corner_RD']))

            center_X = corner_LU[0] + (corner_RD[0] - corner_LU[0]) / 2
            center_Y = corner_LU[1] + (corner_RD[1] - corner_LU[1]) / 2

            # Checking parameters of the text that will be put
            left, up, right, down = draw.textbbox((0, 0), text, font=font)
            # getting coordinates of the text box, (0, 0) — anchor, in our case these numbers don't matter

            text_width = right - left
            text_height = down - up

            # Setting a new start point for inserting text knowing its size

            # Different fonts have different real height, and I don't know how to calculate it — I mean that just
            # dividing by 2 in the last part of "start_position" line doesn't work in every case. So I have to adjust
            # this dividing parameter manually. I am creating a dict with proper values for each font

            divider_for_font = {
                "MarkerFelt.ttc": 2,
                "Arial Bold.ttf": 1.2
            }

            start_position = (float(center_X - text_width / 2),
                              float(center_Y - text_height / divider_for_font.get(font_name, 2)))
            # if there is no value in the dict, it takes "2" as default. And there are float(), because the following
            # .text() method requires float values in the tuple

            # * Inserting the text to the image
            draw.text(start_position, text, fill=font_color, font=font)

            image.show(title=f"Preview of {picture_name} that is being edited")

            is_result_OK = is_daddy_pleased()  # if user likes the result, it returns True and "while" is stopped

            if is_result_OK:
                image.save(temp_path)

    # * Saving result as a new image
    name, extension = picture_name.rsplit('.', maxsplit=1)
    picture_modified_name = f"{name}-modified.{extension}"

    resulted_picture_path = str(text_folder / picture_modified_name)
    image.save(resulted_picture_path)

    Path(temp_path).unlink()  # deleting a temporary file
