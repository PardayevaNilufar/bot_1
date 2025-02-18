from tkinter import Menubutton

from aiogram import types
from loader import dp,bot
from keyboards.inline.tugmalar_test import birinchi_savol



@dp.callback_query_handler(text="12")
async def call_mavjud(call:types.CallbackQuery):
    await call.message.edit_text("noto'g'ri javob",reply_markup=birinchi_savol)




@dp.callback_query_handler(text="23")
async def call_mavjud(call:types.CallbackQuery):
    await call.message.edit_text("noto'g'ri javob",reply_markup=birinchi_savol)




@dp.callback_query_handler(text="24")
async def call_mavjud(call:types.CallbackQuery):
    await call.message.edit_text("to'g'ri javob",reply_markup=birinchi_savol)




@dp.callback_query_handler(text="ortga")
async def call_mavjud(call:types.CallbackQuery):
    await call.message.edit_text("12+12=? nechaga teng",reply_markup=birinchi_savol)

