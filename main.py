import json
import os
from module import distance, point_in_torus, translate

FILENAME = "MyData.json"

def read_data():
    if not os.path.exists(FILENAME):
        return None
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            data = json.load(file)
        # Перевірка наявності потрібних ключів
        if not all(k in data for k in ("x", "y", "r", "R", "lang")):
            return None
        return data
    except (json.JSONDecodeError, FileNotFoundError):
        return None


def write_data(data):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Дані збережено в файл {FILENAME}")


def main():
    data = read_data()

    if data is None:
        try:
            x, y = map(float, input("Введіть координати точки A(x,y): ").split())
            r = float(input("Введіть радіус першого кола r: "))
            R = float(input("Введіть радіус другого кола R: "))
            lang = input("Введіть мову інтерфейсу (uk/en): ").strip().lower()
            write_data({"x": x, "y": y, "r": r, "R": R, "lang": lang})
        except ValueError:
            print("Помилка вводу! Дані не збережено.")
        return

    
    x, y, r, R, lang = data["x"], data["y"], data["r"], data["R"], data["lang"]

    
    if lang not in ("uk", "en"):
        lang = "uk"

    print(translate("lang", lang))
    print(f"Координати точки A(x,y): {x} {y}")
    print(f"Радіус першого кола r: {r}")
    print(f"Радіус другого кола R: {R}")

    d = distance(x, y)
    print(f"{translate('distance', lang)}: {d:.2f}")

    if point_in_torus(x, y, r, R):
        print(translate("inside", lang))
    else:
        print(translate("outside", lang))


if __name__ == "__main__":
    main()
