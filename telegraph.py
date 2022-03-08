import os

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Sinderella import pbot as app
from Sinderella.helper_extra.fsub import ForceSub

from telegraph import upload_file


@app.on_message(filters.command(["telegraph", "tm"]))
async def telegraph(client, message):
    FSub = await ForceSub(client, message)
    if FSub == 400:
        return
    replied = message.reply_to_message
    if not replied:
        await message.reply("Reply to a supported media file")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4", ".webp"),
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply("Not supported!")
        return
    download_location = await client.download_media(
        message=message.reply_to_message,
        file_name="root/downloads/",
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        await message.reply(
            f"**Uploaded To [Telegraph](https://telegra.ph{response[0]})**\n\n**POWERD BY @TeamSinderella**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "••Telegraph Link••",
                            url="https://telegra.ph{}".format(response[0]),
                        )
                    ]
                ]
            ),
            disable_web_page_preview=False,
        )
    finally:
        os.remove(download_location)
