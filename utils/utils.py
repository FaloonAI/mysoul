import time

from aiogram import Bot
from settings.settings import config
from collections import defaultdict

user_message_times: dict[int, list[float]] = defaultdict(list)
blocked_users: dict[int, float] = {}

def ce(emoji_id: str, fallback: str = "⭐") -> str:
    """Хелпер — вставляет кастомный tg-emoji в текст"""
    return f'<tg-emoji emoji-id="{emoji_id}">{fallback}</tg-emoji>'

def is_spam(user_id: int) -> bool:
    now = time.time()

    if user_id in blocked_users:
        if now < blocked_users[user_id]:
            return True
        else:
            del blocked_users[user_id]

    user_message_times[user_id] = [
        t for t in user_message_times[user_id]
        if now - t < config.spam_window
    ]

    user_message_times[user_id].append(now)

    if len(user_message_times[user_id]) > config.spam_limit:
        blocked_users[user_id] = now + config.block_duration
        user_message_times[user_id].clear()
        return True

    return False

async def get_emoji_ids(bot: Bot, input_data: str):
    if "t.me/addemoji/" in input_data:
        pack_name = input_data.split("addemoji/")[1].split("?")[0]

    else:
        pack_name = input_data.strip()

    try:
        sticker_set = await bot.get_sticker_set(pack_name)
        
        result = [f"<b>Пак:</b> {sticker_set.title} (<code>{pack_name}</code>)\n"]
        for sticker in sticker_set.stickers:
            if sticker.custom_emoji_id:
                line = f"{sticker.emoji} | <code>{sticker.custom_emoji_id}</code>"
                result.append(line)
        
        return "\n".join(result)
    except Exception:
        return "❌ Не удалось найти пак. Убедитесь, что имя или ссылка верны."