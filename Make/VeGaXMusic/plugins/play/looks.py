import asyncio
import re
import time
import requests
import aiohttp
import asyncio
import re
from pyrogram import Client, filters
from datetime import datetime
from pyrogram import enums
from config import OWNER_ID
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from VeGaXMusic import app
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import *
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.enums import ChatMembersFilter
import asyncio
import requests
from VeGaXMusic import app
from VeGaXMusic.core.call import KIM
from VeGaXMusic.utils.database import set_loop
from VeGaXMusic.utils.decorators import AdminRightsCheck
from datetime import datetime
from config import BANNED_USERS, PING_IMG_URL, lyrical, START_IMG_URL, MONGO_DB_URI, OWNER_ID
from VeGaXMusic.utils import bot_sys_stats
from VeGaXMusic.utils.decorators.language import language
import random
import time
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from aiohttp import ClientSession
from traceback import format_exc
import config
import re

import asyncio
import random
import time
from datetime import datetime, timedelta

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.raw import types
from pyrogram import enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from VeGaXMusic import app
from config import OWNER_ID
from config import BANNED_USERS, MUSIC_BOT_NAME

from VeGaXMusic.utils.database import  get_client

from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton

from pyrogram import Client, filters
from pyrogram import filters
from datetime import datetime
from pyrogram import enums
from VeGaXMusic.misc import SUDOERS
from config import OWNER_ID
from config import BANNED_USERS
from config import BANNED_USERS, OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import CallbackQuery, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.enums import ChatMemberStatus, ParseMode
from VeGaXMusic import app
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import *
from pyrogram.enums import ChatMembersFilter
from telegraph import upload_file
from asyncio import gather
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import *
from pyrogram.enums import ChatMembersFilter
import asyncio

from pyrogram.enums import ParseMode

from VeGaXMusic import app
from VeGaXMusic.utils.database import is_on_off
from config import LOG_GROUP_ID



from pyrogram import filters
from pyrogram import Client
from VeGaXMusic.core.call import KIM
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from VeGaXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from VeGaXMusic import app
from telegraph import upload_file
from asyncio import gather



# def is_owner(_, __, message):
#     return message.from_user.id == OWNER_ID



def is_owner(_, __, message):
    if message.from_user is not None:
        return message.from_user.id == OWNER_ID
    else:
        return False




def is_owner(_, __, message):
    return getattr(message, 'from_user', None) is not None and message.from_user.id == OWNER_ID


chat_locked = False
mention_locked = False
video_locked = False
link_locked = False
sticker_locked = False
forward_locked = False
photo_locked = False
saap_locked = False
kalays_locked = False
sound_locked = False
voice_locked = False



dev_ids = [8122544723, 7654641648, 7728230165, 7728230165]

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

 


import string
import lyricsgenius as lg
from collections import defaultdict
from pyrogram.types import CallbackQuery, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import (InlineKeyboardButton, ChatPermissions, InlineKeyboardMarkup, Message, User)
from pyrogram import Client, filters
from VeGaXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
import sys
import os
from pyrogram.errors import PeerIdInvalid
from os import getenv
from VeGaXMusic.misc import SUDOERS
from pyrogram import filters, Client
from telegraph import upload_file
from dotenv import load_dotenv
from VeGaXMusic.utils.database import (set_cmode,get_assistant) 
from VeGaXMusic.utils.decorators.admins import AdminActual
from VeGaXMusic import app
unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)

mute_permission = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False, 
    can_send_other_messages=False,
    can_send_polls=False,
    can_add_web_page_previews=False,
    can_change_info=False,
    can_pin_messages=False,
    can_invite_users=True,
)

welcome_enabled = True




chat_locked = False
channel_locked = False
mention_locked = False
video_locked = False
link_locked = False
sticker_locked = False
smsim_locked = False
forward_locked = False
reply_locked = False
photo_locked = False
saap_locked = False
rdods_locked = False


def is_owner(_, __, message):

    return message.from_user.id == OWNER_ID



@app.on_chat_member_updated(group=55551334142424242425)
async def welcome(client, chat_member_updated: ChatMemberUpdated):
    try:
        if chat_member_updated.new_chat_member.status == ChatMemberStatus.BANNED:
            kicked_by = chat_member_updated.new_chat_member.restricted_by
            user = chat_member_updated.new_chat_member.user
            if kicked_by is not None and kicked_by.is_bot:
                message = f"<b><blockquote>تم طرد احد المشرفين:</b></blockquote>\n<b><blockquote>╮◉ المشرف هذا: {user.username} ({user.first_name}) \n╯◉ تم طرده بواسطتي لانه حظر عضو</b></blockquote>"
            else:
                if kicked_by is not None:
                    message = f"<b><blockquote>╮◉ العضو: [{user.first_name}](tg://user?id={user.id})\n│᚜◉ تم طرده من هنا\n╯◉ بواسطة هذا المشرف: [{kicked_by.first_name}](tg://user?id={kicked_by.id})</b></blockquote>"
                    await client.ban_chat_member(chat_member_updated.chat.id, kicked_by.id)
                else:
                    message = f"<b><blockquote>╮◉ تم حظره {user.username} ({user.first_name})\n╯◉ من دردش</b></blockquote>"
            await client.send_message(chat_member_updated.chat.id, message)
    except Exception as e:
        pass
        




#رفع مطور  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#رفع مطور  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
from pyrogram import Client, filters, enums
from pyrogram.types import Message
import time

telethon_status = {}

# --- أوامر القفل والفتح ---
@app.on_message(filters.command(["قفل التليثون"], "") & filters.group, group=84934894939)
async def lock_telethon(client: Client, message: Message):
    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    
    if member.status in [enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR]:
        telethon_status[message.chat.id] = True
        await message.reply("✓ تم تعطيل استخدام التليثون في المجموعة")
    else:
        await message.reply("⚠️ هذا الأمر متاح للمشرفين فقط")

@app.on_message(filters.command(["فتح التليثون"], "") & filters.group, group=959395939449)
async def unlock_telethon(client: Client, message: Message):
    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    
    if member.status in [enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR]:
        telethon_status[message.chat.id] = False
        await message.reply("✓ تم تفعيل استخدام التليثون في المجموعة")
    else:
        await message.reply("⚠️ هذا الأمر متاح للمشرفين فقط")

# --- معالجة الرسائل الجديدة والمعدلة ---
async def check_telethon(client: Client, message: Message):
    chat_id = message.chat.id
    
    if not telethon_status.get(chat_id, False):
        return
    
    user = message.from_user
    if not user or user.id in dev_ids:
        return
    
    try:
        member = await client.get_chat_member(chat_id, user.id)
        if member.status in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]:
            return
    except:
        return
    
    is_edited = message.edit_date is not None
    starts_with_dot = message.text and message.text.startswith(".")
    
    if is_edited or starts_with_dot:
        try:
            await message.delete()
            await client.ban_chat_member(
                chat_id=chat_id,
                user_id=user.id,
                until_date=int(time.time()) + 300
            )
            await client.send_message(
                chat_id,
                f"⛔ تم حظر {user.mention} لمخالفة قواعد التليثون."
            )
        except Exception as e:
            print(f"Error: {e}")

@app.on_message(filters.group & (filters.text | filters.command) & ~filters.private)
async def handle_new_messages(client: Client, message: Message):
    await check_telethon(client, message)

@app.on_edited_message(filters.group & (filters.text | filters.command) & ~filters.private)
async def handle_edited_messages(client: Client, message: Message):
    await check_telethon(client, message)

mutaw = {}

def is_mutaw(user_id):
    return user_id in mutaw and mutaw[user_id] > 0
    
    
