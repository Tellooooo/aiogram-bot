from aiogram.types import Message
from aiogram import Bot


async def get_true_contact(message: Message, bot: Bot):
    if message.contact.user_id == message.from_user.id:
        await message.answer(f"Kontakt to'g'ri ✅")
    else:
        await message.answer(f"Kontakt xato ❌")



