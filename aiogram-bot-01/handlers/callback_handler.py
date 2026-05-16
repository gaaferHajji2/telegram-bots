from aiogram import F, Router

router = Router()

@router.callback_query(F.data == 'Russian/English/Arabic')
async def get_languages(message):
    await message.answer("My Languages are: \n1. English\n2. Russian\n3. Arabic")

@router.callback_query(F.data == "Jafar Loka")
async def get_my_name(message):
    await message.answer("My Name is Jafar Loka.\nI am ITE Engineer & QA Tester")

@router.callback_query(F.data == "Information")
async def get_my_name(call):
    await call.message.answer("This test information message")
    await call.answer("My Name is Jafar Loka.\nI am ITE Engineer & QA Tester", show_alert=True)


@router.callback_query()
async def func(call):
    await call.message.answer('Thank you for clicking')
    await call.answer()