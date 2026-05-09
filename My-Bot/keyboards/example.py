from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# The keyboard argument in ReplyKeyboardMarkup accepts a matrix of buttons (a list of lists). 
# Each inner list represents a single row. For example, the first list contains all buttons 
# for row 1, the second list for row 2, and so on.

# The `is_persistent` argument determines whether the keyboard can be manually toggled (default is `False`). 
# When set to `True`, the manual toggle button disappears, and the keyboard automatically collapses when the user 
# starts typing in the input field. This helps maintain a cleaner interface during active text input.

"""
#### 1. Keyboard Removal Object
```python
from aiogram.types import ReplyKeyboardRemove

remove = ReplyKeyboardRemove()
# Pass `remove` to the `reply_markup` parameter when sending a message to hide the current keyboard.
```

#### 2. Force Reply Object
```python
from aiogram.types import ForceReply

replyer = ForceReply()
# Attach to a message to highlight it and prompt the user to reply directly.
```

"""
menu = ReplyKeyboardMarkup(
    keyboard=[
        [ KeyboardButton(text="Information") ], 
        [ KeyboardButton(text="Add Number"), KeyboardButton(text="Delete Number")]
    ], 
    resize_keyboard=True, 
    input_field_placeholder="JLoka Option To Verifying...", 
    one_time_keyboard=True
)

inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Your Language", callback_data="Russian/English/Arabic"), 
        InlineKeyboardButton(text="Your Name", callback_data="Jafar Loka")
    ]
])