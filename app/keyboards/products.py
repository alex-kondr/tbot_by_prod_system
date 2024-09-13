from aiogram.utils.keyboard import InlineKeyboardBuilder


def prods_keyboard_builder(products: list):
    builder = InlineKeyboardBuilder()

    for product in products:
        builder.button(text=product, callback_data=f"prod_{product}")

    builder.adjust(3)
    return builder.as_markup()


def prod_actions_keyboards(product: str):
    builder = InlineKeyboardBuilder()
    builder.button(text="Продати товар", callback_data=f"sold_prod_{product}")
    builder.button(text="Видалити товар", callback_data=f"del_prod_{product}")
    return builder.as_markup()