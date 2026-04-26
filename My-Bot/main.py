import os
import asyncio
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

load_dotenv()
logging.basicConfig(level=logging.INFO)

api = os.getenv('api_key')
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())