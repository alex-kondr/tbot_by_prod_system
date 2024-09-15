import json
import os

from app.data import list_files



def open_file(path: str = list_files.PRODUCTS) -> list:

    if not os.path.exists(path):
        with open(path, "w") as fh:
            json.dump([], fh)

    with open(path, "r", encoding="utf-8") as file:
        products = json.load(file)

    return products


def save_file(file: list, path: str = list_files.PRODUCTS):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(file, fh, indent=4, ensure_ascii=False)


def del_product(product):
    products = open_file()
    products.remove(product)
    save_file(products)

    return f"Товар '{product}' успішно видалено"


def sold_product(product, path: str = list_files.SOLD_PRODUCTS) -> str:
    del_product(product)

    sold_products = open_file(path)
    sold_products.append(product)
    save_file(sold_products, path)

    return f"Товар '{product}' успішно продано."


def add_product(product, path: str = list_files.PRODUCTS) -> str:
    products = open_file()

    if product not in products:
        products.append(product)
        save_file(products)
        msg = f"Товар '{product}' успішно додано."
    else:
        msg = f"товар '{product}' вже є у списку товарів."

    return msg