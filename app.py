from aiogram import executor
from loader import dp
from main.database import database
from utils.notify_devs import send_notification_to_devs
import handlers

async def on_startup(dispatcher):
    await database.connect()
    await send_notification_to_devs(dispatcher)


async def on_shutdown(dispatcher):
    await database.disconnect()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)