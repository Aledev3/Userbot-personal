from telethon import functions, types


@userbot_personal.on(events.NewMessage)
async def statusOffline(event):
  result = await client(functions.account.UpdateStatusRequest(
        offline=True
    ))
await event.respond("I'm offline")