@app.on_message(filters.command(["رفع مطور"], ""), group=328727)
async def mutawnh(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif len(message.text.split()) > 2:
        target = message.text.split()[2]
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("<b><blockquote>لا يمكن العثور على المستخدم</b></blockquote>")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("<b><blockquote>لا يمكن العثور على المستخدم</b></blockquote>")
            return
            
            
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165 or message.from_user.id == 7728230165:
        global mutaw
        user_id = message.reply_to_message.from_user.id
        
        if user_id == message.from_user.id:
            await message.reply_text("<b><blockquote>هييه مايمديك ترفع نفسك ياروعه!!</b></blockquote>")
            return
            
        if user_id == 7728230165:
            await message.reply_text("<b><blockquote>هييه مايمديك ترفع جاك ياروعه!!</b></blockquote>")
            return
            
        if user_id == OWNER_ID:
            await message.reply_text("<b><blockquote>هييه مايمديك ترفع مطور ياروعه!!</b></blockquote>")
            return       
            
        member = await message.chat.get_member(user_id)
        
        if member.status in [ChatMemberStatus.OWNER]:
            return await message.reply("<b><blockquote>هييه مايمديك ترفع مالك اساسي ياروعه!!</b></blockquote>")

        user_id = message.reply_to_message.from_user.mention
        if user_id in mutaw:
            mutaw[user_id] += 1
            await message.reply_text(f"<b><blockquote> 「  {message.reply_to_message.from_user.mention} 」 \nصاير مطور من قبل </b></blockquote> ")
        else:
            mutaw[user_id] = 1
            chat_id = message.chat.id
            await app.send_message(chat_id, text=f"<b><blockquote>「  {message.reply_to_message.from_user.mention} 」 \nرفعته صار مطور</b></blockquote>")
    else:
        await message.reply_text("<b><blockquote>هذا الامر يخص ❪ الادمن وفوق ❫ بس</b></blockquote>")








@app.on_message(filters.command(["تنزيل مطور"], ""), group=37363828727)
async def remove_mutoruuug(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif len(message.text.split()) > 2:
        target = message.text.split()[2]
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("<b><blockquote>لا يمكن العثور على المستخدم</b></blockquote>")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("<b><blockquote>لا يمكن العثور على المستخدم</b></blockquote>")
            return
            
            
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165 or message.from_user.id == 7728230165:
        global mutaw
        user_id = message.reply_to_message.from_user.id
        
        if user_id == message.from_user.id:
            await message.reply_text("<b><blockquote>هييه مايمديك تنزل نفسك ياروعه!!</b></blockquote>")
            return
            
        if user_id == 7728230165:
            await message.reply_text("<b><blockquote>هييه مايمديك تنزل جاك ياروعه!!</b></blockquote>")
            return
            
        if user_id == OWNER_ID:
            await message.reply_text("<b><blockquote>هييه مايمديك تنزل مطور ياروعه!!</b></blockquote>")
            return       
            
        member = await message.chat.get_member(user_id)
        
        if member.status in [ChatMemberStatus.OWNER]:
            return await message.reply("<b><blockquote>هييه مايمديك تنزل مالك اساسي ياروعه!!</b></blockquote>")
            
        user_id = message.reply_to_message.from_user.mention
        if user_id in mutaw and mutaw[user_id] > 0:
            mutaw[user_id] -= 1
            await message.reply_text(f" <b><blockquote>「  {message.reply_to_message.from_user.mention} 」\nنزلته من المطور</b></blockquote>")
        else:
            chat_id = message.chat.id
            await app.send_message(chat_id, text=f" <b><blockquote>「  {message.reply_to_message.from_user.mention} 」\nمو مطور من قبل</b></blockquote>")
    else:
        await message.reply_text("<b><blockquote>هذا الامر يخص ❪ الادمن وفوق ❫ بس</b></blockquote>")        



@app.on_message(filters.command(["المطورين"], ""), group=3997663626267)
async def list_muytorsutr(client, message):
  usr = await client.get_chat(message.from_user.id)
  name = usr.first_name
  get = await client.get_chat_member(message.chat.id, message.from_user.id)
  if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165 or message.from_user.id == 7728230165:
    chat_id = message.chat.id
    mutawi = [str(user_id) for user_id, rank in mutaw.items() if rank > 0]
    if mutawi:
        mutawi_list = "\n".join(mutawi)
        await app.send_message(chat_id, text=f"<b><blockquote>قائمة المطورين:</b></blockquote>\n\n<b><blockquote>{mutawi_list}</b></blockquote>")
    else:
        await app.send_message(chat_id, text="<b><blockquote>لا يوجد مطورين حالياً</b></blockquote>")
  else:
        await message.reply_text("<b><blockquote>هذا الامر يخص ❪ الادمن وفوق ❫ بس</b></blockquote>")
        
        
        
@app.on_message(filters.command(["مسح المطورين"], ""), group=1311654481)
async def mutawytt(client, message):
  usr = await client.get_chat(message.from_user.id)
  name = usr.first_name
  get = await client.get_chat_member(message.chat.id, message.from_user.id)
  if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165 or message.from_user.id == 7728230165:
    global mutaw
    count = len(mutaw)
    chat_id = message.chat.id
    failed_count = 0
    for member in list(mutaw.keys()):
        user_id = member
        try:
            del mutaw[member]
        except Exception:
            failed_count += 1
    successful_count = count - failed_count
    if successful_count > 0:
        await message.reply_text(f"<b><blockquote>مسحت {successful_count} من المطورين</b></blockquote>")
    else:
        await message.reply_text("<b><blockquote>حجي لا يوجد مطورين ليتم مسحهم</b></blockquote>")
    if failed_count > 0:
        await message.reply_text(f"<b><blockquote>حجي فشل في مسح {failed_count}\nمن المطورين</b></blockquote>")
  else:
        await message.reply_text("<b><blockquote>هذا الامر يخص ❪ الادمن وفوق ❫ بس</b></blockquote>")



#رفع مالك ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#رفع مالك ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓



mallekan = {}

def is_malleka(user_id):
    return user_id in mallekan and mallekan[user_id] > 0

@app.on_message(filters.command(["رفع مالك"], ""), group=3191)
async def mallekann(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif len(message.text.split()) > 2:
        target = message.text.split()[2]
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("<b><blockquote>لا يمكن العثور على المستخدم</b></blockquote>")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("<b><blockquote>لا يمكن العثور على المستخدم</b></blockquote>")
            return
            
            
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165 or message.from_user.id == 7728230165:
        global mallekan
        user_id = message.reply_to_message.from_user.id
        
        if user_id == message.from_user.id:
            await message.reply_text("<b><blockquote>هييه مايمديك رفع نفسك ياروعه!!</b></blockquote>")
            return
            
        if user_id == 7728230165:
            await message.reply_text("<b><blockquote>هييه مايمديك رفع جاك ياروعه!!</b></blockquote>")
            return
            
        if user_id == OWNER_ID:
            await message.reply_text("<b><blockquote>هييه مايمديك رفع مطور ياروعه!!</b></blockquote>")
            return       

        if user_id == bot_id:
            await message.reply_text("<b><blockquote>قولي كيف ارفع نفسي ياروعه!!</b></blockquote>")
            return       
                    
            
        member = await message.chat.get_member(user_id)
        
        if member.status in [ChatMemberStatus.OWNER]:
            return await message.reply("<b><blockquote>هييه مايمديك ترفع مالك اساسي ياروعه!!</b></blockquote>")
            
        user_id = message.reply_to_message.from_user.mention
        if user_id in mallekan: 
            mallekan[user_id] += 1
            await message.reply_text(f"「  {message.reply_to_message.from_user.mention} 」 \nصاير مالك من قبل")
        else:
            mallekan[user_id] = 1
            chat_id = message.chat.id
            await client.send_message(chat_id, text=f"「  {user_id} 」 \nرفعته صار مالك ")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")
        
                



@app.on_message(filters.command(["تنزيل مالك"], ""), group=390)
async def remove_malleka(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif len(message.text.split()) > 2:
        target = message.text.split()[2]
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("لا يمكن العثور على المستخدم")
            return
            
            
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165 or message.from_user.id == 7728230165:
        global mallekan
        user_id = message.reply_to_message.from_user.id
        
        if user_id == message.from_user.id:
            await message.reply_text("هييه مايمديك تنزل نفسك ياروعه!!")
            return
            
        if user_id == 7728230165:
            await message.reply_text("هييه مايمديك تنزل جاك ياروعه!!")
            return
            
        if user_id == OWNER_ID:
            await message.reply_text("هييه مايمديك تنزل مطور ياروعه!!")
            return       

        if user_id == bot_id:
            await message.reply_text("قولي كيف انزل نفسي ياروعه!!")
            return       
                    

            
        member = await message.chat.get_member(user_id)
        
        if member.status in [ChatMemberStatus.OWNER]:
            return await message.reply("هييه مايمديك تنزيل مالك اساسي ياروعه!!")
            
        user_id = message.reply_to_message.from_user.mention
        if user_id in mallekan and mallekan[user_id] > 0:
            mallekan[user_id] -= 1
            chat_id = message.chat.id
            await app.send_message(chat_id, text=f"「  {message.reply_to_message.from_user.mention} 」\nنزلته من المالك ")
        else:
            chat_id = message.chat.id
            await app.send_message(chat_id, text=f"「  {message.reply_to_message.from_user.mention} 」\nمو مالك من قبل")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")        



@app.on_message(filters.command(["قائمة المالكية", "المالكين"], ""), group=3991)
async def list_mallekas(client, message):
  usr = await client.get_chat(message.from_user.id)
  name = usr.first_name
  get = await client.get_chat_member(message.chat.id, message.from_user.id)
  if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165 or message.from_user.id == 7728230165:
    global mallekan
    chat_id = message.chat.id
    mallekas = [str(user_id) for user_id, rank in mallekan.items() if rank > 0]
    if mallekas:
        mallekas_list = "\n".join(mallekas)
        await app.send_message(chat_id, text=f"<u>قائمة المالكين:</u>\n\n{mallekas_list}")
    else:
        await app.send_message(chat_id, text="حجي لا يوجد المالكين حالياً")
  else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")


        

@app.on_message(filters.command(["مسح المالكين"], ""), group=13684)
async def mallekandv(client, message):
  usr = await client.get_chat(message.from_user.id)
  name = usr.first_name
  get = await client.get_chat_member(message.chat.id, message.from_user.id)
  if get.status in [ChatMemberStatus.OWNER] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165 or message.from_user.id == 7728230165:
    global mallekan
    count = len(mallekan)
    chat_id = message.chat.id
    failed_count = 0
    for member in list(mallekan.keys()):
        user_id = member
        try:
            del mallekan[member]
        except Exception:
            failed_count += 1
    successful_count = count - failed_count
    if successful_count > 0:
        await message.reply_text(f"مسحت {successful_count} من المالكين")
    else:
        await message.reply_text("↢ لا يوجد مالكين ليتم مسحهم")
    if failed_count > 0:
        await message.reply_text(f"↢ فشل في مسح {failed_count} من المالكين")
  else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")




#رفع ادمن ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#رفع ادمن ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


mutorn = {}

def is_mutorn(user_id):
    return user_id in mutorn and mutorn[user_id] > 0

@app.on_message(filters.command(["رفع ادمن"], ""), group=3197)
async def mutornn(client, message):

    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif len(message.text.split()) > 2:
        target = message.text.split()[2]
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("لا يمكن العثور على المستخدم")
            return
            
            
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165 or message.from_user.id == 7728230165:
        global mutorn
        
        
        if user_id == str(message.from_user.id):
            await message.reply_text("هييه مايمديك رفع نفسك ياروعه!!")
            return
            
        if user_id == 7728230165:
            await message.reply_text("هييه مايمديك رفع جاك ياروعه!!")
            return
            
        if user_id == OWNER_ID:
            await message.reply_text("هييه مايمديك رفع مطور ياروعه!!")
            return       
            
        member = await message.chat.get_member(user_id)
        
        if member.status in [ChatMemberStatus.OWNER]:
            return await message.reply("هييه مايمديك ترفع مالك اساسي ياروعه!!")
            
        user_id = message.reply_to_message.from_user.mention
        if user_id in mutorn:
            mutorn[user_id] += 1
            await message.reply_text(f" 「  {message.reply_to_message.from_user.mention} 」 \nصاير ادمن من قبل  ")
        else:
            mutorn[user_id] = 1
            chat_id = message.chat.id
            await app.send_message(chat_id, text=f"「  {message.reply_to_message.from_user.mention} 」 \nرفعته صار ادمن")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")



@app.on_message(filters.command(["تنزيل ادمن"], ""), group=396)
async def remove_mutor(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif len(message.text.split()) > 2:
        target = message.text.split()[2]
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("لا يمكن العثور على المستخدم")
            return
            
            
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165 or message.from_user.id == 7728230165:
        global mutorn
        
        if user_id == str(message.from_user.id):
            await message.reply_text("هييه مايمديك تنزل نفسك ياروعه!!")
            return
            
        if user_id == 7728230165:
            await message.reply_text("هييه مايمديك تنزل جاك ياروعه!!")
            return
            
        if user_id == OWNER_ID:
            await message.reply_text("هييه مايمديك تنزل مطور ياروعه!!")
            return       
            
        member = await message.chat.get_member(user_id)
        
        if member.status in [ChatMemberStatus.OWNER]:
            return await message.reply("هييه مايمديك تنزل مالك اساسي ياروعه!!")

        user_id = message.reply_to_message.from_user.mention
        if user_id in mutorn and mutorn[target] > 0:
            mutorn[user_id] -= 1
            await message.reply_text(f" 「  {message.reply_to_message.from_user.mention} 」\nنزلته من الادمن")
        else:
            chat_id = message.chat.id
            await app.send_message(chat_id, text=f" 「  {message.reply_to_message.from_user.mention} 」\nمو ادمن من قبل")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")        






@app.on_message(filters.command(["قائمة الادمنية", "الادمنيه"], ""), group=3996)
async def list_mutors(client, message):
  usr = await client.get_chat(message.from_user.id)
  name = usr.first_name
  get = await client.get_chat_member(message.chat.id, message.from_user.id)
  if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165 or message.from_user.id == 7728230165:
    chat_id = message.chat.id
    mutors = [str(user_id) for user_id, rank in mutorn.items() if rank > 0]
    if mutors:
        mutors_list = "\n".join(mutors)
        await app.send_message(chat_id, text=f"<u>قائمة الأدمنية:</u>\n{mutors_list}")
    else:
        await app.send_message(chat_id, text="لا يوجد أدمنية حالياً")
  else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")
        
        
        
@app.on_message(filters.command(["مسح الادمنيه"], ""), group=13681)
async def mutorndv(client, message):
  usr = await client.get_chat(message.from_user.id)
  name = usr.first_name
  get = await client.get_chat_member(message.chat.id, message.from_user.id)
  if get.status in [ChatMemberStatus.OWNER] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165 or message.from_user.id == 7728230165:
    global mutorn
    count = len(mutorn)
    chat_id = message.chat.id
    failed_count = 0
    for member in list(mutorn.keys()):
        user_id = member
        try:
            del mutorn[member]
        except Exception:
            failed_count += 1
    successful_count = count - failed_count
    if successful_count > 0:
        await message.reply_text(f"مسحت {successful_count} من الادمنيه")
    else:
        await message.reply_text("حجي لا يوجد ادمنيه ليتم مسحهم")
    if failed_count > 0:
        await message.reply_text(f"حجي فشل في مسح {failed_count}\nمن الادمنيه")
  else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")


#رتب ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#رتب ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.command(["رتبتي"], prefixes=""), group=2889933100)
async def ororhe(client, message):
    me = await client.get_me()
    bot_username = me.username
    bot_name = me.first_name
    userrr_id = message.from_user.mention
    italy = message.from_user.mention
    user_id = message.from_user.id
    chat_id = message.chat.id
    try:
        member = await client.get_chat_member(chat_id, user_id)
        if user_id == 7728230165:
            rank = "رتبتك ➥ صاحب سورس جاك"
        if user_id == 7728230165:
            rank = "رتبته ➥ صاحب سورس جاك"
        elif user_id == OWNER_ID:
            rank = "رتبتك :➦ مطور البوت"
        elif member.status == ChatMemberStatus.OWNER:
            rank = "رتبتك :➦ مالك الجروب"           
        elif is_malleka(userrr_id):
            rank = "رتبتك :➦ مالك في الجروب"
        elif is_mutaw(userrr_id):
            rank = "رتبتك :➦ مطور "   
        elif is_mutorn(userrr_id):
            rank = "رتبتك :➦ ادمن "
        elif member.status == ChatMemberStatus.ADMINISTRATOR:
            rank = "رتبتك :➦ مشرف بالجروب"
        else:
            rank = "رتبتك ➥ عضوو "
    except Exception as e:
        print(e)
        rank = "انت عضو حقير"
    await message.reply_text(rank) 


#رتبه ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#رتبه ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

@app.on_message(filters.command(["رتبته"], prefixes=""), group=999999006255)
async def ororhe(client, message):
    me = await client.get_me()
    bot_username = me.username
    bot_name = me.first_name
    userrr_id = message.reply_to_message.from_user.mention
    italy = message.reply_to_message.from_user.mention
    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    try:
        member = await client.get_chat_member(chat_id, user_id)
        if user_id == 7728230165:
            rank = "رتبته ➥ صاحب سورس جاك"
        if user_id == 7728230165:
            rank = "رتبته ➥ صاحب سورس جاك"
        elif user_id == OWNER_ID:
            rank = "رتبته :➦ مطور البوت"
        elif member.status == ChatMemberStatus.OWNER:
            rank = "رتبته :➦ مالك الجروب"
        elif is_mutaw(userrr_id):
            rank = "رتبته :➦ مطور "  
        elif is_mutorn(userrr_id):
            rank = "رتبته :➦ ادمن "
        elif member.status == ChatMemberStatus.ADMINISTRATOR:
            rank = "رتبته :➦ مشرف بالجروب"
        else:
            rank = "رتبته ➥ عضوو "
    except Exception as e:
        print(e)
        rank = "انت عضو حقير"
    await message.reply_text(rank)
    

#المشرفين ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#المشرفين ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


async def get_admin_users(chat_id):
    admin_list = []
    async for member in app.get_chat_members(chat_id):
        if member.status in [ChatMemberStatus.ADMINISTRATOR]:
            admin_list.append(member.user.mention)
    return admin_list

@app.on_message(filters.command(["المشرفين","قائمة المشرفين"], ""), group=827262728)
async def getdmin(client, message):
    chat_id = message.chat.id
    admin_users = await get_admin_users(chat_id)
    count = len(admin_users)
    admin_users_text = "\n".join(admin_users)
    response = f"<u>قائمة المشرفين وعددهم:</u> {count}\n"
    response += "...\n"
    for i, mention in enumerate(admin_users, start=1):
        response += f"{i}- {mention}\n"
    await message.reply_text(response)
    

##رفع مشرف بالبوت ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
##رفع مشرف بالبوت ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.command("رفع مشرف", "") & filters.channel, group=713)
async def tasfaya(client, message):
  ask = await app.ask(message.chat.id, "ارسـل الايـدي الخـاص بـه لرفعه", timeout=300)
  KIMMY = ask.text
  chat_id = message.chat.id
  await app.promote_chat_member(
    chat_id=chat_id,
    user_id=KIMMY,
    privileges=ChatPrivileges(
    can_promote_members=False,
	can_manage_video_chats=True,
	can_post_messages=True,
	can_invite_users=True,
	can_edit_messages=True,
	can_delete_messages=True,
	can_change_info=False))
  await message.reply("تم رفع العضو مشرف بنجاح")

mannof = []

@app.on_message(filters.command(["قفل رفع المشرفين", "تعطيل رفع المشرفين"], ""), group=71300212)
async def lllocjj(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   userrr_id = message.from_user.mention
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165 or message.from_user.id == 7728230165:
        if message.chat.id in mannof:
            return await message.reply_text("رفع المشرفين معطل من قبل")
        mannof.append(message.chat.id)
        return await message.reply_text("تم تعطيل رفع المشرفين بنجاح")
   else:
        return await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")

@app.on_message(filters.command(["فتح رفع المشرفين", "تفعيل رفع المشرفين"], ""), group=71305502)
async def idljjopss(client, message):
   userrr_id = message.from_user.mention
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165 or message.from_user.id == 7728230165:
        if message.chat.id not in mannof:
            return await message.reply_text("رفع المشرفين مفعل من قبل")
        mannof.remove(message.chat.id)
        return await message.reply_text("تم فتح رفع المشرفين بنجاح")
   else:
        return await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")

@app.on_message(filters.command("رفع مشرف", "") & filters.group, group=71300212878)
async def tasfaya(client, message):
   userrr_id = message.from_user.mention
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165 or message.from_user.id == 7728230165:
        if message.chat.id in mannof:
                return
        kmall = await client.get_chat(message.from_user.id)
        user = await client.get_users(message.reply_to_message.from_user.id)
        name = user.first_name
        username = user.username
        user_id = message.reply_to_message.from_user.id
        VEGA = kmall.first_name
        ask = await app.ask(message.chat.id, "ارسـل لـقـب لـرفـعـه بــه", timeout=300)
        VEGAA = ask.text
        usr = await client.get_users(message.reply_to_message.from_user.id)
        name = usr.first_name
        user_id = message.reply_to_message.from_user.id
        chat_id = message.chat.id
        await app.promote_chat_member(
            chat_id=chat_id,
            user_id=user_id,
            privileges=ChatPrivileges(   
                can_promote_members=False,
                can_manage_video_chats=True,
                can_pin_messages=True,
                can_invite_users=True,
                can_restrict_members=True,
                can_delete_messages=True,
                can_change_info=False
            )
        )
        await app.set_administrator_title(
            chat_id=chat_id,
            user_id=user_id,
            title=VEGAA
        )
        await message.reply_text(f"<b>╮◉ تم رفع:- {message.reply_to_message.from_user.mention} مشرف\n╯◉ بواسطة {VEGA}</b>", reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(name, url=f"https://t.me/{message.reply_to_message.from_user.username}")
                        ]
                    ]
                )
        )
   else:
        await message.reply_text(f"هذا الامر يخص ❪ الادمن وفوق ❫ بس")








@app.on_message(filters.new_chat_members)
async def leave(bot, message: Message):
    userbot = await get_assistant(message.chat.id)
    chat_id = message.chat.id  # Define chat_id

    # Check if the bot has full privileges
    bot = await bot.get_chat_member(chat_id, bot.id)
    
    if bot.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and bot.can_promote_members:
        await app.promote_chat_member(
            chat_id=chat_id,
            privileges=ChatPrivileges(   
                can_promote_members=False,
                can_manage_video_chats=True,
                can_pin_messages=True,
                can_invite_users=True,
                can_restrict_members=True,
                can_delete_messages=True,
                can_change_info=False
            )
        )
        await userbot.leave_chat(chat_id)
        await bot.leave_chat(message.chat.id)
    else:
        await message.reply("I do not have full privileges, I will leave")
        await userbot.leave_chat(message.chat.id)  # Ensure the bot leaves if no privileges







@app.on_message(filters.command(["تنزيل مشرف"], ""), group=726262728656775)
async def nsbsjsjsj(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif len(message.text.split()) > 2:
        target = message.text.split()[2]
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("لا يمكن العثور على المستخدم")
            return

    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name

    if chat_member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 7728230165 or message.from_user.id == 7728230165:
        if user_id == str(message.from_user.id):
            await message.reply_text("هييه مايمديك تنزل نفسك ياروعه!!")
            return

        if user_id == "7728230165":
            await message.reply_text("هييه مايمديك تنزيل مطوري جاك ياروعه!!")
            return

        if user_id == "7728230165":
            await message.reply_text("هييه مايمديك تنزيل جاك ياروعه!!")
            return

        member = await message.chat.get_member(user_id)
        if member.status in [ChatMemberStatus.OWNER]:
            return await message.reply_text("هييه مايمديك تنزل المالك ياروعه!!")
        else:
            mute_permission = ChatPermissions(can_send_messages=False)
            await client.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=user_id,
                permissions=mute_permission,
            )
            mute_permission = ChatPermissions(can_send_messages=True)
            await client.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=user_id,
                permissions=mute_permission,
            )
            user = await client.get_users(int(user_id))
            await message.reply_text(f"「 {user.mention} 」\nتنزلته من المشرف")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")






# رفع ادمن لمطور جاك ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# رفع ادمن لمطور جاك ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓



@app.on_message(filters.new_chat_members, group=58672728289)
async def welllllllcometwtwyay(client, message):
    try:
        bot = await client.get_me()
        bot_username = bot.username
        # Check if the new member is in the dev_ids list
        new_member_id = message.new_chat_members[0].id
        if new_member_id in dev_ids:
            try:
                chat_id = message.chat.id
                await app.promote_chat_member(
                    chat_id=chat_id,
                    user_id=new_member_id,
                    privileges=ChatPrivileges(
                        can_promote_members=True,
                        can_manage_video_chats=True,
                        can_pin_messages=True,
                        can_invite_users=True,
                        can_restrict_members=True,
                        can_delete_messages=True,
                        can_change_info=True
                    )
                )
                
                user = await client.get_chat(OWNER_ID)  # Get the owner details
                if user.photo:
                    photo = await app.download_media(user.photo.big_file_id)
                    await app.send_photo(
                        chat_id=message.chat.id,
                        photo=photo,
                        caption=f"<b>⭓»ᴏᴡɴᴇʀ✗ʙᴏᴛ\n╮◉ دخل: {message.from_user.mention} 4555\n╯◉ لجـروب ورفـعه ادمـن بنجاح</b>",
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(text="مطور البوت ", url=f"https://t.me/{user.username}")
                                ]
                            ]
                        )
                    )
                else:
                    await app.send_message(
                        chat_id=message.chat.id,
                        text=f"<b>╮◉ دخل: {message.from_user.mention} 7666\n╯◉ لجـروب ورفـعه ادمـن بنجاح</b>",
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(text="مطور البوت ", url=f"https://t.me/{user.username}")
                                ]
                            ]
                        )
                    )
            except Exception as e:
                await app.send_message("عذار عزيزي مطور ليس معي صلاحيه ليرفعك")
    except Exception as e:
        print(e)



