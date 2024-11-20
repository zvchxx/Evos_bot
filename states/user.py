from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterState(StatesGroup):
    language = State()
    full_name = State()
    phone_number = State()

class FeedbackState(StatesGroup):
    feedback_text = State()