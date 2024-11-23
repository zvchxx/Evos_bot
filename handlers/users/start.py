from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.common import phone_number_share_keyboard
from keyboards.default.user import user_main_menu_keyboard

from keyboards.default.user import languges

from loader import dp, bot, _

from main.config import ADMINS

from states.user import FeedbackState, RegisterState

from utils.user import get_user, add_user


@dp.message_handler(commands="start", state="*")
async def start_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    language = data.get('language')

    await state.finish()
    user = await get_user(chat_id=message.chat.id)
    if user:
        text = _("Evos botiga xush kelibsiz 😊")
        await message.answer(text=text, reply_markup=await user_main_menu_keyboard(language=language))
    else:
        text = "Tilni tanlang\nSelect Language\nВыберите язык"
        await message.answer(text=text, reply_markup=languges)
        await RegisterState.full_name.set()


@dp.message_handler(state=RegisterState.language)
async def language_handler(message: types.Message, state: FSMContext):
    language = message.text
    if language == "🇺🇿 Uzbek":
        language = "uz"
    elif language == "🇷🇺 Русский":
        language = "ru"
    else:
        language = "en"
    await state.update_data(language=language)
    text = _("Sorry, you have to enter your full name", locale=language)
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await RegisterState.full_name.set()


@dp.message_handler(state=RegisterState.full_name)
async def get_full_name_handler(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    data = await state.get_data()
    language = data.get('language')

    text = _("Iltimos, quyidagi tugma orqali telefon raqamingizni kiriting 👇", locale=language)
    await message.answer(text=text, reply_markup=await phone_number_share_keyboard())
    await RegisterState.phone_number.set()


@dp.message_handler(state=RegisterState.phone_number, content_types=types.ContentTypes.CONTACT)
async def get_phone_number_handler(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    data = await state.get_data()
    language = data.get('language')

    new_user = await add_user(message=message, data=data)
    if new_user:
        text = _("Siz roʻyxatdan oʻtdingiz ✅")
        await message.answer(text=text, reply_markup=await user_main_menu_keyboard())
    else:
        text = _("Kechirasiz, keyinroq qayta urinib ko'ring 😔", locale=language)
        await message.answer(text=text)
    await state.finish()


@dp.message_handler(text=_("⚙️ Sozlamalar"))
async def feedback_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    language = data.get('language')

    text = "Tilni tanlang\nSelect Language\nВыберите язык"
    await message.answer(text=text, reply_markup=languges)
    await RegisterState.full_name.set()


@dp.message_handler(text=_("✍️ Fikr bildirish"))
async def feedback_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    language = data.get('language')

    text = _("Fikringizni yozing va menga yuboring 👇", locale=language)
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await FeedbackState.feedback_text.set()


@dp.message_handler(state=FeedbackState.feedback_text)
async def feedback_submit_handler(message: types.Message, state: FSMContext):
    feedback_text = message.text

    data = await state.get_data()
    language = data.get('language')

    for admin in ADMINS:
        await bot.send_message(chat_id=admin, text=f"\n{feedback_text}")

    await message.answer(_("Fikringiz uchun rahmat! ✅", locale=language), reply_markup=await user_main_menu_keyboard())
    await state.finish()