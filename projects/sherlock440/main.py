from other import *
from directories import *
from OCR import recognize_words
from fill import fill_it
from inpaint import inpaint_it
from text import write_text

import time
import sys

# * Starting and checking the directory
print("Checking a folder with images...\n")

files_dict = {number + 1: file.name for number, file in enumerate(original_folder.iterdir())}

if not files_dict:
    print(f"Folder {original_folder} is empty")
    sys.exit()

message = ""
for number, value in files_dict.items():
    message += f"\033[33m{number}\033[0m. {value}\n"

print_cyan("\nChoose a picture")
answer = choose_a_picture(message, len(files_dict))

chosen_picture_name = files_dict[answer]
chosen_picture_path = str(current_directory / original_folder / chosen_picture_name)

# * OCRing
print_cyan("\n\nCHOOSE WORD(S)")
found_words = recognize_words(chosen_picture_path)  # dict
words_to_replace = choose_a_word(tuple(found_words.keys()))  # tuple

# * Choosing how to fill — via just filling or inpainting
print_cyan("\n\nChoose a method")
method = filling_or_inpainting()

if method == 'FILLING':
    path_after_removing = fill_it(chosen_picture_path, words_to_replace, found_words, chosen_picture_name)

elif method == 'INPAINTING':
    path_after_removing = inpaint_it(chosen_picture_path, words_to_replace, found_words, chosen_picture_name)

# * Inserting new text
print_cyan("\n\nAdjust font parameters")
write_text(chosen_picture_name, path_after_removing, words_to_replace, found_words)

# * Finishing
print('\n\n')
print_cyan('*' * 60)
print("I have not used the 'FINALLY' block, so if you are seeing this message, it means that the app works — it's the "
      "proof that magic outside Hogwarts is allowed",
      '\n',
      "\nIt has been spent more than 2 days for making this app, so I hope the developer didn't fuck up the presentation "
      "like he always does.\nThanks for the attention, see you in the Python Practical course (if boredom of DevOps "
      "course will not have killed me before)")
time.sleep(1)
print('🥰')
time.sleep(1)
print('😘')
time.sleep(1)
print('🍆')
time.sleep(1)
print('💦')
