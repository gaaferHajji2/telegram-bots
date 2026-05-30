import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers.message_handler import router as message_router
from handlers.callback_handler import router as callback_handler_router
from handlers.admin_handler import router as admin_router
from handlers.media_handler import router as media_router
from handlers.start import router as start_router
from dotenv import load_dotenv

load_dotenv()

api = os.getenv('api_key')
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())
"""
A one-time keyboard displays its buttons only once. This is controlled by 
the `one_time_keyboard` argument, which accepts a boolean value (default is `False`). 
When set to `True`, the keyboard appears on the first message and automatically 
disappears after the user presses any button. 
However, the user can still manually reopen it by tapping the keyboard icon 
next to the text input field.
"""

"""
A persistent keyboard gives the user continuous access throughout the chat session. 
The `is_persistent` argument determines whether the keyboard can be manually 
toggled (default is `False`). When set to `True`, the manual toggle button disappears, 
and the keyboard automatically collapses when the user starts typing in the input field. 
This helps maintain a cleaner interface during active text input.
"""

async def main():
    dp.include_routers(admin_router, media_router, start_router, message_router, callback_handler_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())