import webcolors
import re


def choose_a_picture(message: str, files_qty: int) -> int:
    print(f"What lucky you are, I have found some \033[37m\033[9mnudes\033[0m pictures in the folder!\n\n{message}")
    # \033[9 — opening ANSI "tag" for crossing out, \033[37m — grey color, \033[0m — returning to normal

    while True:
        answer = input(f"Enter a \033[33mNUMBER\033[0m of a picture you want to edit \033[34m=>\033[0m ")
        if not answer.isdigit():
            print(f"Your answer '\033[32m{answer}\033[0m' is not a digit. Try again...\n")

        elif not 1 <= int(answer) <= files_qty:
            print(f"Your number '\033[32m{answer}\033[0m' is incorrect! Try again...\n")

        else:
            return int(answer)


def choose_a_word(existing_words: tuple) -> tuple:
    print("Which one would you like to replace?")

    while True:
        answer = input("Just \033[33mcopy-past\033[0m it here, sweat pie (you can choose more than one simultaneously with a coma"
                       "separator, but don't tell it anybody)\n"
                       "Your word(s) \033[34m=>\033[0m ")

        words_to_replace = tuple(answer.split(','))
        words_to_replace = tuple(word.strip() for word in words_to_replace)

        if all(word in existing_words for word in words_to_replace):
            return words_to_replace

        else:
            print("It seems you decided to fuck me up and use one of your sordid trick. UP YOURS!\n")


def filling_or_inpainting() -> str:
    print("If you see this message, it means that the program is working. It can't help but cheer up "
          "\033[37m(and be quite suspicious)\033[0m. Anyway, now you have to choose a method to edit the image: just "
          "filling with a color or wacky inpainting. The last one should be used only for difficult background.")
    print("Now is one of few moments in your life when you really can make a decision — user discretion is advised.\n")

    while True:
        answer = input("Choose a method (enter only \033[33mNUMBER\033[0m):\n"
                       "\033[33m1\033[0m. Just FILLING \033[37m(I am also afraid that the app will be crushed if you choose another one)\033[0m\n"
                       "\033[33m2\033[0m. INPAINTING \033[37m(I am a nagger who finds no easy ways and like fucking up)\033[0m\n\n"
                       "Your answer is \033[34m=>\033[0m ")

        if not answer.isdigit():
            print(f"Your answer '\033[32m{answer}\033[0m' is not a digit. Try again...\n")

        elif str(answer) not in '1 2':
            print(f"Your number '\033[32m{answer}\033[0m' is incorrect! Try again...\n")

        else:
            if answer == '1':
                return "FILLING"
            elif answer == '2':
                return "INPAINTING"


def name_to_bgr(color_name: str) -> tuple:
    """It takes the name of color in css3
    https://www.w3.org/wiki/CSS/Properties/color/keywords"""

    while True:
        try:
            rgb = webcolors.name_to_rgb(color_name.lower())

            return rgb.blue, rgb.green, rgb.red

        except ValueError:
            print("It seems your English is not good, because you fucked up with the color name. Try again")
            color_name = input("Write the color again \033[34m=>\033[0m ")


def choose_a_font(message: str, files_qty: int) -> int:
    print(f"It's time to choose a \033[33mfont\033[0m. Here are fonts:\n{message}")

    while True:
        answer = input(f"Enter the \033[33mNUMBER\033[0m of a font you like \033[34m=>\033[0m ")
        if not answer.isdigit():
            print(f"Your answer '\033[32m{answer}\033[0m' is not a digit. Try again...\n")

        elif not 1 <= int(answer) <= files_qty:
            print(f"Your number '\033[32m{answer}\033[0m' is incorrect! Try again...\n")

        else:
            return int(answer)


def choose_a_font_size() -> int:
    print(f"\nIt's time to choose a \033[32mfont SIZE\033[0m!\n"
          f"Tell my ex that size matters \033[31monly\033[0m in cases like this...\n")

    while True:
        answer = input(f"Enter the font size as a \033[32mNUMBER\033[0m "
                       f"('float' will be converted to 'int', because nobody likes decimals) \033[34m=>\033[0m ")
        if not answer.replace('.', '', 1).isdigit():  # removing one point in case it's a decimal
            print(f"Your answer '\033[32m{answer}\033[0m' is not a digit. Try again...\n")

        elif int(float(answer)) <= 0:
            print(f"Your number '\033[32m{answer}\033[0m' is incorrect! Try again...\n")

        else:
            return int(float(answer))


def choose_font_color() -> tuple:
    """It takes the name of color in css3
    https://www.w3.org/wiki/CSS/Properties/color/keywords"""

    print("\nHi mate, I see you have a brown soul, but the good news is that it shouldn't necessary to be connected "
          "with a font color. So...")

    while True:
        color_name = input("Write a \033[33mcolor name\033[0m (being racist is allowed) \033[34m=>\033[0m ")

        try:
            rgb = webcolors.name_to_rgb(color_name.lower())

            return rgb.red, rgb.green, rgb.blue

        except ValueError:
            print("It seems your English is not good, because you fucked up with the color name. Try again...\n")


def is_daddy_pleased():
    while True:
        answer = input("Is the \033[33mresult\033[0m OK? Y/n \033[34m=>\033[0m ")

        if answer.strip().lower() == "yes" or answer.strip().lower() == "y":
            return True

        elif answer.strip().lower() == "no" or answer.strip().lower() == "n":
            print("Okay, let's do it again...\n")
            return False

        else:
            print("Do you have a hangover or why you weren't able to answer this childish question? Try again!\n")


def print_upper(func):
    def wrapper(message):
        f = func(message)
        beginning, text, ending = re.match(r"(^\x1b\[\d+m)(.+?)(\x1b\[0m$)", f, re.DOTALL).groups()
        # re.DOTALL — по умолчанию «.» соответствует любому символу, кроме переноса строки, но этот флаг добавляет его

        print(f"{beginning}{text.upper()}{ending}")

    return wrapper


@print_upper
def print_cyan(message):
    return f"\x1b[36m{message}\x1b[0m"
