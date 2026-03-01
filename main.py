import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import settings

# redis_url = 'redis://localhost:6379/0'
# dp = Dispatcher(storage=RedisStorage.from_url(redis_url))
dp = Dispatcher()

import json

csv_file = 'districts (2).csv'
json_file = 'districts.json'


@dp.message(CommandStart)
async def handler(message: Message) -> None:
    await message.answer('xush kelibsiz')

    await message.answer('viloyatlar')


async def main() -> None:
    bot = Bot(settings.TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # dp.startup.register(startup)
    # dp.shutdown.register(shutdown)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
