import asyncio
import os
import random
import re
import textwrap
import aiofiles
import aiohttp
import time
import requests
import datetime
import sys
import config

from config import *
import numpy as np


from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
from youtubesearchpython.__future__ import VideosSearch










from pytz import timezone
from pyrogram import enums


from pytz import timezone
from pyrogram import filters
from pyrogram import Client
from typing import Union
from random import choice
from VeGaXMusic.core.call import KIM
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from VeGaXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from VeGaXMusic import app
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
###
from pyrogram import Client
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
from pyrogram.enums import ChatMembersFilter
from pyrogram import enums


from VeGaXMusic import app




from pyrogram import Client
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
from VeGaXMusic import app










from asyncio import sleep
from pyrogram import Client, filters
from pyrogram import enums, filters
from VeGaXMusic import app


from VeGaXMusic import  app

from pytz import timezone
from pyrogram import enums


from pytz import timezone
from pyrogram import filters
from pyrogram import Client
from typing import Union
from random import choice

from VeGaXMusic.core.call import KIM
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from VeGaXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from VeGaXMusic import app
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup




from PIL import Image, ImageDraw, ImageFont
from pyrogram import filters, Client, enums
from pyrogram.types import *
from typing import Union, Optional
from VeGaXMusic import app as Hiroko 





from PIL import Image





from pytz import timezone
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram import enums




from pytz import timezone
from pyrogram import enums


from pytz import timezone
from pyrogram import filters
from pyrogram import Client
from typing import Union
from random import choice
from VeGaXMusic.core.call import KIM
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from VeGaXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from VeGaXMusic import app
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
###
from pyrogram import Client
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
from pyrogram.enums import ChatMembersFilter
from pyrogram import enums


from VeGaXMusic import app



from pyrogram import filters

from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from VeGaXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from VeGaXMusic import app
from random import  choice, randint

from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton

from pyrogram.enums import ChatMemberStatus, ParseMode
from pyrogram.enums import ParseMode

from pyrogram import Client
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
from VeGaXMusic import app
from VeGaXMusic import app
from VeGaXMusic.utils.database import is_on_off


from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



from os import getenv

from dotenv import load_dotenv

load_dotenv()

OWNER_ID = getenv("OWNER_ID")

OWNER = getenv("OWNER")

SUDOERS = [OWNER_ID]





#──██████──────██████───█████████████──────██████████████───████████████████────
#──██──██──────██──██───██─────────██────██────────────██───██────────────██────
#──██──██──────██──██───██──█████████───██───████████████───██───███████──██────
#──██──██──────██──██───██──██──────────██──██──────────────██───██───██──██────
#──██──██──────██──██───██──██──────────██──██──────────────██───██───██──██────
#──██──██──────██──██───██──██──────────██──██──────────────██───██───██──██────
#──██──██──────██──██── ██──██──────────██──██──────────────██───██───██──██───
#──██──██──────██──██───██──█████████───██──██───███████────██───███████──██────
#──██───██────██───██───██─────────██───██──██───██────██───██────────────██────
#───██───██──██───██────██──█████████───██──██───████──██───██───███████──██────
#────██───████───██─────██──██──────────██──██─────██──██───██───██───██──██────
#─────██───██───██──────██──██──────────██───██────██──██───██───██───██──██────
#──────██──────██───────██──██───────────██───██───██──██───██───██───██──██────
#───────██────██────────██──█████████─────██──███████──██───██───██───██──██────
#────────██──██─────────██─────────██──────██─────────██────██───██───██──██────
#─────────████──────────█████████████───────████████████────███████───██████────
#───────────────────────────────────────────────────────────────────────────────
# ̷𝖾𝙙𝙚𝙥𝙡𝙤𝙮𝙚𝙙 𝙨𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮
# (2024-2025) 𝙗𝙮: @𝙏𝙊𝙋𝙑𝙀𝙂𝘼
# 𝙂𝙧𝙚𝙚𝙩𝙞𝙣𝙜𝙨 𝙛𝙧𝙤𝙢 : 𝙑𝙚𝙂𝙖




def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj




#مطور البوت ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#مطور البوت ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

get_font = lambda font_size, font_path: ImageFont.truetype(font_path, font_size)
resize_text = (
    lambda text_size, text: (text[:text_size] + "...").upper()
    if len(text) > text_size
    else text.upper()
)