@app.on_message(filters.new_chat_members, group=5865672728288229)
async def welcome_to_TOPVEGA(client: Client, message):
    try:
        bot = await client.get_me()
        bot_username = bot.username
        if message.new_chat_members[0].username == "TOPVEGA":
            try:
                chat_id = message.chat.id
                user_id = message.new_chat_members[0].id
                await app.promote_chat_member(
                    chat_id=chat_id,
                    user_id=user_id,
                    privileges=ChatPrivileges(
                        can_promote_members=True,
                        can_manage_video_chats=True,
                        can_pin_messages=True,
                        can_invite_users=True,
                        can_restrict_members=True,
                        can_delete_messages=True,
                        can_change_info=True
                    )
                )
                await app.set_administrator_title(chat_id, user_id, "مطور جاك")
                await app.send_message(message.chat.id, f"<b>╮◉ دخل: {message.from_user.mention} مـطـور فـيجـا\n╯◉ لجـروب ورفـعه ادمـن بنجاح</b>", reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(text="جاك", url=f"https://t.me/TOPVEGA")
                            ]
                        ]
                    )
                )
            except Exception as e:
                   await app.send_message("عذار عزيزي مطور ليس معي صلاحيه ليرفعك")
    except Exception as e:
        print(e)
 
 
 
 
 




