from aiogram import F, Router
from filters.filter_admin import AdminFilter

router = Router()

@router.message(AdminFilter(), F.text == 'secret')
async def admin_message(message):
    print(f"The user id is: {message.from_user.id}")
    await message.answer("This is secret message")