from aiogram import types


@dp.message_handler()
async def echo_send(message : types.Message):
    if message.text == 'Привет':
        await message.answer('Здравствуй, и тебе не хворать)')
    #await message.reply(message.text)
    #await bot.send_message(message.from_user.id, message.text)