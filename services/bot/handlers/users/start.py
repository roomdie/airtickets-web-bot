from aiogram import types, Dispatcher
from services.bot import config

async def main_handler(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(
        text="App",
        web_app=types.WebAppInfo(url=config.APP_URL)
    )
    keyboard.add(btn)

    await message.answer(
        "<b>Hi 👋</b>\n\n"
        "To order tickets click the button below.",
        reply_markup=keyboard,
    )


def setup(dp: Dispatcher):
    dp.register_message_handler(
        main_handler,
        commands=["start"],
    )




