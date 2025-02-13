import json
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from tary_bot.app.menu import Menu  # Importing from separate menu module

router = Router()

import app.keyboards as kb

# Initialize menu from external JSON file
tary_menu = Menu("/Users/yerasylalimbek/Desktop/ITP project/TaryProject/tary_bot/app/tary_menu.json")

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply("hello!", reply_markup=kb.assistants)

@router.message(F.text == "📜 View Menu")
async def show_menu(message: Message):
# await message.answer(tary_menu.get_menu_text())
    await message.answer("Menu: ", reply_markup=kb.order_overview)

@router.callback_query(F.data.startswith("order_"))
async def process_order(callback_query: CallbackQuery):
    item_name = callback_query.data.split('_')[1]
    await callback_query.answer(f"{item_name} added to your order.")

