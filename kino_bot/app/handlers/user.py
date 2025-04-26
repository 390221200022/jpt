
from aiogram import Router, types
from aiogram.filters import CommandStart
from app.keyboards.reply import main_menu
from app.keyboards.inline import get_subscription_keyboard
from app.middlewares.check_subscription import check_subs
from app.database import save_user
from app.config import CHANNEL_ID, REKLAMA_TEXT
from aiogram import Bot

router = Router()

@router.message(CommandStart())
async def start(message: types.Message):
    await save_user(message.from_user.id)
    if not await check_subs(message.from_user.id):
        await message.answer(
            "Hurmatli foydalanuvchi! Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling 👇",
            reply_markup=get_subscription_keyboard()
        )
        return
    await message.answer("Assalomu alaykum! 🎬 Kinolar olishingiz mumkin!
Raqam yuboring.", reply_markup=main_menu)

@router.message(lambda message: message.text.isdigit())
async def get_movie(message: types.Message, bot: Bot):
    if not await check_subs(message.from_user.id):
        await message.answer(
            "❗ Botdan foydalanish uchun homiy kanallarga obuna bo'ling!",
            reply_markup=get_subscription_keyboard()
        )
        return
    try:
        num = message.text
        async for msg in bot.get_chat_history(chat_id=CHANNEL_ID, limit=200):
            if msg.caption and num in msg.caption.split():
                caption = msg.caption.replace(num, "").strip() + REKLAMA_TEXT
                await bot.copy_message(
                    chat_id=message.chat.id,
                    from_chat_id=CHANNEL_ID,
                    message_id=msg.message_id,
                    caption=caption
                )
                return
        await message.answer("❗ Kechirasiz, bu raqamdagi kino topilmadi.")
    except Exception as e:
        await message.answer("❗ Kino qidirishda xatolik yuz berdi.")
