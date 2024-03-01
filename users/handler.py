from aiogram import types, Router
from aiogram.filters import Command

router = Router()


@router.message(
    Command('start', prefix='/')
)
async def start(message: types.Message):
    await message.reply(text=message.text)
