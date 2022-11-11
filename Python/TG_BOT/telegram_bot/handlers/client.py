from aiogram import types
from create_bot import dp

@dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Доброго времени суток, дорогой Пользователь. Я бот Московсокого образования')
        await message.delete()
    except:
        await message.reply('Напишите боту первым:\nhttps://t.me/MosEDBot')

@dp.message_handler(commands=['Режим_работы'])
async def moscow_ed_open_command (message: types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Чт с 9:00 до 18:00, Пт с 9:00 до 17:00, Сб-Вс - выходные дни')


@dp.message_handler(commands=['Расположение'])
async def moscow_ed_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Страна Россия, г. Москва, ул. Пушкина, д. 27а')

#@dp.message_handler(commands=['Выбор образовательного учреждения'])
#async def moscow_ed_menu_command (message : types.Message):
#   for ret in cur.execute ('SELECT * FROM menu').fetchall():
#       await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')