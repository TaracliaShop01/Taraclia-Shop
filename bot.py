import asyncio
import os
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# 🔑 Токен берется из переменных окружения Render (НЕ вставляйте его сюда напрямую!)
BOT_TOKEN = os.environ.get("8343866837:AAHqp2VEVoijOnzXR_UW8JJ3zJZHgQqJaTo")

# 🔗 Ссылка на ваш сайт
SHOP_URL = "https://taracliashop01.github.io/Taraclia-Shop/"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# 👋 Обработчик команды /start
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
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
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n\n"
        "Добро пожаловать в наш магазин!\n"
        "Нажми на кнопку ниже, чтобы перейти 👇",
        reply_markup=keyboard
    )

# 🌐 Простой веб-сервер для Render (чтобы Web Service не падал)
async def handle(request):
    return web.Response(text="Bot is running!")

async def start_web_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    # Render сам подставляет нужный порт в переменную PORT
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

# 🚀 Запуск
async def main():
    print("Бот запущен...")
    await start_web_server()  # Запускаем веб-сервер
    await dp.start_polling(bot)  # Запускаем бота

if __name__ == "__main__":
    asyncio.run(main())
