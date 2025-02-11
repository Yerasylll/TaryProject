import asyncio
from aiogram import Bot, Dispatcher  # F <- Magic filter

from app.handlers import router

async def main():
    bot = Bot(token="7718789350:AAHJCVL48YSu-lt-0CzpoixddpO-vnWwzBc")
    dp = Dispatcher()  # working with handlers
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is interrupted")