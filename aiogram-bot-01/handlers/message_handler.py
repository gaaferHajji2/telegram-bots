from aiogram import F, Router
from keyboards.example import inline_kb, menu
import texts

router = Router()

# Here we should organize the messages with filters first
@router.message(F.text == 'Hello')
async def check_hello(message):
    await message.answer(texts.say_hello)

@router.message(F.text == 'Information')
async def get_information(message):
    await message.answer("You can find all the necessary information on our website")

@router.message(F.text == "Inline")
async def get_inline_kb(message):
    await message.answer("You request inline keyboard", reply_markup=inline_kb)

# If we set this handler first, then it will capture all messages.
@router.message()
async def check_message(message):
    print(f'Getting message: {message.text}')
    # the answer method must be shorter than 1024 characters. 
    # This limitation is related to the Telegram API.
    await message.answer(texts.hello, reply_markup=menu)
