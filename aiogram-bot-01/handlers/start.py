from aiogram import Router
from aiogram.filters import Command

router = Router()

@router.message(Command('start'))
async def start(message, command):
    if command.args == 'shop':
        await message.answer('Welcome to the store menu')
    elif command.args == 'feedback':
        await message.answer('Here you can leave your feedback')
    else:
        await message.answer('This command is not supported. For more information about our commands, press /help')

@router.message(Command('help'))
async def help(message):
    await message.answer('For assistance, contact the administrator @jafarloka')

