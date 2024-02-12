from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Run this Bot'
        ),
        BotCommand(
            command='help',
            description='For Help'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())