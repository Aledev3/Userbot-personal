from telethon import TelegramClient, events, sync
from telethon import functions, types

import os
import asyncio
import telethon
import glob

@userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.version_telethon"))
async def versiontelethon(event):
    g = (telethon.__version__)
    await e.edit(f"Telethon version -> {g}")