from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Text

from config import ADMIN_ID
from database import DB_NAME
import aiosqlite

# ایجاد کلاس FSM برای ثبت نام
class Form(StatesGroup):
    waiting_for_full_name = State()  # مرحله اول: نام کامل
    waiting_for_phone = State()     # مرحله دوم: شماره تلفن

# شروع ربات و نمایش پیام خوش آمدگویی
async def start_cmd(message: types.Message):
    await message.answer("به ربات خوش آمدید! لطفا نام کامل خود را وارد کنید:")
    await Form.waiting_for_full_name.set()  # وارد کردن نام کامل

# گرفتن نام کامل کاربر
async def process_full_name(message: types.Message, state: FSMContext):
    full_name = message.text  # دریافت نام کامل
    # ذخیره نام کامل در حافظه موقت FSM
    await state.update_data(full_name=full_name)
    
    # درخواست شماره تلفن
    await message.answer("لطفا شماره تلفن خود را وارد کنید:")
    await Form.waiting_for_phone.set()  # مرحله بعدی: شماره تلفن

# گرفتن شماره تلفن کاربر
async def process_phone(message: types.Message, state: FSMContext):
    phone = message.text  # دریافت شماره تلفن
    user_data = await state.get_data()  # دریافت اطلاعات ذخیره‌شده در FSM
    full_name = user_data['full_name']
    
    # ذخیره‌سازی اطلاعات در دیتابیس
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("INSERT INTO users (telegram_id, full_name, phone) VALUES (?, ?, ?)",
                         (message.from_user.id, full_name, phone))
        await db.commit()

    await message.answer(f"با موفقیت ثبت نام کردید!\nنام: {full_name}\nشماره تلفن: {phone}")
    await state.finish()  # پایان مراحل ثبت‌نام

# ثبت‌نام کاربر و ذخیره اطلاعات در دیتابیس
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_cmd, commands=["start"], state="*")  # دستوری برای شروع
    dp.register_message_handler(process_full_name, state=Form.waiting_for_full_name)  # گرفتن نام
    dp.register_message_handler(process_phone, state=Form.waiting_for_phone)  # گرفتن شماره تلفن
