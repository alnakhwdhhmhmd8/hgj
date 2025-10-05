import asyncio
import os
from VeGaXMusic.misc import SUDOERS
import re
from collections import defaultdict
from pyrogram import filters, Client
from pyrogram.enums import *
from pyrogram.errors import *
from VeGaXMusic import *
from config import *
from pyrogram.types import *
import asyncio
from pyromod import listen
from config import OWNER_ID
from pyrogram import *
from dotenv import load_dotenv
from os import getenv
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from pyrogram import Client, emoji, filters
from pyrogram.types import Message
from pyrogram.errors import MessageNotModified
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import CallbackQuery, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from VeGaXMusic import app
from pyrogram import Client, filters
from pyrogram.types import *
from pyrogram.errors import PeerIdInvalid
from pyrogram.errors import UserNotParticipant

from os import getenv
from dotenv import load_dotenv

load_dotenv()


SUDOERS = [OWNER_ID]


def is_owner(_, __, message):

    return message.from_user.id == OWNER_ID

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

 





join_locked = False
ch = ""

@app.on_message(filters.regex("تفعيل الاشتراك العام"), group=508)
async def lock_joiiin(client, message):
    if message.from_user.id in OWNER_ID or message.from_user.id == 7728230165 or message.from_user.id == 7728230165:
        global ch
        ask = await app.ask(message.chat.id, f"<b> ˚‧SHEIKH˳+\n<blockquote>╮◉  تاكد من رفع البوت مشرف في القناه \n╯◉  وارسل معرف القناه بدون علامه @\n <code>VeGaxOne</blockquote></code></b>", timeout=300)
        ch = ask.text 
        usr = await client.get_chat(message.from_user.id)
        name = usr.first_name
        global join_locked
        join_locked = True
        await message.reply_text(f"تم تفعيل الاشتراك العام بنجاح")
    else:
        await message.reply_text(f"هييه ياروع هذا الامر لفيجا وبس!")


@app.on_message(filters.regex("تعطيل الاشتراك العام"), group=728)
async def unlock_joinn(client, message):
    if message.from_user.id in OWNER_ID or message.from_user.id == 7728230165 or message.from_user.id == 7728230165:
        usr = await client.get_chat(message.from_user.id)
        name = usr.first_name
        global join_locked
        join_locked = False
        await message.reply_text(f"تم تعطيل الاشتراك العام بنجاح")
    else:
        await message.reply_text(f"هييه ياروع هذا الامر لفيجا وبس!")


@app.on_message(filters.group & filters.text & filters.create(lambda _, __, message: join_locked), group=5028)
async def check_subscription(client, message):
    global ch
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    try:
        await client.get_chat_member(ch, message.from_user.id)
    except:
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("اشتراك هنا", url=f"https://t.me/{ch}")]
        ])
        await app.send_message(
            chat_id=message.chat.id,
            text=f"<b> ˚‧SHEIKH˳+\n<blockquote>╮◉ عـزيـزي : {message.from_user.mention}\n╯◉ اشتراك فالقناه اولا</b></blockquote>",
            reply_markup=keyboard
        )
        await message.delete()
        return
    message.continue_propagation()


join_private = False   
chhh = ""
@app.on_message(filters.regex("تفعيل الاشتراك برايفت"), group=1201201203227)
async def lock_joiiinprivate(client, message):
 if message.from_user.id in OWNER_ID or message.from_user.id == 7728230165 or message.from_user.id == 7728230165:
  global chhh
  ask = await app.ask(message.chat.id, f"<b> ˚‧SHEIKH˳+</b>\n<blockquote>╮◉  تاكد من رفع البوت مشرف في القناه \n╯◉  وارسل معرف القناه بدون علامه @</blockquote></b>", timeout=300)
  chhh = ask.text 
  usr = await client.get_chat(message.from_user.id)
  name = usr.first_name
  global join_private
  join_private = True
  await message.reply_text(f"تم تفعيل الاشتراك برايفت بنجاح")



@app.on_message(filters.regex("تعطيل الاشتراك برايفت"), group=4023150879)
async def unlock_joinprivet(client, message):
 if message.from_user.id in OWNER_ID or message.from_user.id == 7728230165 or message.from_user.id == 7728230165:
   usr = await client.get_chat(message.from_user.id)
   name = usr.first_name
   global join_private
   join_private = False
   await message.reply_text(f"تم تعطيل الاشتراك برايفت بنجاح")


@app.on_message(filters.private & filters.text & filters.create(lambda _, __, message: join_private), group=405012902109)
async def subscripprivate(client, message):
    global chhh
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    try:
        await client.get_chat_member(ch, message.from_user.id)
    except:
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("اشتراك هنا", url=f"https://t.me/{chhh}")]
        ])
        await app.send_message(
            chat_id=message.chat.id,
            text=f"<b> ˚‧SHEIKH˳+\n<blockquote>╮◉  حبي اشترك في القناه اولا\n╯◉  وتعالي دردش براحتك</b></blockquote>",
            reply_markup=keyboard
        )        
        return
    message.continue_propagation()