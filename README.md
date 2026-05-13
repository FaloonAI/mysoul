# MySoul

**MySoul** is a Telegram bot based on `aiogram 3.x`, designed to automate the Telegram Business profile. The bot can automatically respond to messages on your behalf and provide utilities for working with custom emojis.

## Main functions
- **Business Mode**: Automatic replies in personal chats through profile integration.
- **Emoji Utility**: Quickly get custom emoji IDs from any pack.
- **Anti-Spam**: Built-in flood protection.
- **Clean Architecture**: Separation of logic into routers, handlers and utilities.

---

## Installation
### 1. Cloning a repository
```bash
git clone [https://github.com/FaloonAI/mysoul.git](https://github.com/FaloonAI/mysoul.git)
cd mysoul
```
### 2. Setting up the environment
```bash
python -m venv venv
source venv/bin/activate # For Linux/macOS
# venv\Scripts\activate # For Windows
pip install -r requirements.txt
```
### 3. Configuration
Create a `.env` file in the root folder and fill it in:
```python
BOT_TOKEN=your_token
ADMIN_ID=your_id
SPAM_LIMIT=5
SPAM_WINDOW=10
BLOCK_DURATION=120
```
### 4. Launch
```bash
python bot.py
```
