from aiogram import Dispatcher
from aiogram.types import Message
import logging

from handlers.gemini_api import ask_gemini

logger = logging.getLogger(__name__)

async def cmd_start(message: Message):
    await message.answer("Привет! Я Telegram бот, подключённый к Gemini. Напиши мне что-нибудь.")

async def handle_text(message: Message):
    try:
        gemini_reply = ask_gemini(message.text)
        await message.answer(gemini_reply)
    except Exception as e:
        logger.error(f"Gemini API error: {e}")
        await message.answer("Произошла ошибка при обращении к Gemini.")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])
    dp.register_message_handler(handle_text, content_types=["text"])
