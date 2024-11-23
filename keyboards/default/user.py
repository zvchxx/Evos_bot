from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import _


async def user_main_menu_keyboard(language):
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("🍴 Menyu", locale=language))
            ],
            [
                KeyboardButton(text=_("🛍 Mening buyurtmalarim", locale=language))
            ],
            [
                KeyboardButton(text=_("✍️ Fikr bildirish", locale=language)),
                KeyboardButton(text=_("⚙️ Sozlamalar", locale=language)),
            ]
        ], resize_keyboard=True
    )

    return markup


languges = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 Uzbek"),
            KeyboardButton(text="🇺🇸 English"),
            KeyboardButton(text="🇷🇺 Русский"),
        ]
    ], resize_keyboard=True
)