async def get_userideeboo_img2(
    bg_path: str,
    font_path: str,
    user_id: Union[int, str],
    username: Union[int, str],
    user: Union[int, str],
    user_name: Union[int, str],
    profile_path: Optional[str] = None
):
    bg = Image.open(bg_path)

    if profile_path:
        img = Image.open(profile_path)
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.pieslice([(0, 0), img.size], 0, 360, fill=255)

        circular_img = Image.new("RGBA", img.size, (0, 0, 0, 0))
        circular_img.paste(img, (0, 0), mask)
        resized = circular_img.resize((400, 400))
        bg.paste(resized, (440, 160), resized)

    img_draw = ImageDraw.Draw(bg)

    img_draw.text(
        (529, 627),
        text=str(user_id).upper(),
        font=get_font(46, font_path),
        fill=(255, 255, 255),
    )

    path = f"./userinfo_img_{user_id}.png"
    bg.save(path)
    return path



def make_col():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


def truncate(text):
    list = text.split(" ")
    text1 = ""
    text2 = ""
    for i in list:
        if len(text1) + len(i) < 30:
            text1 += " " + i
        elif len(text2) + len(i) < 30:
            text2 += " " + i

    text1 = text1.strip()
    text2 = text2.strip()
    return [text1, text2]


def get_userideeboo_img(
    bg_path: str,
    font_path: str,
    user_id: Union[int, str],
    user: Union[int, str],
    username: Union[int, str],
    user_name: Union[int, str],
    profile_path: Optional[str] = None
):
    try:
            if os.path.isfile(f"cache/{user_id}.jpg"):
               return profile_path
            youtube = Image.open(profile_path)
            image1 = changeImageSize(1280, 720, youtube)
            image2 = image1.convert("RGBA")
            background = image2.filter(filter=ImageFilter.BoxBlur(5))
            enhancer = ImageEnhance.Brightness(background)
            background = enhancer.enhance(0.6)
            image2 = background

            circle = Image.open("assets/kamall.png")

            # changing circle color
            im = circle
            im = im.convert("RGBA")
            color = make_col()

            data = np.array(im)
            black, lead, blue, alpha = data.T

            white_areas = (black == 150) & (blue == 150) & (lead == 150)
            data[..., :-1][white_areas.T] = color

            im2 = Image.fromarray(data)
            circle = im2
            # done

            image3 = image1.crop((280, 0, 1000, 720))
            lum_img = Image.new("L", [720, 720], 0)
            draw = ImageDraw.Draw(lum_img)
            draw.pieslice([(0, 0), (720, 720)], 0, 360, fill=255, outline="white")
            img_arr = np.array(image3)
            lum_img_arr = np.array(lum_img)
            final_img_arr = np.dstack((img_arr, lum_img_arr))
            image3 = Image.fromarray(final_img_arr)
            image3 = image3.resize((600, 600))

            image2.paste(image3, (50, 70), mask=image3)
            image2.paste(circle, (0, 0), mask=circle)

            # fonts
            font1 = ImageFont.truetype("assets/font2.ttf", 30)
            font2 = ImageFont.truetype("assets/font2.ttf", 70)
            font3 = ImageFont.truetype("assets/font2.ttf", 40)
            font4 = ImageFont.truetype("assets/font2.ttf", 35)

            image4 = ImageDraw.Draw(image2)
            image4.text(
                (670, 150),
                "DeV BoT",
                fill="white",
                font=font2,
                stroke_width=2,
                stroke_fill="red",
                align="left",
            )

            # description
            username = f"USER DeV : @{username} "
            user_id = f" ID DeV : {user_id}"
            name = f"CHANNEL : @kafra_wi_1 "

            image4.text((670, 450), text=user_id, fill="white", font=font4, stroke_width=2, stroke_fill="black", align="left")
            image4.text(
               (670, 500), text=username, fill="white", font=font4, stroke_width=2, stroke_fill="black", align="left"
            )
            image4.text(
               (670, 550), text=name, fill="white", font=font4, stroke_width=2, stroke_fill="black", align="left"
            )

            image2 = ImageOps.expand(image2, border=20, fill=make_col())
            image2 = image2.convert("RGB")
            image2.save(f"cache/{user_id}.jpg")
            file = f"cache/{user_id}.jpg"
            return file
    except Exception as e:
        print(e)
        return YOUTUBE_IMG_URL


