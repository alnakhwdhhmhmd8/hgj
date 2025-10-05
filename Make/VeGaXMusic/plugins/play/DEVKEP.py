import asyncio
import re
import os
from os import getenv
import datetime

from VeGaXMusic.core.userbot import *
from datetime import datetime
from pyrogram import filters, enums

from dotenv import load_dotenv
from pyrogram import filters
from pyrogram import Client, filters
from datetime import datetime
from pyrogram import enums
from config import OWNER_ID
from pyrogram.types import (Message, InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from VeGaXMusic import app
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import *
from pyrogram.enums import ChatMembersFilter
import asyncio
import requests

import os
from inspect import getfullargspec
from pyrogram.types import CallbackQuery, InputMediaPhoto, Message, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

from pyrogram import filters
from pyrogram.types import Message
from VeGaXMusic.core.userbot import assistants

from VeGaXMusic import app
from VeGaXMusic.misc import SUDOERS
from VeGaXMusic.utils.database.assistantdatabase import get_client, get_assistant


from pyrogram import Client, filters
from VeGaXMusic import app
from config import OWNER_ID
from VeGaXMusic.utils.database.mongodatabase import get_served_chats, get_served_users, set_must, get_must, del_must, get_must_ch, set_must_ch
from VeGaXMusic.utils.database.memorydatabase import get_active_chats, remove_active_video_chat, remove_active_chat
import os 
from pyrogram.enums import ParseMode
import shutil
import asyncio 

from VeGaXMusic import app
from VeGaXMusic.core.call import KIM
from VeGaXMusic.utils.database.memorydatabase import set_loop
from VeGaXMusic.utils.decorators import AdminRightsCheck
from datetime import datetime
from VeGaXMusic.utils import bot_sys_stats
from VeGaXMusic.utils.decorators.language import language
import random
import time
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from aiohttp import ClientSession
from traceback import format_exc
import config
import re
import string
import lyricsgenius as lg
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
from VeGaXMusic.utils.database.memorydatabase import set_cmode
from VeGaXMusic.utils.decorators.admins import AdminActual
from VeGaXMusic import app
import platform
import re
import socket
import uuid
import os
import speedtest
import asyncio
import platform
from sys import version as pyver
from datetime import datetime
from config import STRING1, OWNER_ID, BOT_TOKEN

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid, FloodWait
from pyrogram.types import CallbackQuery, InputMediaPhoto, Message, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from pytgcalls.__version__ import __version__ as pytgver

from pyrogram import enums


import config
from config import OWNER_ID
from config import BANNED_USERS, MUSIC_BOT_NAME
from VeGaXMusic import YouTube, app
from VeGaXMusic import app as Client
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from pyrogram.errors import PeerIdInvalid
from config import  bot_id, db
from VeGaXMusic.core.userbot import assistants
from VeGaXMusic.misc import SUDOERS, pymongodb
from VeGaXMusic.plugins import ALL_MODULES
from VeGaXMusic.utils.database.mongodatabase import get_served_chats, get_served_users
from VeGaXMusic.utils.decorators.language import language, languageCB
from VeGaXMusic.utils.inline.stats import back_stats_buttons, stats_buttons

loop = asyncio.get_running_loop()


SUDORS = [OWNER_ID]


# Commands

def is_owner(_, __, message):

    return message.from_user.id == OWNER_ID


from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

import config
from VeGaXMusic import  app
from config import OWNER_ID
from config import BANNED_USERS, MUSIC_BOT_NAME


#مكاتب الصوره الجديده ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
import asyncio
import os
import random
import re
import textwrap
import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
from youtubesearchpython.__future__ import VideosSearch
import numpy as np

from config import YOUTUBE_IMG_URL


import asyncio
import os
import time
import requests
import datetime
import random
import os
import time
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram import enums, filters
from VeGaXMusic import app

from pytz import timezone
from pyrogram import enums
import aiohttp
import datetime
from pytz import timezone
from pyrogram import filters
from pyrogram import Client
from typing import Union
from random import choice
from config import OWNER_ID
from config import BANNED_USERS
from config import BANNED_USERS, OWNER_ID
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
from pyrogram import Client, filters
import re
from pyrogram.types import Message


import asyncio
from PIL import Image, ImageDraw, ImageFont
from pyrogram import filters, Client, enums
from pyrogram.types import *
from typing import Union, Optional
from VeGaXMusic import app as Hiroko 

# Function to get font and resize text



import requests
from PIL import Image
import os





def is_owner(_, __, message):
    if message.from_user is not None:
        return message.from_user.id == OWNER_ID
    else:
        return False




def is_owner(_, __, message):
    return getattr(message, 'from_user', None) is not None and message.from_user.id == OWNER_ID





OWNER_ID = getenv("OWNER_ID")

OWNER = getenv("OWNER")
               



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

     









@app.on_message(filters.command(["/start", "رجوع"], "") & filters.private, group=7262737)
async def kep(client, message):
    if message.from_user.id in SUDORS:
        kep = ReplyKeyboardMarkup([["قسم الشيخ"], ["قسم الاذاعه"], ["قسم البوت","قسم المساعد"], ["التواصل و الاحصائيات"], ["النسخه الاحتياطيه"], ["الاشتراك الاجباري"], ["تعليمات"], ["قفل الكيبورد"]], resize_keyboard=True)
        await message.reply_text("<b><blockquote>╮◉ مـرحـبآ بڪ عزيـزي المطـور الاساسـي\n╯◉ اليك كيب التحكم بالبوت من الشيخ</b></blockquote>", reply_markup=kep)



@app.on_message(filters.command(["قفل الكيبورد"], "") & filters.private, group=121314151615440)
async def keplook(client, message):
   if message.from_user.id in SUDORS:
        message = await message.reply("<b>╮◉ تم الغاء الكيبورد بنجاح\n╯◉ لظهره مره اخر » /start</b>", reply_markup= ReplyKeyboardRemove(selective=True))
   else:
        await message.reply("هذا الامر لا يخصك")



# قسم الشيخ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# قسم الشيخ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.command(["قسم الشيخ"], "") & filters.private, group=855400005)
async def cast(client, message):
 if message.from_user.id in SUDORS:
    kep = ReplyKeyboardMarkup([["ᴍᴀᴅᴏ","ᴍᴀᴅᴏ"], ["ꜱʜᴇɪᴋʜ"], ["المطور"], ["حول"], ["رجوع"]], resize_keyboard=True)
    await message.reply_text("<b><blockquote>╮◉ مـرحـبآ بك عزيزي المطور\n╯◉ هنا قسم الشيخ والمطورين</b></blockquote>", reply_markup=kep)
 

# قسم الاذاعه ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# قسم الاذاعه ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓




@app.on_message(filters.command(["قسم الاذاعه"], "") & filters.private, group=8055321)
async def cast(client, message):
 if message.from_user.id in SUDORS:
    kep = ReplyKeyboardMarkup([["إذاعة للجروبات"], ["إذاعة بالتوجيه للجروبات"], ["إذاعة للمستخدمين"], ["إذاعة بالتوجيه للمستخدمين"], ["إذاعة للقنوات"], ["إذاعة بالتوجيه للقنوات"], ["رجوع"]], resize_keyboard=True)
    await message.reply_text("<b><blockquote>╮◉ مـرحـبآ بك عزيزي المطور\n╯◉ هنا قسم الاذاعه من الشيخ</b></blockquote>", reply_markup=kep)
 else:
    await message.reply("هذا الامر لا يخصك")


# قسم المساعد ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# قسم المساعد ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓



@app.on_message(filters.command(["قسم المساعد"], "") & filters.private, group=1110340)
async def helpercn(client, message):
 if message.from_user.id in SUDORS:
   kep = ReplyKeyboardMarkup([["فحص المساعد"], ["اضف الاسم الاول","ازالة الاسم الاول"],["تغير يوزر المساعد"], ["اضف بايو","ازالة بايو"],["اضف الاسم التاني","ازالة الاسم التاني"], ["اضف صوره", "ازالة صوره"],["ازالة كل صور"], ["غادر القنوات","غادر الجروبات"], ["مغادره المساعد"], ["الغاء"], ["رجوع"]], resize_keyboard=True)
   await message.reply_text("<b><blockquote>╮◉ مـرحـبآ بك عزيزي المطور\n╯◉ هنا قسم المساعد من الشيخ</b></blockquote>", reply_markup=kep)
 else:
    await message.reply("هذا الامر لا يخصك")

# قسم البوت ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# قسم البوت ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.command(["قسم البوت"], "") & filters.private, group=1140)
async def booty(client, message):
 if message.from_user.id in SUDORS:
   kep = ReplyKeyboardMarkup([["تعين اسم البوت"], ["ترويج"], ["تفعيل الترويج","تعطيل الترويج"],["فحص البوت", "سرعه البوت"], ["معلومات التنصيب"], ["تحديث البوت"], ["الغاء"], ["رجوع"]], resize_keyboard=True)
   await message.reply_text("<b><blockquote>╮◉ مـرحـبآ بك عزيزي المطور\n╯◉ هنا قسم البوت من الشيخ</b></blockquote>", reply_markup=kep)
 else:
    await message.reply("هذا الامر لا يخصك")

# قسم التواصل ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# قسم التواصل ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
        
        
@app.on_message(filters.command(["التواصل و الاحصائيات"], "") & filters.private, group=80716)
async def cast(client, message):
 if message.from_user.id in SUDORS:
    kep = ReplyKeyboardMarkup([["الاحصائيات "], ["المجموعات","المستخدمين"], ["احصائيات عامه"], ["تفعيل التواصل", "تعطيل التواصل"], ["الغاء"], ["رجوع"]], resize_keyboard=True)
    await message.reply_text("<b><blockquote>╮◉ مـرحـبآ بك عزيزي المطور\n╯◉ هنا قسم • الاحصائيات من الشيخ</b></blockquote>", reply_markup=kep)
 else:
    await message.reply("هذا الامر لا يخصك")  
   
# قسم النسخه الاحطياطيه ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# قسم النسخه الاحطياطيه ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.command(["النسخه الاحتياطيه"], "") & filters.private, group=8066556774)
async def cast(client, message):
 if message.from_user.id in SUDORS:
    kep = ReplyKeyboardMarkup([["جلب نسخه للجروبات","رفع نسخه للجروبات"],["جلب نسخه للمستخدمين","رفع نسخه للمستخدمين"], ["جلب نسخه للقنوات","رفع نسخه للقنوات"], ["الغاء"], ["رجوع"]], resize_keyboard=True)
    await message.reply_text("<b><blockquote>╮◉ مـرحـبآ بك عزيزي المطور\n╯◉ هنا • قسم النسخه الاحتياطيه من الشيخ</b></blockquote>", reply_markup=kep)
 else:
    await message.reply("هذا الامر لا يخصك")

# قسم الاشتراك ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# قسم الاشتراك ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.command(["الاشتراك الاجباري"], "") & filters.private, group=8066993)
async def cast(client, message):
 if message.from_user.id in SUDORS:
    kep = ReplyKeyboardMarkup([["تفعيل الاشتراك العام", "تعطيل الاشتراك العام"], ["تفعيل الاشتراك برايفت", "تعطيل الاشتراك برايفت"], ["اضف قناه الاشتراك للتشغيل"], ["قناة الاشتراك", "حذف قناة الاشتراك"], ["تفعيل الاشتراك للتشغيل", "تعطيل الاشتراك للتشغيل"], ["الغاء"], ["رجوع"]], resize_keyboard=True)
    await message.reply_text("<b><blockquote>╮◉ مـرحـبآ بك عزيزي المطور\n╯◉ هنا قسم الاشتراك الاجباري من الشيخ</b></blockquote>", reply_markup=kep)
 else:
    await message.reply("هذا الامر لا يخصك")


@app.on_message(filters.command(["الاحصائيات"], "") & filters.private, group=7111655578)
async def get_ehs(client, message):
  if message.from_user.id in SUDORS:
    text = f'<blockquote><b>مرحبا بك في الاحصائيات البوت من الشيخ</b>\n\n</blockquote>'
    text += f'<blockquote>1: عدد المستخدمين: {len(users)}\n</blockquote>'
    text += f'<blockquote>2: عدد المجموعات: {len(groups)}\n</blockquote>'
    text += f'<blockquote>3: عدد القنوات: {len(channel)}</blockquote>'
    await message.reply(text)    
  else:
       await message.reply("هذا الامر لا يخصك")






    #اذاه للمستخدمين  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

    #اذاه للمستخدمين  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


file_path = "users.txt"

def load_users_data():
    users = set()
    try:
        with open("users.txt", "r") as file:
            for line in file:
                user_id = line.strip()
                users.add(user_id)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Error loading user data: {e}")
    return users

def save_users(users):
    try:
        with open("users.txt", "w") as file:
            for item in users:
                file.write(f"{item}\n")
    except Exception as e:
        print(f"Error saving user data: {e}")

users = load_users_data()
 

@app.on_message(filters.text & filters.private, group=625447854)
async def users_me(client, message):
    user_id = str(message.from_user.id)
    if user_id not in users:
        users.add(user_id)
        save_users(users)
        text = '🙍 شخص جديد دخل الى البوت !\n\n'
        text += f'🎯 الأسم: {message.from_user.first_name}\n'
        text += f'♻️ الايدي: {message.from_user.id}\n\n'
        text += f'🌐 اصبح عدد المستخدمين: {len(users)}'
        await app.send_message(OWNER_ID, text)

 



@app.on_message(filters.command("رفع نسخه للمستخدمين", "") & filters.private, group=827178363666)
async def start_users(client, message):
    if message.from_user.id in SUDORS: 

        ask = await app.ask(message.chat.id, "ارسل الملف المراد رفعه", timeout=300)
        if ask and ask.document:
            try:
                file_path = await ask.download("./users.txt")
                with open(file_path, "r") as file:
                    users = set(file.read().splitlines())
                    for chat_id in users:
                        if chat_id not in users:
                            users.append(chat_id)
                    save_users(users)
                    await app.send_message(message.chat.id, f" تم رفع نسخة للمستخدمين بنجاح وعددها : {len(users)}")
            except Exception as e:
                print(f"فشل في فتح ملف للمستخدمين: {e}")
        else:
            await app.send_message(message.chat.id, "يجب أن يكون للمستخدمين بصيغة نصية (.txt)")
    



@app.on_message(filters.command(["جلب نسخه للمستخدمين"], "") & filters.private, group=7842873644343)
async def get_users_backup(client, message: Message):
 if message.from_user.id in SUDORS:

    try:
        with open("users.txt", "r") as file:
            users = file.readlines()
            user_count = len(users)

            if user_count > 0:
                await message.reply_document(document="users.txt")
                await message.reply_text(f"تم جلب {len(users)} من المستخدمين")
            else:
                await message.reply_text("لا يوجد المستخدمين لجلبهم")
    except FileNotFoundError:
        await message.reply_text("فشل في جلب ملف القنوات:")
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")




@app.on_message(filters.command(["إذاعة للمستخدمين"], "") & filters.private, group=544444544)
async def broadcaast_users_message(client, message):
 if message.from_user.id in SUDORS:

    ask = await app.ask(message.chat.id, "ارسل النص المراد اذاعته", timeout=300)
    text = ask.text
    ask = await app.ask(message.chat.id, "اذا كنت تريد الاذاعه بالتثبيت ارسل نعم", timeout=300)
    pin_message = ask.text.lower() == "نعم"
    for user_id in users:
        try:
            if pin_message:
                dd = await app.send_message(user_id, text)
                await dd.pin(disable_notification=False,both_sides=True)
            else:
                await app.send_message(user_id, text)
        except Exception as e:
            print(f"Error sending message to user {user_id}: {e}")
    await message.reply("• تم الإذاعة بنجاح", quote=True)
 else:
        await message.reply("هذا الامر لا يخصك")



@app.on_message(filters.command(["إذاعة بالتوجيه للمستخدمين"], "") & filters.private, group=548178744544)
async def broadcast_mese_message(client, message):
 
 if message.from_user.id in SUDORS:
    forwarded_message = await app.ask(message.chat.id, "• ارسل الرسالة الموجهة الآن", timeout=300)
    if forwarded_message:
        for user_id in users:
            try:
                await forwarded_message.forward(int(user_id))
            except Exception as e:
                print(f"Error sending message to {user_id}: {e}")
        await message.reply("• تم الإذاعة بنجاح", quote=True)
    else:
        await message.reply("• لم يتم إرسال أي رسالة موجهة", quote=True)
 else:
        await message.reply("هذا الامر لا يخصك")



    #اذاه للجروبات  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

    #اذاه للجروبات  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓



file_path = "groups.txt"

def load_groups_data():
    groups = set()
    try:
        with open("groups.txt", "r") as file:
            for line in file:
                group_id = line.strip()
                groups.add(group_id)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Error loading user data: {e}")
    return groups

def save_groups(groups):
    try:
        with open("groups.txt", "w") as file:
            for item in groups:
                file.write(f"{item}\n")
    except Exception as e:
        print(f"Error saving user data: {e}")

def delete_group(group_id):
    try:
        groups = load_groups_data()
        if group_id in groups:
            groups.remove(group_id)
            save_groups(groups)
            print(f"Deleted group {group_id} from the file.")
        else:
            print(f"Group {group_id} not found in the file.")
    except Exception as e:
        print(f"Error deleting group {group_id}: {e}")

groups = load_groups_data()



@app.on_raw_update(group=7)
async def kick_from_hgroup(app: Client, m: Update, _, __):
   try:
     name = re.search(r"first_name='([^']+)'", str(_)).group(1)
     title = re.search(r"title='([^']+)'", str(__)).group(1)
     if m.new_participant:
      get = await app.get_me()
      if m.new_participant.peer.user_id == get.id:
        print("🌀")
      else:  return 
      if m.new_participant.kicked_by:
        print("🌀")
      delete_group(str(f'-100{m.channel_id}'))
      text = '• تم طرد البوت من مجموعة:\n\n'
      text += f'• اسم الي طردني : [{name}](tg://user?id={m.new_participant.kicked_by})\n'
      text += f'• ايدي الي طردني : {m.new_participant.kicked_by}\n'
      text += f'\n• معلومات المجموعة: \n'
      text += f'\n• ايدي المجموعة: `-100{m.channel_id}`'
      text += f'\n• اسم المجموعه: {title}'
      text += '\n• تم مسح جميع بيانات الجروب'
      await app.send_message(OWNER_ID, text)
   except:
     pass



@app.on_message(filters.text & filters.group, group=625414788854)
async def groupsss_me(client, message):
    group_id = str(message.chat.id)
    if group_id not in groups:
        groups.add(group_id)
        save_groups(groups)
        text = '• تم تفعيل البوت في مجموعة جديدة\n'
        text += f'• اسم المجموعة: {message.chat.title}\n'
        if message.chat.username:
            text += f'• رابط المجموعة: https://t.me/{message.chat.username}\n'
        text += '\n• معلومات الذي قام بتفعيلي:\n'
        text += f'• اسمهم: {message.from_user.mention}\n'
        text += f'• الايدي: {message.from_user.id}\n'
        text += f'\n• عدد الجروبات الآن : {len(groups)}'
        await app.send_message(OWNER_ID, text)





@app.on_message(filters.command("رفع نسخه للجروبات", "") & filters.private, group=8996656)
async def stasrt_groupss(client, message):
    
    if message.from_user.id in SUDORS:
        ask = await app.ask(message.chat.id, "ارسل  الملف المراد رفعه", timeout=300)
        if ask and ask.document:
            try:
                file_path = await ask.download("./groups.txt")
                with open(file_path, "r") as file:
                    groups = set(file.read().splitlines())
                    for chat_id in groups:
                        if chat_id not in groups:
                            groups.append(chat_id)
                    save_groups(groups)
                    await app.send_message(message.chat.id, f"تم رفع نسخة للجروبات بنجاح وعددها : {len(groups)}")
            except Exception as e:
                print(f"فشل في فتح ملف للجروبات: {e}")
        else:
            await app.send_message(message.chat.id, "الرجاء الرد على رسالة النسخة المراد رفعها")
    else:
        await message.reply("هذا الامر لا يخصك")


@app.on_message(filters.command(["جلب نسخه للجروبات"], "") & filters.private, group=711249843)
async def gt_grrrs_backup(client, message: Message):
 if message.from_user.id in SUDORS:

    try:
        with open("groups.txt", "r") as file:
            groups = file.readlines()
            group_count = len(groups)

            if group_count > 0:
                await message.reply(f"تم جلب  {group_count} من الجروبات")
                with open("groups.txt", "rb") as backup_file:
                    await message.reply_document(document=backup_file)
            else:
                await message.reply(".لا توجد مجموعات متاحة")
    except FileNotFoundError:
        await message.reply(".ملف المجموعات غير موجود")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")
 else:
        await message.reply("هذا الامر لا يخصك")




@app.on_message(filters.command(["إذاعة للجروبات"], "") & filters.private, group=512531544)
async def brossst_groups_mesage(client, message):
 
 if message.from_user.id in SUDORS:
    ask = await app.ask(message.chat.id, "ارسل النص المراد اذاعته", timeout=300)
    text = ask.text
    ask = await app.ask(message.chat.id, "اذا كنت تريد الاذاعه بالتثبيت ارسل نعم", timeout=300)

    pin_message = ask.text.lower() == "نعم"

    for group_id in groups:
        try:
            if pin_message:
                dd = await app.send_message(group_id, text)
                await dd.pin(disable_notification=False,both_sides=True)
            else:
                await app.send_message(group_id, text)
        except Exception as e:
            print(f"Error sending message to user {group_id}: {e}")
    await message.reply("• تم الإذاعة بنجاح", quote=True)
 else:
        await message.reply("هذا الامر لا يخصك") 





@app.on_message(filters.command(["إذاعة بالتوجيه للجروبات"], "") & filters.private, group=5497828544)
async def brosaast_me_message(client, message):
 if message.from_user.id in SUDORS:

    forwarded_message = await app.ask(message.chat.id, "• ارسل الرسالة الموجهة الآن", timeout=300)
    if forwarded_message:
        for group_id in groups:
            try:
                await forwarded_message.forward(int(group_id))
            except Exception as e:
                print(f"Error sending message to {group_id}: {e}")
        await message.reply("• تم الإذاعة بنجاح", quote=True)
    else:
        await message.reply("• لم يتم إرسال أي رسالة موجهة", quote=True)
 else:
        await message.reply("هذا الامر لا يخصك")



    #اذاه للقنوات  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

    #اذاه للقنوات  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


import os
from pyrogram import Client, filters
from pyrogram.types import Message

file_path = "channel.txt"

def load_channel_data():
    channels = set()
    try:
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    user_id = line.strip()
                    if user_id:  # تأكد من أن السطر ليس فارغًا
                        channels.add(user_id)
    except Exception as e:
        print(f"حدث خطأ أثناء تحميل بيانات القنوات: {e}")
    return channels

def save_channel(channels):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            for item in channels:
                file.write(f"{item}\n")
    except Exception as e:
        print(f"حدث خطأ أثناء حفظ بيانات القنوات: {e}")

channels = load_channel_data()

@app.on_message(filters.text & filters.channel, group=625454)
async def channel_group(client, message):
    chat_id = str(message.chat.id)
    if chat_id not in channels:
        channels.add(chat_id)
        save_channel(channels)
        text = '• تم اضافة البوت الى قناه جديدة\n'
        text += f'• اسم القناه: {message.chat.title}\n'
        if message.chat.username:
            text += f'• رابط القناة: https://t.me/{message.chat.username}\n'
        text += f'\n• عدد القنوات الآن: {len(channels)}'
        await app.send_message(OWNER_ID, text)

@app.on_message(filters.command("رفع نسخه للقنوات", "") & filters.private)
async def upload_channels_backup(client, message: Message):
    if message.from_user.id not in SUDORS:
        return await message.reply("⚠️ هذا الأمر لا يخصك")
    
    ask = await app.ask(
        message.chat.id,
        "📤 يرجى إرسال الملف الذي يحتوي على نسخة القنوات",
        timeout=300
    )
    
    if not ask.document:
        return await message.reply("❌ يجب أن يكون الملف مرسل كوثيقة")
    
    try:
        downloaded_file = await ask.download(file_path)
        updated_channels = load_channel_data()
        await message.reply(f"✅ تم تحديث نسخة القنوات بنجاح\nعدد القنوات الآن: {len(updated_channels)}")
    except Exception as e:
        await message.reply(f"❌ فشل في تحديث ملف القنوات:\n{str(e)}")

@app.on_message(filters.command("جلب نسخه للقنوات", "") & filters.private)
async def download_channels_backup(client, message: Message):
    if message.from_user.id not in SUDORS:
        return await message.reply("⚠️ هذا الأمر لا يخصك")
    
    if not os.path.exists(file_path):
        return await message.reply("❌ لا يوجد ملف للقنوات بعد")
    
    try:
        channel_count = len(load_channel_data())
        if channel_count == 0:
            return await message.reply("❌ لا توجد قنوات مسجلة بعد")
            
        await message.reply_document(
            document=file_path,
            caption=f"📊 إحصائيات القنوات:\nعدد القنوات: {channel_count}"
        )
    except Exception as e:
        await message.reply(f"❌ فشل في جلب ملف القنوات:\n{str(e)}")




@app.on_message(filters.command(["إذاعة للقنوات"], "") & filters.private, group=54544)
async def broadcast_message(client, message):
 
 if message.from_user.id in SUDORS:
    ask = await app.ask(message.chat.id, "ارسل النص المراد اذاعته", timeout=300)
    text = ask.text
    ask = await app.ask(message.chat.id, "اذا كنت تريد الاذاعه بالتثبيت ارسل نعم", timeout=300)
    pin_message = ask.text.lower() == "نعم"
    for chat_id in channel:
        try:
            sent_message = await app.send_message(int(chat_id), f"{text}")
            if pin_message:
                await sent_message.pin()
        except Exception as e:
            print(f"Error sending message to {chat_id}: {e}")
 else:
        await message.reply("هذا الامر لا يخصك")


@app.on_message(filters.command(["إذاعة بالتوجيه للقنوات"], "") & filters.private, group=548787544)
async def broadcast_mee_message(client, message):
 if message.from_user.id in SUDORS:
 
    forwarded_message = await app.ask(message.chat.id, "• ارسل الرسالة الموجهة الآن", timeout=300)
    if forwarded_message:
        for user in channel:
            try:
                await forwarded_message.forward(int(user))
            except Exception as e:
                print(f"Error sending message to {user}: {e}")
        await message.reply("• تم الإذاعة بنجاح", quote=True)
    else:
        await message.reply("• لم يتم إرسال أي رسالة موجهة", quote=True)
 else:
        await message.reply("هذا الامر لا يخصك")



@app.on_message(filters.text & filters.private, group=5662)
async def cmd(app, msg):
    if msg.from_user.id in SUDORS:
        db.delete(f"{msg.from_user.id}:fbroadcast:{bot_id}")
        db.delete(f"{msg.from_user.id}:pinbroadcast:{bot_id}")
        db.delete(f"{msg.from_user.id}:broadcast:{bot_id}")
        db.delete(f"{msg.from_user.id}:users_up:{bot_id}")

    if msg.text == "تفعيل التواصل":
        if not db.get(f"{msg.from_user.id}:twasl:{bot_id}"):
            await msg.reply("» تم تفعيل التواصل", quote=True)
            db.set(f"{msg.from_user.id}:twasl:{bot_id}", 1)
        else:
            await msg.reply("» التواصل مفعل من قبل", quote=True)

    if msg.text == "تعطيل التواصل":
        if db.get(f"{msg.from_user.id}:twasl:{bot_id}"):
            await msg.reply("» تم تعطيل التواصل", quote=True)
            db.delete(f"{msg.from_user.id}:twasl:{bot_id}")
        else:
            await msg.reply("» التواصل غير مفعل", quote=True)


@app.on_message(filters.private, group=793874)
async def twasl(app, msg):
	if msg.from_user.id not in SUDORS:
		for user in SUDORS:
			if db.get(f"{user}:twasl:{bot_id}"):
				await msg.forward(user)
	if msg.from_user.id in SUDORS:
		if msg.reply_to_message:
			if msg.reply_to_message.forward_from:
				try:
					await msg.copy(msg.reply_to_message.forward_from.id)
					await msg.reply(f"╮◉ تم إرسال رسالتك إلى {msg.reply_to_message.forward_from.first_name}\n╯◉ بنجاح", quote=True)
				except Exception as Error:
					await msg.reply(f"• لم يتم ارسال رسالتك بسبب: {str(Error)}", quote=True)
					pass
        
        

assistants = []

@app.on_message(filters.command("فحص المساعد", "") & filters.private, group=8073476566)
async def userrrrr(client, message):
    if message.from_user.id in SUDORS:
        msg = await message.reply_text("🔎")
        start = datetime.datetime.now()
        u = g = sg = c = b = a_chat = 0
        
        
        assistant_client = await get_client(1)
        Meh = await assistant_client.get_me()  
        
       
        photo = None
        try:
            profile_photos = []
            async for photo_obj in assistant_client.get_chat_photos("me", limit=1):
                profile_photos.append(photo_obj)
                break
            
            if profile_photos:
                photo_path = await assistant_client.download_media(profile_photos[0].file_id)
                photo = photo_path if os.path.exists(photo_path) else None
        except Exception as e:
            print(f"Error getting profile photo: {str(e)}")
        
        # معلومات المساعد (تم التصحيح هنا)
        assistant_name = Meh.first_name or "المساعد"
        assistant_username = f"@{Meh.username}" if Meh.username else "لا يوجد معرف"
        assistant_id = Meh.id
        assistant_url = f"https://t.me/{Meh.username}" if Meh.username else f"tg://user?id={Meh.id}"

        

        async for dialog in assistant_client.get_dialogs():
            try:
                if dialog.chat.type == enums.ChatType.PRIVATE:
                    u += 1
                elif dialog.chat.type == enums.ChatType.BOT:
                    b += 1
                elif dialog.chat.type == enums.ChatType.GROUP:
                    g += 1
                elif dialog.chat.type == enums.ChatType.SUPERGROUP:
                    sg += 1
                    try:
                        user_s = await assistant_client.get_chat_member(dialog.chat.id, "me")
                        if user_s.status in (
                            enums.ChatMemberStatus.OWNER,
                            enums.ChatMemberStatus.ADMINISTRATOR,
                        ):
                            a_chat += 1
                    except:
                        continue
                elif dialog.chat.type == enums.ChatType.CHANNEL:
                    c += 1
            except Exception as e:
                print(f"Error processing chat: {str(e)}")

        end = datetime.datetime.now()
        assistants.append(1)
        ms = (end - start).seconds
        
        caption = f"""
<b> ˚‧SHEIKH˳+\n
╮◉ احصائيات المساعد [{ms}] ثانيه
│᚜◉ اسم المساعد: {assistant_name}
│᚜◉ معرف المساعد: {assistant_username}
│᚜◉ ايدي المساعد: {assistant_id}
│᚜◉ يمتلك [{u}] رساله في الخاص
│᚜◉ موجود في [{g}] مجموعه
│᚜◉ موجود في [{sg}] مجموعه خارقه
│᚜◉ موجود في [{c}] قناه
│᚜◉ ادمن في [{a_chat}] جروب
╯◉ البوتات [{b}]
</b>"""
        
        try:
            if photo:
                await message.reply_photo(
                    photo=photo,
                    caption=caption,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("ꜱʜᴇɪᴋʜ", url=SUPPORT_CHANNEL),
                                InlineKeyboardButton(assistant_name, url=assistant_url)
                            ]
                        ]
                    )
                )
                os.remove(photo)
            else:
                await message.reply_text(
                    text=caption,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("ꜱʜᴇɪᴋʜ", url=SUPPORT_CHANNEL),
                                InlineKeyboardButton(assistant_name, url=assistant_url)
                            ]
                        ]
                    )
                )
        except Exception as e:
            print(f"Error sending message: {str(e)}")
            await message.reply_text(caption)
        
        await msg.delete()
    else:
        await message.reply("هذا الامر لا يخصك")
        
        
        
        
