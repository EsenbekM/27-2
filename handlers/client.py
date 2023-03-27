from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from config import bot, dp
from keyboards.client_kb import start_markup
from database.bot_db import sql_command_random
from parser.movies import parser


# @dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        f"Салалекум хозяин {message.from_user.full_name}",
        reply_markup=start_markup
    )


# @dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        f"Разбирайся сам!"
    )


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = "By whom invented Python?"
    answers = [
        "Harry Potter",
        "Putin",
        "Guido Van Rossum",
        "Voldemort",
        "Griffin",
        "Linus Torvalds",
    ]
    # await message.answer_poll()
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=10,
        reply_markup=markup
    )


async def get_random_user(message: types.Message):
    random_user = await sql_command_random()
    await message.answer_photo(
        photo=random_user[-1],
        caption=f"{random_user[2]} {random_user[3]} {random_user[4]} "
                f"{random_user[5]}\n@{random_user[1]}"
    )


async def get_movies(message: types.Message):
    movies = parser()
    count = int(message.text.split()[1]) if len(message.text.split()) > 1 else 10
    for movie in movies:
        if count == 0:
            break
        await message.answer(
            f"<a href='{movie['url']}'>{movie['title']}</a>\n"
            f"<b>{movie['content']}</b>\n"
            f"#Y{movie['year']}\n"
            f"#{movie['country']}\n"
            f"#{movie['genre']}\n",
            reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton("СМОТРЕТЬ!👻", url=movie['url'])
            ),
            parse_mode=ParseMode.HTML
        )
        count -= 1


def register_hadlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(get_random_user, commands=['get'])
    dp.register_message_handler(get_movies, commands=['movies'])