@app.on_message(filters.command(["المطور", "مطور", "مطور البوت"], ""), group=7728230165)
async def dev(client: Client, message: Message):
    bot_username = client.me.username
    msg = await message.reply("🤖")
    await sleep(1)
    await msg.delete()
    user = await client.get_chat(OWNER_ID)
    name = user.first_name
    username = user.username
    bio = user.bio
    user_id = user.id
    photo = None  # Define photo variable outside the conditional block

    if user.photo:
        photo = user.photo.big_file_id
        photo = await client.download_media(photo)
        link = f"https://t.me/{message.chat.username}"
        title = message.chat.title if message.chat.title else message.chat.first_name

        chat_title = f"<b>╭◉ɴᴧᴍᴇ : {message.from_user.mention} \n│᚜◉ᴄʜᴀᴛ ɴᴧᴍᴇ : {title}" if message.from_user else f"╰◉ᚐᴄʜᴀᴛ ɴᴧᴍᴇ: {message.chat.title}</b>"
        
        try:
            await client.send_message(username, f"<b><blockquote> ˚‧SHEIKH˳+</b></blockquote>\n<b><blockquote>عـزيزي المطور هناك شخص يريدك</b></blockquote>\n<b><blockquote>{chat_title}</b></blockquote>\n<b><blockquote>╰◉ᚐᴄʜᴀᴛ ɪᴅ : {message.chat.id}</b></blockquote>",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
        except:
            pass
    
    if photo:  # Check if photo is available before processing
        welcome_photo = get_userideeboo_img(
            bg_path="assets/userinfo.png",
            font_path="assets/hiroko.ttf",
            user_id=user.id,
            user=user.username,
            username=user.username,
            user_name=user.first_name,
            profile_path=photo,
        )
        await message.reply_photo(photo=welcome_photo,
            caption=f"<b><blockquote>⭓ᴅᴇᴠ✘ʙᴏᴛ♪</b></blockquote>\n\n<b><blockquote>╭◉ᚐᴅᴇᴠ ɴᴧᴍᴇ : {name}\n│᚜◉ ᴅᴇᴠ ᴜsᴇꝛ : @{username}\n╰◉ᚐʙɪᴏ : {bio}</b></blockquote>",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
    else:
        await message.reply_text(f"<b><blockquote>˚‧SHEIKH˳+</b></blockquote>\n\n<b><blockquote>╭◉ᚐᴅᴇᴠ ɴᴧᴍᴇ : {name}\n│᚜◉ ᴅᴇᴠ ᴜsᴇꝛ : @{username}\n╰◉ᚐʙɪᴏ : {bio}</b></blockquote>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(name, url=f"https://t.me/{message.from_user.username}")],]))
    
    try:
        if photo:
            os.remove(photo)  # Remove the downloaded photo if available
    except:
        pass






#علي العراقي ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#علي العراقي ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


    
@app.on_message(filters.command(["جاك"], "") & filters.group, group=7728230165)
async def handle_user_info(client, message):
    user = await client.get_chat("Cr7s7uii")
    msg = await message.reply("😈")
    await sleep(2)
    await msg.delete()
    name = user.first_name
    if user.photo:
        photo = await app.download_media(user.photo.big_file_id)
        await message.reply_photo(photo, caption=f"<blockquote><b>╭◉ᚐɴᴧᴍᴇ : {name}\n│᚜◉ᚐᴜsᴇꝛ : @{user.username}\n│᚜◉ᚐɪᴅ : <code>{user.id}</code>\n╰◉ᚐʙɪᴏ : {user.bio}</b></blockquote>", 
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            name, url=f"https://t.me/{user.username}")    
                    ],
                ]
            ),
        )
    else:
        await message.reply_text(f"<blockquote><b>╭◉ᚐɴᴧᴍᴇ : {name}\n│᚜◉ᚐᴜsᴇꝛ : @{user.username}\n│᚜◉ᚐɪᴅ : <code>{user.id}</code>\n╰◉ᚐʙɪᴏ : {user.bio}</b></blockquote>", 
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            name, url=f"https://t.me/{message.from_user.username}"
                        )
                    ]
                ]
            )
        )    


