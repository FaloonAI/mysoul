from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):
    bot_token: SecretStr
    admin_id: int
    spam_limit: int
    spam_window: int
    block_duration: int

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

config = Settings()