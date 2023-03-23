from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta

from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.date import DateTrigger
from apscheduler.triggers.interval import IntervalTrigger

from config import ADMINS, bot


async def send_message_time(bot: Bot):
    await bot.send_message(chat_id=ADMINS[0],
                           text='это сообщение через несколько сек после запуска бота')


async def send_message_cron(bot: Bot):
    await bot.send_message(chat_id=ADMINS[0],
                           text='Это сообщение будет отправляться каждый день')


async def send_message_interval(bot: Bot):
    await bot.send_message(chat_id=ADMINS[0],
                           text='Это сообщение будет оптравляться с интервалом в 1 минуту')


async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone='Asia/Bishkek')
    scheduler.add_job(send_message_time,
                      trigger=DateTrigger(run_date=datetime.now() + timedelta(seconds=10)),
                      kwargs={'bot': bot})
    scheduler.add_job(send_message_cron,
                      trigger=CronTrigger(
                          hour=11,
                          minute=20,
                          start_date=datetime.now(), ),
                      kwargs={'bot': bot})
    scheduler.add_job(send_message_interval,
                      trigger=IntervalTrigger(seconds=60,),
                      kwargs={'bot': bot})
    scheduler.start()
