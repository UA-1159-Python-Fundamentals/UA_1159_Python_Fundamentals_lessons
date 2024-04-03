from directories import inpaint_folder

import cv2
import numpy as np


def inpaint_it(picture_path, words_to_replace, found_words, picture_name) -> str:
    # * Загружаем изображением и создаём его представление в виде массива NumPy
    image = cv2.imread(picture_path)
    # Переменная image содержит изображение в формате BGR (синий, зелёный, красный)

    # * Создаём маску — указываем области изображения, над которым будем работать (в нашем случае вся картинка)
    blacked = np.zeros(image.shape[:2], np.uint8)
    # ? откуда я взял название переменной (blacked) — секрет
    # np.zeros — создаёт массив из одних только нулей, соответствующих чёрному цвету
    # image.shape[:2] — возвращает размеры массива (высоту, ширину и количество цветовых каналов).
    # Нам важна нужна только высота и ширина, чтобы создать чёрно-белую маску, поэтому делаем срез первых двух
    # элементов
    # np.uint8 — указываем типа элементов в массиве, «uit8» означает, что там будут целые числа от 0 (черный)
    # до 255 (белый)

    print("This method is quite slow... wait")
    for word in words_to_replace:
        if len(words_to_replace) > 1:
            print(f"Working with '{word}'...")

        corner_LU, corner_RD = (tuple(found_words[word]['corner_LU']),
                                tuple(found_words[word]['corner_RD']))  # tuple is required for the cv2.rectangle

        # * Нарисуем белый прямоугольник над областью, которую предстоит закрасить
        cv2.rectangle(blacked, corner_LU, corner_RD, 255, thickness=-1)
        # blacked — указываем нашу маску
        # (612, 114) и (1074, 286) — координаты (X, Y) левого верхнего и правого нижнего угла
        # 255 — белый цвет заливки прямоугольника
        # thickness=-1 — заливка всей внутренней области прямоугольника. На самом деле, этот параметр указывает толщина
        # ободка, но значение «-1» особенное и указывает на заливку всей фигуры


    # * Применяем инпейтинг, то есть заливку на основе окружающих пикселей
    inpainted_image = cv2.inpaint(image, blacked, 100, cv2.INPAINT_TELEA)
    # указываем исходное изображение и маску
    # 100 — это значение inpaintRadius, то есть радиуса окружности вокруг закрашиваемого объекта, определяющей диапазон
    # пикселей для использования при заливке. У меня очень большой, чтобы область была максимально размытой
    # cv2.INPAINT_TELEA — название алгоритма заливки

    # * Сохраняем результат как новое изображение
    name, extension = picture_name.rsplit('.', maxsplit=1)
    picture_modified_name = f"{name}-modified.{extension}"

    resulted_picture_path = str(inpaint_folder / picture_modified_name)
    cv2.imwrite(resulted_picture_path, inpainted_image)
    
    return resulted_picture_path
