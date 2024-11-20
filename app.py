from aiogram import executor
from loader import dp
from main.database import database
from utils.notify_devs import send_notification_to_devs


async def on_shutdown(dispatcher):
    await send_notification_to_devs(dispatcher)

    await database.disconnect()

if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=on_shutdown, skip_updates=True)