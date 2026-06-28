from aiogram import F, Router
from aiogram.types import FSInputFile, URLInputFile
from keyboards.example import inline_kb, menu
import texts
from states.state_sample import DialogBot

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
    await message.answer_photo(img, caption="Test Image")

@router.message(F.text == 'URL Image')
async def get_url_image(message):
    img = URLInputFile('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2G6bAmQHdOrFPYKaqpmR0E7i3qWq93Idw7w&s')
    await message.answer_photo(img, caption="Test Image with URL")

@router.message(F.text == 'File')
async def get_file(message):
    file = FSInputFile('files/jloka.txt')
    # we have also:
        # 1--> answer_video.
        # 2--> answer_animation.
        # 3--> answer_video_note.
        # 4--> In the same way, you can send other, 
        # less frequently used data types such as: audio, stickers, polls, and more
    await message.answer_document(document=file, caption="📄 Here is your text file!")

@router.message(F.text == 'step', DialogBot.step1)
async def set_state(message, state):
    await state.set_state(DialogBot.step2)
    await state.update_data(num2=2025)
    await message.answer("Step2 has been saved")

@router.message(F.text == 'step', DialogBot.step2)
async def set_state(message, state):
    await message.answer(f"Step3 Data is: {state.get_data()}")
    await state.clear()

@router.message(F.text == 'step')
async def set_state(message, state):
    await state.set_state(DialogBot.step1)
    await state.update_data(num1=2026)
    await message.answer("Step1 has been saved")

# If we set this handler first, then it will capture all messages.
@router.message()
async def check_message(message):
    print(f'Getting message: {message.text}')
    # the answer method must be shorter than 1024 characters. 
    # This limitation is related to the Telegram API.
    await message.answer(texts.hello, reply_markup=menu)
