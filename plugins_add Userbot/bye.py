from telethon import events


@userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.bye"))
async def bye_(event):
    await event.edit("the command is coming")