@app.on_message(filters.command(["غادر الجروبات"], "") & filters.private, group=8073476566)
async def kickmeall(client, message: Message):
 if message.from_user.id in SUDORS:

    ss = await message.reply_text("جاري مغادرة المحادثات...")
    er = 0
    done = 0
    client = await get_client(1)
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except Exception as e: 
                er += 1
                print(f"Error leaving group {chat}: {e}") 
    await ss.edit_text(
        f"<code>تم مغادره المساعد من : {done} مجموعه بنجاح</code>"
    )
 else:
        await message.reply("هذا الامر لا يخصك")

@app.on_message(filters.command(["غادر القنوات"], "") & filters.private, group=8073566)
async def kickmeall(client, message: Message):
 if message.from_user.id in SUDORS:

    oo = await message.reply_text("جاري مغادرة القنوات...")
    er = 0
    done = 0
    client = await get_client(1) 
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL,): 
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except Exception as e: 
                er += 1
                print(f"Error leaving group {chat}: {e}")  
    await oo.edit_text(
        f"<code>تم مغادره المساعد من : {done} قناه بنجاح</code>"
    )

 else:
        await message.reply("هذا الامر لا يخصك")



@app.on_message(filters.command(["اضف صوره"], "") , group=8123456433578906)
async def set_pfp(client, message):
 if message.from_user.id in SUDORS:

    from VeGaXMusic.core.userbot import assistants

    if not message.reply_to_message or not message.reply_to_message.photo:
        return await eor(message, text="قم بالرد بي : <code>اضف صوره</code>")
    for num in assistants:
        client = await get_client(num)
        photo = await message.reply_to_message.download()
        try:
            await client.set_profile_photo(photo=photo)
            await eor(message, text="تم اضافه صوره للمساعد بنجاح")
            os.remove(photo)
        except Exception as e:
            await eor(message, text=e)
            os.remove(photo)
 else:
        await message.reply("هذا الامر لا يخصك")

