from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#The keyboard argument in ReplyKeyboardMarkup accepts a matrix of buttons (a list of lists). 
# Each inner list represents a single row. For example, the first list contains all buttons 
# for row 1, the second list for row 2, and so on.

menu = ReplyKeyboardMarkup(
    keyboard=[
        [ KeyboardButton(text="Information") ], 
        [ KeyboardButton(text="Add Number"), KeyboardButton(text="Delete Number")]
    ], 
    resize_keyboard=True, 
    input_field_placeholder="JLoka Option To Verifying...", 
    one_time_keyboard=True
)