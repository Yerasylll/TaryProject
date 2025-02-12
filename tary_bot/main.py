# import json
# import asyncio
# from aiogram import Bot, Dispatcher
#
# from tary_bot.app.handlers import router
#
# async def main():
#     bot = Bot(token="7718789350:AAHJCVL48YSu-lt-0CzpoixddpO-vnWwzBc")
#     dp = Dispatcher()
#     dp.include_router(router)
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":
#     try:
#         asyncio.run(main())
#     except KeyboardInterrupt:
#         print("Bot is interrupted")
#

import json
import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from tary_bot.app.handlers import router

# Load environment variables
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

async def main():
    bot = Bot(token="7718789350:AAHJCVL48YSu-lt-0CzpoixddpO-vnWwzBc")
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is interrupted")