@app.on_message(filters.command(["ازالة صوره"], "") & filters.private, group=8123456433578906)
async def del_pfp(client, message):
 
 if message.from_user.id in SUDORS:

    from VeGaXMusic.core.userbot import assistants

    for num in assistants:
        client = await get_client(num)
        photos = [p async for p in client.get_chat_photos("me")]
        try:
            if photos:
                await client.delete_profile_photos(photos[0].file_id)
                await eor(message, text="تم حذف صوره المساعد بنجاح")
            else:
                await eor(message, text="حدث خطاء اثناء الاحذف")
        except Exception as e:
            await eor(message, text=e)
 else:
        await message.reply("هذا الامر لا يخصك")

@app.on_message(filters.command(["ازالة كل صور"], "") & filters.private, group=81234433578906)
async def del_pfp(client, message):
 if message.from_user.id in SUDORS:

    from VeGaXMusic.core.userbot import assistants

    for num in assistants:
        assistant_client = await get_client(num)  
        photos = [p async for p in assistant_client.get_chat_photos("me")]
        try:
            if photos:
                for photo in photos:
                    await assistant_client.delete_profile_photos(photo.file_id)
                await eor(message, text="تم حذف كل صور المساعد بنجاح")
            else:
                await eor(message, text="حدث خطاء اثناء الاحذف")
        except Exception as e:
            await eor(message, text=str(e)) 

 else:
        await message.reply("هذا الامر لا يخصك")

