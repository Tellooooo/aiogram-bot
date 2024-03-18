from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault



async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Ishni boshlash'
        ),
        BotCommand(
            command='help',
            description='yordam'
        ),
        BotCommand(
            command='cancel',
            description="o'chirish"
        )
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
