from aiogram import types, Dispatcher
from config import bot, ADMINS
from database.bot_db import sql_command_all, sql_command_delete
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def ban(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMINS:
            await message.answer("Ты не мой БОСС!")
        elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await bot.kick_chat_member(
                message.chat.id,
                message.reply_to_message.from_user.id,
            )
            await message.answer(f"{message.from_user.first_name} братан кикнул "
                                 f"{message.reply_to_message.from_user.full_name}")
    else:
        await message.answer("Пиши в группе!")


async def delete_data(message: types.Message):
    users = await sql_command_all()
    for user in users:
        await message.answer_photo(
            photo=user[-1],
            caption=f"{user[2]} {user[3]} {user[4]} "
                    f"{user[5]}\n@{user[1]}",
            reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton(f"DELETE {user[2]}",
                                     callback_data=f"DELETE {user[0]}")
            )
        )


async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace("DELETE ", ""))
    await call.answer(text="Удалено!", show_alert=True)
    await call.message.delete()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix="!/")
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith("DELETE "))
