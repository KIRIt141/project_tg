from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


async def inline_key():
    keyboar = InlineKeyboardBuilder()
    keyboar.add(InlineKeyboardButton(text='Sleep', callback_data='Sleep')),
    keyboar.add(InlineKeyboardButton(text='Not sleeping', callback_data='Not_Sleeping')),
    keyboar.add(InlineKeyboardButton(text='Сheck friends', callback_data='Check your friends')),
    keyboar.add(InlineKeyboardButton(text='Fan button', url='https://www.youtube.com/watch?v=PskJj9jw3mQ&ab_channel=%D0%90%D1%81%D1%82%D1%80%D0%BE%D0%A7%D0%B5%D0%BB'))
    return keyboar.adjust(2, 1).as_markup()


# knopka = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='Статус пользователей')],
#     [KeyboardButton(text='Задать свой стаутс')],
# ],
#         resize_keyboard=True,
#         input_field_placeholder="Goul")

# knopka = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Cплю', url='https://www.youtube.com/@kiwkisquad')], 
#     [InlineKeyboardButton(text='Не сплю', url='https://www.youtube.com/@kiwkisquad')],
#     [InlineKeyboardButton(text='Проверить друзей', url='https://www.youtube.com/watch?v=qRyshRUA0xM&ab_channel=%24sudoteachIT%E2%9A%99%EF%B8%8F')]
# ])

# status = ['Сплю', 'Не сплю', 'Проверить друзей']

# async def inline_key():
#     keyboar = InlineKeyboardBuilder()
#     for status_key in status:
#         keyboar.add(InlineKeyboardButton(text=status_key, url='https://www.youtube.com/watch?v=6_WvZlaHtgw&ab_channel=Krakenshel'))
#     return keyboar.adjust(2).as_markup()


# status = ['Сплю', 'Не сплю', 'Проверить друзей']


