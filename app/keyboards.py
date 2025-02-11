from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import ReplyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📜 View Menu")],
    [InlineKeyboardButton(text="🛒 Place Order")],
    [InlineKeyboardButton(text="📞 Contact Support")]],
    resize_keyboard=True,
    input_field_placeholder="Choose a point menu...")

