import math
import json

def translate(text, lang):
    translations = {
        "uk": {
            "inside": "Точка знаходиться всередині тора.",
            "outside": "Точка не знаходиться всередині тора.",
            "lang": "Мова: Українська",
            "distance": "Відстань до точки A"
        },
        "en": {
            "inside": "The point is inside the torus.",
            "outside": "The point is not inside the torus.",
            "lang": "Language: English",
            "distance": "Distance to point A"
        }
    }
    return translations.get(lang, translations["uk"]).get(text, text)


def distance(x, y):
    return math.sqrt(x ** 2 + y ** 2)



def point_in_torus(x, y, r, R):
    d = distance(x, y)
    return R - r <= d <= R + r
