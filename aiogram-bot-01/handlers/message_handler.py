from aiogram import F, Router
from aiogram.types import FSInputFile, URLInputFile
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

@router.message(F.text == 'Image')
async def get_image(message):
    img = FSInputFile('files/images.png')
    await message.answer_photo(img, 'Check this image')

@router.message(F.text == 'URL Image')
async def get_url_image(message):
    img = URLInputFile('https://zelenyimir.ru/wp-content/uploads/2023/03/moree.jpg')
    await message.answer_photo(img, 'Check this url message')

# If we set this handler first, then it will capture all messages.
@router.message()
async def check_message(message):
    print(f'Getting message: {message.text}')
    # the answer method must be shorter than 1024 characters. 
    # This limitation is related to the Telegram API.
    await message.answer(texts.hello, reply_markup=menu)
