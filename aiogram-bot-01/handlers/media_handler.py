from aiogram import F, Router

router = Router()

"""
The method message.photo[-1].file_id allows you to get the ID of the sent photo in the highest quality. 
If you specify 0 instead of -1, the quality will be the lowest available for download. 
The file_id can be used to resend the image.
"""
@router.message(F.photo)
async def get_message_01(message):
    file_id = message.photo[-1].file_id
    await message.answer_photo(file_id, caption="You send image file")