@app.on_message(filters.command(["اضف الاسم الاول"], "") & filters.private, group=8123456433578906)
async def set_name(client, message):
 if message.from_user.id in SUDORS:

    from VeGaXMusic.core.userbot import assistants

    if not message.reply_to_message or not message.reply_to_message.text:
        return await eor(message, text="قم بالرد بي : <code> اضف الاسم الاول </code>")

    name = message.reply_to_message.text  # Move this line outside the if block
    for num in assistants:
        client = await get_client(num)
        try:
            await client.update_profile(first_name=name)
            await eor(message, text=f"تم اضافه الاسم الاول  بنجاح :  {name} .")
        except Exception as e:
            await eor(message, text=e)
 else:
        await message.reply("هذا الامر لا يخصك")



@app.on_message(filters.command(["ازالة الاسم الاول"], "") & filters.private, group=8123456433578906)
async def delete_name(client, message):
 if message.from_user.id in SUDORS:

    
    for num in assistants:
        client = await get_client(num)
        try:
            await client.update_profile(first_name="`")
            await eor(message, text="تم حذف الاسم الاول  بنجاح")
        except Exception as e:
            await eor(message, text=f"خطاااء: {e}")
 else:
        await message.reply("هذا الامر لا يخصك")



@app.on_message(filters.command(["اضف الاسم التاني"], "") & filters.private, group=8456433578906)
async def set_name(client, message):
 if message.from_user.id in SUDORS:

    from VeGaXMusic.core.userbot import assistants

    if not message.reply_to_message or not message.reply_to_message.text:
        return await eor(message, text="قم بالرد بي : <code>اضف الاسم تاني</code>")

    for num in assistants:
        client = await get_client(num)
        my_name = message.reply_to_message.text
        try:
            await client.update_profile(last_name=my_name)
            await eor(message, text=f"تم اضافه الاسم التاني بنجاح : {my_name}.")
        except Exception as e:
            await eor(message, text=f"An error occurred: {str(e)}")
 else:
        await message.reply("هذا الامر لا يخصك")


