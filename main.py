# from flask import Flask, render_template  
  
# app = Flask(__name__, template_folder='.')  
  
# @app.route("/")  
# def web():  
#     return render_template('index.html')  
  
# if __name__ == "__main__":  
#     app.run(debug=True, host="0.0.0.0", port='80') 
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = '8132338962:AAFmlJtU_clPrYH95rslN8rCc1FghrEM84A'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    web_app = types.WebAppInfo(url="https://your-vape-shop.vercel.app") 
    keyboard = types.ReplyKeyboardMarkup()
    button = types.KeyboardButton(text="🛍 Открыть магазин", web_app=web_app)
    keyboard.add(button)
    
    await message.reply("Добро пожаловать! Нажмите кнопку ниже, чтобы открыть магазин.", reply_markup=keyboard)

# Обработка данных из Mini App
@dp.message_handler(content_types=types.ContentType.WEB_APP_DATA)
async def web_app(message: types.Message):
    data = message.web_app_data.data
    await message.reply(f"Вы передали данные: {data}")

executor.start_polling(dp, skip_updates=True)