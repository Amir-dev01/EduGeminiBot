import google.generativeai as genai
import os

# Используйте ваш ключ из config.py или вставьте напрямую для теста
# Если ключ из config.py:
from config import GEMINI_API_KEY

# Если хотите вставить напрямую для теста:
# GEMINI_API_KEY = "ВАШ_API_КЛЮЧ_GEMINI"

if not GEMINI_API_KEY:
    print("GEMINI_API_KEY не установлен. Пожалуйста, установите переменную окружения или укажите ключ напрямую.")
else:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        print("Доступные модели:")
        for m in genai.list_models():
            print(f"  - {m.name} (поддерживаемые методы: {m.supported_generation_methods})")
            if 'gemini-pro' in m.name:
                print(f"    Найден 'gemini-pro' или связанная модель: {m.name}")

    except Exception as e:
        print(f"Ошибка при получении списка моделей: {e}")