@app.on_message(filters.command(["ꜱᴏʜᴀɪʟᴀ","سوهيلا","سهيله","سوسو"], "") & filters.group, group=7728230165)
async def handle_user_info(client, message):
    user = await client.get_chat("Q_Sohaila")
    msg = await message.reply("❤️‍🔥")
    await sleep(2)
    await msg.delete()
    name = user.first_name
    if user.photo:
        photo = await app.download_media(user.photo.big_file_id)
        await message.reply_photo(photo, caption=f"<blockquote><b>╭◉ᚐɴᴧᴍᴇ : {name}\n│᚜◉ᚐᴜsᴇꝛ : @{user.username}\n│᚜◉ᚐɪᴅ : <code>{user.id}</code>\n╰◉ᚐʙɪᴏ : {user.bio}</b></blockquote>", 
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            name, url=f"https://t.me/{user.username}")    
                    ],
                ]
            ),
        )
    else:
        await message.reply_text(f"<blockquote><b>╭◉ᚐɴᴧᴍᴇ : {name}\n│᚜◉ᚐᴜsᴇꝛ : @{user.username}\n│᚜◉ᚐɪᴅ : <code>{user.id}</code>\n╰◉ᚐʙɪᴏ : {user.bio}</b></blockquote>", 
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            name, url=f"https://t.me/{message.from_user.username}"
                        )
                    ]
                ]
            )
        )    



##توكسي ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
##توكسي ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.command(["جاكّ","ꜰᴏx","جاكيي"], ""), group=82036)
async def handle_user_info(client, message):
    user = await client.get_chat("DevVeGa")
    msg = await message.reply("😈")
    await sleep(2)
    await msg.delete()
    name = user.first_name
    if user.photo:
        photo = await app.download_media(user.photo.big_file_id)
        await message.reply_photo(photo, caption=f"<blockquote><b>╭◉ᚐɴᴧᴍᴇ : {name}\n│᚜◉ᚐᴜsᴇꝛ : @{user.username}\n│᚜◉ᚐɪᴅ : <code>{user.id}</code>\n╰◉ᚐʙɪᴏ : {user.bio}</b></blockquote>", 
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            name, url=f"https://t.me/{user.username}")    
                    ],
                ]
            ),
        )
    else:
        await message.reply_text(f"<blockquote><b>╭◉ᚐɴᴧᴍᴇ : {name}\n│᚜◉ᚐᴜsᴇꝛ : @{user.username}\n│᚜◉ᚐɪᴅ : <code>{user.id}</code>\n╰◉ᚐʙɪᴏ : {user.bio}</b></blockquote>", 
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            name, url=f"https://t.me/{message.from_user.username}"
                        )
                    ]
                ]
            )
        )    



@app.on_message(filters.command(["مادو","ᴍᴀᴅᴏ","مادو"], ""), group=82036)
async def handle_user_info(client, message):
    user = await client.get_chat("wwvvwt")
    msg = await message.reply("😈")
    await sleep(2)
    await msg.delete()
    name = user.first_name
    if user.photo:
        photo = await app.download_media(user.photo.big_file_id)
        await message.reply_photo(photo, caption=f"<blockquote><b>╭◉ᚐɴᴧᴍᴇ : {name}\n│᚜◉ᚐᴜsᴇꝛ : @{user.username}\n│᚜◉ᚐɪᴅ : <code>{user.id}</code>\n╰◉ᚐʙɪᴏ : {user.bio}</b></blockquote>", 
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            name, url=f"https://t.me/{user.username}")    
                    ],
                ]
            ),
        )
    else:
        await message.reply_text(f"<blockquote><b>╭◉ᚐɴᴧᴍᴇ : {name}\n│᚜◉ᚐᴜsᴇꝛ : @{user.username}\n│᚜◉ᚐɪᴅ : <code>{user.id}</code>\n╰◉ᚐʙɪᴏ : {user.bio}</b></blockquote>", 
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            name, url=f"https://t.me/{message.from_user.username}"
                        )
                    ]
                ]
            )
        )    
        


