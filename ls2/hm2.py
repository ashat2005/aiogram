from aiogram import Bot, Dispatcher, types, executor
import config
bot = Bot(token= config.token)
dp = Dispatcher(bot)
@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Здраствуйте {message.from_user.first_name}")
    await message.reply("Какое напровление вы предпочитаете: /Backend , /Frontend , /Android , /UIUX")
@dp.message_handler(commands='Backend')
async def backend(message:types.Message):
    await message.reply("Backend — это внутренняя часть сайта и сервера и т.д \nСтоимость 10000 сом в месяц \nОбучение: 5 месяц")
@dp.message_handler(commands='Frontend')
async def frontend(message:types.Message):
    await message.reply("Frontend - это внешний вид сайта \nСтоимость 10000 сом в месяц \nОбучение: 7 месяц")
@dp.message_handler(commands='Android')
async def android(message:types.Message):
    await message.reply("Android - это создание приложений \nСтоимоть 10000сом в месяц \nОбучение: 7 месяц")
@dp.message_handler(commands='UIUX')
async def ui(message:types.Message):
    await message.reply("UI-UX - это создание дизайн сайта его внешний вид и т.д \nСтоимость 10000 в месяц \nОбучение: 3 месяц")
executor.start_polling(dp)
print("dfsdf")