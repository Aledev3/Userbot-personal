from telethon import TelegramClient, events, sync
from telethon import Button
from telethon import functions, types
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

import os
import asyncio
import telethon
import glob

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
ACCOUNT = os.environ.get('USERNAME')

userbot_personal = TelegramClient("userbot_personal", API_ID, API_HASH)

async def usbot():

  @userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.info"))
  async def statususerbot(event):
    await event.edit("**The userbot is online!** ✅\n\n🤖 Version: 1.1\n📜 GitHub: [1](https://github.com/Aledev3/Userbot-personal) [2](https://github.com/Shad0wGlitch/userbot-for-aledev)\n\n**Made with** ❤️ **by** @OgDeltwin & @Muffa0")
    
with userbot_personal:
  if not API_ID and not API_HASH:
    print("Configure your API_ID && API_HASH in your .env file otherwise the bot will not work.")
    exit()
  else:
    userbot_personal.loop.run_until_complete(usbot())
    print("The userbot is online! Logged in as:", ACCOUNT, "(Terminal)")
    print("Made with ❤️  by @OgDeltwin & @Muffa0")
    userbot_personal.run_until_disconnected()

  #ONLY FOR DEV:
  #@userbot_personal.on(events.Raw)
  #async def handler(update):
    # Print all incoming updates
    #await userbot_personal.send_message("me",update.stringify())
