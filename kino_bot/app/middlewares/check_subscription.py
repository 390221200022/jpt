
from aiogram import types
from app.database import load_sponsors
from app.config import BOT_TOKEN
import aiohttp

async def check_subs(user_id: int):
    sponsors = load_sponsors()
    async with aiohttp.ClientSession() as session:
        for sponsor in sponsors:
            chat_username = sponsor['link'].split("/")[-1]
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/getChatMember?chat_id=@{chat_username}&user_id={user_id}"
            async with session.get(url) as resp:
                data = await resp.json()
                status = data.get("result", {}).get("status")
                if status not in ["member", "administrator", "creator"]:
                    return False
    return True