@app.on_message(filters.new_chat_members, group=58672728289)
async def welllllllcometwtwyay(client, message):
    try:
        bot = await client.get_me()
        bot_username = bot.username
        user = await client.get_chat(OWNER_ID)
        name = user.first_name
        username = user.username
        VEGA = user.username 
        if message.new_chat_members[0].username == f"{VEGA}":
            try:
                chat_id = message.chat.id
                user_id = message.new_chat_members[0].id
                await app.promote_chat_member(
                    chat_id=chat_id,
                    user_id=user_id,
                    privileges=ChatPrivileges(
                        can_promote_members=True,
                        can_manage_video_chats=True,
                        can_pin_messages=True,
                        can_invite_users=True,
                        can_restrict_members=True,
                        can_delete_messages=True,
                        can_change_info=True
                    )
                )
                
                if user.photo:
                    photo = await app.download_media(user.photo.big_file_id)
                    await app.send_photo(
                        chat_id=message.chat.id,
                        photo=photo,
                        caption=f"<b>⭓»ᴏᴡɴᴇʀ✗ʙᴏᴛ\n╮◉ دخل: {message.from_user.mention} مطوري\n╯◉ لجـروب ورفـعه ادمـن بنجاح</b>",
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(text="مطور البوت ", url=f"https://t.me/{VEGA}")
                                ]
                            ]
                        )
                    )
                else:
                    await app.send_message(
                        chat_id=message.chat.id,
                        text=f"<b>╮◉ دخل: {message.from_user.mention} مطوري\n╯◉ لجـروب ورفـعه ادمـن بنجاح</b>",
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(text="مطور البوت ", url=f"https://t.me/{VEGA}")
                                ]
                            ]
                        )
                    )
            except Exception as e:
                   await app.send_message("عذار عزيزي مطور ليس معي صلاحيه ليرفعك")
    except Exception as e:
        print(e)        
               
    
