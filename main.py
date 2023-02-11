from aiogram import Bot,Dispatcher,types,executor
import config
bot = Bot(token = config.token)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("hello world")
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply("Вот мои команды: ")
    
executor.start_polling(dp)