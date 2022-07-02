from telethon import TelegramClient, events, sync
from telethon import functions, types

import os
import asyncio
import telethon
import glob

@userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.stopuserbot"))
async def _stopuserbot(event):
    await event.edit("3 sec and the userbot will go offline.")
    await userbot_personal.disconnect()
    await asyncio.sleep(3)