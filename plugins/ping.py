from telethon import TelegramClient, events, sync
from telethon import functions, types

import os
import asyncio
import telethon
import glob

@userbot_personal.on(events.NewMessage(outgoing=True, pattern=r".ping"))
async def _ping(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("**Pong!**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("**Pong!**\n`{}`".format(ms))