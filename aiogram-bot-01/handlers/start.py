from aiogram import Router
from aiogram.filters import CommandStart, Command

router = Router()

@router.message(CommandStart())
async def start(message):
    await message.answer('We are glad to see you in our bot')

@router.message(Command('help'))
async def help(message):
    await message.answer('For assistance, contact the administrator @jafarloka')