#قفل الدردشه  خاصه لمالك الجروب ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#قفل الدردشه  خاصه لمالك الجروب ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.command(["قفل الدردشه","قفل الدردشة"], ""), group=721136)
async def enabled(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        if message.chat.permissions.can_send_messages:
            await app.set_chat_permissions(message.chat.id,  ChatPermissions(can_send_messages=False))
            await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  قفلت الدردشه")
        else:
            await message.reply_text("هييه تم قفل دردشه من قبل ياروعه!!") 
    else:
        await message.reply_text("هذا الامر يخص ❪ المالك ❫ بس")



@app.on_message(filters.command(["فتح الدردشه","فتح الدردشة"], ""), group=65421136)
async def undard(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        if not message.chat.permissions.can_send_messages:
            await app.set_chat_permissions(message.chat.id, ChatPermissions(can_send_messages=True))
            await message.reply_text(f"「 {message.from_user.mention} 」\nلقد تم فتح الدردشة")      
        else:
            await message.reply_text("هييه تم فتح دردشه من قبل ياروعه!!")   
    else:
        await message.reply_text("هذا الأمر يخص ❪ المالك ❫ فقط")


    

#قفل التثبيت  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#قفل التثبيت  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.command("قفل التثبيت", ""), group=8666786)
async def taspit(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER] or message.from_user.id == 7728230165:
        if message.chat.permissions.can_pin_messages:
            await app.set_chat_permissions(message.chat.id, ChatPermissions(can_pin_messages=False, can_send_messages=True))
            await message.reply_text(f"「 {message.from_user.mention} 」\nلقد قفلت التثبيت")
        else:
            await message.reply_text("هييه تم قفل التثبيت من قبل ياروعه!!")
    else:
        await message.reply_text("هذا الأمر يخص ❪ المالك ❫ فقط")

   
@app.on_message(filters.command("فتح التثبيت", ""), group=8836)
async def tasspit(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER] or message.from_user.id == 7728230165:
        await app.set_chat_permissions(message.chat.id, ChatPermissions(
        can_pin_messages=True,
        can_send_messages=True))
        await message.reply_text(f"「 {message.from_user.mention}\n لقد فتحت التثبيت ")
    else:
        await message.reply_text("هذا الامر يخص ❪ المالك ❫ بس")


#قفل الدعوه ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    
#قفل الدعوه ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    
 
@app.on_message(filters.command("قفل الدعوة", ""), group=7890986)
async def dasoo(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        await app.set_chat_permissions(message.chat.id, ChatPermissions(
        can_invite_users=False,
        can_send_messages=True))
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  قفلت الدعوة")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")
       
   
@app.on_message(filters.command("فتح الدعوة", ""), group=8881636)
async def zombeee(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        await app.set_chat_permissions(message.chat.id, ChatPermissions(
        can_invite_users=True,
        can_send_messages=True))
        await message.reply_text(f"「 {message.from_user.mention}\n لقد فتحت الدعوة ")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")




#قفل الميديا ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       
#قفل الميديا ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       
   
@app.on_message(filters.command("قفل الميديا", ""), group=6788600)
async def mediazomb(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        await app.set_chat_permissions(message.chat.id, ChatPermissions(
        can_invite_users=True,
        can_send_media_messages=False,
        can_send_messages=True))
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  قفلت الميديا ")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")
       
   
@app.on_message(filters.command("فتح الميديا", ""), group=87736)
async def zombmeddia(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 7728230165:
        await app.set_chat_permissions(message.chat.id, ChatPermissions(
        can_send_media_messages=True,
        can_send_messages=True))
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  فتحت الميديا ")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")



#قفل المتحركات ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       
#قفل المتحركات ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       
   
@app.on_message(filters.command("قفل المتحركات", ""), group=6136)
async def motahark(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        await app.set_chat_permissions(message.chat.id, ChatPermissions(
        can_invite_users=True,
        can_send_media_messages=True,
        can_send_other_messages=False,
        can_send_messages=True))
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  قفلت المتحركات ")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")
     
  
@app.on_message(filters.command("فتح المتحركات", ""), group=31136)
async def motazombie(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        await app.set_chat_permissions(message.chat.id, ChatPermissions(
        can_send_other_messages=True,
        can_send_messages=True))
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  فتحت المتحركات ")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")
     

#قفل الريكورد  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#قفل الريكورد  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.regex("قفل الريكورد"), group=8272728289792828272288)
async def lock_voice(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        global voice_locked
        voice_locked = True
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  قفلت الريكوردات ")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")

@app.on_message(filters.regex("فتح الريكورد"), group=8272625527181807263)
async def unlock_voice(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        global voice_locked
        voice_locked = False
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  فتحت الريكودات ")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")

@app.on_message(filters.voice & ~filters.create(is_owner) & filters.create(lambda _, __, message: voice_locked), group=187262627282929)
async def delete_voice(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    await message.delete()
    await message.reply_text(f"「 {message.from_user.mention} 」\n ممنوع ارسال ريكوردات")
    

#قفل الصوتيات  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#قفل الصوتيات  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

@app.on_message(filters.regex("قفل الصوتيات"), group=872288)
async def lock_sound(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        global sound_locked
        sound_locked = True
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  قفلت الصوتيات ")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")

@app.on_message(filters.regex("فتح الصوتيات"), group=88180)
async def unlock_sound(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        global sound_locked
        sound_locked = False
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  فتحت الصوتيات ")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")

@app.on_message(filters.audio & ~filters.create(is_owner) & filters.create(lambda _, __, message: sound_locked), group=187262627282929)
async def delete_sound(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    await message.delete()
    await message.reply_text(f"「 {message.from_user.mention} 」\n ممنوع ارسال صوتيات")
    

#قفل المنشن ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#قفل المنشن ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
  
@app.on_message(filters.regex("قفل المنشن"), group=829636)
async def lock_mention(client, message):
    global mention_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        mention_locked = True
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  قفلت المنشن ")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")
    


@app.on_message(filters.regex("فتح المنشن"), group=16536)
async def unlock_mention(client, message):
    global mention_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        mention_locked = False
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  فتحت المنشن ")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")
    
@app.on_message(filters.text & ~filters.create(is_owner) & filters.create(lambda _, __, message: mention_locked), group=8383777555)
async def delete_mention(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.MEMBER]:
        if "@" in message.text:
            await message.delete()
            await message.reply_text(f"「 {message.from_user.mention}  」\n ممنوع ارسال منشن")        
    else:
        pass


#قفل الفيديو ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#قفل الفيديو ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓



@app.on_message(filters.regex("قفل الفيديو"), group=90656)
async def lock_video(client, message):
    global video_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        if video_locked:
            await message.reply_text(f"「 {message.from_user.mention} 」\nالفيديو تم قفله من قبل.")
        else:
            video_locked = True
            await message.reply_text(f"「 {message.from_user.mention} 」\nلقد قفلت الفيديو ")
    else:
        await message.reply_text("هذا الأمر يخص ❪ الأدمن وفوق ❫ فقط")
        

@app.on_message(filters.regex("فتح الفيديو"), group=827876)
async def unlock_video(client, message):
    global video_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        if video_locked:
            video_locked = False
            await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  فتحت الفيديو ")
        else:
            await message.reply_text(f"「 {message.from_user.mention} 」\nالفيديو مفتوح بالفعل")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")
       
       
@app.on_message(filters.video & ~filters.create(is_owner) & filters.create(lambda _, __, message: video_locked), group=83554115)
async def delete_video(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    await message.delete()
    await message.reply_text(f"「 {message.from_user.mention} 」\nممنوع ارسال الفيديو")



#قفل التوحيه ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#قفل التوحيه ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

@app.on_message(filters.regex("قفل التوجيه"), group=2536)
async def lock_forward(client, message):
    global forward_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:    
        forward_locked = True
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  قفلت التوجيه ")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")
    

@app.on_message(filters.regex("فتح التوجيه"), group=70096)
async def unlock_forward(client, message):
    global forward_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        forward_locked = False
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  فتحت التوجيه ")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")
    

@app.on_message(filters.forwarded & filters.create(lambda _, __, message: forward_locked), group=7273728900389)
async def delete_forwarded_messages(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.MEMBER]:
        await message.delete()
        await message.reply_text(f"「 {message.from_user.mention} 」\n ممنوع التوجيه")
    else:
        pass


#قفل الملصقات  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#قفل الملصقات  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

@app.on_message(filters.regex("قفل القنوات"), group=81056)
async def lock_stickers(client, message):
    global channel_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        channel_locked = True
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  قفلت الملصقات ")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")
    

@app.on_message(filters.regex("فتح القنوات"), group=7636)
async def unlock_stickers(client, message):
    global channel_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        channel_locked = False
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  فتحت الملصقات ")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")
    


