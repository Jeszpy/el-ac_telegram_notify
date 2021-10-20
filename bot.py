import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '2070861903:AAFNwC84mSIkzCUb5q4imWJPGCnQDYFZR3o'


logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
23    This handler will be called when user sends `/start` or `/help` command
24    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")



@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)