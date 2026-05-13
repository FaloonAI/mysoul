import logging

from aiogram import Router
from aiogram.types import Message
from utils.utils import ce, is_spam
from utils.data import NEWS_EMOJI

logger = logging.getLogger(__name__)
router = Router()

@router.business_message()
async def handle_business_message(message: Message):
    user = message.from_user

    if user.id == 1184490028:
        return

    if is_spam(user.id):
        logger.warning(f"[SPAM] Заблокирован {user.full_name} ({user.id})")
        return

    try:
        if message.text:
            text_lower = message.text.lower().strip()

            if any(g in text_lower for g in ["привет", "здравствуй", "hi", "hello"]):
                await message.answer(
                    f"Привет, {user.first_name}! \nОжидайте ответ от Faloon-а"
                    f"{ce(NEWS_EMOJI['sparkle'], '✨')}"
                )

            elif "как дела" in text_lower:
                await message.answer(
                    f"Отлично! А у тебя как? "
                    f"{ce(NEWS_EMOJI['fire'], '🔥')}"
                )

            elif any(g in text_lower for g in ["спасибо", "благодарю", "thanks"]):
                await message.answer(
                    f"Всегда пожалуйста! "
                    f"{ce(NEWS_EMOJI['thumbsup'], '👍')}"
                )
        else:
            await message.answer(
                f"{ce(NEWS_EMOJI['eyes'], '👀')}"
            )

    except Exception as e:
        logger.error(f"Ошибка при отправке сообщения: {e}")

@router.message()
async def handle_regular_message(message: Message):
    logger.info(f"[REGULAR] От {message.from_user.full_name}: {message.text}")
    await message.answer(
        f"{ce(NEWS_EMOJI['check'], '✔️')} Сообщение получено (обычный режим)"
    )