
from aiogram import Router, types, F
from app.database import load_sponsors, save_sponsors, get_all_users
from app.config import ADMINS

router = Router()

@router.message(F.from_user.id.in_(ADMINS), F.text.startswith("/addhomiy"))
async def add_sponsor(message: types.Message):
    try:
        name, link = message.text.split(maxsplit=2)[1:]
        sponsors = load_sponsors()
        sponsors.append({"name": name, "link": link})
        save_sponsors(sponsors)
        await message.answer("✅ Homiy kanal muvaffaqiyatli qo‘shildi.")
    except:
        await message.answer("❌ Xato. Foydalanish: /addhomiy KanalNomi https://t.me/KanalLink")

@router.message(F.from_user.id.in_(ADMINS), F.text.startswith("/delhomiy"))
async def del_sponsor(message: types.Message):
    try:
        index = int(message.text.split(maxsplit=1)[1])
        sponsors = load_sponsors()
        if 0 <= index < len(sponsors):
            sponsors.pop(index)
            save_sponsors(sponsors)
            await message.answer("✅ Homiy kanal olib tashlandi.")
        else:
            await message.answer("❌ Bunday raqam topilmadi.")
    except:
        await message.answer("❌ Xato. Foydalanish: /delhomiy Raqam")

@router.message(F.from_user.id.in_(ADMINS), F.text.startswith("/xabar"))
async def broadcast(message: types.Message, bot):
    text = message.text.split(maxsplit=1)[1]
    users = get_all_users()
    count = 0
    for user_id in users:
        try:
            await bot.send_message(user_id, text)
            count += 1
        except:
            continue
    await message.answer(f"✅ {count} ta foydalanuvchiga xabar yuborildi.")
