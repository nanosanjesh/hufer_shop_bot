from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# 🔹 کیبورد برای شروع ربات
def start_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("شروع سفارش"))
    return keyboard

# 🔹 کیبورد برای ثبت‌نام (دریافت شماره تلفن)
def register_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(KeyboardButton("📱 ارسال شماره تلفن", request_contact=True))
    return keyboard
# 🔹 کیبورد برای نمایش لیست محصولات
def product_list_keyboard(products):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for product in products:
        keyboard.add(KeyboardButton(product.name))  # استفاده از نام محصول
    keyboard.add(KeyboardButton("🏠 بازگشت به منو"))
    return keyboard

# 🔹 کیبورد کاربر بعد از انتخاب محصول (سبد خرید)
def cart_actions_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(
        KeyboardButton("🛒 مشاهده سبد خرید"),
        KeyboardButton("✅ تایید سفارش"),
        KeyboardButton("🏠 بازگشت به منو")
    )
    return keyboard

# 🔹 کیبورد برای تایید یا لغو سفارش
def confirm_order_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(
        KeyboardButton("📤 ارسال فیش واریزی"),
        KeyboardButton("❌ لغو سفارش")
    )
    return keyboard

# 🔹 کیبورد برای ارسال فیش واریزی (اختیاری)
def payment_receipt_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(KeyboardButton("📤 ارسال تصویر فیش"))
    return keyboard

# 🔹 کیبورد مدیریت برای ادمین (افزودن یا مشاهده محصولات)
def admin_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        KeyboardButton("➕ افزودن محصول"),
        KeyboardButton("📦 لیست محصولات")
    )
    return keyboard

# 🔹 کیبورد دکمه‌های اینلاین برای هر محصول (افزودن به سبد خرید)
def product_inline_keyboard(product_id: int):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("➕ افزودن به سبد خرید", callback_data=f"add_to_cart:{product_id}"))
    return markup
