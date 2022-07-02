from telethon import TelegramClient, events, sync
from telethon import functions, types

import os
import asyncio
import telethon
import glob

@userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.reboot"))
async def reboot(event):
    await event.delete()
    import os, sys, threading
    os.system("clear")
  
    os.execl(sys.executable, sys.executable, *sys.argv)
    thereading.Thread(target=_restart, args=(bot, msg)).start()