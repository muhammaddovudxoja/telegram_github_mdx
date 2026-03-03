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
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import settings
from models.regions import Region, District
from models.market import Cart, Category, Product


# redis_url = 'redis://localhost:6379/0'
# dp = Dispatcher(storage=RedisStorage.from_url(redis_url))
dp = Dispatcher()











#                   BOT-2 PROJECT
# def category_inline():
#     categories = Category.get_all()
#     ikm = InlineKeyboardBuilder()
#
#     for category in categories:
#         ikm.row(
#             InlineKeyboardButton(
#                 text=category.name,
#                 callback_data=f"category:{category.id}"
#             )
#         )
#
#     return ikm
#
# def product_inline(category_id):
#     products = Product.filter(category_id=category_id)
#     ikm = InlineKeyboardBuilder()
#
#     for product in products:
#         ikm.row(
#             InlineKeyboardButton(
#                 text=f"{product.name} - {product.price} so'm",
#                 callback_data=f"add:{product.id}"
#             )
#         )
#
#     ikm.row(
#         InlineKeyboardButton(text="🛒 Savat", callback_data="cart"),
#         InlineKeyboardButton(text="🔙 Back", callback_data="back:category"),
#     )
#
#     return ikm
#
#
# @dp.message(CommandStart())
# async def start_handler(message: Message):
#     await message.answer("🛍 Marketga xush kelibsiz")
#     ikm = category_inline()
#     await message.answer("📂 Categoriyalar:", reply_markup=ikm.as_markup())
#
# @dp.callback_query(F.data.startswith("category:"))
# async def category_callback(callback: CallbackQuery):
#     category_id = int(callback.data.split(":")[1])
#
#     ikm = product_inline(category_id)
#
#     await callback.message.edit_text(
#         "🛒 Mahsulotlar:",
#         reply_markup=ikm.as_markup()
#     )
#
# @dp.callback_query(F.data.startswith("add:"))
# async def add_to_cart(callback: CallbackQuery):
#     product_id = int(callback.data.split(":")[1])
#     user_id = callback.from_user.id
#
#     item = Cart.filter(
#         Cart.user_id == user_id,
#         Cart.product_id == product_id
#     ).first()
#
#     if item:
#         Cart.update(item.id, quantity=item.quantity + 1)
#     else:
#         Cart.create(user_id=user_id, product_id=product_id)
#
#     await callback.answer("✅ Savatga qo'shildi")
#
#
# @dp.callback_query(F.data == "cart")
# async def show_cart(callback: CallbackQuery):
#     user_id = callback.from_user.id
#     items = Cart.filter(Cart.user_id == user_id)
#
#     text = "🛍 Savatingiz:\n\n"
#     total = 0
#
#     ikm = InlineKeyboardBuilder()
#
#     for item in items:
#         subtotal = item.product.price * item.quantity
#         total += subtotal
#
#         text += f"{item.product.name} x{item.quantity} = {subtotal} so'm\n"
#
#         ikm.row(
#             InlineKeyboardButton(text="➖", callback_data=f"minus:{item.product.id}"),
#             InlineKeyboardButton(text="➕", callback_data=f"plus:{item.product.id}"),
#             InlineKeyboardButton(text="❌", callback_data=f"remove:{item.product.id}")
#         )
#
#     text += f"\n💰 Jami: {total} so'm"
#
#     ikm.row(
#         InlineKeyboardButton(text="🚚 Yetkazib berish", callback_data="delivery"),
#         InlineKeyboardButton(text="📦 Olib ketish", callback_data="pickup"),
#     )
#
#     await callback.message.edit_text(text, reply_markup=ikm.as_markup())
#
#
#
# @dp.callback_query(F.data.startswith("plus:"))
# async def plus(callback: CallbackQuery):
#     product_id = int(callback.data.split(":")[1])
#     user_id = callback.from_user.id
#
#     item = Cart.filter(
#         Cart.user_id == user_id,
#         Cart.product_id == product_id
#     ).first()
#
#     Cart.update(item.id, quantity=item.quantity + 1)
#
#     await show_cart(callback)
#
#
# @dp.callback_query(F.data.startswith("minus:"))
# async def minus(callback: CallbackQuery):
#     product_id = int(callback.data.split(":")[1])
#     user_id = callback.from_user.id
#
#     item = Cart.filter(
#         Cart.user_id == user_id,
#         Cart.product_id == product_id
#     ).first()
#
#     if item.quantity > 1:
#         Cart.update(item.id, quantity=item.quantity - 1)
#     else:
#         Cart.delete(item.id)
#
#     await show_cart(callback)
#
# @dp.callback_query(F.data.startswith("remove:"))
# async def remove(callback: CallbackQuery):
#     product_id = int(callback.data.split(":")[1])
#     user_id = callback.from_user.id
#
#     item = Cart.filter(
#         Cart.user_id == user_id,
#         Cart.product_id == product_id
#     ).first()
#
#     Cart.delete(item.id)
#
#     await show_cart(callback)
#
#
# @dp.callback_query(F.data == "delivery")
# async def delivery(callback: CallbackQuery):
#     await callback.message.answer(
#         "📍 Lokatsiyangizni yuboring",
#         reply_markup=ReplyKeyboardMarkup(
#             keyboard=[[KeyboardButton(text="📍 Lokatsiya yuborish", request_location=True)]],
#             resize_keyboard=True
#         )
#     )







