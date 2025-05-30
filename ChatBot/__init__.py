import time
import logging

from pyrogram import Client
from motor.motor_asyncio import AsyncIOMotorClient

import config

# Logger Setup
logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    level=logging.INFO,
)
LOGGER = logging.getLogger("ChatBot")

# Database Connection
db = AsyncIOMotorClient(config.MONGO_URL).Anonymous
START_TIME = time.time()

from ChatBot.aaru_gemini import AaruGemini

chatbot_api = AaruGemini(api_key="AIzaSyCmZYuxe4JeEbGURuJa6jPoQNvt677tp0E")  # Replace with your real key
class Bot(Client):
    def __init__(self):
        super().__init__(
            name="ChatBot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self, *args, **kwargs):
        """Starts the bot and logs details"""
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name
        self.username = self.me.username
        LOGGER.info(f"Bot started as {self.name} (@{self.username}). 💖")

    async def stop(self):
        """Stops the bot gracefully"""
        await super().stop()
        LOGGER.info("Bot stopped.")

app = Bot()
