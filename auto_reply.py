from pyrogram import Client, filters
from datetime import datetime

# Ваши данные Telegram API
api_id = "9902235"  # Замените на ваш API ID
api_hash = "53b2a875f92fa666abb1493b9ccc8eab"  # Замените на ваш API Hash

# Даты, в которые бот должен работать
WORK_DATES = [
    (12, 30),  # 30 декабря
    (12, 31),  # 31 декабря
    (1, 1),    # 1 января
    (1, 2),    # 2 января
    (1, 3),    # 3 января
]

AUTO_REPLY_MESSAGE = (
    "Доброго дня🎅\n"
    "Вітаємо Вас із Новорічними святами!🎄\n"
    "Нагадуємо, що лише 5 днів на рік з 30.12.2023 по 03.01.2024 (включно) куратори вихідні.\n"
    "Ви можете наразі написати всі ваші питання в чат і отримати відповіді в першу чергу\n"
    "Ми допоможемо Вам вирішити всі Ваші питання з 04.01.2024 за графіком з 11:00 до 19:00 без вихідних🤝 \n"
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


def main():
    # Запуск приложения
    print("Бот запущен...")
    app.run()


if __name__ == "__main__":
    main()