@app.on_message(filters.command(["ازالة الاسم التاني"], "") & filters.private, group=8123456433578906)
async def delete_name(client, message):
 if message.from_user.id in SUDORS:

    for num in assistants:
        client = await get_client(num)
        try:
            await client.update_profile(last_name="`")
            await eor(message, text="تم حذف الاسم التاني بنجاح")
        except Exception as e:
            await eor(message, text=f"Error: {e}")
 else:
        await message.reply("هذا الامر لا يخصك")

        


@app.on_message(filters.command(["اضف بايو"], "") & filters.private, group=8123456433578906)
async def set_bio(client, message):
 if message.from_user.id in SUDORS:

    from VeGaXMusic.core.userbot import assistants

    if not message.reply_to_message or not message.reply_to_message.text:
        return await eor(message, text=" قم بالرد بي : <code>اضف بايو</code>")
    
    bio = message.reply_to_message.text
    for num in assistants:
        client = await get_client(num)
        try:
            await client.update_profile(bio=bio)
            await eor(message, text="تم اضافه بايو  بنجاح")
        except Exception as e:
            await eor(message, text=e)
 else:
        await message.reply("هذا الامر لا يخصك")



@app.on_message(filters.command(["ازالة بايو"], "") & filters.private, group=8123456433578906)
async def delete_name(client, message):
 if message.from_user.id in SUDORS:

    for num in assistants:
        client = await get_client(num)
        try:
            await client.update_profile(bio="")
            await eor(message, text="تم حذف بايو بنجاح")
        except Exception as e:
            await eor(message, text=f"خطاااء: {e}")
 else:
        await message.reply("هذا الامر لا يخصك")


