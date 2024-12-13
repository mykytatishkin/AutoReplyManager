from pyrogram import Client, filters
from datetime import datetime

# Ваши данные Telegram API
api_id = "27937710"  # Замените на ваш API ID
api_hash = "bbf15be9075169be696be545cab08a7a"  # Замените на ваш API Hash

# Настройки рабочего времени
WORK_HOURS = {
    'start': (9, 0),  # Начало работы: 9:00
    'end': (18, 0),  # Конец работы: 18:00
    'work_days': range(0, 5),  # Рабочие дни: ПН=0, ..., ПТ=4
}

AUTO_REPLY_MESSAGE = (
    "Здравствуйте! Я сейчас не могу ответить. "
    "Пожалуйста, напишите в рабочее время (ПН-ПТ с 9:00 до 18:00)."
)


def is_working_time() -> bool:
    """Проверка, находится ли текущее время в рабочем интервале."""
    now = datetime.now()
    current_time = (now.hour, now.minute)
    current_day = now.weekday()

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