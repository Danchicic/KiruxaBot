from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot
    chat_id_to_send: str


env = Env()
env.read_env()

config = Config(
    tg_bot=TgBot(
        token=env('BOT_TOKEN'),
    ),
    chat_id_to_send=env('CHAT_ID')
)
