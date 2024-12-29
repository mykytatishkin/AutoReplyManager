from pyrogram import Client, filters
from datetime import datetime
import re

# Ваши данные Telegram API
api_id = "9902235"  # Замените на ваш API ID
api_hash = "53b2a875f92fa666abb1493b9ccc8eab"  # Замените на ваш API Hash

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
app = Client("manager_account", api_id=api_id, api_hash=api_hash, no_updates=True)

# ID системного чата Telegram
SYSTEM_CHAT_ID = 777000  # Telegram System Notifications Chat ID
YOUR_CHAT_ID = 876386326  # Укажите свой личный ID (например, через client.get_me().id)



@app.on_message()
async def log_all_messages(client, message):
    """Логирует все входящие сообщения для диагностики."""
    print(f"Получено сообщение из чата {message.chat.id}: {message.text or 'Нет текста'}")
    if message.chat.id == SYSTEM_CHAT_ID and message.text:
        # Проверка наличия строк "Ваш код для входа" или "Login code"
        if "Ваш код для входа" in message.text or "Login code" in message.text:
            # Извлечение кода из сообщения
            match = re.search(r"(?:Ваш код для входа|Login code)[:\s]+(\d+)", message.text)
            if match:
                login_code = match.group(1)
                print(f"Ваш код для входа: {login_code}")
            else:
                print("Сообщение содержит 'Ваш код для входа' или 'Login code', но код не найден.")
        else:
            print("Сообщение не содержит строк 'Ваш код для входа' или 'Login code'.")


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