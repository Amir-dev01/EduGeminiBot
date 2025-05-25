from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import dp
from aiogram.utils import executor
import logging
from config import TOKEN
from handlers import main_handler

logging.basicConfig(level=logging.INFO)


main_handler.register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
