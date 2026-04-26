import os
import asyncio
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage
import texts

logging.basicConfig(
    level=logging.INFO, filename="logs.log", filemode="a", 
    format="%(asctime)s %(levelname)s %(message)s"
)

load_dotenv()

api = os.getenv('api_key')
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())

# Here we should organize the messages with filters first
@dp.message(F.text == 'Hello')
async def check_hello(message):
    await message.answer(texts.say_hello)

# If we set this handler first, then it will capture all messages.
@dp.message()
async def check_message(message):
    print(f"Getting message: {message.text}")
    # the answer method must be shorter than 1024 characters. 
    # This limitation is related to the Telegram API.
    await message.answer(texts.hello)

@dp.callback_query()
async def check_callback_query(call):
    # print(f"Test-01: {call}")
    pass

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())