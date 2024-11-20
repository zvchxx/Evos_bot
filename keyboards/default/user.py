from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def user_main_menu_keyboard():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🍴 Menyu")
            ],
            [
                KeyboardButton(text="🛍 Mening buyurtmalarim")
            ],
            [
                KeyboardButton(text="✍️ Fikr bildirish"),
                KeyboardButton(text="⚙️ Sozlamalar"),
            ]
        ], resize_keyboard=True
    )

    return markup

async def user_main_menu_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Fikr bildirish"))
    return markup