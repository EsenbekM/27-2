from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from decouple import config

storage = MemoryStorage()

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

ADMINS = (5367214519, )
OPENAI_TOKEN = "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"
