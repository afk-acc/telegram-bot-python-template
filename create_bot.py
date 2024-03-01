from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import settings
# bot = Bot(token=os.getenv('TOKEN'))
bot = Bot(token=settings.TOKEN)
dp = Dispatcher(storage=MemoryStorage())