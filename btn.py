from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📮 Hisob to'ldirish")
        ],
        [
            KeyboardButton("💳 Hisob raqamlar"),
            KeyboardButton("📤 Yechib olish")
        ],
        [
            KeyboardButton("📆 Amallar, 💰Kurs-Zahira"),
            KeyboardButton("📲 Bog'lanish")
        ]
    ], resize_keyboard=True
)

hisob_toldirish = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🔙 Bosh menyu")
        ],
        [
            KeyboardButton("🇺🇿 1XBET UZB"),
            KeyboardButton("🇷🇺 1XBET RUB")
        ],
        [
            KeyboardButton("🇺🇸 1XBET USD")
        ]
    ], resize_keyboard=True
)

# inline
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

cards_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='UZCARD / HUMO', callback_data='add_card')
        ],
        [
            InlineKeyboardButton(text='1XBET RUB', callback_data='xbet_rub'),
            InlineKeyboardButton(text='1XBET USD', callback_data='xbet_usd'),
            InlineKeyboardButton(text='1XBET UZB', callback_data='xbet_uzb')
        ]
    ]
)
