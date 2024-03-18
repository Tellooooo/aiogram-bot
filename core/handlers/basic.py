from aiogram import Bot
from aiogram.types import Message
import json

async def get_start(message: Message, bot: Bot):
    # print('salom')
    await bot.send_message(message.from_user.id, f'<b> {message.from_user.first_name} Nma gaaaaaaaaap </b>')
    await message.answer(f'<s>salom {message.from_user.first_name}. </s>')
    await message.reply(f'<tg-spoiler>salom {message.from_user.first_name}. </tg-spoiler>')


async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Yaxshi. San rasm yubording, uni ozimga saqlab qoydim.')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')


async def get_hello(message: Message, bot: Bot):
    await message.answer(f'Sangayam salom!')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)