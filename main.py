from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import dp
from aiogram.utils import executor
import logging
from config import TOKEN
from handlers.commands import set_default_commands
from handlers import (
    cheat,
    start
)

logging.basicConfig(level=logging.INFO)

start.register_handlers(dp)
cheat.register_handlers(dp)



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=set_default_commands, skip_updates=True)
