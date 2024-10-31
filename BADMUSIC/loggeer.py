import logging
import pytz
import time
from pymongo import MongoClient
from config import LOG_FILE_NAME
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from Abg import patch
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from pyrogram import Client
from pyrogram.enums import ParseMode
import config
import uvloop

uvloop.install()

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
SUKH2 = logging.getLogger(__name__)
boot = time.time()
mongodb = MongoCli(config.MONGO_DB_URI)
db = mongodb.Badmusic
mongo = MongoClient(config.MONGO_DB_URI)
OWNER = config.OWNER_ID

class app(Client):
    def __init__(self):
        super().__init__(
            name="app",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            lang_code="en",
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.DEFAULT,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

    async def stop(self):
        await super().stop()


def SUKH2(name: str) -> logging.Logger:
    return logging.getLogger(name)