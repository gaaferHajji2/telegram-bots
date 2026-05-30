from aiogram import Router
from aiogram.filters import Command

router = Router()

users = {}

@router.message(Command('referral'))
async def start(message, command):
    # Welcome message
    await message.answer(f'Welcome, {message.from_user.first_name}')
    
    user_id = str(message.from_user.id)
    ref_id = command.args
    
    if user_id not in users:
        # Add new user to the database
        users[user_id] = []
        
    if ref_id is None:
        return
        
    # If an argument is provided with the command
    try:
        users[ref_id].append(user_id)
    except KeyError:
        pass