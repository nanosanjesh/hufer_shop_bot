from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# 🔹 کیبورد اصلی برای کاربران
user_main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
user_main_keyboard.add(KeyboardButton("🛍 مشاهده محصولات"))
user_main_keyboard.add(KeyboardButton("🛒 سبد خرید"), KeyboardButton("📞 پشتیبانی"))

# 🔹 کیبورد برای ارسال شماره تماس (اختیاری اگر بخوای مستقیماً بفرسته)
phone_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
phone_keyboard.add(KeyboardButton("ارسال شماره تماس", request_contact=True))

# 🔹 دکمه تایید ارسال فیش واریزی
confirm_payment_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
confirm_payment_keyboard.add(KeyboardButton("✅ فیش را ارسال کردم"))

# 🔹 دکمه‌های ادمین برای مدیریت محصول
admin_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
admin_keyboard.add(KeyboardButton("➕ افزودن محصول"))
admin_keyboard.add(KeyboardButton("📦 لیست محصولات"))
admin_keyboard.add(KeyboardButton("🏠 بازگشت به منو"))

# 🔹 کیبورد inline برای هر محصول (افزودن به سبد خرید)
def product_inline_keyboard(product_id: int):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("➕ افزودن به سبد خرید", callback_data=f"add_{product_id}"))
    return markup
