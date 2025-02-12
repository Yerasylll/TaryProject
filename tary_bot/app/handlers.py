# from aiogram import F, Router
# from aiogram.types import Message, CallbackQuery
# from aiogram.filters import CommandStart, Command
# from aiogram.fsm.state import State, StatesGroup
# from aiogram.fsm.context import FSMContext
#
# import tary_bot.app.keyboards as kb
#
# router = Router()
#
# class MenuItem:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def __str__(self):
#         return f"{self.name} - {self.price} KZT"
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
# # Initialize menu
# tary_menu = Menu("tary_menu.json")
#
# @router.message(F.text == "📜 View Menu")
# async def show_menu(message: Message):
#     await message.answer(tary_menu.get_menu_text())
#
# @router.callback_query(F.data.startswith("order_"))
# async def process_order(callback_query: CallbackQuery):
#     item_name = callback_query.data.split('_')[1]
#     await callback_query.answer(f"{item_name} added to your order.")

import json
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from tary_bot.app.menu import Menu  # Importing from separate menu module

router = Router()

# Initialize menu from external JSON file
tary_menu = Menu("'/Users/yerasylalimbek/Desktop/ITP project/TaryProject/tary_bot/app/tary_menu.json'")


@router.message(F.text == "📜 View Menu")
async def show_menu(message: Message):
    await message.answer(tary_menu.get_menu_text())

@router.callback_query(F.data.startswith("order_"))
async def process_order(callback_query: CallbackQuery):
    item_name = callback_query.data.split('_')[1]
    await callback_query.answer(f"{item_name} added to your order.")

