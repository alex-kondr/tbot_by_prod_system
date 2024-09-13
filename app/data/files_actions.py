import json

from app.data import list_files


def open_file(path: str = list_files.PRODUCTS) -> list:
    with open(path, "r", encoding="utf-8") as file:
        products = json.load(file)

    return products