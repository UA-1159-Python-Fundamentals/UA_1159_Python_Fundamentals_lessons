import sys
from pathlib import Path

try:
    current_directory = Path(__file__).parent

    fonts_folder = current_directory / "Fonts"
    original_folder = current_directory / "Жалкие пародии"
    resulted_folder = current_directory / "Неповторимые оригиналы"
    fill_folder = resulted_folder / "fill"
    inpaint_folder = resulted_folder / "inpaint"
    text_folder = resulted_folder / "text"

    # Create folders if they aren't exist
    for folder in (fonts_folder,
                   original_folder,
                   resulted_folder,
                   fill_folder,
                   inpaint_folder,
                   text_folder):
        folder.mkdir(parents=True, exist_ok=True)
except PermissionError as error:
    print(f"{error}\nYou have no permissions to create new folder")
    sys.exit()