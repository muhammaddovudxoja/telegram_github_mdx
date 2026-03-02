import asyncio
import csv
import logging
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import settings
from models.regions import Region, District


class DistrictUpdate(StatesGroup):
    name = State()


# redis_url = 'redis://localhost:6379/0'
# dp = Dispatcher(storage=RedisStorage.from_url(redis_url))
dp = Dispatcher()


# district_file = 'districts (2).csv'


def region_inline_buttons():
    regions = Region.get_all()
    ikm = InlineKeyboardBuilder()
    for region in regions:
        ikm.row(
            InlineKeyboardButton(text=region.name, callback_data=f'region:{region.id}'),
        )
    return ikm


def district_inline_buttons(region_id):
    districts = District.filter(region_id=region_id)
    ikm = InlineKeyboardBuilder()
    for district in districts:
        ikm.row(
            InlineKeyboardButton(text=district.name, callback_data=f'district:{district.id}'),
            InlineKeyboardButton(text='✏️', callback_data=f'change_district:{district.id}'),
            InlineKeyboardButton(text='❌', callback_data=f'remove_district:{district.id}'),
        )
    ikm.row(
        InlineKeyboardButton(text='🔙 Back', callback_data=f'back:region'),
    )
    return ikm


@dp.message(CommandStart())
async def handler(message: Message) -> None:
    await message.answer('xush kelibsiz')
    ikm = region_inline_buttons()
    await message.answer('Viloyatlar', reply_markup=ikm.as_markup())


@dp.callback_query(F.data.startswith(f'region:'))
async def region_callback(callback: CallbackQuery, state: FSMContext) -> None:
    region_id = int(callback.data.removeprefix("region:"))
    ikm = district_inline_buttons(region_id)

    sent_message = await callback.message.edit_text('Tumanlar', reply_markup=ikm.as_markup())
    await state.update_data(last_message_id=sent_message.message_id, region_id=region_id)


@dp.callback_query(F.data.startswith(f'back:'))
async def back_callback(callback: CallbackQuery) -> None:
    key = callback.data.removeprefix("back:")
    if key == 'region':
        ikm = region_inline_buttons()
        await callback.message.edit_text('Viloyatlar')
        await callback.message.edit_reply_markup(inline_message_id=callback.inline_message_id,
                                                 reply_markup=ikm.as_markup())


@dp.callback_query(F.data.startswith(f'remove_district:'))
async def remove_district_callback(callback: CallbackQuery) -> None:
    district_id = int(callback.data.removeprefix("remove_district:"))
    districts = District.delete(district_id)
    await callback.answer(f"{districts.name} o'chirildi", show_alert=True)
    ikm = district_inline_buttons(districts.region_id)
    await callback.message.edit_reply_markup(callback.inline_message_id, reply_markup=ikm.as_markup())


@dp.callback_query(F.data.startswith(f'change_district:'))
async def change_district_callback(callback: CallbackQuery, state: FSMContext) -> None:
    district_id = int(callback.data.removeprefix("change_district:"))
    cim = callback.inline_message_id
    await state.update_data(district_id=district_id, inline_message_id=cim)
    await state.set_state(DistrictUpdate.name)
    await callback.message.answer('Tumanning yangi nomini kiriting')


@dp.message(DistrictUpdate.name)
async def district_update(message: Message, bot: Bot, state: FSMContext) -> None:
    new_district_name = message.text
    data = await state.get_data()
    district_id = data['district_id']
    message_id = data['last_message_id']
    district = District.update(district_id, name=new_district_name)
    ikm = district_inline_buttons(district.region_id)
    await bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=message_id, reply_markup=ikm.as_markup())
    await state.clear()
    await message.answer("Tumanning nomi o'zgartirildi")


@dp.message(Command('migrate'))
async def migrate(message: Message) -> None:
    with open('districts (2).csv', encoding="utf-8-sig") as f1, open('regions.csv', encoding="utf-8-sig") as f2:
        regions = csv.DictReader(f2)
        districts = csv.DictReader(f1)
        Region.bulk_create(list(regions))
        District.bulk_create(list(districts))
    await message.answer('Bazaga yozildi')


async def main() -> None:
    bot = Bot(settings.TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # dp.startup.register(startup)
    # dp.shutdown.register(shutdown)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
