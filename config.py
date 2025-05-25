from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import dotenv_values

TOKEN = "8133390811:AAHjsNVRo4acWwNV90w7QNoQSHJClWxeIjM"
GEMINI_API_KEY = "AIzaSyBJwRK98gpe74JH-8VNeLLAhXeR2KaBc9g"
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)