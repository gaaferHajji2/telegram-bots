from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()
users = {}

@router.message(CommandStart())
async def cmd_start(message: Message):
    # Extract the payload from the start command
    # If the link is t.me/bot?start=123, message.text will be "/start 123"
    # Or you can use message.args if available in your aiogram version context
    
    args = message.text.split()
    ref_id = None
    
    if len(args) > 1:
        ref_id = args[1]  # This is the '123' from ?start=123

    user_id = str(message.from_user.id)
    
    # Welcome message
    await message.answer(f'Welcome, {message.from_user.first_name}!')
    
    if user_id not in users:
        users[user_id] = []
        
    if ref_id:
        try:
            # Ensure the referrer exists in users dict before appending
            if ref_id not in users:
                users[ref_id] = []
            users[ref_id].append(user_id)
            print("The user data is: ", users)
            await message.answer(f"You were referred by user ID: {ref_id}")
        except Exception as e:
            print(f"Error processing referral: {e}")
