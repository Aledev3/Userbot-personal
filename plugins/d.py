from telethon import TelegramClient, events, sync
from telethon import functions, types

import os
import asyncio
import telethon
import glob

@userbot_personal.on(events.NewMessage(outgoing=True))
async def t_p(event):
    if event.text == ".d":
      await event.edit("d lol")
