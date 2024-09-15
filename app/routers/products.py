from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.data import files_actions, list_files
from app.keyboards.products import prods_keyboard_builder, prod_actions_keyboards
from app.forms.product import ProductForm


prods_router = Router()


@prods_router.message(F.text == "Показати всі товари")
async def show_products(message: Message, state: FSMContext):
    products = files_actions.open_file()
    keyboard = prods_keyboard_builder(products)
    await message.answer(
        text="Виберіть товар",
        reply_markup=keyboard
    )


@prods_router.callback_query(F.data.startswith("prod_"))
async def product_actions(callback: CallbackQuery, state: FSMContext):
    product = callback.data.split("_")[-1]
    keyboard = prod_actions_keyboards(product)
    await callback.message.answer(
        text=product,
        reply_markup=keyboard
        )


@prods_router.callback_query(F.data.startswith("sold_prod_"))
async def sold_product(callback: CallbackQuery, state: FSMContext):
    product = callback.data.split("_")[-1]
    msg = files_actions.sold_product(product)
    await callback.message.answer(text=msg)


@prods_router.callback_query(F.data.startswith("del_prod_"))
async def del_product(callback: CallbackQuery, state: FSMContext):
    product = callback.data.split("_")[-1]
    msg = files_actions.del_product(product)
    await callback.message.answer(text=msg)


@prods_router.message(F.text == "Додати новий товар")
async def add_product(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(ProductForm.name)
    await message.answer(text="Введіть назву товару")


@prods_router.message(ProductForm.name)
async def save_new_product(message: Message, state: FSMContext):
    data = await state.update_data(name=message.text)
    await state.clear()
    msg = files_actions.add_product(data.get("name"))
    await message.answer(text=msg)


@prods_router.message(F.text == "Показати продані товари")
async def show_sold_prods(message: Message, state: FSMContext):
    sold_products = files_actions.open_file(list_files.SOLD_PRODUCTS)

    msg = ""
    for i, prod in enumerate(sold_products, start=1):
        msg += f"{i}. {prod}\n"

    await message.answer(text=msg)
