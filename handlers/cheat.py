from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.gemini_api import ask_gemini

class CheatFSM(StatesGroup):
    waiting_for_subject = State()
    waiting_for_topic = State()

SUBJECTS = ["Математика", "История", "Информатика", "Физика", "Биология"]

def subject_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = [InlineKeyboardButton(text=subj, callback_data=subj) for subj in SUBJECTS]
    markup.add(*buttons)
    return markup

# Старт
async def start_cheatsheet(message: types.Message, state: FSMContext):
    await message.answer("Выбери предмет для шпаргалки:", reply_markup=subject_keyboard())
    await CheatFSM.waiting_for_subject.set()

# Выбор предмета
async def subject_selected(callback: types.CallbackQuery, state: FSMContext):
    subject = callback.data
    await state.update_data(subject=subject)
    await callback.message.edit_text(f"Предмет: {subject}\nТеперь введи тему:")
    await CheatFSM.waiting_for_topic.set()

# Ввод темы
async def topic_received(message: types.Message, state: FSMContext):
    data = await state.get_data()
    subject = data.get("subject")
    topic = message.text

    prompt = f"Сделай шпаргалку по теме '{topic}' по предмету '{subject}'. Кратко и понятно, без воды."
    await message.answer("Генерирую шпаргалку...")

    try:
        result = ask_gemini(prompt)
        await message.answer(result)
    except Exception:
        await message.answer("Ошибка при обращении к ИИ. Попробуй позже.")
    await state.finish()

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_cheatsheet, commands=["cheat"], state="*")
    dp.register_callback_query_handler(subject_selected, lambda c: c.data in SUBJECTS, state=CheatFSM.waiting_for_subject)
    dp.register_message_handler(topic_received, state=CheatFSM.waiting_for_topic)
