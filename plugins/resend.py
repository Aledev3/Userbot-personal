from telethon import TelegramClient, events, sync
from telethon import functions, types

import os
import asyncio
import telethon
import glob

@userbot_personal.on(outgoing=True, pattern=r"\.resend")
async def _(event):
    await event.delete()
    m = await event.get_reply_message()
    if not m:
        return
    await event.respond(m)
    
# ...
