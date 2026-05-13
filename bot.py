import asyncio
import logging
import sys

from settings.settings import config
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers import common, business

# ====================== НАСТРОЙКИ ======================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)

bot = Bot(token=config.bot_token.get_secret_value(), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# ====================== ЗАПУСК ======================
async def main():
    print("🚀 Бот запущен!")
    await bot.delete_webhook(drop_pending_updates=True)

    dp.include_router(common.router)
    dp.include_router(business.router)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())