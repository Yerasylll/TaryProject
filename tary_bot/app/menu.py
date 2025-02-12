import json
import os
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} KZT"

class Menu:
    def __init__(self, file_path):
        # Get the absolute path of the JSON file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(base_dir, "..", file_path)

        if not os.path.exists(full_path):
            raise FileNotFoundError(f"Menu file not found: {full_path}")

        with open(full_path, 'r') as f:
            data = json.load(f)

        self.items = [MenuItem(item["name"], item["price_kzt"]) for category in data["menu"] for item in
                      category["items"]]

    def get_menu_text(self):
        return "\n".join(str(item) for item in self.items)

    def get_menu_keyboard(self):
        keyboard = InlineKeyboardMarkup()
        for item in self.items:
            keyboard.add(InlineKeyboardButton(f"{item.name} - {item.price} KZT", callback_data=f"order_{item.name}"))
        return keyboard
