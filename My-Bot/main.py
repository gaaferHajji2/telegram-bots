import os
import asyncio
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

logging.basicConfig(
    level=logging.INFO, filename="logs.log", filemode="a", 
    format="%(asctime)s %(levelname)s %(message)s"
)

load_dotenv()

api = os.getenv('api_key')
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())

@dp.message()
async def check_message(message):
    print(f"Getting message: {message}")

@dp.callback_query()
async def check_callback_query(call):
    print(f"Test-01: {call}")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())