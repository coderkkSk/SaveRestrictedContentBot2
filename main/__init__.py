#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = int(1604400)
API_HASH = "8e6598bb138e8e7890b0fa19d6a152f6"
BOT_TOKEN = "6651017840:AAFmdHWRjthzG2lfevZnAiPIPYORGFllOmQ"
SESSION = "BQAYezAANQwPVO7Jqd_J3SEk52YjVBORnBFwSY3QOiEiPlY7YLpIkCDE6LNZJz1ge5z0MLbYCrVrb2b15YqGtca_z9AC-OqjpiTj_dmiNwFo_e9peXTHME06zewEToIz_dZ6riZFFAuNn-GtoM-rapwOVxtD96_JhoaluNHrU5qVwQLNTrUp-nxOiaoJs2BRB00cV_LCpLAx1pDV9aahc0H4hAYLmuEy5NAGVlUW6f03VSN9GkyKp1KX2f7geN67Guv6YMbRM6Sg8huG0PpVPZlitO4GOLyUKK_QAF0Z9qPUFue7rGAw3e-58mpwecjkwYFVatqAyDi4fmlxfnr2T0kTb0WghQAAAAGGJj8xAA"
FORCESUB = "jogumotaru"
AUTH = int(6545620785)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
