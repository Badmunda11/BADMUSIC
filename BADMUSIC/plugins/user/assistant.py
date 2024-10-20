# Copyright (C) 2024 by Badhacker98@Github, < https://github.com/Badhacker98 >.
# Owner https://t.me/ll_BAD_MUNDA_ll

import os
from inspect import getfullargspec

from pyrogram import filters
from pyrogram.types import Message

from BADMUSIC import app
from BADMUSIC.misc import SUDOERS
from BADMUSIC.utils.database import get_client


@Client.on_message(filters.command("setpfp", prefixes=".") & SUDOERS)
async def set_pfp(client, message):
    from BADMUSIC.core.userbot import assistants

    if not message.reply_to_message or not message.reply_to_message.photo:
        return await eor(message, text="Reply to a photo")
    for num in assistants:
        client = await get_client(num)
        photo = await message.reply_to_message.download()
        try:
            await client.set_profile_photo(photo=photo)
            await eor(message, text="Successfully Changed PFP.")
            os.remove(photo)
        except Exception as e:
            await eor(message, text=e)
            os.remove(photo)


@Client.on_message(filters.command("setbio", prefixes=".") & SUDOERS)
async def set_bio(client, message):
    from BADMUSIC.core.userbot import assistants

    if len(message.command) == 1:
        return await eor(message, text="Give some text to set as bio.")
    elif len(message.command) > 1:
        for num in assistants:
            client = await get_client(num)
            bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await eor(message, text="Changed Bio.")
        except Exception as e:
            await eor(message, text=e)
    else:
        return await eor(message, text="Give some text to set as bio.")


@Client.on_message(filters.command("setname", prefixes=".") & SUDOERS)
async def set_name(client, message):
    from BADMUSIC.core.userbot import assistants

    if len(message.command) == 1:
        return await eor(message, text="Give some text to set as name.")
    elif len(message.command) > 1:
        for num in assistants:
            client = await get_client(num)
            name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await eor(message, text=f"name Changed to {name} .")
        except Exception as e:
            await eor(message, text=e)
    else:
        return await eor(message, text="Give some text to set as name.")


@Client.on_message(filters.command("delpfp", prefixes=".") & SUDOERS)
async def del_pfp(client, message):
    from BADMUSIC.core.userbot import assistants

    for num in assistants:
        client = await get_client(num)
        photos = [p async for p in client.get_chat_photos("me")]
        try:
            if photos:
                await client.delete_profile_photos(photos[0].file_id)
                await eor(message, text="Successfully deleted photo")
            else:
                await eor(message, text="No profile photos found.")
        except Exception as e:
            await eor(message, text=e)


@Client.on_message(filters.command("delallpfp", prefixes=".") & SUDOERS)
async def delall_pfp(client, message):
    from BADMUSIC.core.userbot import assistants

    for num in assistants:
        client = await get_client(num)
        photos = [p async for p in client.get_chat_photos("me")]
        try:
            if photos:
                await client.delete_profile_photos([p.file_id for p in photos[1:]])
                await eor(message, text="Successfully deleted photos")
            else:
                await eor(message, text="No profile photos found.")
        except Exception as e:
            await eor(message, text=e)


async def eor(msg: Message, **kwargs):
    func = (
        (msg.edit_text if msg.from_user.is_self else msg.reply)
        if msg.from_user
        else msg.reply
    )
    spec = getfullargspec(func.__wrapped__).args
    return await func(**{k: v for k, v in kwargs.items() if k in spec})
