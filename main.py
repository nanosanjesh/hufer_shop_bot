from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN
from database import init_db
from handlers import register_handlers

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

async def on_startup(dp):
    await init_db()
    print("Database initialized.")

register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
