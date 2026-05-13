import logging

from datetime import datetime
from utils.utils import ce, get_emoji_ids
from utils.data import NEWS_EMOJI
from aiogram import Router, Bot
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

logger = logging.getLogger(__name__)
router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f"{ce(NEWS_EMOJI['check'], '✔️')} <b>Профильный бот успешно запущен!</b>\n\n"
        f"Теперь я буду автоматически отвечать от твоего имени в подключённых чатах."
    )

@router.message(Command("status"))
async def cmd_status(message: Message):
    await message.answer(
        f"{ce(NEWS_EMOJI['bell'], '🔔')} <b>Статус профильного бота</b>\n\n"
        f"• Время: {datetime.now().strftime('%H:%M:%S')}\n"
        f"• Библиотека: aiogram 3.x\n"
        f"• Режим: Chat Automation (Business)\n"
        f"• Chat ID: <code>{message.chat.id}</code>"
    )

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        f"{ce(NEWS_EMOJI['chat'], '💬')} <b>Доступные команды:</b>\n"
        "/start — Запуск бота\n"
        "/status — Статус бота\n"
        "/emoji_id — Список ID-эмодзи\n"
        "/help — Эта справка"
    )

@router.message(Command("emoji_id"))
async def cmd_emoji_id(message: Message, command: CommandObject, bot: Bot):
    if not command.args:
        return await message.answer(
            "Пришлите данные после команды, например:\n"
            "<code>/emoji_id NewsEmoji</code>\n"
            "<code>/emoji_id https://t.me/addemoji/PackName</code>"
        )

    status_msg = await message.answer("🔍 Обрабатываю запрос...")
    response = await get_emoji_ids(bot, command.args)
    await status_msg.edit_text(response)