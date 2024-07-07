import logging
from aiogram import Bot, Dispatcher, executor, types
from db_bot import *
from btn import *

API_TOKEN = '7357038647:AAHNXsX4gg1oaggg7Yj41zOWIzGB7lTCiNg'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Start command handler
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = str(message.from_user.id)
    check = await check_user(user_id)
    get_contact = types.ReplyKeyboardMarkup(resize_keyboard=True)
    contact_button = types.KeyboardButton('📞 Raqamni yuborish', request_contact=True)
    get_contact.add(contact_button)
    if check is None:
        caption = "<b>Telefon raqamingizni pastdagi tugmani bosib yuboring</b>"
        await bot.send_message(chat_id=message.from_user.id, text=caption, parse_mode="HTML", reply_markup=get_contact)
    else:
        caption = "<b>TestPay</b> - telegram tarmog`idagi yirik\nvalyuta ayirboshlash sistemasi"
        await bot.send_message(chat_id=message.from_user.id, text=caption, parse_mode="HTML", reply_markup=menu)


# Help command handler
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply(
        "I can do the following:\n/start - Welcome message\n/help - List of commands\nAnd I can echo any message you send!")


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_user_phone(message: types.Message):
    phone = message.contact.phone_number
    user_id = str(message.from_user.id)
    await add_user(user_id, phone)
    caption = "<b>TestPay</b> - telegram tarmog`idagi yirik\nvalyuta ayirboshlash sistemasi"
    await bot.send_message(chat_id=message.from_user.id, text=caption, parse_mode="HTML", reply_markup=menu)


@dp.message_handler(text="📮 Hisob to'ldirish")
async def fill_in(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Hisobingizga pul solmoqchi bo'lgan Kontorani bosing:",
                           reply_markup=hisob_toldirish)


@dp.message_handler(text="🔙 Bosh menyu")
async def back_menu(message: types.Message):
    await message.delete()
    await bot.send_message(chat_id=message.from_user.id, text="Bosh menyu", reply_markup=menu)


@dp.message_handler(text="💳 Hisob raqamlar")
async def payment(message: types.Message):
    information = '''
🧰 UZCARD & HUMO: 

📌 1XBET UZB: 

📌 1XBET RUB: 

📌 1XBET USD:     
    '''
    await message.answer(information, reply_markup=cards_button)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
