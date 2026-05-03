import os
import asyncio
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage
from keyboards.example import menu, inline_kb
import texts

logging.basicConfig(
    level=logging.INFO, filename='logs.log', filemode='a', 
    format='%(asctime)s %(levelname)s %(message)s'
)

load_dotenv()

api = os.getenv('api_key')
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())

"""
A one-time keyboard displays its buttons only once. This is controlled by 
the `one_time_keyboard` argument, which accepts a boolean value (default is `False`). 
When set to `True`, the keyboard appears on the first message and automatically 
disappears after the user presses any button. 
However, the user can still manually reopen it by tapping the keyboard icon 
next to the text input field.
"""

"""
A persistent keyboard gives the user continuous access throughout the chat session. 
The `is_persistent` argument determines whether the keyboard can be manually 
toggled (default is `False`). When set to `True`, the manual toggle button disappears, 
and the keyboard automatically collapses when the user starts typing in the input field. 
This helps maintain a cleaner interface during active text input.
"""

# Here we should organize the messages with filters first
@dp.message(F.text == 'Hello')
async def check_hello(message):
    await message.answer(texts.say_hello)

@dp.message(F.text == 'Information')
async def get_information(message):
    await message.answer("You can find all the necessary information on our website")

@dp.message(F.text == "Inline")
async def get_inline_kb(message):
    await message.answer("Yoy request inline keyboard", reply_markup=inline_kb)

@dp.callback_query(F.data == 'Russian/English/Arabic')
async def get_languages(message):
    await message.answer("My Languages are: \n1. Russian\n2. Arabic\n3. English")

@dp.callback_query(F.data == "Jafar Loka")
async def get_my_name(message):
    await message.answer("My Name is Jafar Loka.\nI am ITE Engineer & QA Tester")


# If we set this handler first, then it will capture all messages.
@dp.message()
async def check_message(message):
    print(f'Getting message: {message.text}')
    # the answer method must be shorter than 1024 characters. 
    # This limitation is related to the Telegram API.
    await message.answer(texts.hello, reply_markup=menu)

@dp.callback_query()
async def check_callback_query(call):
    # print(f'Test-01: {call}')
    pass

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())