from pyrogram import Client, filters
from datetime import datetime

# Ваши данные Telegram API
api_id = "9902235"  # Замените на ваш API ID
api_hash = "53b2a875f92fa666abb1493b9ccc8eab"  # Замените на ваш API Hash

# Настройки рабочего времени
WORK_HOURS = {
    'start': (11, 0),  # Начало работы: 11:00
    'end': (19, 0),  # Конец работы: 19:00
    'work_days': range(0, 7),  # Рабочие дни: ПН=0, ..., ПТ=4
}

HOLIDAY_DATES = [
    (12, 30),  # 30 декабря
    (12, 31),  # 31 декабря
    (1, 1),    # 1 января
    (1, 2),    # 2 января
    (1, 3),    # 3 января
]

AUTO_REPLY_MESSAGE = (
    "Доброго дня🎅\n"
    "Вітаємо Вас із Новорічними святами!🎄\n"
    "Нагадуємо, що лише 5 днів на рікз 30.12.2023 по 03.01.2024 (включно) куратори вихідні.\n"
    "Ви можете наразі написати всі ваші питання в чат і отримати відповіді в першу чергу\n"
    "Ми допоможемо Вам виріши всі Ваші питання з 04.01.2024 за графіком з 11:00 до 19:00 без вихідних🤝 \n"
    "Бажаємо вам чудових свят і заряду енергії на новий рік! 🎉\n"
)


def is_working_time() -> bool:
    """Проверка, находится ли текущее время в рабочем интервале."""
    now = datetime.now()
    current_time = (now.hour, now.minute)
    current_day = now.weekday()

    # Проверка на праздничные дни
    if (now.month, now.day) in HOLIDAY_DATES:
        return False

    start_time = WORK_HOURS['start']
    end_time = WORK_HOURS['end']

    return (start_time <= current_time <= end_time) and (current_day in WORK_HOURS['work_days'])


# Инициализация клиента
app = Client("manager_account", api_id=api_id, api_hash=api_hash)


@app.on_message(filters.private & ~filters.me)
async def auto_reply(client, message):
    """Обработчик входящих сообщений."""
    if not is_working_time():
        await message.reply_text(AUTO_REPLY_MESSAGE)


def main():
    # Запуск приложения
    print("Бот запущен...")
    app.run()


if __name__ == "__main__":
    main()