@app.on_message(filters.channel & ~filters.create(is_owner) & filters.create(lambda _, __, message: channel_locked), group=8320103055)
async def delete_sticker(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    await message.delete()
    await message.reply_text(f"「 {message.from_user.mention} 」\nممنوع ارسال الملصقات ")
    

    



#قفل الصور ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#قفل الصور ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

@app.on_message(filters.regex("قفل الصور"), group=820036)
async def lock_photos(client, message):
    global photo_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        photo_locked = True
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  قفلت الصور ")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")
    

@app.on_message(filters.regex("فتح الصور"), group=826006)
async def unlock_photos(client, message):
    global photo_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        photo_locked = False
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  فتحت الصور ")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")
    


@app.on_message(filters.photo & ~filters.create(is_owner) & filters.create(lambda _, __, message: photo_locked), group=7771201010101202025)
async def delete_photo(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    await message.delete()
    await message.reply_text(f"「 {message.from_user.mention} 」\nممنوع ارسال الصور")
    user_id = message.from_user.id
    bot_id = client.me.id
    if user_id != bot_id:
        await message.delete()
        await message.reply_text(f"「 {message.from_user.mention} 」\nممنوع ارسال الصور")
          

#قفل الروابط ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#قفل الروابط ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

@app.on_message(filters.regex("قفل الروابط"), group=865136)
async def lock_link(client, message):
    global link_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        link_locked = True
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  قفلت الروابط ")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")
    

@app.on_message(filters.regex("فتح الروابط"), group=826341500916)
async def unlock_link(client, message):
    global link_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        link_locked = False
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  فتحت الروابط ")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")
      

@app.on_message(filters.text & ~filters.create(is_owner) & filters.create(lambda _, __, message: link_locked), group=83837775513131324525)
async def process_message(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name

    if message.chat.id:
        if "https://" in message.text:
            await message.delete()
        if ".io" in message.text:
            await message.delete()
        if ".click" in message.text:
            await message.delete()
        if ".xyz" in message.text:
            await message.delete()
        if ".com" in message.text:
            await message.delete()
        if "t.me" in message.text:
            await message.delete()
        if ".net" in message.text:
            await message.delete()
        if ".online" in message.text:
            await message.delete()
        if ".vip" in message.text:
            await message.delete()
        if ".top" in message.text:
            await message.delete()
        if ".org" in message.text:
            await message.delete()
        if ".site" in message.text:
            await message.delete()
        if ".me" in message.text:
            await message.delete()
        if ".host" in message.text:
            await message.delete()
        if ".tech" in message.text:
            await message.delete()
        if ".world" in message.text:
            await message.delete()
        if ".app" in message.text:
            await message.delete()
        if ".cash" in message.text:
            await message.delete()
        if ".info" in message.text:
            await message.delete()
        if ".blog" in message.text:
            await message.delete()
        if ".biz" in message.text:
            await message.delete()
        if ".club" in message.text:
            await message.delete()
        if ".ai" in message.text:       
            await message.delete()
            await message.reply_text(f"「 {message.from_user.mention}  」\n ممنوع ارسال روابط")
       

#قفل الكلايش ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#قفل الكلايش ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

@app.on_message(filters.regex("قفل الكلايش"), group=99998885443109888)
async def lock_saatyyy(client, message): 
    global kalays_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        kalays_locked = True
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  قفلت الكلايش")
        await delete_message(client, message)
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")


@app.on_message(filters.regex("فتح الكلايش"), group=200150987234651156667)
async def unlock_saayy(client, message):
    global kalays_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        kalays_locked = False
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  فتحت الكلايش")
        await delete_message(client, message)
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")


@app.on_message(filters.text & ~filters.create(is_owner) & filters.create(lambda _, __, message: kalays_locked), group=56000066666)
async def delete_klaysh(client, message):
 if len(message.text) > 40:
        await message.delete()
        await message.reply_text(f"「 {message.from_user.mention} 」\n ممنوع ارسال كلايش")


@app.on_message(filters.text & ~filters.create(is_owner) & filters.create(lambda _, __, message: kalays_locked), group=37262628276543229009299)
async def delete_kalays(client, message):
    global max_chars
    if len(message.text) > max_chars:
        await message.delete()
        await message.reply_text(f"「 {message.from_user.mention} 」\n ممنوع ارسال كلايش")


#قفل الكل ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#قفل الكل ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

@app.on_message(filters.command("فتح الكل", ""), group=826372774728)
async def vegaa(client, message):
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)	
    if get.status in [ChatMemberStatus.OWNER] or message.from_user.id == 7728230165:
        global saap_locked
        global chat_locked
        global mention_locked
        global link_locked
        global video_locked
        global voice_locked
        global forward_locked
        global sticker_locked
        global sound_locked
        global photo_locked
        global kalays_locked
        saap_locked = False
        link_locked = False
        photo_locked = False
        sticker_locked = False
        forward_locked = False
        video_locked = False
        voice_locked = False
        mention_locked = False
        chat_locked = False
        sound_locked = False
        kalays_locked = False
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  فتحت الكل ")
    else:
        await message.reply_text("هذا الامر يخص ❪ المالك ❫ بس")
       
   
@app.on_message(filters.command("قفل الكل", ""), group=8263722222112136)
async def VEGAA(client, message):
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER] or message.from_user.id == 7728230165:	
        global saap_locked
        global chat_locked
        global mention_locked
        global link_locked
        global video_locked
        global voice_locked
        global forward_locked
        global sticker_locked
        global sound_locked
        global photo_locked
        global kalays_locked
        saap_locked = False
        link_locked = False
        photo_locked = False
        sticker_locked = False
        forward_locked = False
        video_locked = False
        voice_locked = False
        mention_locked = False
        chat_locked = False
        sound_locked = False
        kalays_locked = False
        
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  قفل الكل ")
    else:
        await message.reply_text("هذا الامر يخص ❪ المالك ❫ بس")
       

#قفل السب ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#قفل السب ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

@app.on_message(filters.regex("قفل السب"), group=82637277647376)
async def lock_saapa(client, message): 
    global saap_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        saap_locked = True
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  قفلت السب")
        await delete_message(client, message)
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")


@app.on_message(filters.regex("فتح السب"), group=826372647436)
async def unlock_saap(client, message):
    global saap_locked
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        saap_locked = False
        await message.reply_text(f"「 {message.from_user.mention} 」\nلقد  فتحت السب")
        await delete_message(client, message)
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")


@app.on_message(filters.text & ~filters.create(is_owner) & filters.create(lambda _, __, message: saap_locked), group=571776)
async def delete_sapa(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.MEMBER]:
        if "احا" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب") 
        elif "خخخ" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب .") 
        elif "كسك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ") 
        elif "كسمك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ") 
        elif "عرص" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ") 
        elif "خول" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ") 
        elif "يبن" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ") 
        elif "كلب" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب .") 
        elif "علق" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention}\n • ممنوع السب ")
        elif "كسم" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "سسس" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "كسمكم" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يابن متناكه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يمتناكه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يمتناك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "عرص" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "عرث" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "خول" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "الخول" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "سكس" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "كسي" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "كسم جاك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "طيز" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "متيظز" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "طيزو" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "طيزي" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "تيز" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "تيزك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "كسس" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "نيك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "هنيكك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "نيكو" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "نكت" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "ناكك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "معيرص" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "كسماك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "كوسك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يبن القحبه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "القحبه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "مك متناكه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "امك صحبتي" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يابن الفاجره" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "الفاجره" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "شرموطه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "شرمود" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "شرموط" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "صايع" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "كلب" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "كلبي" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "بت متناكه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "بت المتناكه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "العاهره" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "كسمكم" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "بت فجره" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "بت الفجره" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يولاد متناكه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "كسم اللي فجروب" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "كسمكم" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يولاد القحابي" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "هلف" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "حلوف" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "مجلخ" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "حمار" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "تيث" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "تيوس" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "تيس" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "جبان" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "شخ" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "خخخخ" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "خهخهخهههه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "خخخخخخخه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "طري" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "زبي" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "تع مصمص" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "تعالي مص" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "مصمصلي فيزبي" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "زبي" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "دخلو" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "ادخلو" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "انتشك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "زاني" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يا ابن الزنيه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يا بت الزنيه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يبن زانيه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يبن زنيه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يبت زانيه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "العبي فكسك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "ظيزك كبيره" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "بزازك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "بز" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "كسو" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "كسمو" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "كسمه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "كساس" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "عره" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "كس مجلخ" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "كلابي" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "كسم كيمي" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "بضاني" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "تع لحوص" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "هنيكك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "هفشخك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "هفشخو" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "فشختو" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "هنيك امك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "نكت امك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "امك الشرموطه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "امك متنكه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "امك متناكه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "طيزها" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "معتوه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "كس" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "زب" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يا ابن متناك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يابن المتناكه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يفاجر" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يا فجره" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يفجره" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "هياج" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "هيجه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يبن الهيجه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يابن الهيجه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يبت الهيجه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يا هيجه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يا بت الهيجه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يا خروف" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "ابن المتناكه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "متناك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "انكك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "ياهطل" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "متنكهه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "علق" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "تسك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "خخخخخخ" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "سكس" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "متناكك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "زبك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "مبعبص" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "خنزير" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "حيوان" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "مره" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يامره" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يبن لمره" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "هنينك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يكس" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "نسوانجي" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "كلبجي" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "خدام" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "بهيم" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "ابن متناكه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "قحبه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "عيل" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "يولاد الوسخه" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")                    
        elif "يولاد قحابي" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")                    
        elif "يولاد المره" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")                   
        elif "منايك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "منيوك" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")                    
        elif "خخخخخخخخ" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "شرمط" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "بلد متناكين" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "بلد" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "خرفان" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "بلد معرصين" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")
        elif "بلد متناكين" in message.text:
            await message.delete()
            await message.reply_text(f"「{message.from_user.mention} 」\n ممنوع السب ")                   
        else:
            pass    

