from telethon import TelegramClient, events, sync
from telethon import Button
from telethon import functions, types

import os
import asyncio


API_ID = 12416208
API_HASH ="aa15730cc72680d05bbcd400f3476081"

userbot_personal = TelegramClient("userbot_personal", API_ID, API_HASH)





async def usbot():

  
  @userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.status"))
  async def statususerbot(event):
    await event.edit("userbot online")

  @userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.name"))
  async def nameprofilyou(event):
    x = event.text.split(" ", maxsplit=1)[1]
    result = await userbot_personal(functions.account.UpdateProfileRequest(
          first_name=x,
      ))
    await event.edit(f"name put as **{x}**")

  @userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.stopuserbot"))
  async def _stopuserbot(event):
    await event.edit("fra 3 secondi andra offline l'userbot")
    await userbot_personal.disconnect()
    await asyncio.sleep(3)





  
print("Userbot Personal Online!")


with userbot_personal:
  userbot_personal.loop.run_until_complete(usbot())
  userbot_personal.run_until_disconnected()

