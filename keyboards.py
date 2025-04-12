from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# کیبورد برای شروع
def start_keyboard():
    button = KeyboardButton('شروع')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button)
    return keyboard

# کیبورد برای ثبت‌نام کاربر
def register_keyboard():
    button1 = KeyboardButton('ثبت شماره تلفن', request_contact=True)  # درخواست شماره تلفن
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button1)
    return keyboard

# کیبورد برای مشاهده محصولات
def product_keyboard(products):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for product in products:
        button = KeyboardButton(f'{product.name}')  # نام محصول به عنوان دکمه
        keyboard.add(button)
    return keyboard

# کیبورد برای افزودن به سبد خرید
def cart_keyboard():
    button1 = KeyboardButton('افزودن به سبد خرید')
    button2 = KeyboardButton('مشاهده سبد خرید')
    button3 = KeyboardButton('تایید سفارش')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(button1, button2, button3)
    return keyboard

# کیبورد برای تایید سفارش
def order_confirmation_keyboard():
    button1 = KeyboardButton('تایید سفارش')
    button2 = KeyboardButton('لغو سفارش')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(button1, button2)
    return keyboard

# کیبورد برای ارسال فیش واریزی
def payment_receipt_keyboard():
    button = KeyboardButton('ارسال فیش واریزی', request_photo=True)  # درخواست تصویر فیش واریزی
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(button)
    return keyboard
