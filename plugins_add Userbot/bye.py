from telethon import eventi


@userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.bye"))
