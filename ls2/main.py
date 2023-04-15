from aiogram import Bot,Dispatcher,types,executor
import config
import sqlite3

bot = Bot(token = config.token)
dp = Dispatcher(bot)

connect = sqlite3.connect('users.db')
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    username VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    id_user INTEGER,
    chat_id INTEGER
    );
    """)
connect.commit()
@dp.message_handler(commands=["start"])
async def start(message:types.Message):
    cursor = connect.cursor()
    #ВЫБЕРИТЬ id_user ОТ users, ГДЕ id_user = {message.from_user.id}
    cursor.execute(f"SELECT id_user FROM users WHERE id_user = {message.from_user.id};")
    res = cursor.fetchall()
    print(res)
    if message.from_user.username == "askhatprog":
            await message.answer("Проверка связи")
    if res == []:
        #ВСТАВИТЬ В ЗНАЧЕНИЯ пользователей
        cursor.execute(f"""INSERT INTO users VALUES ('{message.from_user.username}',
        '{message.from_user.first_name}', '{message.from_user.last_name}',
        {message.from_user.id}, {message.chat.id})""")
        
    connect.commit()
    await message.answer(f"Здраствуйте {message.from_user.full_name}")
@dp.message_handler(commands='help')
async def help(message:types.Message):
    await message.reply(f"Вот мои команды: /start")

executor.start_polling(dp)    