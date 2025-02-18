

from aiogram import types
from loader import dp,bot

from utils.jami_savollar import savollar



def send_question(savollar):
    for i,savol in enumerate(savollar,start=1):
        print(f"Savol {i} {savol['savol']}")
        for r,javob in enumerate(savollar,start=1):
            print(f"{r}. {javob}")

#


@dp.message_handler(commands="test_yechish")
async def test(message: types.Message):
    for i in savollar:
        print(i)
        await message.answer(i)
