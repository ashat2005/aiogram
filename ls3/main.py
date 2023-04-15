from aiogram import Bot, Dispatcher,types,executor
import config
import logging
bot = Bot(token = config.token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    await message.answer(f"Здраствуйте {message.from_user.full_name}")

executor.start_polling(dp)