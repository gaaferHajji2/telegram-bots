from aiogram.filters import BaseFilter

admins = [1046276866, 1234567890]

class AdminFilter(BaseFilter):
    def __init__(self):
        pass

    async def __call__(self, message):
        print(f"The user id is: {message.from_user.id}")
        return message.from_user.id in admins