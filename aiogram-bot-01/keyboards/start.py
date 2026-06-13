from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📜 Menu", callback_data='menu')]
    ]
)

present = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🎁 Get Gift", callback_data='get_present')]
    ]
)