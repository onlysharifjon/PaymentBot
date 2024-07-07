from aiogram.dispatcher.filters.state import State, StatesGroup


class BotStates(StatesGroup):
    humo_uzcard = State()
    uzb = State()
    rub = State()
    usd = State()
    fill_uzb = State()
    fill_rub = State()
    fill_usd = State()
