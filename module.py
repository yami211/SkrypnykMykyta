import math
import json

def translate(key, lang):
    texts = {
        "uk": {
            "enter_coords": "Введіть координати точки A(x,y): ",
            "enter_r": "Введіть радіус першого кола r: ",
            "enter_R": "Введіть радіус другого кола R: ",
            "enter_lang": "Введіть мову інтерфейсу (uk/en): ",
            "data_saved": "Дані збережено в файл",
            "lang_name": "Мова: Українська",
            "coords": "Координати точки A(x,y):",
            "radius_r": "Радіус першого кола r:",
            "radius_R": "Радіус другого кола R:",
            "distance": "Відстань до точки A:",
            "inside": "Точка знаходиться всередині тора.",
            "outside": "Точка не знаходиться всередині тора.",
            "input_error": "Помилка вводу! Дані не збережено."
        },
        "en": {
            "enter_coords": "Enter coordinates of point A(x,y): ",
            "enter_r": "Enter radius of the first circle r: ",
            "enter_R": "Enter radius of the second circle R: ",
            "enter_lang": "Enter interface language (uk/en): ",
            "data_saved": "Data saved to file",
            "lang_name": "Language: English",
            "coords": "Coordinates of point A(x,y):",
            "radius_r": "Radius of the first circle r:",
            "radius_R": "Radius of the second circle R:",
            "distance": "Distance to point A:",
            "inside": "The point is inside the torus.",
            "outside": "The point is not inside the torus.",
            "input_error": "Input error! Data not saved."
        }
    }
    return texts.get(lang, texts["uk"]).get(key, key)


def distance(x, y):
    return math.sqrt(x ** 2 + y ** 2)

def point_in_torus(x, y, r, R):
    d = distance(x, y)
    return R - r <= d <= R + r
