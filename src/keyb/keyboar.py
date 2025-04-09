from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def inline_key():
    keyboar = InlineKeyboardBuilder()
    keyboar.add(InlineKeyboardButton(text='Sleep', callback_data='Sleep')),
    keyboar.add(InlineKeyboardButton(text='Not sleeping', callback_data='Not_Sleeping')),
    keyboar.add(InlineKeyboardButton(text='Сheck friends', callback_data='Check your friends')),
    keyboar.add(InlineKeyboardButton(text='Fan button', url='https://www.youtube.com/watch?v=PskJj9jw3mQ&ab_channel=%D0%90%D1%81%D1%82%D1%80%D0%BE%D0%A7%D0%B5%D0%BB'))
    return keyboar.adjust(2, 1).as_markup()
