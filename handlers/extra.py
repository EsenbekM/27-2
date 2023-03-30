from aiogram import types, Dispatcher
from config import bot, OPENAI_TOKEN
import openai
from .loader import download_audio

openai.api_key = OPENAI_TOKEN


# @dp.message_handler()
async def filter_bad_words(message: types.Message):
    if "youtube.com" in message.text:
        await message.answer("Loading...")
        video = open(download_audio(message.text), "rb")
        await message.answer_audio(video)


    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    await message.answer(response['choices'][0]["text"])


def register_hadlers_client(dp: Dispatcher):
    dp.register_message_handler(filter_bad_words)
