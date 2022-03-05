from telethon import TelegramClient, events, sync
from telethon import Button
import os


API_ID = 123
API_HASH ="179ahdis"

userbot_personal = TelegramClient("userbot_personal", API_ID, API_HASH)





async def usbot():


@userbot_personal.on(events.NewMessage(outgoing=True, pattern=r".status"))
async def statususerbot(event):
   await event.edit("userbot online")





print("Userbot Personal Online!")


with userbot_personal:
  userbot_personal.loop.run_until_complete(usbot())
  userbot_personal.run_until_disconnected()