# Region District Bot Project
# class DistrictUpdate(StatesGroup):
#     name = State()
#
#
#
# district_file = 'districts (2).csv'
#
#
# def region_inline_buttons():
#     regions = Region.get_all()
#     ikm = InlineKeyboardBuilder()
#     for region in regions:
#         ikm.row(
#             InlineKeyboardButton(text=region.name, callback_data=f'region:{region.id}'),
#         )
#     return ikm
#
#
# def district_inline_buttons(region_id):
#     districts = District.filter(region_id=region_id)
#     ikm = InlineKeyboardBuilder()
#     for district in districts:
#         ikm.row(
#             InlineKeyboardButton(text=district.name, callback_data=f'district:{district.id}'),
#             InlineKeyboardButton(text='✏️', callback_data=f'change_district:{district.id}'),
#             InlineKeyboardButton(text='❌', callback_data=f'remove_district:{district.id}'),
#         )
#     ikm.row(
#         InlineKeyboardButton(text='🔙 Back', callback_data=f'back:region'),
#     )
#     return ikm
#
#
# @dp.message(CommandStart())
# async def handler(message: Message) -> None:
#     await message.answer('xush kelibsiz')
#     ikm = region_inline_buttons()
#     await message.answer('Viloyatlar', reply_markup=ikm.as_markup())
#
#
# @dp.callback_query(F.data.startswith(f'region:'))
# async def region_callback(callback: CallbackQuery, state: FSMContext) -> None:
#     region_id = int(callback.data.removeprefix("region:"))
#     ikm = district_inline_buttons(region_id)
#
#     sent_message = await callback.message.edit_text('Tumanlar', reply_markup=ikm.as_markup())
#     await state.update_data(last_message_id=sent_message.message_id, region_id=region_id)
#
#
# @dp.callback_query(F.data.startswith(f'back:'))
# async def back_callback(callback: CallbackQuery) -> None:
#     key = callback.data.removeprefix("back:")
#     if key == 'region':
#         ikm = region_inline_buttons()
#         await callback.message.edit_text('Viloyatlar')
#         await callback.message.edit_reply_markup(inline_message_id=callback.inline_message_id,
#                                                  reply_markup=ikm.as_markup())
#
#
# @dp.callback_query(F.data.startswith(f'remove_district:'))
# async def remove_district_callback(callback: CallbackQuery) -> None:
#     district_id = int(callback.data.removeprefix("remove_district:"))
#     districts = District.delete(district_id)
#     await callback.answer(f"{districts.name} o'chirildi", show_alert=True)
#     ikm = district_inline_buttons(districts.region_id)
#     await callback.message.edit_reply_markup(callback.inline_message_id, reply_markup=ikm.as_markup())
#
#
# @dp.callback_query(F.data.startswith(f'change_district:'))
# async def change_district_callback(callback: CallbackQuery, state: FSMContext) -> None:
#     district_id = int(callback.data.removeprefix("change_district:"))
#     cim = callback.inline_message_id
#     await state.update_data(district_id=district_id, inline_message_id=cim)
#     await state.set_state(DistrictUpdate.name)
#     await callback.message.answer('Tumanning yangi nomini kiriting')
#
#
# @dp.message(DistrictUpdate.name)
# async def district_update(message: Message, bot: Bot, state: FSMContext) -> None:
#     new_district_name = message.text
#     data = await state.get_data()
#     district_id = data['district_id']
#     message_id = data['last_message_id']
#     district = District.update(district_id, name=new_district_name)
#     ikm = district_inline_buttons(district.region_id)
#     await bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=message_id, reply_markup=ikm.as_markup())
#     await state.clear()
#     await message.answer("Tumanning nomi o'zgartirildi")
#
#
# @dp.message(Command('migrate'))
# async def migrate(message: Message) -> None:
#     with open('districts (2).csv', encoding="utf-8-sig") as f1, open('regions.csv', encoding="utf-8-sig") as f2:
#         regions = csv.DictReader(f2)
#         districts = csv.DictReader(f1)
#         Region.bulk_create(list(regions))
#         District.bulk_create(list(districts))
#     await message.answer('Bazaga yozildi')


async def main() -> None:
    bot = Bot(settings.TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # dp.startup.register(startup)
    # dp.shutdown.register(shutdown)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
