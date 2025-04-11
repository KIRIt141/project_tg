import asyncio
import logging

from loader import dp
from config import bot

logging.basicConfig(level=logging.INFO)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())

