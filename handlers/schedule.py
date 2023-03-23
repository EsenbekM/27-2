import datetime

from aiogram import Bot
from database.bot_db import sql_command_get_id_name
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.date import DateTrigger
from config import bot, ADMINS


async def go_to_sleep(bot: Bot):
    users = await sql_command_get_id_name()
    for user in users:
        await bot.send_message(user[0], f"Иди спать {user[1]}")


async def wake_up(bot: Bot):
    video = open('media/video.mp4', 'rb')
    await bot.send_video(ADMINS[0], video=video, caption="ВСТАВААААААЙ!!!")


async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")

    # scheduler.add_job(
    #     go_to_sleep,
    #     trigger=CronTrigger(
    #         hour=20,
    #         minute=55,
    #         start_date=datetime.datetime.now()
    #     ),
    #     kwargs={"bot": bot}
    # )

    scheduler.add_job(
        wake_up,
        trigger=DateTrigger(
            run_date=datetime.datetime(
                year=2024, month=1, day=1, hour=12, minute=0, second=0
            )
        ),
        kwargs={"bot": bot}
    )

    scheduler.start()
