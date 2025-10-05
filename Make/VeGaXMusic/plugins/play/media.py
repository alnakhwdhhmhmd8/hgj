import asyncio
import os
import time
import requests
import random
import aiohttp
from config import *
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from VeGaXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from VeGaXMusic import app
from telegraph import upload_file
from asyncio import gather
from random import  choice, randint




# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂[𝗩.𝗘.𝗚.𝗔]▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
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
# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂[𝗩.𝗘.𝗚.𝗔]▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
# ̷𝖾𝙙𝙚𝙥𝙡𝙤𝙮𝙚𝙙 𝙨𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮
# (2024-2025) 𝙗𝙮: @𝙏𝙊𝙋𝙑𝙀𝙂𝘼
# 𝙂𝙧𝙚𝙚𝙩𝙞𝙣𝙜𝙨 𝙛𝙧𝙤𝙢 : 𝙑𝙚𝙂𝙖

 

from pyrogram import Client, filters, enums





@app.on_message(filters.command(["m"], ""), group=509)
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        return await message.reply("Please Reply to Photo or Video")
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (replied.video and replied.video.file_name.endswith(".mp4") and replied.video.file_size <= 5242880)
        or (replied.document and replied.document.file_name.endswith((".jpg", ".jpeg", ".png", ".gif", ".mp4")) and replied.document.file_size <= 5242880)):
        return await message.reply("◍ عذرا هذا العنصر غير مدعوم\n√")
    download_location = await app.download_media(message=message.reply_to_message,file_name="root/downloads/")
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(text=document)
    else:
        await message.reply(f"`https://telegra.ph{response[0]}`", parse_mode=enums.ParseMode.MARKDOWN)
    finally:
        os.remove(download_location)


#البايو ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#البايو ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

biof = []
@app.on_message(filters.command(["قفل البايو", "تعطيل البايو"], ""), group=509)
async def iddlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in biof:
        return await message.reply_text(" حجي انت تم معطل من قبل")
      biof.append(message.chat.id)
      return await message.reply_text(" تم تعطيل البايو بنجاح")
   else:
      return await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")

@app.on_message(filters.command(["فتح البايو", "تفعيل البايو"], ""), group=678)
async def biopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if not message.chat.id in biof:
        return await message.reply_text(" حجي انت البايو مفعل من قبل ")
      biof.remove(message.chat.id)
      return await message.reply_text("تم فتح  البايو بنجاح")
   else:
      return await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")


@app.on_message(filters.command(["بايو", "البايو"], ""), group=444)
async def biio(client, message):
    if message.chat.id in biof:
        return 
    nq = await client.get_chat(message.from_user.id)
    bio = nq.bio if nq.bio else "لا يوجد بايو للحساب..؟"
    await message.reply_text(bio)






 
#تحويل الصور ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#تحويل الصور ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

 
@app.on_message(filters.command(["حول صوره", "تحويل الصوره"], ""), group=555)
async def sticker_photo(client: Client, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("الرد على ملصق.")
    if not reply.sticker:
        return await message.reply("الرد على ملصق.")
    m = await message.reply("يتم المعالجه..")
    f = await reply.download(f"{reply.sticker.file_unique_id}.png")
    await gather(*[message.reply_photo(f),message.reply_document(f)])
    await m.delete()
    os.remove(f)

    

#تحويل صوره لملصق ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#تحويل صوره لملصق ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

@app.on_message(filters.command(["حول ملصق"], ""), group=5267)
async def sticker_photo(client: Client, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("الرد على صورة.")
    if not reply.photo:
        return await message.reply("الرد على صورة.")
    m = await message.reply("💣")
    photo = reply.photo.file_id
    file_path = await client.download_media(photo)
    await client.send_sticker(
        chat_id=message.chat.id,
        sticker=file_path
    )
    await m.delete()
    os.remove(file_path)





@app.on_message(filters.command(['استك'], prefixes=""), group=1282)
async def sticker_id(_, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("عزيزي قم برد علي الاستيكر")
    if not reply.sticker:
        return await message.reply("عزيزي قم برد علي الاستيكر")
    await message.reply_text(f"<code>{reply.sticker.file_id}</code>\n\n<b>عزيزي هذا هو ايدي الاستيكر المطلوب:</b>")



#▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▇▇▒▒▇▇▇▇▇▇▒▒▇▇▇▇▇▇▇▒▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▇▇▒▒▒▒▒▒▒▒▒▇▇▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▇▇▒▒▒▒▒▒▒▇▇▒▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▇▇▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▇▇▒▒▒▒▒▇▇▒▒▒▒▒▇▇▇▇▇▇▒▒▇▇▒▒▒▒▒▒▒▒▒▒▇▇▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▇▇▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▇▇▇▇▇▒▒▇▇▇▇▇▇▇▇▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▇▇▒▇▇▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▇▇▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▇▇▇▒▒▒▒▒▒▒▒▇▇▇▇▇▇▒▒▇▇▇▇▇▇▇▇▇▇▒▒▇▇▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▇▇▇▇▒▒▒▒▒▒▒▒▇▇▇▇▇▒▒▆▆▒▒▒▒▒▒▒▒▇▇▒▒▇▇▇▇▇▇▇▇▜▒▒▇▇▒▒▆▆▆▆▆▆▆▆▆
#▒▇▇▒▒▒▇▇▒▒▒▇▇▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒▒▇▇▒▒▇▇▇▒▒▒▒▒▒▒▒▇▇▒▒▆▆▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▇▇▇▒▒▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒▒▇▇▒▒▒▒▇▇▇▒▒▒▒▒▒▇▇▒▒▆▆▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▇▇▇▒▒▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▇▇▇▇▇▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▇▇▇▒▒▒▒▒▇▇▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▇▇▇▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▇▇▇▒▒▒▒▒▇▇▒▒▒▒▒▇▇▒▒▒▇▇▒▒▒▒▒▒▒▒▇▇▇▒▒▒▒▇▇▒▒▆▆▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▇▇▇▇▇▒▒▒▒▙▇▇▇▇▇▇▉▒▒▒▒▇▇▒▒▇▇▇▇▇▇▇▇▇
#▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    