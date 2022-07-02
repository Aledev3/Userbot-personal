from telethon import TelegramClient, events, sync
from telethon import functions, types

import os
import asyncio
import telethon
import glob

@userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.delm"))
async def _delm(event):
    await event.delete()
    d = await event.get_reply_message()
    await d.delete()
    await event.respond("Message deleted")