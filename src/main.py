import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery 

from src.keyb import inline_key as kb
from db import init_db, add_user, sleep_yes, sleep_no, all_users
from dotenv import load_dotenv

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
logging.basicConfig(level=logging.INFO)
dp = Dispatcher()
init_db()


@dp.message(Command('start'))
async def cmd_start(message:Message):
    user_id = message.from_user.id
    username = message.from_user.username
    add_user(user_id, username)
    await message.answer(f'Hello {message.from_user.full_name}. This bot is designed to monitor your friends sleep.', reply_markup=await kb.inline_key())


@dp.callback_query(F.data == 'Sleep')
async def Sleep(callback:CallbackQuery):
    user_id = callback.from_user.id
    username = callback.from_user.username
    sleep_status = 'Sleep'
    sleep_yes(user_id, username, sleep_status)
    await callback.answer()
    await callback.message.answer('😵 Sleep')

@dp.callback_query(F.data == 'Not_Sleeping')
async def Not_Sleep(callback:CallbackQuery):
    user_id = callback.from_user.id
    username = callback.from_user.username
    sleep_status = 'Not_Sleeping'
    sleep_no(user_id, username, sleep_status)
    await callback.answer()
    await callback.message.answer('👁 Not sleeping')

@dp.callback_query(F.data == 'Check your friends')
async def Check_friends(callback:CallbackQuery):
    users = all_users()
    if not users:
        response = 'No user data'
    else:
        response = 'Friends statuses:\n'
        for user in users:
            status = '👁 Not sleeping' if user[2] == 'Not_Sleeping' else '😵 Sleep'
            response += f'{user[1]}: {status}\n'
    await callback.answer()
    await callback.message.answer(response)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    print('Бот польностью готов к работе')
    asyncio.run(main())

