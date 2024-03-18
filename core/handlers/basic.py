from aiogram import Bot
from aiogram.types import Message
import json
from core.keyboards.reply import reply_keyboard, loc_tel_poll_keyboard




async def get_start(message: Message, bot: Bot):
    await message.answer(f'<s>salom {message.from_user.first_name}. </s>',
                        reply_markup=loc_tel_poll_keyboard)


async def get_location(message: Message, bot: Bot):
    await message.answer(f"San manzilingni yubording!\r\a"
                         f"{message.location.latitude}\r\n{message.location.longitude}")


async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Yaxshi. San rasm yubording, uni ozimga saqlab qoydim.')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')


async def get_hello(message: Message, bot: Bot):
    await message.answer(f'Sangayam salom!')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)