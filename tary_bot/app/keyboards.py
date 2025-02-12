# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
#
# assistants = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text="📜 View Menu")],
#     [KeyboardButton(text="🛒 Place Order")],
#     [KeyboardButton(text="📞 Contact Support")]],
#     resize_keyboard=True,
# )
#
# class Menu:
#     def __init__(self, file_path):
#         with open(file_path, 'r') as f:
#             data = json.load(f)
#         self.items = [MenuItem(item["name"], item["price_kzt"]) for category in data["menu"] for item in category["items"]]
#
#     def get_menu_text(self):
#         return "\n".join(str(item) for item in self.items)
#
#     def get_menu_keyboard(self):
#         keyboard = InlineKeyboardMarkup()
#         for item in self.items:
#             keyboard.add(InlineKeyboardButton(f"{item.name} - {item.price} KZT", callback_data=f"order_{item.name}"))
#         return keyboard
#
# tary_menu = Menu("tary_bot/tary_menu.json")
#
# for category in tary_menu['menu']['items']:
#     menu_keyboard = InlineKeyboardMarkup(keyboard=[
#         [InlineKeyboardButton(f"{item['name']} - {item['price_kzt']} KZT", callback_data=f"order_{item['name']}")]
#     ])
#
#
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
tary_menu = Menu("tary_menu.json")

# Creating Inline Keyboard dynamically from menu
menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f"{item.name} - {item.price} KZT", callback_data=f"order_{item.name}")]
    for item in tary_menu.items
])
