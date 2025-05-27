import logging
from aiogram import Dispatcher
from aiogram.types import BotCommand

# Настройка логирования для этого модуля (необязательно, но полезно для отладки)
logger = logging.getLogger(__name__)

async def set_default_commands(dp: Dispatcher):
    """
    Устанавливает стандартные команды для кнопки "Меню" бота.
    Эта функция должна быть вызвана при запуске бота.
    """
    commands = [
        BotCommand("start", "Начать работу с ботом"),
        BotCommand("cheat", "шпаргалка"),

    ]
    await dp.bot.set_my_commands(commands)
    logger.info("Команды меню успешно установлены.")