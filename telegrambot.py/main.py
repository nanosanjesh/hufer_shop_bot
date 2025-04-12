from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm import FSMContext
from aiogram.fsm.state import State, StatesGroup

import logging
from config import API_TOKEN  # وارد کردن توکن از فایل config

# تنظیمات لاگ‌گیری
logging.basicConfig(level=logging.INFO)

# ایجاد نمونه‌هایی از ربات و دیسپچر
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# ایجاد کلاس FSM برای ثبت نام
class Form(StatesGroup):
    waiting_for_full_name = State()  # مرحله اول: نام کامل
    waiting_for_phone = State()     # مرحله دوم: شماره تلفن

# دستورات و کارها در ربات
@dp.message_handler(Command("start"))
async def cmd_start(message: Message):
    await message.answer("سلام! به ربات خوش آمدید.")
    await Form.waiting_for_full_name.set()  # وارد کردن نام کامل

@dp.message_handler(state=Form.waiting_for_full_name)
async def process_full_name(message: Message, state: FSMContext):
    full_name = message.text  # دریافت نام کامل
    await state.update_data(full_name=full_name)
    
    await message.answer("لطفا شماره تلفن خود را وارد کنید:")
    await Form.waiting_for_phone.set()  # مرحله بعدی: شماره تلفن

@dp.message_handler(state=Form.waiting_for_phone)
async def process_phone(message: Message, state: FSMContext):
    phone = message.text  # دریافت شماره تلفن
    user_data = await state.get_data()  # دریافت اطلاعات ذخیره‌شده در FSM
    full_name = user_data['full_name']
    
    # ثبت اطلاعات یا ذخیره‌سازی آن‌ها در دیتابیس
    await message.answer(f"با موفقیت ثبت نام کردید!\nنام: {full_name}\nشماره تلفن: {phone}")
    await state.finish()  # پایان مراحل ثبت‌نام

async def on_start():
    logging.info("Starting bot...")
    await dp.start_polling()

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp)  # اجرای ربات