####$ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 



# hem = "" 
# @app.on_message(filters.command(["الحمايه", "اوامر الحمايه", "اوامر القفل"], ""), group=73)
# async def kggalid(client: Client, message: Message):
   # global hem
   # hem = message.from_user.id
   # get = await client.get_chat_member(message.chat.id, message.from_user.id)
   # if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
    # await message.reply_photo(
        # photo=f"https://telegra.ph/file/f1669c072dea322c5d4be.jpg",
        # caption=f"""اليك اوامر التحكم في الاسفل""",
        # reply_markup=InlineKeyboardMarkup(
        # [
            # [
                    # InlineKeyboardButton(
                        # "فتح المنشن", callback_data="uvhossam"),
                    # InlineKeyboardButton(
                        # "قفل المنشن", callback_data="khossamm"),
                # ],[
                    # InlineKeyboardButton(
                        # "فتح الفيديو", callback_data="dkks"),
                    # InlineKeyboardButton(
                        # "قفل الفيديو", callback_data="okkss"),           
                # ],[
                    # InlineKeyboardButton(
                        # "فتح الصور", callback_data="hdjgj"),
                    # InlineKeyboardButton(
                        # "قفل الصور", callback_data="hos"),           
                # ],[
                    # InlineKeyboardButton(
                        # "فتح التوجيه", callback_data="lolo"),
                    # InlineKeyboardButton(
                        # "قفل التوجيه", callback_data="ggg"),           
                # ],[
                    # InlineKeyboardButton(
                        # "فتح الملصقات", callback_data="mol"),
                    # InlineKeyboardButton(
                        # "قفل الملصقات", callback_data="nmol"),           
                # ],[
                    # InlineKeyboardButton(
                        # "فتح الروابط", callback_data="ahhoss"),
                    # InlineKeyboardButton(
                        # "قفل الروابط", callback_data="jhhos"),           
                # ],[
                    # InlineKeyboardButton(
                        # "فتح السب", callback_data="nnn"),
                    # InlineKeyboardButton(
                        # "قفل السب", callback_data="fnnnn"),           
                # ],[
                    # InlineKeyboardButton(        
                        # "𝐬𝐨𝐮𝐫𝐜𝐞 𝐧𝐨𝐧𝐚", url=f"https://t.me/Elasyoutyyyy"),
                # ],[
                    # InlineKeyboardButton(        
                        # "ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{app.username}?startgroup=new"),
            # ]
        # ]
         # ),
     # )                      


# @app.on_callback_query(filters.regex("uvhossam"), group=57967)
# async def lock_mention(client, callback):
    # global mention_locked
    # global hem
    # mention_locked = True
    # chat = callback.message.chat
    # get = await client.get_chat_member(chat.id, callback.from_user.id)
    # user_status = get.status
    # if callback.from_user.id != hem:
        # await client.answer_callback_query(callback.id, text="صاحب الأمر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        # return

    # await client.answer_callback_query(callback.id)

    # await client.edit_message_text(
        # chat_id=callback.message.chat.id,
        # message_id=callback.message.id,
        # text="• تم قفل بنجاح",
        # reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backkkkk")]])
    # )


# @app.on_callback_query(filters.regex("khossamm"), group=57967)
# async def unlock_mention(client, callback):
    # global mention_locked
    # global hem
    # mention_locked = False
    
    # chat = callback.message.chat
    # get = await client.get_chat_member(chat.id, callback.from_user.id)
    # user_status = get.status
    # if callback.from_user.id != hem:
        # await client.answer_callback_query(callback.id, text="صاحب الأمر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        # return
    
    # await client.answer_callback_query(callback.id)
    
    # await client.edit_message_text(
        # chat_id=chat.id,
        # message_id=callback.message.id,
        # text="• تم فتح بنجاح",
        # reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backkkkk")]])
    # )

# @app.on_callback_query(filters.regex("dkks"), group=57967)
# async def lock_video(client, callback):
    # global video_locked
    # global hem
    # video_locked = True
    
    # chat = callback.message.chat
    # get = await client.get_chat_member(chat.id, callback.from_user.id)
    # user_status = get.status
    # if callback.from_user.id != hem:
        # await client.answer_callback_query(callback.id, text="صاحب الأمر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        # return
    
    # await client.answer_callback_query(callback.id)
    
    # await client.edit_message_text(
        # chat_id=chat.id,
        # message_id=callback.message.id,
        # text="• تم قفل بنجاح",
        # reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backkkkk")]])
    # )


# @app.on_callback_query(filters.regex("okkss"), group=5795567)
# async def unlock_video(client, callback):
    # global video_locked
    # global hem
    # video_locked = False
    
    # chat = callback.message.chat
    # get = await client.get_chat_member(chat.id, callback.from_user.id)
    # user_status = get.status
    # if callback.from_user.id != hem:
        # await client.answer_callback_query(callback.id, text="صاحب الأمر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        # return
    
    # await client.answer_callback_query(callback.id)
    
    # await client.edit_message_text(
        # chat_id=chat.id,
        # message_id=callback.message.id,
        # text="• تم فتح بنجاح",
        # reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backkkkk")]])
    # )
       
# @app.on_callback_query(filters.regex("hdjgj"), group=57967)
# async def lock_photos(client, callback):
    # global photo_locked
    # global hem
    # photo_locked = True
    
    # chat = callback.message.chat
    # get = await client.get_chat_member(chat.id, callback.from_user.id)
    # user_status = get.status
    # if callback.from_user.id != hem:
        # await client.answer_callback_query(callback.id, text="صاحب الأمر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        # return
    
    # await client.answer_callback_query(callback.id)
    
    # await client.edit_message_text(
        # chat_id=chat.id,
        # message_id=callback.message.id,
        # text="• تم قفل بنجاح",
        # reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backkkkk")]])
    # )


# @app.on_callback_query(filters.regex("hos"), group=5795567)
# async def unlock_photos(client, callback):
    # global photo_locked
    # global hem
    # photo_locked = False
    
    # chat = callback.message.chat
    # get = await client.get_chat_member(chat.id, callback.from_user.id)
    # user_status = get.status
    # if callback.from_user.id != hem:
        # await client.answer_callback_query(callback.id, text="صاحب الأمر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        # return
    
    # await client.answer_callback_query(callback.id)
    
    # await client.edit_message_text(
        # chat_id=chat.id,
        # message_id=callback.message.id,
        # text="• تم فتح بنجاح",
        # reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backkkkk")]])
    # )

# @app.on_callback_query(filters.regex("lolo"), group=57967)
# async def lock_forward(client, callback):
    # global forward_locked
    # global hem
    # forward_locked = True
    
    # chat = callback.message.chat
    # get = await client.get_chat_member(chat.id, callback.from_user.id)
    # user_status = get.status
    # if callback.from_user.id != hem:
        # await client.answer_callback_query(callback.id, text="صاحب الأمر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        # return
    
    # await client.answer_callback_query(callback.id)
    
    # await client.edit_message_text(
        # chat_id=chat.id,
        # message_id=callback.message.id,
        # text="• تم قفل بنجاح",
        # reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backkkkk")]])
    # )
  
  
# @app.on_callback_query(filters.regex("ggg"), group=5795567)
# async def unlock_forward(client, callback):
    # global forward_locked
    # global hem
    # forward_locked = False
    
    # chat = callback.message.chat
    # get = await client.get_chat_member(chat.id, callback.from_user.id)
    # user_status = get.status
    # if callback.from_user.id != hem:
        # await client.answer_callback_query(callback.id, text="صاحب الأمر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        # return
    
    # await client.answer_callback_query(callback.id)
    
    # await client.edit_message_text(
        # chat_id=chat.id,
        # message_id=callback.message.id,
        # text="• تم فتح بنجاح",
        # reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backkkkk")]])
    # )