@app.on_message(filters.command(["تغير يوزر المساعد", "اليوزر"], "") & filters.private, group=800009666)
async def changeusername(client, message):
 if message.from_user.id in SUDORS:

   try:
    if message.text == "تغير يوزر المساعد":
      return await message.reply_text("• الان قم بالرد علي اليوزر الجديد بدون علامة @ باستخدام كلمه اليوزر •")
    name = message.reply_to_message.text
    client = await get_client(1)
    await client.set_username(name)
    await message.reply_text("<b>تم تغير الاسم المستخدم بنجاح .</b>")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير الاسم المستخدم")
 else:
        await message.reply("هذا الامر لا يخصك")

    



async def eor(msg: Message, **kwargs):
    func = (
        (msg.edit_text if msg.from_user.is_self else msg.reply)
        if msg.from_user
        else msg.reply
    )
    spec = getfullargspec(func.__wrapped__).args
    return await func(**{k: v for k, v in kwargs.items() if k in spec})





@app.on_message(filters.command(["تنظيف"], "") & filters.private, group=8045679008654326)
async def clean(client, message):
    try:
        await message.delete()
    except:
        pass
    downloads = os.path.realpath("downloads")
    down_dir = os.listdir(downloads)
    pth = os.path.realpath(".")
    os_dir = os.listdir(pth)

    if down_dir:
        for file in down_dir:
            os.remove(os.path.join(downloads, file))
    if os_dir:
        for lel in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg *.png")
    await message.reply_text("» تم تنظيف تخزين البوت بنجاح")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("<b>⇆ يتم تنزيل موارد ...</b>")
        test.download()
        m = m.edit("<b>⇆ جاري بداء الفحص...</b>")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("<b>↻ يرجئ الانتظار...</b>")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(["سرعه البوت"], "") & filters.private, group=866543450098706)
