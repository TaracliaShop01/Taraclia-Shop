import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# 🔑 Вставьте сюда токен, который дал вам @BotFather
BOT_TOKEN = "8343866837:AAHqp2VEVoijOnzXR_UW8JJ3zJZHgQqJaTo"

# 🔗 Вставьте сюда ссылку на ваш магазин
SHOP_URL = "https://taracliashop01.github.io/Taraclia-Shop/"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# 👋 Обработчик команды /start
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    # Создаём кнопку со ссылкой
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🛍 Открыть магазин",
                    url=SHOP_URL
                )
            ]
        ]
    )

    # Отправляем приветствие с кнопкой
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n\n"
        "Добро пожаловать в наш бот!\n"
        "Нажми на кнопку ниже, чтобы перейти в магазин 👇",
        reply_markup=keyboard
    )


# 🚀 Запуск бота
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
