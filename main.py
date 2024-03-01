from aiogram import Bot, Dispatcher
import asyncio
import logging
import os
from create_bot import bot, dp
from users.handler import router as users_router


@dp.startup()
async def on_startup():
    print("bot is started")


async def main():
    dp.include_routers(users_router)
    await dp.start_polling(bot)


asyncio.run(main())