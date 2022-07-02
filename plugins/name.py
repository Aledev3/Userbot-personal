from telethon import TelegramClient, events, sync
from telethon import functions, types

import os
import asyncio
import telethon
import glob

@userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.name"))
async def nameprofilyou(event):
    x = event.text.split(" ", maxsplit=1)[1]
    result = await userbot_personal(functions.account.UpdateProfileRequest(
          first_name=x,
      ))
    await event.edit(f"Account logged in as **{x}**")