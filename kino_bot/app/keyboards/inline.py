
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.database import load_sponsors

def get_subscription_keyboard():
    sponsors = load_sponsors()
    keyboard = InlineKeyboardMarkup(row_width=1)
    for sponsor in sponsors:
        keyboard.add(InlineKeyboardButton(text=sponsor['name'], url=sponsor['link']))
    keyboard.add(InlineKeyboardButton(text="✅ Obuna bo'ldim", callback_data="check_subs"))
    return keyboard
