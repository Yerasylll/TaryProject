from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

assistants = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="start")],
    [KeyboardButton(text="help")],
    [KeyboardButton(text="basket")]
])

main = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="")],
        [KeyboardButton(text="")],
        [KeyboardButton(text=""),
         KeyboardButton(text="")]],
    resize_keyboard=True,
    input_field_placeholder="Choose a point menu...")

catalog = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="T-shirt", callback_data="t-shirt")],
        [InlineKeyboardButton(text="Sneakers", callback_data="sneakers")],
        [InlineKeyboardButton(text="Cap", callback_data="cap")],
])

get_number = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Number", callback_data="number")]],
    resize_keyboard=True
)