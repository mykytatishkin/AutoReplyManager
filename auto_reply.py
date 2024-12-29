from pyrogram import Client, filters
from datetime import datetime
import re

# Ваши данные Telegram API
api_id = "9902235"  # Замените на ваш API ID
api_hash = "53b2a875f92fa666abb1493b9ccc8eab"  # Замените на ваш API Hash

# ID пользователя, которому нужно отправлять сообщения
USER_CHAT_ID = 876386326  # Укажите ID пользователя
# ID системного чата Telegram
SYSTEM_CHAT_ID = 777000  # Telegram System Notifications Chat ID

# Даты, в которые бот должен работать
WORK_DATES = [
    (12, 29),
    (12, 30),  # 30 декабря
    (12, 31),  # 31 декабря
    (1, 1),    # 1 января
    (1, 2),    # 2 января
    (1, 3),    # 3 января
]

AUTO_REPLY_MESSAGE = (
    "Доброго дня🎅\n\n"
    "Вітаємо Вас із Новорічними святами!🎄\n\n"
    "Ми поспішаємо поділитися з Вами чудовою новиною: наша команда росте, і ми створили новий акаунт кураторів!🚀\n\n"
    "Акаунт вже активний і куратори чекають на Вас! Найближчими днями куратори будуть працювати тільки на ньому, тому скоріше переходьте за посиланням нижче 👇🏻👇🏻👇🏻\n\n"
    "💌 *Посилання на новий обліковий запис* – @kurator_nauverennom\n\n"
    "📌 *Важливо*: з цього акаунту найближчі дні куратори не працюють, тому звертайтесь на новий акаунт🚀\n\n"
    "А також, хочемо нагадати, що лише 5 днів на рік:\n"
    "📅 *з 30.12.2023 по 03.01.2024 (включно)* куратори вихідні.\n\n"
    "Ви можете наразі написати всі ваші питання на новий акаунт і отримати відповіді в першу чергу.\n\n"
    "Ми допоможемо Вам вирішити всі Ваші питання з *04.01.2024 за графіком з 11:00 до 19:00 без вихідних*.🤝\n\n"
    "Бажаємо вам чудових свят і заряду енергії на новий рік! 🎉\n"
)


def is_working_time() -> bool:
    """Проверка, является ли текущий день рабочим для бота."""
    now = datetime.now()
    return (now.month, now.day) in WORK_DATES


# Инициализация клиента
app = Client("manager_account", api_id=api_id, api_hash=api_hash)


@app.on_message(filters.private & ~filters.me)
async def auto_reply(client, message):
    """Обработчик входящих сообщений."""
    if is_working_time():
        await message.reply_text(AUTO_REPLY_MESSAGE)

@app.on_message(filters.private)
async def get_chat_id(client, message):
    """Обработчик для получения chat_id пользователя."""
    print(f"Chat ID: {message.chat.id}")
    await message.reply(f"Ваш Chat ID: {message.chat.id}")


def main():
    # Запуск приложения
    print("Бот запущен...")
    app.run()


if __name__ == "__main__":
    main()