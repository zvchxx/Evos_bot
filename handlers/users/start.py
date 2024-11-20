from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.common import phone_number_share_keyboard
from keyboards.default.user import user_main_menu_keyboard

from loader import dp, bot

from main.config import ADMINS

from states.user import FeedbackState, RegisterState

from utils.user import get_user, add_user


@dp.message_handler(commands="start", chat_id=ADMINS, state="*")
async def start_handler(message: types.Message, state: FSMContext):
    await state.finish()
    user = await get_user(chat_id=message.chat.id)
    if user:
        text = "Evos botiga xush kelibsiz 😊"
        await message.answer(text=text, reply_markup=await user_main_menu_keyboard())
    else:
        text = "Kechirasiz, siz to'liq ismingizni kiritishingiz kerak 😊"
        await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
        await RegisterState.full_name.set()


@dp.message_handler(state=RegisterState.full_name)
async def get_full_name_handler(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)

    text = "Iltimos, quyidagi tugma orqali telefon raqamingizni kiriting 👇"
    await message.answer(text=text, reply_markup=await phone_number_share_keyboard())
    await RegisterState.phone_number.set()


@dp.message_handler(state=RegisterState.phone_number, content_types=types.ContentTypes.CONTACT)
async def get_phone_number_handler(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    data = await state.get_data()
    new_user = await add_user(message=message, data=data)
    if new_user:
        text = "Siz roʻyxatdan oʻtdingiz ✅"
        await message.answer(text=text, reply_markup=await user_main_menu_keyboard())
    else:
        text = "Kechirasiz, keyinroq qayta urinib ko'ring 😔"
        await message.answer(text=text)
    await state.finish()


@dp.message_handler(text="Fikr bildirish")
async def feedback_handler(message: types.Message):
    text = "Fikringizni yozing va menga yuboring 👇"
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await FeedbackState.feedback_text.set()


@dp.message_handler(state=FeedbackState.feedback_text)
async def feedback_submit_handler(message: types.Message, state: FSMContext):
    feedback_text = message.text

    for admin in ADMINS:
        await bot.send_message(chat_id=admin, text=f"Yangi fikr:\n\n{feedback_text}")

    await message.answer("Fikringiz uchun rahmat! ✅", reply_markup=await user_main_menu_keyboard())
    await state.finish()