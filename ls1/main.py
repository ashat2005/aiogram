# from aiogram import Bot,Dispatcher,types,executor
# import config
# bot = Bot(token = config.token)
# dp = Dispatcher(bot)
# @dp.message_handler(commands=['start',"go"])
# async def start(message: types.Message):
#     image = open("/home/askhat/Desktop/aiogram/photo_2023-01-30_09-16-46.jpg","rb")
#     await bot.send_photo(message.chat.id, image)
#     await message.answer(f"Здраствуйте {message.from_user.full_name}")
#     await message.answer_location(40.51914515061428, 72.80247654671)
#     await message.answer_photo("https://klike.net/uploads/posts/2021-12/1638345229_2.jpg")
#     await message.answer_contact("+996704646665", first_name="Асхат")
#     await message.answer_audio("https://dl2.mp3party.net/online/10727491.mp3")
# @dp.message_handler(commands=['help'])
# async def help(message: types.Message):
#     await message.reply("Вот мои команды: ")
# @dp.message_handler(text=['привет'])
# async def hi(message: types.Message):
#     await message.answer("привет как дела?")
# @dp.message_handler()
# async def not_found(message: types.Message):
#     await message.reply("я вас не понимаю, введите /help")

# executor.start_polling(dp)