@app.on_message(filters.command(["كفراوي","ᴋᴀꜰʀᴀᴡɪ","كفر"], ""), group=82036)
async def handle_user_info(client, message):
    user = await client.get_chat("KA_FRA_WI1")
    msg = await message.reply("😈")
    await sleep(2)
    await msg.delete()
    name = user.first_name
    if user.photo:
        photo = await app.download_media(user.photo.big_file_id)
        await message.reply_photo(photo, caption=f"<blockquote><b>╭◉ᚐɴᴧᴍᴇ : {name}\n│᚜◉ᚐᴜsᴇꝛ : @{user.username}\n│᚜◉ᚐɪᴅ : <code>{user.id}</code>\n╰◉ᚐʙɪᴏ : {user.bio}</b></blockquote>", 
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            name, url=f"https://t.me/{user.username}")    
                    ],
                ]
            ),
        )
    else:
        await message.reply_text(f"<blockquote><b>╭◉ᚐɴᴧᴍᴇ : {name}\n│᚜◉ᚐᴜsᴇꝛ : @{user.username}\n│᚜◉ᚐɪᴅ : <code>{user.id}</code>\n╰◉ᚐʙɪᴏ : {user.bio}</b></blockquote>", 
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            name, url=f"https://t.me/{message.from_user.username}"
                        )
                    ]
                ]
            )
        )    

#سوهيلا ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#سوهيلا ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓



# @app.on_message(filters.command(["سهيله","سوهيلا","سوسو"], ""), group=82637878936)
# async def handle_user_info(client, message):
    # user = await client.get_chat("S_O_HA_I_L_A")
    # msg = await message.reply("❤️")
    # await sleep(2)
    # await msg.delete()
    # name = user.first_name
    # if user.photo:
        # photo = await app.download_media(user.photo.big_file_id)
        # await message.reply_photo(photo, caption=f"<blockquote><b>╭◉ᚐɴᴧᴍᴇ : {name}\n│᚜◉ᚐᴜsᴇꝛ : @{user.username}\n│᚜◉ᚐɪᴅ : <code>{user.id}</code>\n╰◉ᚐʙɪᴏ : {user.bio}</b></blockquote>", 
            # reply_markup=InlineKeyboardMarkup(
                # [
                    # [
                        # InlineKeyboardButton(
                            # name, url=f"https://t.me/{user.username}")    
                    # ],
                # ]
            # ),
        # )
    # else:
        # await message.reply_text(f"<blockquote><b>╭◉ᚐɴᴧᴍᴇ : {name}\n\n│᚜◉ᚐᴜsᴇꝛ : @{user.username}\n│᚜◉ᚐɪᴅ : <code>{user.id}</code>\n╰◉ᚐʙɪᴏ : {user.bio}</b></blockquote>", 
            # reply_markup=InlineKeyboardMarkup(
                # [
                    # [
                        # InlineKeyboardButton(
                            # name, url=f"https://t.me/{message.from_user.username}"
                        # )
                    # ]
                # ]
            # )
        # )




@app.on_message(filters.command(["دعم","رئيس","تنفيذي","هكر"], ""), group=8236)
async def handle_user_info(client, message):
    user = await client.get_chat("CeoVega")
    name = user.first_name
    if user.photo:
        photo = await app.download_media(user.photo.big_file_id)
        await message.reply_photo(photo, caption=f"<blockquote><b>╭◉ᚐɴᴧᴍᴇ : {name}\n│᚜◉ᚐᴜsᴇꝛ : @{user.username}\n│᚜◉ᚐɪᴅ : <code>{user.id}</code>\n╰◉ᚐʙɪᴏ : {user.bio}</b></blockquote>", 
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            name, url=f"https://t.me/{user.username}")    
                    ],
                ]
            ),
        )
    else:
        await message.reply_text(f"<blockquote><b>╭◉ᚐɴᴧᴍᴇ : {name}\n\n│᚜◉ᚐᴜsᴇꝛ : @{user.username}\n│᚜◉ᚐɪᴅ : <code>{user.id}</code>\n╰◉ᚐʙɪᴏ : {user.bio}</b></blockquote>", 
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            name, url=f"https://t.me/{message.from_user.username}"
                        )
                    ]
                ]
            )
        )





