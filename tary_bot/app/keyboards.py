from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from tary_bot.app.menu import Menu  # Importing from separate menu module

# Basic reply keyboard
assistants = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📜 View Menu")],
        [KeyboardButton(text="🛒 Place Order")],
        [KeyboardButton(text="📞 Contact Support")]
    ],
    resize_keyboard=True,
)

# Initialize menu object
tary_menu = Menu('/Users/yerasylalimbek/Desktop/ITP project/TaryProject/tary_bot/app/tary_menu.json')

# Creating Inline Keyboard dynamically from menu
menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=f"{item.name} - {item.price} KZT", callback_data=f"order_{item.name}")]
    for item in tary_menu.items
])

# order_skim = InlineKeyboardMarkup(keyboard=[
#         [InlineKeyboardButton(text="Негізгі Тағамдар")],
# ])

order_overview = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Негізгі Тағамдар", callback_data="")],
        [InlineKeyboardButton(text="Сүт Коктейльдері", callback_data="")],
        [InlineKeyboardButton(text="Сусындар", callback_data="")],
        [InlineKeyboardButton(text="Салаттар", callback_data="")],
        [InlineKeyboardButton(text="Десерттер", callback="")],
        [InlineKeyboardButton(text="Сорпалар",  callback_data="")],
        [InlineKeyboardButton(text="Нан Тағамдары", callback_data="")],
        [InlineKeyboardButton(text="Таңғы Ас", callback_data="")],
        [InlineKeyboardButton(text="Салқындатқыш Сусындар", callback_data="")],
        [InlineKeyboardButton(text="Кофе", callback_data="")]]
)