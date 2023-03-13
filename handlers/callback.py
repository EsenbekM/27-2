from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp


# @dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_2")
    markup.add(button_1)

    question = "Сколько дней в году?"
    answers = [
        "123",
        "365",
        "666",
        "32",
        "БЕССКОНЕЧНОСТЬ",
        "-3",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Стыдно не знать",
        open_period=10,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    question = "Сколько?"
    answers = [
        '4',
        '8',
        '4, 6',
        '2, 4',
        '5',
    ]

    photo = open('media/problem1.jpg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo, caption="HAHAHAH")

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Стыдно не знать",
        open_period=10,
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_1")
    dp.register_callback_query_handler(quiz_3, text="button_2")
