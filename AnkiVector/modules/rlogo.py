import os
import io
import requests
import shutil 
import random
import re
import glob
import time
import sys
import base64

from bs4 import *
from io import BytesIO
from requests import get
from pyrogram import filters	
from PIL import Image, ImageDraw, ImageFont
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AnkiVector.services.pyrogram import pbot
from AnkiVector.function.pluginhelpers import get_text
from AnkiVector import OWNER_ID, BOT_USERNAME, SUPPORT_CHAT
from AnkiVector.helper_extra.fsub import ForceSub
from AnkiVector.helper_extra.blogo_helper import download_images, mainne
# ==================== Logo ====================

@pbot.on_message(filters.command("logo") & ~filters.edited & ~filters.bot)
async def logo(client, message):
 FSub = await ForceSub(client, message)
 if FSub == 400:
        return            
 quew = get_text(message)
 if not quew:
     await client.send_message(message.chat.id, "Please Give Me A Text For The Logo.")
     return
 mritzme = await client.send_message(message.chat.id, "**Your Logo Is Creating. Please Wait.⏳**")
 try:
    text = get_text(message)
    LOGO_API = f"https://api.singledevelopers.net/logo?name={text}"
    randc = (LOGO_API)
    img = Image.open(io.BytesIO(requests.get(randc).content))
    murl = requests.get(f"https://api.singledevelopers.net/logo?name={text}").history[1].url
    logogend = f"**Logo Generated Successfully**"
    fname = "Sally.png"
    img.save(fname, "png")
    await mritzme.edit(logogend, disable_web_page_preview=True)
    await client.send_photo(message.chat.id, photo=murl, caption = f"**Made By @NipunGroupBot 🌹**")
    if os.path.exists(fname):
            os.remove(fname)
 except Exception as e:
    await client.send_message(message.chat.id, f'Error, Report @TheSallySupport, {e}')
   

# ==================== HQ Logo ====================
   
@pbot.on_message(filters.command(["hqlogo", "logohq"]) & ~filters.edited & ~filters.bot)
async def hqlogo(client, message):
 FSub = await ForceSub(client, message)
 if FSub == 400:
        return            
 quew = get_text(message)
 if not quew:
     await client.send_message(message.chat.id, "Please Give Me A Text For The Logo.")
     return
 mritzme = await client.send_message(message.chat.id, "**Your Logo Is Creating. Please Wait.⏳**")
 try:
    text = get_text(message)
    LOGO_API = f"https://api.singledevelopers.net/logohq?name={text}"
    randc = (LOGO_API)
    img = Image.open(io.BytesIO(requests.get(randc).content))
    murl = requests.get(f"https://api.singledevelopers.net/logohq?name={text}").history[1].url
    logogend = f"**Logo Generated Successfully**"
    fname = "Sally.png"
    img.save(fname, "png")
    await mritzme.edit(logogend, disable_web_page_preview=True)
    await client.send_photo(message.chat.id, photo=murl, caption = f"**Made By @NipunGroupBot 🌹**")
    if os.path.exists(fname):
            os.remove(fname)
 except Exception as e:
    await client.send_message(message.chat.id, f'Error, Report @TheSallySupport, {e}')
   
   
@pbot.on_message(filters.command("brandcrowd") & ~filters.edited & ~filters.bot)
async def brandcrowd(client, message):
    pablo = await client.send_message(message.chat.id,"**Logo In A Process. Please Wait.⏳**")
    Godzilla = get_text(message)
    if not Godzilla:
        await pablo.edit("Invalid Command Syntax, Please Check Help Menu To Know More!")
        return
    lmao = Godzilla.split(":", 1)
    try:
        typeo = lmao[1]
    except BaseException:
        typeo = "name"
        await pablo.edit(
             "Give name and type for logo Idiot. like `/brandcrowd Sally:Girl`")
    name = lmao[0]
    mainne(name, typeo)
    caption = "<b>Made By @NipunGroupBot ⚡️<b>"
    pate = "logo@Sally.jpg"
    await client.send_photo(message.chat.id, pate)
    try:
        os.remove(pate)
    except:
        pass
    await pablo.delete()
    
CAT_LOGO = "https://raw.githubusercontent.com/Jisan09/Files/main/backgroud/black.jpg"
CAT_FONT = "https://github.com/Jisan09/Files/blob/main/fonts/Streamster.ttf"

"""    
@pbot.on_message(filters.command("catlogo") & ~filters.edited & ~filters.bot)	
async def catlogo(client, message):
 FSub = await ForceSub(client, message)
 if FSub == 400:
        return            
 quew = get_text(message)
 if not quew:
     await client.send_message(message.chat.id, "Please Give Me A Text For The Logo.")
     return
 mritzme = await client.send_message(message.chat.id, "**Logo In A Process. Please Wait.⏳**")
 try:
    text = get_text(message)
    randc = CAT_LOGO
    img = Image.open(io.BytesIO(requests.get(randc).content))
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "red"
    shadowcolor = "red"
    randf = glob.glob("./AnkiVector/resources/Streamster.ttf")
    font = ImageFont.truetype(randf, 120)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y = ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="red", stroke_width=1, stroke_fill="red")
    fname = "catub_byAV.png"
    img.save(fname, "png")
    await mritzme.edit(logogend, disable_web_page_preview=True)
    await client.send_photo(message.chat.id, photo=murl, caption = f"**Made By @NipunGroupBot⚡ 🌹**")
    if os.path.exists(fname):
            os.remove(fname)
 except Exception as e:
    await client.send_message(message.chat.id, f'Error, Report @{SUPPORT_CHAT}, {e}')
"""
HELPSTRINGS = """
 Logo Maker
/logo [TEXT]: Create a logo
/hqlogo [TEXT]: Create a HQ logo
 
 """
__help__ = HELPSTRINGS
__funtools__ = HELPSTRINGS
__mod_name__ = "🌹Logo Maker🌹"