@app.on_message(filters.command(["بطه","كوكي","كتاليا","طبف","ᴋᴀᴛᴀʟɪᴀ"], ""), group=828636)
async def handle_user_inf(client, message):
    user = await client.get_chat("KATAVEGA")
    name = user.first_name
    if user.photo:
        photo = await app.download_media(user.photo.big_file_id)
        await message.reply_photo(photo, caption=f"<blockquote><b>╭◉ᚐɴᴧᴍᴇ : {name}\n│᚜◉ᚐᴜsᴇꝛ : @{user.username}\n│᚜◉ᚐɪᴅ : <code>{user.id}</code>\n╰◉ᚐʙɪᴏ : {user.bio}</b></blockquote>", 
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            name, url=f"https://t.me/{user.username}")    
                    ],
                ]
            ),
        )
    else:
        await message.reply_text(f"<blockquote><b>╭◉ᚐɴᴧᴍᴇ : {name}\n\n│᚜◉ᚐᴜsᴇꝛ : @{user.username}\n│᚜◉ᚐɪᴅ : <code>{user.id}</code>\n╰◉ᚐʙɪᴏ : {user.bio}</b></blockquote>", 
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            name, url=f"https://t.me/{message.from_user.username}"
                        )
                    ]
                ]
            )
        )






# وقت او الساعه ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# وقت او الساعه ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.command(["الساعه","الوقت","تاريخ","وقت"], ""), group=88000666556413218)
async def khalid(client: Client, message: Message):
    egypt_tz = timezone('Egypt')
    current_time = datetime.datetime.now(egypt_tz).strftime("%H:%M:%S")    
    date = message.date.strftime("%Y-%m-%d")
    await message.reply_video(
        video=f"https://telegra.ph/file/6594430ed5f7209f39a36.mp4",
        caption=f"""<b><blockquote> ˚‧SHEIKH˳+</b></blockquote>\n\n<b><blockquote>عـزيـزي :{message.from_user.mention}</b></blockquote>\n<blockquote> الـيك الان الوقت والتاريخ بتوقيت القاهره\n\n╭◉ᚐᴅᴀᴛᴇ : {date}\n╰◉ᚐᴛɪᴍᴇ : <code>{current_time}</code></b></blockquote>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [                   
                    InlineKeyboardButton(
                        "⸢ꜱʜᴇɪᴋʜ⸥", url=f"https://t.me/kafra_wi_1"),
                ],
            ]
        ),
    )
    
    
    


@app.on_message(filters.command(["جاك","مطور جاكو","صاحب سورس جاكو","جاكي","مطور السورس","𝐉𝐀𝐊","ᴊᴀᴋ"], ""), group=11)
async def yas(client, message):
    usr = await client.get_chat("wwvvwt")
    name = usr.first_name
    if usr.photo:
        photo = await app.download_media(usr.photo.big_file_id)
        photo=photo
        await message.reply_photo(photo=photo, caption=f"<blockquote><b>╭◉ᚐɴᴧᴍᴇ :  {name}\n│᚜◉ᚐᴜsᴇꝛ : @{usr.username}\n│᚜◉ᚐɪᴅ : <code>{usr.id}</code>\n╰◉ᚐʙɪᴏ : {usr.bio}</b></blockquote>", 
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(name, url=f"https://t.me/{usr.username}")]]),
        )
    else:
        await message.reply_text(f"<blockquote><b>╭◉ᚐɴᴧᴍᴇ : {name}\n│᚜◉ᚐᴜsᴇꝛ: @{usr.username}\n│᚜◉ᚐɪᴅ : <code>{usr.id}</code>\n╰◉ᚐʙɪᴏ : {usr.bio}</b></blockquote>", 
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(name, url=f"https://t.me/{message.from_user.username}")]]),
        )



@app.on_chat_member_updated(filters=lambda _, response: response.new_chat_member, group=65443)
async def welcome_devs(_, response: ChatMemberUpdated):
    dev_ids = [7728230165, 7728230165, 7728230165, 7728230165]
    if response.from_user.id in dev_ids and response.new_chat_member.status == ChatMemberStatus.MEMBER:
        info = await app.get_chat(response.from_user.id)
        name = info.first_name
        username = info.username
        bio = info.bio
        markup = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(name, url=f"https://t.me/{username}")],
                [
                    InlineKeyboardButton(
                        "ꜱʜᴇɪᴋʜ", url=SUPPORT_CHANNEL
                    ),
                ],
            ]
        )
        await app.download_media(info.photo.big_file_id, file_name=os.path.join("downloads", "developer.jpg"))
        await app.send_photo(
            chat_id=response.chat.id,
            reply_markup=markup,
            photo="downloads/developer.jpg", 
            caption=f"<blockquote><b> ✘ᴍᴜsɪᴄ | ꜱʜᴇɪᴋʜ⋆\n╮◉ نورتني » {name}\n╯◉ صاحب سورس جاكو</b></blockquote>"
        )

