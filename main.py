from aiogram.utils import executor
import logging

from config import dp, bot, ADMINS
from handlers import client, callback, extra, admin, fsm_anketa, schedule
from database.bot_db import sql_create


async def on_startup(dp):
    await schedule.set_scheduler()
    await bot.send_message(ADMINS[0], "Я родился!")
    sql_create()


async def on_shutdown(dp):
    await bot.send_message(ADMINS[0], "ПОКА ПОКА!")

client.register_hadlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsm_anketa.register_handlers_fsm_anketa(dp)

extra.register_hadlers_client(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup, on_shutdown=on_shutdown)
