from aiogram import F, Router

router = Router()

@router.callback_query(F.data == 'Russian/English/Arabic')
async def get_languages(message):
    await message.answer("My Languages are: \n1. English\n2. Russian\n3. Arabic")

@router.callback_query(F.data == "Jafar Loka")
async def get_my_name(message):
    await message.answer("My Name is Jafar Loka.\nI am ITE Engineer & QA Tester")
