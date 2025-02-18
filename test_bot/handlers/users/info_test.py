
from keyboards.inline.tugmalar_test import birinchi_savol
from aiogram import types
from loader import dp,bot
from data.config import ADMINS



@dp.message_handler(commands="test")
async def test_yechish(message:types.Message):
    text=f"assalomu alaykum testimizga xush kelibsiz \n"
    text+="marhamat testni boshlashingiz mumkin!"
    await message.answer(text)
    await message.answer("12+12=? nechga teng",reply_markup=birinchi_savol)

    await message.answer("")