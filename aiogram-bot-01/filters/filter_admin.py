import os
from dotenv import load_dotenv
from aiogram.filters import Filter

load_dotenv()
admins = [1046276866, 1234567890, int(os.getenv('my_id'))]

class AdminFilter(Filter):
    def __init__(self):
        pass

    async def __call__(self, message):
        return message.from_user.id in admins