# from flask import Flask, render_template  
  
# app = Flask(__name__, template_folder='.')  
  
# @app.route("/")  
# def web():  
#     return render_template('index.html')  
  
# if __name__ == "__main__":  
#     app.run(debug=True, host="0.0.0.0", port='80') 

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# === Инициализация бота ===
API_TOKEN = '8132338962:AAFmlJtU_clPrYH95rslN8rCc1FghrEM84A'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# === Команда /start ===
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    web_app = types.WebAppInfo(url="https://merry-cat-76e7c2.netlify.app/") 
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text="🛍 Открыть магазин", web_app=web_app)]],
        resize_keyboard=True
    )
    
    await message.answer("Добро пожаловать! Нажмите кнопку ниже, чтобы открыть магазин.", reply_markup=keyboard)

# === Получение данных из Mini App ===
@dp.message(lambda message: message.web_app_data is not None)
async def handle_web_app_data(message: types.Message):
    data = message.web_app_data.data
    await message.answer(f"Вы передали данные: {data}")

# === Запуск бота ===
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())