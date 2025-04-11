from aiogram.types import Message, CallbackQuery 
from aiogram import F
from loader import dp
from src.db import init_db, add_user, sleep_yes, sleep_no, all_users

init_db()

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
