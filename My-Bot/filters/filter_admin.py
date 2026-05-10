import os
from dotenv import load_dotenv
from aiogram.filters import Filter

load_dotenv()
# print(f"My Id is: {os.getenv('my_id')}")
admins = [1046276866, 1234567890, int(os.getenv('my_id'))]

class AdminFilter(Filter):
    def __init__(self):
        pass

    async def __call__(self, message):
        # print(f"The user id is: {message.from_user.id}")
        return message.from_user.id in admins