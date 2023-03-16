from aiogram import types, Dispatcher
from config import bot, OPENAI_TOKEN
import openai

openai.api_key = OPENAI_TOKEN


# @dp.message_handler()
async def filter_bad_words(message: types.Message):
    bad_words = ['html', 'css', 'js', 'дурак', 'жинди']
    username = f"@{message.from_user.username}" \
        if message.from_user.username is not None else message.from_user.full_name
    for word in bad_words:
        if word in message.text.lower().replace(' ', ''):
            await message.answer(f"Не матерись {username}, Сам ты {word}")
            # await bot.delete_message(message.chat.id, message.message_id)
            await message.delete()
            break

    if message.text.startswith('.'):
        # await bot.pin_chat_message(message.chat.id, message.message_id)
        await message.pin()

    if message.text == 'dice':
        a = await bot.send_dice(message.chat.id)
        # print(a.dice.value)
        # await message.answer_dice(emoji="🎳")

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
