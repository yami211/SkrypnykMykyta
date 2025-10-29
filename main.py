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
        if not all(k in data for k in ("x", "y", "r", "R", "lang")):
            return None
        return data
    except (json.JSONDecodeError, FileNotFoundError):
        return None


def write_data(data):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"{translate('data_saved', data['lang'])} {FILENAME}")


def main():
    data = read_data()

    if data is None:
        lang = input("Введіть мову інтерфейсу (uk/en): ").strip().lower()
        if lang not in ("uk", "en"):
            lang = "uk"
        try:
            x, y = map(float, input(translate("enter_coords", lang)).split())
            r = float(input(translate("enter_r", lang)))
            R = float(input(translate("enter_R", lang)))
            write_data({"x": x, "y": y, "r": r, "R": R, "lang": lang})
        except ValueError:
            print(translate("input_error", lang))
        return

    x, y, r, R, lang = data["x"], data["y"], data["r"], data["R"], data["lang"]

    if lang not in ("uk", "en"):
        lang = "uk"

    print(translate("lang_name", lang))
    print(f"{translate('coords', lang)} {x} {y}")
    print(f"{translate('radius_r', lang)} {r}")
    print(f"{translate('radius_R', lang)} {R}")

    d = distance(x, y)
    print(f"{translate('distance', lang)} {d:.2f}")

    if point_in_torus(x, y, r, R):
        print(translate("inside", lang))
    else:
        print(translate("outside", lang))


if __name__ == "__main__":
    main()
