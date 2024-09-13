from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from app.data import files_actions
from app.keyboards.products import prods_keyboard_builder, prod_actions_keyboards


prods_router = Router()


@prods_router.message(F.text == "Показати всі товари")
async def show_products(message: Message, state: FSMContext):
    products = files_actions.open_file()
    keyboard = prods_keyboard_builder(products)
    return message.answer(
        text="Виберіть товар",
        reply_markup=keyboard
    )


@prods_router.callback_query(F.data.startswith("prod_"))
async def product_actions(callback: CallbackQuery, state: FSMContext):
    product = callback.data.split("_")[-1]
    keyboard = prod_actions_keyboards(product)
    return callback.message.answer(
        text=product,
        reply_markup=keyboard
        )
