import logging
import asyncio
import config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types
import handlers
import admin_notice
from services import database

logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
    level=logging.INFO,
)


async def main():
    bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    db = database.implement.AsyncPostgreSQL(
        database_name=config.PSQL_DB_NAME,
        username=config.PSQL_USERNAME,
        password=config.PSQL_PASSWORD,
        hostname=config.PSQL_HOSTNAME,
        port=5432
    )
    _bot = await bot.get_me()
    logging.info(f"Bot: @{_bot.username}")
    session = await database.manager.create_async_session(db)
    bot["session"] = session
    #
    # middlewares.setup(dp)
    # filters.setup(dp)
    handlers.setup(dp)

    await admin_notice.send(dp)
    try:
        await dp.skip_updates()     # Don't use this in production
        await dp.start_polling(allowed_updates=types.AllowedUpdates.all())
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot stopped!")
