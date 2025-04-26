
import asyncio
import logging
from aiogram import Bot, Dispatcher
from app.config import BOT_TOKEN
from app.handlers import user, admin

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    dp.include_routers(
        user.router,
        admin.router,
    )

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
