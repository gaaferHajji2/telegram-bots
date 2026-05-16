from aiogram import F, Router
from filters.filter_admin import AdminFilter

router = Router()
router.message.filter(AdminFilter())

@router.message(F.text == 'secret')
async def admin_message(message):
    # print(f"The user id is: {message.from_user.id}")
    await message.answer("This is secret message")

@router.message(F.text == 'admin')
async def admin_message(message):
    # print(f"The user id is: {message.from_user.id}")
    await message.answer("This is admin message")