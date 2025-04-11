from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery 
from src.keyb import inline_key 
from loader import dp
from src.db import add_user


@dp.message(Command('start'))
async def cmd_start(message:Message):
    user_id = message.from_user.id
    username = message.from_user.username
    add_user(user_id, username)
    await message.answer(f'Hello {message.from_user.full_name}. This bot is designed to monitor your friends sleep.', reply_markup=inline_key())