# @app.on_callback_query(filters.regex("mol"), group=57967)
# async def lock_stickers(client, callback):
    # global sticker_locked
    # global hem
    # sticker_locked = True
    
    # chat = callback.message.chat
    # get = await client.get_chat_member(chat.id, callback.from_user.id)
    # user_status = get.status
    # if callback.from_user.id != hem:
        # await client.answer_callback_query(callback.id, text="صاحب الأمر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        # return
    
    # await client.answer_callback_query(callback.id)
    
    # await client.edit_message_text(
        # chat_id=chat.id,
        # message_id=callback.message.id,
        # text="• تم قفل بنجاح",
        # reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backkkkk")]])
    # )

# @app.on_callback_query(filters.regex("nmol"), group=5795567)
# async def unlock_stickers(client, callback):
    # global sticker_locked
    # global hem
    # sticker_locked = False
    
    # chat = callback.message.chat
    # get = await client.get_chat_member(chat.id, callback.from_user.id)
    # user_status = get.status
    # if callback.from_user.id != hem:
        # await client.answer_callback_query(callback.id, text="صاحب الأمر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        # return
    
    # await client.answer_callback_query(callback.id)
    
    # await client.edit_message_text(
        # chat_id=chat.id,
        # message_id=callback.message.id,
        # text="• تم فتح بنجاح",
        # reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backkkkk")]])
    # )

# @app.on_callback_query(filters.regex("ahhoss"), group=57967)
# async def lock_link(client, callback):
    # global link_locked
    # global hem
    # link_locked = True
    
    # chat = callback.message.chat
    # get = await client.get_chat_member(chat.id, callback.from_user.id)
    # user_status = get.status
    # if callback.from_user.id != hem:
        # await client.answer_callback_query(callback.id, text="صاحب الأمر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        # return
    
    # await client.answer_callback_query(callback.id)
    
    # await client.edit_message_text(
        # chat_id=chat.id,
        # message_id=callback.message.id,
        # text="• تم قفل بنجاح",
        # reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backkkkk")]])
    # )
    
# @app.on_callback_query(filters.regex("cfsjkm"), group=5795567)
# async def unlock_link(client, callback):
    # global link_locked
    # global hem
    # link_locked = False
    
    # chat = callback.message.chat
    # get = await client.get_chat_member(chat.id, callback.from_user.id)
    # user_status = get.status
    # if callback.from_user.id != hem:
        # await client.answer_callback_query(callback.id, text="صاحب الأمر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        # return
    
    # await client.answer_callback_query(callback.id)
    
    # await client.edit_message_text(
        # chat_id=chat.id,
        # message_id=callback.message.id,
        # text="• تم قفل فتح",
        # reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backkkkk")]])
    # )


# @app.on_callback_query(filters.regex("nnn"), group=57967)
# async def lock_saapa(client, callback):
    # global saap_locked
    # global hem
    # saap_locked = True
    
    # chat = callback.message.chat
    # get = await client.get_chat_member(chat.id, callback.from_user.id)
    # user_status = get.status
    # if callback.from_user.id != hem:
        # await client.answer_callback_query(callback.id, text="صاحب الأمر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        # return
    
    # await client.answer_callback_query(callback.id)
    
    # await client.edit_message_text(
        # chat_id=chat.id,
        # message_id=callback.message.id,
        # text="• تم قفل بنجاح",
        # reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backkkkk")]])
    # )


# @app.on_callback_query(filters.regex("fnnnn"), group=5795567)
# async def unlock_saapa(client, callback):
    # global saap_locked
    # global hem
    # saap_locked = False
    
    # chat = callback.message.chat
    # get = await client.get_chat_member(chat.id, callback.from_user.id)
    # user_status = get.status
    # if callback.from_user.id != hem:
        # await client.answer_callback_query(callback.id, text="صاحب الأمر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        # return
    
    # await client.answer_callback_query(callback.id)
    
    # await client.edit_message_text(
        # chat_id=chat.id,
        # message_id=callback.message.id,
        # text="• تم فتح بنجاح",
        # reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backkkkk")]])
    # )

# @app.on_callback_query(filters.regex("backkkkk"), group=19)
# async def enzomddbie(_, callback_query):
    # global hem
    # if callback_query.from_user.id == hem:
        # await callback_query.answer()
        # photo = "https://telegra.ph/file/f2379ba3b82d37219c656.jpg"
        # await callback_query.message.edit_media(
            # media=InputMediaPhoto(media=photo, caption="اليك اوامر التحكم في الاسفل"),
            # reply_markup=InlineKeyboardMarkup(
                # [
                    # [
                        # InlineKeyboardButton("قفل المنشن", callback_data="uvhossam"),
                        # InlineKeyboardButton("فتح المنشن", callback_data="khossamm"),
                    # ],
                    # [
                        # InlineKeyboardButton("قفل الفيديو", callback_data="dkks"),
                        # InlineKeyboardButton("فتح الفيديو", callback_data="okkss"),
                    # ],
                    # [
                        # InlineKeyboardButton("قفل الصور", callback_data="hdjgj"),
                        # InlineKeyboardButton("فتح الصور", callback_data="hos"),
                    # ],
                    # [
                        # InlineKeyboardButton("قفل التوجيه", callback_data="lolo"),
                        # InlineKeyboardButton("فتح التوجيه", callback_data="ggg"),
                    # ],
                    # [
                        # InlineKeyboardButton("قفل الملصقات", callback_data="mol"),
                        # InlineKeyboardButton("فتح الملصقات", callback_data="nmol"),
                    # ],
                    # [
                        # InlineKeyboardButton("قفل الروابط", callback_data="ahhoss"),
                        # InlineKeyboardButton("فتح الروابط", callback_data="cfsjkm"),
                    # ],
                    # [
                        # InlineKeyboardButton("قفل السب", callback_data="nnn"),
                        # InlineKeyboardButton("فتح السب", callback_data="fnnnn"),
                    # ],
                    # [
                        # InlineKeyboardButton("𝐬𝐨𝐮𝐫𝐜𝐞 𝐧𝐨𝐧𝐚", url="https://t.me/Elasyoutyyyy"),
                    # ],
                    # [
                        # InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{app.get_me().username}?startgroup=new"),
                    # ]
                # ]
            # ),
        # )
            
#الحمايه ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#الحمايه ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

# @app.on_message(filters.command(["mmk"], ""), group=85007761376662726)
# async def kggalid(client: Client, message: Message):
    # usr = await client.get_chat(message.from_user.id)
    # name = usr.first_name
    # user_id = message.from_user.id
    # get = await client.get_chat_member(message.chat.id, message.from_user.id)
    # if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 7728230165:
           # await message.reply_video(
            # video="https://graph.org/file/7ea7cf24b9536256880ad.mp4",
            # caption=f"""**⭓ᴍᴜˢɪᴄ♪✘⸢ᴠᴇɢᴧ♪\n╮⦿ مـرحبـا بـك: {message.from_user.mention}\n╯⦿ في اوامر الحمايه من جاك**""",
            # reply_markup=InlineKeyboardMarkup(
                # [
                    # [          
                    # InlineKeyboardButton(
                        # "« اوامر قفل »", callback_data="lockdd"),       
                    # InlineKeyboardButton(
                        # "« اوامر الادمن »", callback_data="abimnn"),
                # ],[
                    # InlineKeyboardButton(
                        # "« اوامر مالكين »", callback_data="Maalek"),
                # ],[        
                    # InlineKeyboardButton(
                       # "ᴠᴇɢᴧ", url=f"https://t.me/VeGaOne"),                        
                # ],
            # ]
        # ),
    # )
    # else:
        # await message.reply_text("هذا الامر يخص ❪الادمن وفوق❫ بس")




#تفعيل الحمايه  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#تفعيل الحمايه  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

# @app.on_message(filters.command(["تفعيل الحمايه","تفعيل الحماية"], ""), group=601123409006432)
# async def kggalid(client: Client, message: Message):
    # usr = await client.get_chat(message.from_user.id)
    # name = usr.first_name
    # chat_idd = message.chat.id
    # chat_name = message.chat.title
    # chat_username = f"@{message.chat.username}"
    # user_id = message.from_user.id
    # get = await client.get_chat_member(message.chat.id, message.from_user.id)
    # if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
       # photo = await client.download_media(message.chat.photo.big_file_id)
       # await message.reply_photo(photo=photo, caption=f"""**⭓ᴍᴜˢɪᴄ♪✘⸢ᴠᴇɢᴧ♪\n╮⦿ مـرحـبا بـك:. {message.from_user.mention}\n│᚜⦿ تم تفعيل الحمايه بنجاح\n│᚜⦿ في جروب: {chat_name}\n╯⦿ من سورس جاك**""",
        # reply_markup=InlineKeyboardMarkup(
            # [
                # [
                    # InlineKeyboardButton(
                        # "الاوامر", callback_data="Musicvega"),
                # ],[
                    # InlineKeyboardButton("ᴠᴇɢᴧ", url="https://t.me/VeGaOne"),
                    # ],
            # ]
        # ),
    # )
    # else:
        # await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")
        