async def spedtest(client, message):
    m = await message.reply("🔎")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""<b>لوحه التحكم بسرعه البوت من الشيخ<b>
    
<u><b>❥͜͡ᴄʟɪᴇɴᴛ»ꜱʜᴇɪᴋʜ </b></u>
<b>╭◉ ɪsᴩ </b> {result['client']['isp']}
<b>╰◉ ᴄᴏᴜɴᴛʀʏ </b> {result['client']['country']}
  
<u><b>❥͜͡sᴇʀᴠᴇʀ»ꜱʜᴇɪᴋʜ </b></u>
<b>╭◉  ɴᴀᴍᴇ </b> {result['server']['name']}
<b>│᚜◉ ᴄᴏᴜɴᴛʀʏ </b> {result['server']['country']}, {result['server']['cc']}
<b>│᚜◉ sᴩᴏɴsᴏʀ </b> {result['server']['sponsor']}
<b>│᚜◉ ʟᴀᴛᴇɴᴄʏ </b> {result['server']['latency']}  
<b>╰◉  ᴩɪɴɢ </b> {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=result["share"], caption=output
    )
    await m.delete()


@app.on_message(filters.command(["فحص البوت"], "") & filters.private, group=80600998767755664446)
async def serverinfoo(client, message):
    sysrep = await message.reply("🔎")
    try:
        await message.delete()
    except:
        pass
    SUDORS = len(SUDORS)
    mod = len(ALL_MODULES)
    hostname = socket.gethostname()
    bot_username = client.me.username
    bot_user = await client.get_me()
    bot_name = bot_user.first_name
    bot_id = bot_user.id
    user = await client.get_users(bot_user.id)
    usr = await client.get_chat(message.from_user.id)
    owner = user.first_name
    name = user.first_name
    username = user.username
    ip_address = socket.gethostbyname(socket.gethostname())
    architecture = platform.machine()
    processor = platform.processor()
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    sp = platform.system()
    ram = str(round(psutil.virtual_memory().total / (1024.0**3))) + " ɢʙ"
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}ɢʜᴢ"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}ᴍʜᴢ"
    except:
        cpu_freq = "ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    total = str(total)
    used = hdd.used / (1024.0**3)
    used = str(used)
    free = hdd.free / (1024.0**3)
    free = str(free)
    platform_release = platform.release()
    platform_version = platform.version()

    await sysrep.edit_text(
        f"""<b>
➻ <u><b>{MUSIC_BOT_NAME} sʏsᴛᴇᴍ sᴛᴀᴛs<b></u>

<b>╭◉  ᴩʏᴛʜᴏɴ </b> {pyver.split()[0]}
<b>│᚜◉ ᴩʏʀᴏɢʀᴀᴍ </b> {pyrover}
<b>│᚜◉ ᴩʏ-ᴛɢᴄᴀʟʟs </b> {pytgver}
<b>│᚜◉ sᴜᴅᴏᴇʀs </b> {SUDORS}
<b>╰◉  ᴍᴏᴅᴜʟᴇs </b> {mod}

<b>╭◉  ɪᴘ </b> 127.0.1.1.8
<b>│᚜◉ ᴍᴀᴄ </b> {mac_address}
<b>│᚜◉ ʜᴏsᴛɴᴀᴍᴇ </b> VeGaXMusic
<b>│᚜◉ ᴘʟᴀᴛғᴏʀᴍ </b> {sp}
<b>│᚜◉ ᴘʀᴏᴄᴇssᴏʀ </b> {processor}
<b>│᚜◉ ᴀʀᴄʜɪᴛᴇᴄᴛᴜʀᴇ </b> {architecture}
<b>╰◉  ᴘʟᴀᴛғᴏʀᴍ ʀᴇʟᴇᴀsᴇ </b> {platform_release}

        <b><u>sᴛᴏʀᴀɢᴇ</b><u/>
<b>╭◉  ᴀᴠᴀɪʟᴀʙʟᴇ </b> {total[:4]} ɢɪʙ
<b>│᚜◉ ᴜsᴇᴅ </b> {used[:4]} ɢɪʙ
<b>╰◉  ғʀᴇᴇ </b> {free[:4]} ɢɪʙ

<b>╭◉  ʀᴀᴍ </b> 64 ɢɪʙ
<b>│᚜◉ ᴩʜʏsɪᴄᴀʟ ᴄᴏʀᴇs :</b> {p_core}
<b>│᚜◉ ᴛᴏᴛᴀʟ ᴄᴏʀᴇs :</b> {t_core}
<b>╰◉  ᴄᴩᴜ ғʀᴇǫᴜᴇɴᴄʏ :</b> {cpu_freq}</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="ᴄʟᴏsᴇ",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        ),
    )






##معلومات التنصيب ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
##معلومات التنصيب ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
##معلومات التنصيب ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


get_font = lambda font_size, font_path: ImageFont.truetype(font_path, font_size)
resize_text = (
    lambda text_size, text: (text[:text_size] + "...").upper()
    if len(text) > text_size
    else text.upper()
)


async def get_kamalbot_img2(
    bg_path: str,
    font_path: str,
    bot_id: Union[int, str],
    bot_username: Union[int, str],    
    bot_name: Union[int, str],
    bot_user: Union[int, str],
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
        text=str(bot_id).upper(),
        font=get_font(46, font_path),
        fill=(255, 255, 255),
    )

    path = f"./userinfo_img_{bot_id}.png"
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


def get_kamalbot_img(
    bg_path: str,
    font_path: str,
    bot_username: Union[int, str],    
    bot_id: Union[int, str],
    bot_name: Union[int, str],
    bot_user: Union[int, str],
    profile_path: Optional[str] = None
):
    try:
            if os.path.isfile(f"cache/{bot_id}.jpg"):
               return profile_path
            youtube = Image.open(profile_path)
            image1 = changeImageSize(1280, 720, youtube)
            image2 = image1.convert("RGBA")
            background = image2.filter(filter=ImageFilter.BoxBlur(5))
            enhancer = ImageEnhance.Brightness(background)
            background = enhancer.enhance(0.6)
            image2 = background

            circle = Image.open("assets/kamall.png")

            # تغيير لون الدائرة
            im = circle
            im = im.convert("RGBA")
            color = make_col()

            data = np.array(im)
            black, lead, blue, alpha = data.T

            white_areas = (black == 150) & (blue == 150) & (lead == 150)
            data[..., :-1][white_areas.T] = color

            im2 = Image.fromarray(data)
            circle = im2
            # منتهي

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

            # الخطوط
            font1 = ImageFont.truetype("assets/font2.ttf", 30)
            font2 = ImageFont.truetype("assets/font2.ttf", 70)
            font3 = ImageFont.truetype("assets/font2.ttf", 40)
            font4 = ImageFont.truetype("assets/font2.ttf", 35)

            image4 = ImageDraw.Draw(image2)
            image4.text(
                (670, 150),
                "SHEIKH MUSIC",
                fill="white",
                font=font2,
                stroke_width=2,
                stroke_fill="red",
                align="left",
            )

            # وصف لظهور عالصوره
            bot_username = f" USER Bot: @{bot_username}"
            bot_id = f"ID Bot : {bot_id}"
            bot_name = f" CHANNEL @kafra_wi_1"

            image4.text((670, 450), text=bot_id, fill="white", font=font4, stroke_width=2, stroke_fill="black", align="left")
            image4.text(
               (670, 500), text=bot_username, fill="white", font=font4, stroke_width=2, stroke_fill="black", align="left"
            )
            image4.text(
               (670, 550), text=bot_name, fill="white", font=font4, stroke_width=2, stroke_fill="black", align="left"
            )

            image2 = ImageOps.expand(image2, border=20, fill=make_col())
            image2 = image2.convert("RGB")
            image2.save(f"cache/{bot_id}.jpg")
            file = f"cache/{bot_id}.jpg"
            return file
    except Exception as e:
        print(e)
        return YOUTUBE_IMG_URL


@app.on_message(filters.command(["معلومات التنصيب"], "") & filters.private & filters.private, group=881899)
async def deev(client, message: Message):
 
 if message.from_user.id in SUDORS:
    bot_username = client.me.username
    msg = await message.reply("⚡")
    await sleep(2)
    await msg.delete()
    bot_user = await client.get_me()
    bot_name = bot_user.first_name
    bot_id = bot_user.id
    user = await client.get_users(bot_user.id)
    usr = await client.get_chat(message.from_user.id)
    owner = user.first_name
    name = user.first_name
    username = user.username
    user_id = user.id
    photo = await app.download_media(user.photo.big_file_id)
    welcome_photo = get_kamalbot_img(
        bg_path="assets/userinfo.png",
        font_path="assets/hiroko.ttf",
        bot_username=bot_username,
        bot_user = await client.get_me(),
        bot_name=bot_name,
        bot_id=bot_id,
        profile_path=photo,
    )    
    
    reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton(name, url=f"https://t.me/{app.username}?startgroup=ne")]]
    )
    
    await message.reply_photo(
        welcome_photo,
        caption=f"<b><blockquote>━━「 معلومات تنصيب البوت علي الشيخ 」━━</blockquote>\n\n<blockquote>╭◉ᚐʙᴏᴛ.ɴᴀᴍᴇ : {bot_name}\n│᚜◉ᴜꜱᴇʀ : @{bot_username}\n╰◉ᚐᴛᴏᴋᴇɴ : <code>{BOT_TOKEN}</code></blockquote>\n\n <blockquote>˹sᴛꝛɪɴɢ✗ᴩʏʀᴏɢʀᴀᴍ : {pyrover} </blockquote>\n<code>{STRING1}</code></b>",
        reply_markup=reply_markup
    )
 else:
        await message.reply("هذا الامر لا يخصك")




@app.on_message(filters.command(["اضف قناه الاشتراك للتشغيل"],"") & filters.private, group = 2)
async def add_must(c,msg):
 if msg.from_user.id in SUDORS:

    try:
        m = await c.ask(msg.chat.id, "عزيزي المطور كم بارسال رابط القناه بدون علامه : @ \nو قم برفع البوت ادمن في القناه")
        try:
            chat = await c.get_chat(m.text)
        except:
            return await msg.reply(" تاكد عزيزي المطور من يوزر القناه او الجروب ")
        await set_must(c.me.username,chat.username)
        await msg.reply("تمت اضافه القناه بنجاح")
    except Exception as e:
        await msg.reply(f"- حدث خطا -> {e}")
 else:
        await msg.reply("هذا الامر لا يخصك")





@app.on_message(filters.command(["قناة الاشتراك"],"") & filters.private, group = 2)
async def get_ch_must(c,msg):
 if msg.from_user.id in SUDORS:

    db = await get_must(c.me.username)
    if db:
        await msg.reply(f"<blockquote>قناة الاشتراك الاجباري ->> @{db}</blockquote>")
    else:
        return await msg.reply(" لم يتم تعيين قناة الاشتراك ")
 else:
        await msg.reply("هذا الامر لا يخصك")
    




@app.on_message(filters.command(["حذف قناة الاشتراك"],"") & filters.private, group = 2)
async def rem_ch_must(c,msg):
 if msg.from_user.id in SUDORS:
   if msg.text.strip() == "حذف قناة الاشتراك":
    done = await del_must(c.me.username)
    if done:
        return await msg.reply("<blockquote>تم حذف قناة الاشتراك بنجاح</blockquote>")
    else:
        return await msg.reply("لم يتم تعيين قناة الاشتراك")
 else:
        await msg.reply("هذا الامر لا يخصك")





@app.on_message(filters.command(["تفعيل الاشتراك للتشغيل"],"") & filters.private, group = 2)
async def en_ch_must(c,msg):
 if msg.from_user.id in SUDORS:

    status = await get_must_ch(c.me.username)
    if status == "معطل" :
        await set_must_ch(c.me.username,"enable")
        return await msg.reply("<blockquote>تم تفعيل الاشتراك للتشغيل بنجاح</blockquote>")
    else:
        await msg.reply("الاشتراك الاجباري مفعل من قبل")
 else:
        await msg.reply("هذا الامر لا يخصك")






@app.on_message(filters.command(["تعطيل الاشتراك للتشغيل"],"") & filters.private, group = 2)
async def dis_ch_must(c,msg):
 if msg.from_user.id in SUDORS:

    status = await get_must_ch(c.me.username)
    if status == "مفعل" :
        await set_must_ch(c.me.username,"disable")
        return await msg.reply("<blockquote>تم تعطيل الاشتراك للتشغيل بنجاح</blockquote>")
    else:
        await msg.reply("الاشتراك الاجباري معطل من قبل")
 else:
        await msg.reply("هذا الامر لا يخصك")