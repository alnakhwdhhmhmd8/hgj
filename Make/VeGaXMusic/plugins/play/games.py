
import asyncio
import config
import re
import os
import requests
from os import getenv
from pyrogram import Client, filters
from VeGaXMusic import app
from config import OWNER_ID
from pyrogram import filters, Client
from pyrogram import filters
from pyrogram import Client
from typing import Union
from aiohttp import ClientSession
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.enums import ChatMemberStatus, ParseMode
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from VeGaXMusic.misc import SUDOERS
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from VeGaXMusic.utils.database import (set_cmode,get_assistant)
from pyrogram.types import (InlineKeyboardButton, ChatPermissions, InlineKeyboardMarkup, Message, User)
from datetime import datetime
from pyrogram import enums
from config import OWNER_ID
from pyrogram.errors import MessageNotModified


from pyrogram.types import CallbackQuery

from pyrogram.types import CallbackQuery, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from VeGaXMusic import app
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import *
from pyrogram.enums import ChatMembersFilter
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup                           
import asyncio
from VeGaXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram)
from VeGaXMusic import app
import pyrogram
from VeGaXMusic.misc import SUDOERS
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from config import OWNER_ID
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from pyrogram.enums import ParseMode
from VeGaXMusic import app
from VeGaXMusic.utils.database import is_on_off
from config import LOG_GROUP_ID


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
from aiohttp import ClientSession
from traceback import format_exc
import config
import re
import string
from pyrogram import enums
import lyricsgenius as lg
from pyrogram.types import (InlineKeyboardButton, ChatPermissions, InlineKeyboardMarkup, Message, User)
from pyrogram import Client, filters
from VeGaXMusic import Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app
from typing import Union
import sys
import os
from asyncio import sleep

import os
import asyncio
from pyrogram import Client, filters
from pyrogram import types
from pyrogram import enums
from pyrogram import enums
from pyrogram import Client
from pyrogram.types import ChatPermissions, ChatPrivileges
from pyrogram.errors import PeerIdInvalid
from os import getenv
from VeGaXMusic.misc import SUDOERS
from config import OWNER_ID
from config import BANNED_USERS
from config import BANNED_USERS, OWNER_ID
from pyrogram import filters, Client
from telegraph import upload_file
from dotenv import load_dotenv
from VeGaXMusic.utils.database import (set_cmode,get_assistant) 
from VeGaXMusic.utils.decorators.admins import AdminActual
from VeGaXMusic import app
import asyncio
import asyncio  

import os
import time
import requests
import re
import random
import time
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import schedule
import time
from pyrogram import client, filters
import json
import random
from typing import List, Union
import time
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
import datetime
from VeGaXMusic import app
import asyncio
import config
import asyncio
import config
import re
import os
import requests
from os import getenv
from pyrogram import Client, filters
from VeGaXMusic import app
from config import OWNER_ID
from pyrogram import filters, Client
from pyrogram import filters
from pyrogram import Client
from typing import Union
from aiohttp import ClientSession
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.enums import ChatMemberStatus, ParseMode
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from VeGaXMusic.misc import SUDOERS
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from VeGaXMusic.utils.database import (set_cmode,get_assistant)
from pyrogram.types import (InlineKeyboardButton, ChatPermissions, InlineKeyboardMarkup, Message, User)
from datetime import datetime
from pyrogram import enums
from config import OWNER_ID
from pyrogram.errors import MessageNotModified


from pyrogram.types import CallbackQuery

from pyrogram.types import CallbackQuery, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from VeGaXMusic import app
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import *
from pyrogram.enums import ChatMembersFilter
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup                           
import asyncio
from VeGaXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram)
from VeGaXMusic import app
import pyrogram
from VeGaXMusic.misc import SUDOERS
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from config import OWNER_ID
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from pyrogram.enums import ParseMode
from VeGaXMusic import app
from VeGaXMusic.utils.database import is_on_off
from config import LOG_GROUP_ID
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InputMediaVideo, InlineKeyboardMarkup, InlineKeyboardButton
from VeGaXMusic import app

from pyrogram import Client, enums, filters
import asyncio
from VeGaXMusic import app as app

from pyrogram.handlers import MessageHandler

from pyrogram import types
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import random
from VeGaXMusic import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from pyrogram import filters, Client

from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from VeGaXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube)
from VeGaXMusic import app
from random import  choice, randint
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges
from pyrogram import enums
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random

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


from datetime import datetime, timedelta



from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.raw import types
from pyrogram import enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from VeGaXMusic import app
from config import OWNER_ID

from VeGaXMusic import app
import random
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from VeGaXMusic import Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app
from VeGaXMusic import app
from random import  choice, randint

from VeGaXMusic.core.call import KIM
from VeGaXMusic.utils.database import get_assistant

from random import choice
from pyrogram.types import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


import asyncio


import random

from VeGaXMusic import app
from pyrogram import enums
from pyrogram.enums import ChatType, ChatMemberStatus, ParseMode, ChatMemberStatus
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)



from pyrogram import filters, Client

from pyrogram import Client, filters


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

 
gamessof = []

@app.on_message(filters.command(["تعطيل الالعاب","قفل الالعاب"], ""), group=509)
async def gamesslock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:

      if message.chat.id in gamessof:
         return await message.reply_text("الالعاب معطل من قبل")
      gamessof.append(message.chat.id)
      return await message.reply_text("تم تعطيل الالعاب بنجاح")
   else:
      return await message.reply_text("هييه ميخصك الامر ياروع!!")

@app.on_message(filters.command(["تفعيل الالعاب","فتح الالعاب"], ""), group=678)
async def gamessopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
      if not message.chat.id in gamessof:
         return await message.reply_text("الالعاب مفعل من قبل ")
      gamessof.remove(message.chat.id)
      return await message.reply_text("تم تفعيل الالعاب بنجاح")
   else:
      return await message.reply_text("هييه ميخصك الامر ياروع!!")
      
      


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery


@app.on_message(filters.command(["تسالي", "العاب", "الالعاب"], ""), group=738378)
async def show_games_menu(client: Client, message: Message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن")
    
    await message.reply_photo(
        photo="https://i.imgur.com/GY2uiXo.jpeg",
        caption=f"<b>⭓ɢᴧᴍᴇꜱ✘ꜱʜᴇɪᴋʜ♪\n<blockquote>╮◉ مـرحـبـا بـك: {message.from_user.mention()}\n╯◉ لـيك قـايـمـة تسالي مـن جاك</b></blockquote>",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("꙳.العاب شات.꙳", callback_data="gem1"),
                    InlineKeyboardButton("꙳.العاب الرفع.꙳", callback_data="gem2"),
                ],
                [
                    InlineKeyboardButton("ᴠᴇɢᴀ", url=SUPPORT_CHANNEL),
                ],
            ]
        )
    )

@app.on_callback_query(filters.regex("^gemas$"), group=186373882)
async def games_main_menu(_: Client, query: CallbackQuery):
    await query.answer()
    await query.edit_message_text(
        f"""<b>⭓ɢᴧᴍᴇꜱ✘ꜱʜᴇɪᴋʜ♪\n<blockquote>╮◉ هنا تسالي و العاب شات \n╯◉ لـيك قـايـمـة تسالي مـن جاك</b></blockquote>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("꙳.العاب شات.꙳", callback_data="gem1"),
                    InlineKeyboardButton("꙳.العاب الرفع.꙳", callback_data="gem2"),
                ],
                [
                    InlineKeyboardButton("ꜱʜᴇɪᴋʜ", url=SUPPORT_CHANNEL),
                ],
            ]
        )
    )

@app.on_callback_query(filters.regex("^gem1$"), group=165564)
async def chat_games_menu(_: Client, query: CallbackQuery):
    await query.answer("gem1")
    await query.edit_message_text(
        """<u><b>مرحبا بك عزيزي في العاب شات من جاك</b></u>

<blockquote>╮◉  كت
│᚜◉ تويت
│᚜◉ اسال
│᚜◉ اصراحه
│᚜◉ انصحني
│᚜◉ لوخيروك
│᚜◉ حكمه
│᚜◉ معاني
│᚜◉ اعلام
│᚜◉ حجره
│᚜◉ اكس او
│᚜◉ ابراج
│᚜◉ زوجني
╯◉  نكته
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("˹➻ٰ", callback_data="gemas")]]
        )
    )

@app.on_callback_query(filters.regex("^gem2$"), group=17554)
async def animal_games_menu(_: Client, query: CallbackQuery):
    await query.answer("gem2")
    await query.edit_message_text(
        """<b>
<b>تسالي رفع الحيونات بالرتب:</b></u>

╮◉ رفع كلب
│᚜◉ رفع حمار
│᚜◉ رفع بقره
│᚜◉ رفع قرد
│᚜◉ رفع تيس
│᚜◉ رفع خروف
│᚜◉ رفع خنزير
│᚜◉ رفع نسناس
╯◉  رفع رقاصه 

تنزيل رتب الحيونات

╮◉  تنزيل كلب
│᚜◉ تنزيل حمار
│᚜◉ تنزيل بقره
│᚜◉ تنزيل قرد
│᚜◉ تنزيل تيس
│᚜◉ تنزيل خروف
│᚜◉ تنزيل نسناس
│᚜◉ تنزيل خنزير
╯◉  تنزيل رقاصه

<u><b>لجلب قوائم رفع الحيونات:</b></u>

╮◉ قائمه الكلاب + كلاب
│᚜◉ قائمه الحمير + حمير
│᚜◉ قايمه البقر + بقر
│᚜◉ قايمه القرود + قرود
│᚜◉ قايمه التيوس + تيوس
│᚜◉ قايمه الخرفان + خرفان
│᚜◉ قائمه نسانيس + نسانيس
│᚜◉ قايمه الخنازير + خنازير
╯◉  قايمه الرقصات + رقصات
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("˹➻ٰ", callback_data="gemas")]]
        )
    )







@app.on_message(filters.command(["نقاطي"], ""), group=550544474)
async def show_score(client, message):
    user_id = message.from_user.id
    score = user_scores.get(user_id, 0)
    if score == 0:
        await message.reply_text("ليس هناك نقاط") 
    else:
        user = await client.get_users(user_id) 
        await message.reply(f"「 {user.mention} 」 \n نقاطك الحالية هي : {score} ⭐️")
        



@app.on_message(filters.command(["نقاطته"], ""), group=5544474)
async def show_score(client, message):
    user_id = message.reply_to_message.from_user.id
    score = user_scores.get(user_id, 0)
    if score == 0:
        await message.reply_text("ليس هناك نقاط") 
    else:
        user = await client.get_users(user_id) 
        await message.reply(f"「 {user.mention} 」 \n نقاطته الحالية هي : {score} ⭐️")
        


        
@app.on_message(filters.command("توب النقاط", ""), group=918171)
async def top_points(client, message):
    user_id = message.from_user.id	
    scores = {uid: score for uid, score in user_scores.items() if score > 0}
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    if not sorted_scores:
        await message.reply_text("ليس هناك لاعبين")
        return  

    text = "اكثر الاشخاص  تجميع لنقاط :\n\n"    
    k = 0
    for user_id, score in sorted_scores:  
        user = await client.get_users(user_id)
        k += 1
        text += f"{k} :- {user.mention} = {score} ⭐️\n"
        if k >= 5:
            break
    await message.reply_text(text)







kalab = []

@app.on_message(filters.command(["رفع كلب"], ""), group=555430754)
async def taafl_user(client, message):
    if message.chat.id in gamessof:
          return await message.reply_text("الالعاب معطله من قبل الادمن")
    

    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user = await client.get_users(message.reply_to_message.from_user.id)
        name = user.first_name
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        target = message.command[1].strip("@")
        user = await client.get_users(target)      
    else:
        await message.reply_text("قم بالرد عالمستخدم او ارسال يوزر او ايدي.!!")
        return

    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name

    if target == message.from_user.id:
        await message.reply_text("هييه مايمديك ترفع نفسك ياروعه!!")
        return

    if target == " 7728230165":
        await message.reply_text("هييه مايمديك ترفع جاك ياروعه!!")
        return
    
    if target == " 7728230165":
        await message.reply_text("هييه مايمديك ترفع جاك ياروعه!!")
        return

    if target == OWNER_ID:
        await message.reply_text("هييه مايمديك ترفع مطوري ياروعه!!")
        return

    member = await message.chat.get_member(target)
    if member.status in [ChatMemberStatus.OWNER]:
        return await message.reply("هييه مايمديك ترفع مالك اساسي ياروعه!!")
    
    
    if target in kalab:
        await message.reply_text(f"「 {user.mention} 」\nهيه مرفوع الكلب من قبل ")
        return
        
    kalab.append(target)
    await message.reply_video(
        video="https://telegra.ph/file/d37ca40b1d9918fa8b750.mp4",
        caption=f"<b>⭓ɢᴧᴍᴇꜱ✘ꜱʜᴇɪᴋʜ♪\n╮◉ الفاعل هو : {message.from_user.mention}\n╯◉ كلب هو : {user.mention}</b>",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🐶كلبجي", url=f"https://t.me/{user.username}")]])
    )
    
    
 

@app.on_message(filters.command(["كلاب","قائمة الكلاب","قايمه الكلاب"], ""), group=137762627)
async def get_restr_users(client: Client, message: Message):
   if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن")
   

   usr = await client.get_chat(message.from_user.id)
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id ==  7728230165:
         count = len(kalab)
         response = f" <u>قائمة الكلاب وعددهم :</u> {count}\n"
         for user in kalab:
             user = await client.get_users(user)
             response += f"{user.mention} \n"
         await message.reply_text(response)
   else:
    
        await message.reply_text(f"حجي هذا الامر ليس لك ")



@app.on_message(filters.command(["تنزيل كلب"], ""), group=555430754)
async def taafl_user(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن")    
    
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user = await client.get_users(message.reply_to_message.from_user.id)
        name = user.first_name
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        target = message.command[1].strip("@")
        user = await client.get_users(target)
        
    else:
        await message.reply_text("قم بالرد عالمستخدم او ارسال يوزر او ايدي.!!")
        return

    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name

    if target == message.from_user.id:
        await message.reply_text("هييه مايمديك تنزل نفسك ياروعه!!")
        return

    if target == " 7728230165":
        await message.reply_text("هييه مايمديك تنزل جاك ياروعه!!")
        return

    if target == OWNER_ID:
        await message.reply_text("هييه مايمديك تنزل مطوري ياروعه!!")
        return

    member = await message.chat.get_member(target)
    if member.status in [ChatMemberStatus.OWNER]:
        return await message.reply("هييه مايمديك تنزل مالك اساسي ياروعه!!")
        
    if target not in kalab:
        await message.reply_text(f"「 {user.mention} 」\nهييه ما مرفوع كلب")
    else:
        kalab.remove(target)
        await message.reply_text(f"「 {user.mention} 」\nنزلته من منصب الكلب")




##رفع خنزير ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓



anzeer = []

@app.on_message(filters.command(["رفع خنزير"], ""), group=5075754)
async def taafl_user(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن")     
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user = await client.get_users(message.reply_to_message.from_user.id)
        name = user.first_name
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        target = message.command[1].strip("@")
        user = await client.get_users(target)      
    else:
        await message.reply_text("قم بالرد عالمستخدم او ارسال يوزر او ايدي.!!")
        return

    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name

    if target == message.from_user.id:
        await message.reply_text("هييه مايمديك ترفع نفسك ياروعه!!")
        return

    if target == " 7728230165":
        await message.reply_text("هييه مايمديك ترفع جاك ياروعه!!")
        return
    
    if target == " 7728230165":
        await message.reply_text("هييه مايمديك ترفع جاك ياروعه!!")
        return

    if target == OWNER_ID:
        await message.reply_text("هييه مايمديك ترفع مطوري ياروعه!!")
        return

    member = await message.chat.get_member(target)
    if member.status in [ChatMemberStatus.OWNER]:
        return await message.reply("هييه مايمديك ترفع مالك اساسي ياروعه!!")
    
    
    if target in anzeer:
        await message.reply_text(f"「 {user.mention} 」\nهيه مرفوع خنزير من قبل ")
        return
        
    anzeer.append(target)
    await message.reply_video(
        video="https://telegra.ph/file/f630d33ec1b405f678c9d.mp4",
        caption=f"<b>⭓ɢᴧᴍᴇꜱ✘ꜱʜᴇɪᴋʜ♪\n╮◉ الفاعل هو : {message.from_user.mention}\n╯◉ الخنزير هو : {user.mention}</b>",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الخنزير🐷", url=f"https://t.me/{user.username}")]])
    )
    
    
 

@app.on_message(filters.command(["خنازير","قائمة خنازير","قايمه خنازير"], ""), group=132627)
async def get_restr_users(client: Client, message: Message):
   if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
   usr = await client.get_chat(message.from_user.id)
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id ==  7728230165:
         count = len(anzeer)
         response = f" <u>قائمة الخنازير وعددهم :</u> {count}\n"
         for user in anzeer:
             user = await client.get_users(user)
             response += f"{user.mention} \n"
         await message.reply_text(response)
   else:
        await message.reply_text(f"حجي هذا الامر ليس لك ")



@app.on_message(filters.command(["تنزيل خنزير"], ""), group=55074)
async def taafl_user(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
    
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user = await client.get_users(message.reply_to_message.from_user.id)
        name = user.first_name
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        target = message.command[1].strip("@")
        user = await client.get_users(target)
        
    else:
        await message.reply_text("قم بالرد عالمستخدم او ارسال يوزر او ايدي.!!")
        return

    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name

    if target == message.from_user.id:
        await message.reply_text("هييه مايمديك تنزل نفسك ياروعه!!")
        return

    if target == "7728230165":
        await message.reply_text("هييه مايمديك تنزل جاك ياروعه!!")
        return

    if target == OWNER_ID:
        await message.reply_text("هييه مايمديك تنزل مطوري ياروعه!!")
        return

    member = await message.chat.get_member(target)
    if member.status in [ChatMemberStatus.OWNER]:
        return await message.reply("هييه مايمديك تنزل مالك اساسي ياروعه!!")
        
    if target not in anzeer:
        await message.reply_text(f"「 {user.mention} 」\nهييه ما مرفوع خنزير")
    else:
        anzeer.remove(target)
        await message.reply_text(f"「 {user.mention} 」\nنزلته من منصب خنزير")




##رفع قرد ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓



keerd = []

@app.on_message(filters.command(["رفع قرد"], ""), group=5554)
async def taafl_user(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
    
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user = await client.get_users(message.reply_to_message.from_user.id)
        name = user.first_name
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        target = message.command[1].strip("@")
        user = await client.get_users(target)      
    else:
        await message.reply_text("قم بالرد عالمستخدم او ارسال يوزر او ايدي.!!")
        return

    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name

    if target == message.from_user.id:
        await message.reply_text("هييه مايمديك ترفع نفسك ياروعه!!")
        return

    if target == " 7728230165":
        await message.reply_text("هييه مايمديك ترفع جاك ياروعه!!")
        return
    
    if target == " 7728230165":
        await message.reply_text("هييه مايمديك ترفع جاك ياروعه!!")
        return

    if target == OWNER_ID:
        await message.reply_text("هييه مايمديك ترفع مطوري ياروعه!!")
        return

    member = await message.chat.get_member(target)
    if member.status in [ChatMemberStatus.OWNER]:
        return await message.reply("هييه مايمديك ترفع مالك اساسي ياروعه!!")
    
    
    if target in keerd:
        await message.reply_text(f"「 {user.mention} 」\nهيه مرفوع قرد من قبل ")
        return
        
    keerd.append(target)
    await message.reply_video(
        video="https://telegra.ph/file/7be16cfcb1f9b8c3a2e62.mp4",
        caption=f"<b>⭓ɢᴧᴍᴇꜱ✘ꜱʜᴇɪᴋʜ♪\n╮◉ الفاعل هو : {message.from_user.mention}\n╯◉ القرد هو : {user.mention}</b>",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("القرد🐒", url=f"https://t.me/{user.username}")]])
    )
    
    
 

@app.on_message(filters.command(["قرود","قائمة القرود","قايمه القرود"], ""), group=62627)
async def get_restr_users(client: Client, message: Message):
   if message.chat.id in gamessof:
       return await message.reply_text("الالعاب معطله من قبل الادمن") 
       
   usr = await client.get_chat(message.from_user.id)
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id ==  7728230165:
         count = len(keerd)
         response = f" <u>قائمة القرود وعددهم :</u> {count}\n"
         for user in keerd:
             user = await client.get_users(user)
             response += f"{user.mention} \n"
         await message.reply_text(response)
   else:
        await message.reply_text(f"حجي هذا الامر ليس لك ")



@app.on_message(filters.command(["تنزيل قرد"], ""), group=555430754)
async def taafl_user(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن")     
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user = await client.get_users(message.reply_to_message.from_user.id)
        name = user.first_name
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        target = message.command[1].strip("@")
        user = await client.get_users(target)
        
    else:
        await message.reply_text("قم بالرد عالمستخدم او ارسال يوزر او ايدي.!!")
        return

    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name

    if target == message.from_user.id:
        await message.reply_text("هييه مايمديك تنزل نفسك ياروعه!!")
        return

    if target == " 7728230165":
        await message.reply_text("هييه مايمديك تنزل جاك ياروعه!!")
        return

    if target == OWNER_ID:
        await message.reply_text("هييه مايمديك تنزل مطوري ياروعه!!")
        return

    member = await message.chat.get_member(target)
    if member.status in [ChatMemberStatus.OWNER]:
        return await message.reply("هييه مايمديك تنزل مالك اساسي ياروعه!!")
        
    if target not in keerd:
        await message.reply_text(f"「 {user.mention} 」\nهييه ما مرفوع قرد")
    else:
        keerd.remove(target)
        await message.reply_text(f"「 {user.mention} 」\nنزلته من منصب قرد")




##رفع نسناس ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


nsnas = []

@app.on_message(filters.command(["رفع نسناس"], ""), group=555430754)
async def taafl_user(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
        
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user = await client.get_users(message.reply_to_message.from_user.id)
        name = user.first_name
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        target = message.command[1].strip("@")
        user = await client.get_users(target)      
    else:
        await message.reply_text("قم بالرد عالمستخدم او ارسال يوزر او ايدي.!!")
        return

    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name

    if target == message.from_user.id:
        await message.reply_text("هييه مايمديك ترفع نفسك ياروعه!!")
        return

    if target == " 7728230165":
        await message.reply_text("هييه مايمديك ترفع جاك ياروعه!!")
        return
    
    if target == " 7728230165":
        await message.reply_text("هييه مايمديك ترفع جاك ياروعه!!")
        return

    if target == OWNER_ID:
        await message.reply_text("هييه مايمديك ترفع مطوري ياروعه!!")
        return

    member = await message.chat.get_member(target)
    if member.status in [ChatMemberStatus.OWNER]:
        return await message.reply("هييه مايمديك ترفع مالك اساسي ياروعه!!")
    
    
    if target in nsnas:
        await message.reply_text(f"「 {user.mention} 」\nهيه مرفوع نسناس من قبل ")
        return
        
    nsnas.append(target)
    await message.reply_video(
        video="https://telegra.ph/file/729fcb2de9633ca844651.mp4",
        caption=f"<b>⭓ɢᴧᴍᴇꜱ✘ꜱʜᴇɪᴋʜ♪\n╮◉ الفاعل هو : {message.from_user.mention}\n╯◉ نسناس هو : {user.mention}</b>",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🐵نسناس", url=f"https://t.me/{user.username}")]])
    )
    
    
 

@app.on_message(filters.command(["نسانيس","قائمة نسانيس","قايمه نسانيس"], ""), group=1377627)
async def get_restr_users(client: Client, message: Message):
   if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
       
   usr = await client.get_chat(message.from_user.id)
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id ==  7728230165:
         count = len(nsnas)
         response = f" <u>قائمة النسانيس وعددهم :</u> {count}\n"
         for user in nsnas:
             user = await client.get_users(user)
             response += f"{user.mention} \n"
         await message.reply_text(response)
   else:
        await message.reply_text(f"حجي هذا الامر ليس لك ")



@app.on_message(filters.command(["تنزيل نسناس"], ""), group=555430754)
async def taafl_user(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
        
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user = await client.get_users(message.reply_to_message.from_user.id)
        name = user.first_name
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        target = message.command[1].strip("@")
        user = await client.get_users(target)
        
    else:
        await message.reply_text("قم بالرد عالمستخدم او ارسال يوزر او ايدي.!!")
        return

    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name

    if target == message.from_user.id:
        await message.reply_text("هييه مايمديك تنزل نفسك ياروعه!!")
        return

    if target == " 7728230165":
        await message.reply_text("هييه مايمديك تنزل جاك ياروعه!!")
        return

    if target == OWNER_ID:
        await message.reply_text("هييه مايمديك تنزل مطوري ياروعه!!")
        return

    member = await message.chat.get_member(target)
    if member.status in [ChatMemberStatus.OWNER]:
        return await message.reply("هييه مايمديك تنزل مالك اساسي ياروعه!!")
        
    if target not in nsnas:
        await message.reply_text(f"「 {user.mention} 」\nهييه ما مرفوع نسناس")
    else:
        nsnas.remove(target)
        await message.reply_text(f"「 {user.mention} 」\nنزلته من منصب نسناس")
        
        
        


##رفع تيس ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


teess = []

@app.on_message(filters.command(["رفع تيس"], ""), group=555430754)
async def taafl_user(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
        
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user = await client.get_users(message.reply_to_message.from_user.id)
        name = user.first_name
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        target = message.command[1].strip("@")
        user = await client.get_users(target)      
    else:
        await message.reply_text("قم بالرد عالمستخدم او ارسال يوزر او ايدي.!!")
        return

    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name

    if target == message.from_user.id:
        await message.reply_text("هييه مايمديك ترفع نفسك ياروعه!!")
        return

    if target == " 7728230165":
        await message.reply_text("هييه مايمديك ترفع جاك ياروعه!!")
        return
    
    if target == " 7728230165":
        await message.reply_text("هييه مايمديك ترفع جاك ياروعه!!")
        return

    if target == OWNER_ID:
        await message.reply_text("هييه مايمديك ترفع مطوري ياروعه!!")
        return

    member = await message.chat.get_member(target)
    if member.status in [ChatMemberStatus.OWNER]:
        return await message.reply("هييه مايمديك ترفع مالك اساسي ياروعه!!")
    
    
    if target in teess:
        await message.reply_text(f"「 {user.mention} 」\nهيه مرفوع تيس من قبل ")
        return
        
    teess.append(target)
    await message.reply_video(
        video="https://telegra.ph/file/3c83a0f2bf8bdfae6f6b7.mp4",
        caption=f"<b>⭓ɢᴧᴍᴇꜱ✘ꜱʜᴇɪᴋʜ♪\n╮◉ الفاعل هو : {message.from_user.mention}\n╯◉ تيس هو : {user.mention}</b>",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("تيس🐏", url=f"https://t.me/{user.username}")]])
    )
    
    
 

@app.on_message(filters.command(["تيوس","قائمة التيوس","قايمه التيوس"], ""), group=137762627)
async def get_restr_users(client: Client, message: Message):
   if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن")
    
   usr = await client.get_chat(message.from_user.id)
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id ==  7728230165:
         count = len(teess)
         response = f" <u>قائمة تيوس وعددهم :</u> {count}\n"
         for user in teess:
             user = await client.get_users(user)
             response += f"{user.mention} \n"
         await message.reply_text(response)
   else:
        await message.reply_text(f"حجي هذا الامر ليس لك ")



@app.on_message(filters.command(["تنزيل تيس"], ""), group=555430754)
async def taafl_user(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
        
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user = await client.get_users(message.reply_to_message.from_user.id)
        name = user.first_name
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        target = message.command[1].strip("@")
        user = await client.get_users(target)
        
    else:
        await message.reply_text("قم بالرد عالمستخدم او ارسال يوزر او ايدي.!!")
        return

    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name

    if target == message.from_user.id:
        await message.reply_text("هييه مايمديك تنزل نفسك ياروعه!!")
        return

    if target == " 7728230165":
        await message.reply_text("هييه مايمديك تنزل جاك ياروعه!!")
        return

    if target == OWNER_ID:
        await message.reply_text("هييه مايمديك تنزل مطوري ياروعه!!")
        return

    member = await message.chat.get_member(target)
    if member.status in [ChatMemberStatus.OWNER]:
        return await message.reply("هييه مايمديك تنزل مالك اساسي ياروعه!!")
        
    if target not in teess:
        await message.reply_text(f"「 {user.mention} 」\nهييه ما مرفوع تيس")
    else:
        teess.remove(target)
        await message.reply_text(f"「 {user.mention} 」\nنزلته من منصب تيس")





##رفع حمار ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓




hoomar = []

@app.on_message(filters.command(["رفع حمار"], ""), group=555454)
async def taafl_user(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
        
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user = await client.get_users(message.reply_to_message.from_user.id)
        name = user.first_name
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        target = message.command[1].strip("@")
        user = await client.get_users(target)      
    else:
        await message.reply_text("قم بالرد عالمستخدم او ارسال يوزر او ايدي.!!")
        return

    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name

    if target == message.from_user.id:
        await message.reply_text("هييه مايمديك ترفع نفسك ياروعه!!")
        return

    if target == " 7728230165":
        await message.reply_text("هييه مايمديك ترفع جاك ياروعه!!")
        return
    
    if target == " 7728230165":
        await message.reply_text("هييه مايمديك ترفع جاك ياروعه!!")
        return

    if target == OWNER_ID:
        await message.reply_text("هييه مايمديك ترفع مطوري ياروعه!!")
        return

    member = await message.chat.get_member(target)
    if member.status in [ChatMemberStatus.OWNER]:
        return await message.reply("هييه مايمديك ترفع مالك اساسي ياروعه!!")
    
    
    if target in hoomar:
        await message.reply_text(f"「 {user.mention} 」\nهيه مرفوع تيس من قبل ")
        return
        
    hoomar.append(target)
    await message.reply_video(
        video="https://telegra.ph/file/bcd92746e45bceb9ee8f1.mp4",
        caption=f"<b>⭓ɢᴧᴍᴇꜱ✘ꜱʜᴇɪᴋʜ♪\n╮◉ الفاعل هو : {message.from_user.mention}\n╯◉ الحمار هو : {user.mention}</b>",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الحمار", url=f"https://t.me/{user.username}")]])
    )
    
    
 

@app.on_message(filters.command(["حمير","قائمة الحمير","قايمه الحمير"], ""), group=1372627)
async def get_restr_users(client: Client, message: Message):
   if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن")    
   usr = await client.get_chat(message.from_user.id)
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id ==  7728230165:
         count = len(hoomar)
         response = f" <u>قائمة الحمير وعددهم :</u> {count}\n"
         for user in hoomar:
             user = await client.get_users(user)
             response += f"{user.mention} \n"
         await message.reply_text(response)
   else:
        await message.reply_text(f"حجي هذا الامر ليس لك ")



@app.on_message(filters.command(["تنزيل حمار"], ""), group=555430754)
async def taafl_user(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
    
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user = await client.get_users(message.reply_to_message.from_user.id)
        name = user.first_name
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        target = message.command[1].strip("@")
        user = await client.get_users(target)
        
    else:
        await message.reply_text("قم بالرد عالمستخدم او ارسال يوزر او ايدي.!!")
        return

    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name

    if target == message.from_user.id:
        await message.reply_text("هييه مايمديك تنزل نفسك ياروعه!!")
        return

    if target == " 7728230165":
        await message.reply_text("هييه مايمديك تنزل جاك ياروعه!!")
        return

    if target == OWNER_ID:
        await message.reply_text("هييه مايمديك تنزل مطوري ياروعه!!")
        return

    member = await message.chat.get_member(target)
    if member.status in [ChatMemberStatus.OWNER]:
        return await message.reply("هييه مايمديك تنزل مالك اساسي ياروعه!!")
        
    if target not in hoomar:
        await message.reply_text(f"「 {user.mention} 」\nهييه ما مرفوع حمار")
    else:
        hoomar.remove(target)
        await message.reply_text(f"「 {user.mention} 」\nنزلته من منصب حمار")



##رفع رقاصه  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓



rrkasa = []

@app.on_message(filters.command(["رفع رقاصه"], ""), group=5430754)
async def taafl_user(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
        
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user = await client.get_users(message.reply_to_message.from_user.id)
        name = user.first_name
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        target = message.command[1].strip("@")
        user = await client.get_users(target)      
    else:
        await message.reply_text("قم بالرد عالمستخدم او ارسال يوزر او ايدي.!!")
        return

    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name

    if target == message.from_user.id:
        await message.reply_text("هييه مايمديك ترفع نفسك ياروعه!!")
        return

    if target == " 7728230165":
        await message.reply_text("هييه مايمديك ترفع جاك ياروعه!!")
        return
    
    if target == " 7728230165":
        await message.reply_text("هييه مايمديك ترفع جاك ياروعه!!")
        return

    if target == OWNER_ID:
        await message.reply_text("هييه مايمديك ترفع مطوري ياروعه!!")
        return

    member = await message.chat.get_member(target)
    if member.status in [ChatMemberStatus.OWNER]:
        return await message.reply("هييه مايمديك ترفع مالك اساسي ياروعه!!")
    
    
    if target in rrkasa:
        await message.reply_text(f"「 {user.mention} 」\nهيه مرفوع رقاصه من قبل ")
        return
        
    rrkasa.append(target)
    await message.reply_video(
        video="https://telegra.ph/file/5baa14ede564fb553afbe.mp4",
        caption=f"<b>⭓ɢᴧᴍᴇꜱ✘ꜱʜᴇɪᴋʜ♪\n╮◉ الفاعل هو : {message.from_user.mention}\n╯◉ الراقصه هي : {user.mention}</b>",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💃الراقصه", url=f"https://t.me/{user.username}")]])
    )
    
    
 

@app.on_message(filters.command(["رقصات","قائمة الراقصات","قايمه الرقصات"], ""), group=1377627)
async def get_restr_users(client: Client, message: Message):
   usr = await client.get_chat(message.from_user.id)
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id ==  7728230165:
         count = len(rrkasa)
         response = f" <u>قائمة الرقصات وعددهم :</u> {count}\n"
         for user in rrkasa:
             user = await client.get_users(user)
             response += f"{user.mention} \n"
         await message.reply_text(response)
   else:
        await message.reply_text(f"حجي هذا الامر ليس لك ")



@app.on_message(filters.command(["تنزيل رقاصه"], ""), group=55544)
async def taafl_user(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
        
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user = await client.get_users(message.reply_to_message.from_user.id)
        name = user.first_name
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        target = message.command[1].strip("@")
        user = await client.get_users(target)
        
    else:
        await message.reply_text("قم بالرد عالمستخدم او ارسال يوزر او ايدي.!!")
        return

    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name

    if target == message.from_user.id:
        await message.reply_text("هييه مايمديك تنزل نفسك ياروعه!!")
        return

    if target == " 7728230165":
        await message.reply_text("هييه مايمديك تنزل جاك ياروعه!!")
        return

    if target == OWNER_ID:
        await message.reply_text("هييه مايمديك تنزل مطوري ياروعه!!")
        return

    member = await message.chat.get_member(target)
    if member.status in [ChatMemberStatus.OWNER]:
        return await message.reply("هييه مايمديك تنزل مالك اساسي ياروعه!!")
        
    if target not in rrkasa:
        await message.reply_text(f"「 {user.mention} 」\nهييه ما مرفوع رقاصه")
    else:
        rrkasa.remove(target)
        await message.reply_text(f"「 {user.mention} 」\nنزلته من منصب رقاصه")
        
        

#رفع بقره ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


akrra = []

@app.on_message(filters.command(["رفع بقره"], ""), group=554)
async def taafl_user(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
        
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user = await client.get_users(message.reply_to_message.from_user.id)
        name = user.first_name
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        target = message.command[1].strip("@")
        user = await client.get_users(target)      
    else:
        await message.reply_text("قم بالرد عالمستخدم او ارسال يوزر او ايدي.!!")
        return

    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name

    if target == message.from_user.id:
        await message.reply_text("هييه مايمديك ترفع نفسك ياروعه!!")
        return

    if target == " 7728230165":
        await message.reply_text("هييه مايمديك ترفع جاك ياروعه!!")
        return
    
    if target == " 7728230165":
        await message.reply_text("هييه مايمديك ترفع جاك ياروعه!!")
        return

    if target == OWNER_ID:
        await message.reply_text("هييه مايمديك ترفع مطوري ياروعه!!")
        return

    member = await message.chat.get_member(target)
    if member.status in [ChatMemberStatus.OWNER]:
        return await message.reply("هييه مايمديك ترفع مالك اساسي ياروعه!!")
    
    
    if target in akrra:
        await message.reply_text(f"「 {user.mention} 」\nهيه مرفوع بقره من قبل ")
        return
        
    akrra.append(target)
    await message.reply_video(
        video="https://telegra.ph/file/9ba8e1b40e62280979295.mp4",
        caption=f"<b>⭓ɢᴧᴍᴇꜱ✘ꜱʜᴇɪᴋʜ♪\n╮◉ الفاعل هو : {message.from_user.mention}\n╯◉ بقره هو : {user.mention}</b>",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("البقره🐮", url=f"https://t.me/{user.username}")]])
    )
    
    
 

@app.on_message(filters.command(["بقر","قائمة البقر","قايمه البقر"], ""), group=132627)
async def get_restr_users(client: Client, message: Message):
   if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن")    
   usr = await client.get_chat(message.from_user.id)
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id ==  7728230165:
         count = len(akrra)
         response = f" <u>قائمة القبر وعددهم :</u> {count}\n"
         for user in akrra:
             user = await client.get_users(user)
             response += f"{user.mention} \n"
         await message.reply_text(response)
   else:
        await message.reply_text(f"حجي هذا الامر ليس لك ")



@app.on_message(filters.command(["تنزيل بقره"], ""), group=555454)
async def taafl_user(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
        
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user = await client.get_users(message.reply_to_message.from_user.id)
        name = user.first_name
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        target = message.command[1].strip("@")
        user = await client.get_users(target)
        
    else:
        await message.reply_text("قم بالرد عالمستخدم او ارسال يوزر او ايدي.!!")
        return

    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name

    if target == message.from_user.id:
        await message.reply_text("هييه مايمديك تنزل نفسك ياروعه!!")
        return

    if target == " 7728230165":
        await message.reply_text("هييه مايمديك تنزل جاك ياروعه!!")
        return

    if target == OWNER_ID:
        await message.reply_text("هييه مايمديك تنزل مطوري ياروعه!!")
        return

    member = await message.chat.get_member(target)
    if member.status in [ChatMemberStatus.OWNER]:
        return await message.reply("هييه مايمديك تنزل مالك اساسي ياروعه!!")
        
    if target not in akrra:
        await message.reply_text(f"「 {user.mention} 」\nهييه ما مرفوع بقره")
    else:
        akrra.remove(target)
        await message.reply_text(f"「 {user.mention} 」\nنزلته من منصب بقره")
        
        
##تسالي اخري ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
##تسالي اخري ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
##تسالي اخري ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
##تسالي اخري ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
##تسالي اخري ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
##تسالي اخري ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓






@app.on_message(filters.command(["صرصار"], ""), group=2728281)
async def mmmy(client: Client, message: Message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
        
    global user
    user = message.from_user.id
    await message.reply_photo(
        photo="https://graph.org/file/0331103b1c119716bad44.jpg",
        caption=f"<b> ˚‧SHEIKH˳+\n╮◉ عزيزي: {message.from_user.mention()}\n╯◉ اضغط علي صرصار لقتله</b>",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🪳", callback_data="ddddf")]])
    )

@app.on_callback_query(filters.regex("ddddf"), group=186373866582)
async def mpdtsf(client, query: CallbackQuery):
    global user
    chat = query.message.chat
    get = await client.get_chat_member(chat.id, query.from_user.id)
    user_status = get.status
    if query.from_user.id != user:
        await client.answer_callback_query(query.id, text="هييه مايمديك الامر ياروعه!!", show_alert=True)
        return

    await client.answer_callback_query(query.id)
        
    await query.message.reply_video(
        video="https://graph.org/file/fb6ae3a43f73ef2aee8a9.mp4",
        caption=f"<b> ˚‧SHEIKH˳+\n╮◉ عزيزي: {query.from_user.mention()}\n╯◉ أصبحت ملك الصراصير</b>",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        query.from_user.first_name,
                        url=f"https://t.me/{query.from_user.username}"
                    )
                ],
            ]
        )
    )
    
    
    
    
    
    
    
#خنزير ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#خنزير ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓



@app.on_message(filters.command(["خنزير"], ""), group=72828771)
async def mmmypout(client: Client, message: Message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
        
    global user
    user = message.from_user.id
    await message.reply_photo(
        photo="https://graph.org/file/c6234a6aedfbe638e0683.jpg",
        caption=f"<b> ˚‧SHEIKH˳+\n╮◉ عزيزي: {message.from_user.mention()}\n╯◉ ايقذ الخنزير</b>",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🪳", callback_data="xxxc")]])
    )

@app.on_callback_query(filters.regex("xxxc"), group=1882)
async def mpdtsflkp(client, query: CallbackQuery):
    global user
    chat = query.message.chat
    get = await client.get_chat_member(chat.id, query.from_user.id)
    user_status = get.status
    if query.from_user.id != user:
        await client.answer_callback_query(query.id, text="هييه مايمديك الامر ياروعه!!", show_alert=True)
        return

    await client.answer_callback_query(query.id)
        
    await query.message.reply_video(
        video="https://graph.org/file/274b6971aeb298bdcd6fe.mp4",
        caption=f"<b> ˚‧SHEIKH˳+\n╮◉ عزيزي: {query.from_user.mention()}\n╯◉ أصبحت ملك الخنازير</b>",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        query.from_user.first_name,
                        url=f"https://t.me/{query.from_user.username}"
                    )
                ],
            ]
        )
    )
    
    
    
    
#رقص ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

@app.on_message(filters.command(["رقص"], ""), group=72871)
async def mkmmmy(client: Client, message: Message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
        
    global user
    user = message.from_user.id
    await message.reply_photo(
        photo="https://telegra.ph/file/ac5909b46118805a7f72e.jpg",
        caption=f"<b> ˚‧SHEIKH˳+\n╮◉ عزيزي: {message.from_user.mention()}\n╯◉ شاهد الراقصه</b>",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💃", callback_data="ooop")]])
    )

@app.on_callback_query(filters.regex("ooop"), group=1889872)
async def mpdtposf(client, query: CallbackQuery):
    global user
    chat = query.message.chat
    get = await client.get_chat_member(chat.id, query.from_user.id)
    user_status = get.status
    if query.from_user.id != user:
        await client.answer_callback_query(query.id, text="هييه مايمديك الامر ياروعه!!", show_alert=True)
        return

    await client.answer_callback_query(query.id)
        
    await query.message.reply_video(
        video="https://telegra.ph/file/a6d8f722d328e2667937a.mp4",
        caption=f"<b> ˚‧SHEIKH˳+\n╮◉ عزيزي: {query.from_user.mention()}\n╯◉ أنت ترقص جيدا </b>",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        query.from_user.first_name,
                        url=f"https://t.me/{query.from_user.username}"
                    )
                ],
            ]
        )
    )
    
    
    
    
    
#نمله ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#نمله ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓



@app.on_message(filters.command(["نمله"], ""), group=771)
async def mmdvmy(client: Client, message: Message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
        
    global user
    user = message.from_user.id
    await message.reply_photo(
        photo="https://graph.org/file/bd1024b2f29996675596d.jpg",
        caption=f"<b> ˚‧SHEIKH˳+\n╮◉ عزيزي: {message.from_user.mention()}\n╯◉ اقتل النمله</b>",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🪳", callback_data="namla")]])
    )

@app.on_callback_query(filters.regex("namla"), group=42)
async def mpdtsjjlf(client, query: CallbackQuery):
    global user
    chat = query.message.chat
    get = await client.get_chat_member(chat.id, query.from_user.id)
    user_status = get.status
    if query.from_user.id != user:
        await client.answer_callback_query(query.id, text="هييه مايمديك الامر ياروعه!!", show_alert=True)
        return

    await client.answer_callback_query(query.id)
        
    await query.message.reply_video(
        video="https://graph.org/file/2d20cb201e06612588136.mp4",
        caption=f"<b> ˚‧SHEIKH˳+\n╮◉ عزيزي: {query.from_user.mention()}\n╯◉ حسباالله ونعم الوكيل فيك</b>",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        query.from_user.first_name,
                        url=f"https://t.me/{query.from_user.username}"
                    )
                ],
            ]
        )
    )
        
    
##قتل ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
##قتل ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓



@app.on_message(filters.command(["قتل","تخ","بيو"], ""), group=1025565554)
async def kill_user(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
        
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user = await client.get_users(message.reply_to_message.from_user.id)
        name = user.first_name
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        target = message.command[1].strip("@")
        user = await client.get_users(target)
    else:
        await message.reply_text("قم بالرد عالمستخدم او ارسال يوزر او ايدي.!!")
        return

    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name

    if target == message.from_user.id:
        await message.reply_text("هييه مايمديك قتل نفسك ياروعه!!")
        return

    if target == " 7728230165":
        await message.reply_text("هييه مايمديك قتل جاك ياروعه!!")
        return

    if target == OWNER_ID:
        await message.reply_text("هييه مايمديك قتل مطوري ياروعه!!")
        return

    member = await message.chat.get_member(target)
    if member.status in [ChatMemberStatus.OWNER]:
        return await message.reply("هييه مايمديك قتل مالك اساسي ياروعه!!")


    await message.reply_video(
        video="https://telegra.ph/file/fa6dcb9baf32196d8f114.jpg",
        caption=f"<b> ˚‧SHEIKH˳+\n╮◉ المجرم هو : {message.from_user.mention}\n╯◉ الضحية : {user.mention}</b>",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("المرحوم", url=f"https://t.me/{user.username}")]])
    )

    



###تف ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.command(["تف","تفو","اتفو"], ""), group=5554)
async def taafl_user(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
        
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user = await client.get_users(message.reply_to_message.from_user.id)
        name = user.first_name
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        target = message.command[1].strip("@")
        user = await client.get_users(target)
    else:
        await message.reply_text("قم بالرد عالمستخدم او ارسال يوزر او ايدي.!!")
        return

    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name

    if target == message.from_user.id:
        await message.reply_text("هييه مايمديك تف نفسك ياروعه!!")
        return

    if target == " 7728230165":
        await message.reply_text("هييه مايمديك تف جاك ياروعه!!")
        return

    if target == OWNER_ID:
        await message.reply_text("هييه مايمديك تف مطوري ياروعه!!")
        return

    member = await message.chat.get_member(target)
    if member.status in [ChatMemberStatus.OWNER]:
        return await message.reply("هييه مايمديك تف مالك اساسي ياروعه!!")


    await message.reply_video(
        video="https://t.me/kafra_wi_1/127",
        caption=f"<b> ˚‧SHEIKH˳+\n╮◉ الفاعل هو : {message.from_user.mention}\n╯◉ المعفن : {user.mention}</b>",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("المعفن", url=f"https://t.me/{user.username}")]])
    )


##محح ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓



@app.on_message(filters.command(["مح","محح","موه","مووه","مو"], ""), group=55880954)
async def tabossafl_user(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
        
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user = await client.get_users(message.reply_to_message.from_user.id)
        name = user.first_name
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        target = message.command[1].strip("@")
        user = await client.get_users(target)
    else:
        await message.reply_text("قم بالرد عالمستخدم او ارسال يوزر او ايدي.!!")
        return

    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name

    if target == message.from_user.id:
        await message.reply_text("هييه مايمديك تبوس نفسك ياروعه!!")
        return

    if target == " 7728230165":
        await message.reply_text("هييه مايمديك تبوس جاك ياروعه!!")
        return

    if target == OWNER_ID:
        await message.reply_text("هييه مايمديك تبوس مطوري ياروعه!!")
        return

    member = await message.chat.get_member(target)
    if member.status in [ChatMemberStatus.OWNER]:
        return await message.reply("هييه مايمديك تبوس مالك اساسي ياروعه!!")


    await message.reply_video(
        video="https://t.me/kafra_wi_1/127",
        caption=f"<b> ˚‧SHEIKH˳+\n╮◉ المتحرش هو : {message.from_user.mention}\n╯◉ الضحيه : {user.mention}</b>",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الضحية", url=f"https://t.me/{user.username}")]])
    )





###حجر ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓




game_state = {}

options = ["حجرة", "ورقة", "مقص"]

def get_winner(chat_id):
    player1_choice = game_state[chat_id]["player1"]["choice"]
    player2_choice = game_state[chat_id]["player2"]["choice"]
    player1_name = game_state[chat_id]["player1"]["name"]
    player2_name = game_state[chat_id]["player2"]["name"]
    
    if player1_choice == player2_choice:
        return "تعادل"
    elif (player1_choice == "حجرة" and player2_choice == "مقص") or (player1_choice == "ورقة" and player2_choice == "حجرة") or (player1_choice == "مقص" and player2_choice == "ورقة"):
        game_state[chat_id]["player1"]["score"] += 1
        return f"{player1_name}"
    else:
        game_state[chat_id]["player2"]["score"] += 1
        return f"{player2_name}"

@app.on_message(filters.command(["حجره"], ""), group=8536362)
async def start(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
        
    if message.chat.id not in game_state:
        game_state[message.chat.id] = {
            "player1": {
                "name": message.from_user.first_name,
                "choice": None,
                "score": 0
            },
            "player2": {
                "name": None,
                "choice": None,
                "score": 0
            }
        }
        await message.reply(
            f"<b>» {game_state[message.chat.id]['player1']['name']} \n╮◉ بدأ لعبة حجرة ورقة مقص\n╯◉ انتظر اللاعب الثاني</b>",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("اضغط للعب", callback_data="join")],
                    [InlineKeyboardButton("ꜱʜᴇɪᴋʜ", url=SUPPORT_CHANNEL)]
                ]
            )
        )
    else:
        await message.reply("هناك لعبة جارية بالفعل في هذه الدردشة. انتظر حتى تنتهي.")

@app.on_callback_query(filters.regex("join"))
async def join(client, callback_query):
    if callback_query.message.chat.id in game_state:
        if callback_query.from_user.first_name != game_state[callback_query.message.chat.id]["player1"]["name"]:
            game_state[callback_query.message.chat.id]["player2"]["name"] = callback_query.from_user.first_name
            await callback_query.message.edit(
                f"<b>» {game_state[callback_query.message.chat.id]['player1']['name']} \n» {game_state[callback_query.message.chat.id]['player2']['name']}\n╮◉ يلعبان حجرة ورقة مقص\n╯◉ دور اللاعب: {game_state[callback_query.message.chat.id]['player1']['name']}\n ɢᴧᴍᴇꜱ ♪〩⸢ꜱʜᴇɪᴋʜ♪ </b>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("حجرة", callback_data="حجرة"),
                         InlineKeyboardButton("ورقة", callback_data="ورقة"),
                         InlineKeyboardButton("مقص", callback_data="مقص")],[
                         InlineKeyboardButton("ꜱʜᴇɪᴋʜ", url=SUPPORT_CHANNEL)
                         ]
                    ]
                )
            )
        else:
            await callback_query.answer("انت منضم للعبه بالفعل", show_alert=True)
    else:
        await callback_query.answer("لا توجد لعبة جارية في هذه الدردشة.", show_alert=True)

@app.on_callback_query(filters.regex("^(حجرة|ورقة|مقص)$"))
def choose(client, callback_query):
    if callback_query.message.chat.id in game_state:
        user_choice = callback_query.data
        bot_choice = choice(options)
        user_name = callback_query.from_user.first_name
        bot_name = client.get_me().first_name

        if user_name == game_state[callback_query.message.chat.id]["player1"]["name"]:
            game_state[callback_query.message.chat.id]["player1"]["choice"] = user_choice
            callback_query.message.edit(
                f"<b>╮◉ اللاعب الأول: {game_state[callback_query.message.chat.id]['player1']['name']} \n╯◉ لقد لعب \n╮◉ اللاعب الثاني: {game_state[callback_query.message.chat.id]['player2']['name']}\n╯◉ اختر الآن</b>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("حجرة", callback_data="حجرة"),
                         InlineKeyboardButton("ورقة", callback_data="ورقة"),
                         InlineKeyboardButton("مقص", callback_data="مقص")],
                         [InlineKeyboardButton("ꜱʜᴇɪᴋʜ", url=SUPPORT_CHANNEL)]
                    ]
                )
            )
        elif user_name == game_state[callback_query.message.chat.id]["player2"]["name"]:
            if game_state[callback_query.message.chat.id]["player1"]["choice"] is None:
                callback_query.answer("لا يمكنك اللعب حتى يلعب اللاعب الأول.", show_alert=True)
            else:
                game_state[callback_query.message.chat.id]["player2"]["choice"] = user_choice
                winner = get_winner(callback_query.message.chat.id)
                name_player1 = game_state[callback_query.message.chat.id]['player1']['name']
                name_player2 = game_state[callback_query.message.chat.id]['player2']['name']
                choice_player1 = game_state[callback_query.message.chat.id]['player1']['choice']
                choice_player2 = game_state[callback_query.message.chat.id]['player2']['choice']
                player1_score = game_state[callback_query.message.chat.id]['player1']['score']
                player2_score = game_state[callback_query.message.chat.id]['player2']['score']
                callback_query.message.edit(
                    f"<b>╮◉ الإسم : {name_player1}\n│᚜◉  الإختيار : {choice_player1}\n╯◉ النقاط : {player1_score}\n\n╮◉ الإسم : {name_player2}\n│᚜◉ الإختيار : {choice_player2}\n│᚜◉ النقاط : {player2_score}\n╯◉ اللاعب الفائز هو\n ➦ {winner}</b>"
                )
                del game_state[callback_query.message.chat.id]
        else:
            callback_query.answer("أنت لست جزء من هذه اللعبة.", show_alert=True)
    else:
        callback_query.answer("لا توجد لعبة جارية في هذه الدردشة.", show_alert=True)






##زوجني ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.command(['زوجني'], prefixes="") & filters.group, group=82726267277)
async def call_random_member(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
        
    chat_id = message.chat.id
    members = []
    async for member in client.get_chat_members(chat_id):
        # تخطي البوتات والحسابات المحذوفة
        if not member.user.is_bot and not member.user.is_deleted:
            members.append(member)
    
    if not members:
        return await message.reply_text("لا يوجد أعضاء متاحين للزواج!")
    
    random_member = random.choice(members)
    random_member_mention = random_member.user.mention
    sender_mention = message.from_user.mention
    
    random_message = random.choice([
        f"👰 {sender_mention} اخترت لك هذه العروسة:\n{random_member_mention}\n\nيجب على العروسة الموافقة على طلب يدها أولاً ليتم الزفاف!",
        f"💍 {sender_mention} هذه زوجتك المستقبلية:\n{random_member_mention}\n\nبانتظار موافقة العروسة لإتمام الزفاف!"
    ])
    
    # تخزين معلومات المرسل والعضو المختار في الكيبورد
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("✅ موافقة", callback_data=f"pair_yes_{message.from_user.id}_{random_member.user.id}"),
                InlineKeyboardButton("❌ رفض", callback_data=f"pair_no_{message.from_user.id}_{random_member.user.id}"),
            ],
        ]
    )
    
    await message.reply_text(
        text=random_message, 
        reply_markup=keyboard,
    )

@app.on_callback_query()
async def handle_callback_query(client, query):
    data = query.data.split('_')
    action = data[1]
    sender_id = int(data[2])
    selected_id = int(data[3])
    
    # التحقق من أن المستخدم الذي ضغط على الزر هو العضو المختار أو صاحب الأمر
    if query.from_user.id not in [selected_id, sender_id]:
        return await query.answer("⚠️ هذا الخيار ليس لك!", show_alert=True)
    
    if action == "yes":
        # التحقق من أن الضاغط هو العضو المختار فقط
        if query.from_user.id != selected_id:
            return await query.answer("فقط العروسة يمكنها الموافقة!", show_alert=True)
            
        selected_member = await client.get_chat_member(query.message.chat.id, selected_id)
        sender_member = await client.get_chat_member(query.message.chat.id, sender_id)
        
        if selected_member.user.is_deleted:
            return await query.message.edit_text("❌ العضو المختار لم يعد موجوداً!")
            
        congrat_message = random.choice([
            f"🎉 تمت الموافقة!\n{selected_member.user.mention} وافقت على الزواج من {sender_member.user.mention}\n\nمبروك للعروسين! 💍\nخذوها إلى الخاص واستمتعو بشهر العسل! 🍯",
            f"💕 مبارك للعروسين!\n{selected_member.user.mention} قبلت عرض {sender_member.user.mention}\n\nالف مبروك! لا تنسو إحضار أولاد لنا في المستقبل! 👶"
        ])
        await query.message.edit_text(congrat_message)
        
    elif action == "no":
        # التحقق من أن الضاغط هو العضو المختار أو صاحب الأمر
        if query.from_user.id == selected_id:
            await query.message.edit_text(f"❌ {query.from_user.mention} رفضت عرض الزواج!")
        else:
            await query.message.edit_text(f"❌ {query.from_user.mention} ألغى طلب الزواج!")
        
        
        
        
##معاني ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

EMO = [
  "👞:حذاء",
  "⭐:نجمة",
  "🕞:ساعة",
  "🍑:خوخ",
  "🛢️:نفط",
  "🎂:كيكة",
  "⚽:كورة",
  "🩳:شورت",
  "📒:كتاب",
  "🌹:وردة",
  "✏️:قلم",
  "🔥:نار",
  "💸:فلوس",
  "💻:لاب"
]
@app.on_message(filters.regex("^معاني$") & filters.group, group=233344408)
@app.on_edited_message(filters.regex("^معاني$") & filters.group, group=4343233322)
async def game_3(client, message):
   if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
        
   A = choice(EMO)
   emo = A.split(":")[0]
   ans = A.split(":")[1]
   re = f"{ans}"
   ASK = await app.ask(
     message.chat.id,
     "اسرع واحد يرسل معنى الايموجي {}".format(emo),
     reply_to_message_id=message.id,
     timeout=15,
     filters=filters.regex(re)
   )
   await ASK.reply(
    f"عاش: {ASK.from_user.mention}\n اجابتك صحيحة"
   )
   
   
   



##حكمه ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.command(["احكام","حكمه"], ""), group=888736)
async def bottttt(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
        
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    selections = ["※ صورة وجهك او رجلك او خشمك او يدك ؟ ",
" ※ اصدر اي صوت يطلبه منك الاعبين ؟ ",
" ※ سكر خشمك و قول كلمة من اختيار الاعبين الي معك ؟ ",
" ※ روح الى اي قروب عندك في الواتس اب و اكتب اي شيء يطلبه منك الاعبينالحد الاقصى 3 رسائل ؟ ",
" ※ قول نكتة ولازم احد الاعبين يضحك اذا ضحك يعطونك ميوت الى ان يجي دورك مرة ثانية ؟ ",
" ※ سمعنا صوتك و غن اي اغنية من اختيار الاعبين الي معك ؟ ",
" ※ ذي المرة لك لا تعيدها ؟ ",
" ※ ارمي جوالك على الارض بقوة و اذا انكسر صور الجوال و ارسله في الشات العام ؟ ",
" ※ صور اي شيء يطلبه منك الاعبين ؟ ",
" ※ اتصل على ابوك و قول له انك رحت مع بنت و احين هي حامل.... ؟ ",
" ※ سكر خشمك و قول كلمة من اختيار الاعبين الي معك ؟ ",
" ※ اعطي اي احد جنبك كف اذا مافيه احد جنبك اعطي نفسك و نبي نسمع صوته ؟ ",
" ※ ارمي جوالك على الارض بقوة و اذا انكسر صور الجوال و ارسله في الشات العام ؟ ",
" ※ روح عند اي احد بالخاص و قول له انك تحبه و الخ ؟ ",
" ※ اكتب في الشات اي شيء يطلبه منك الاعبين في الخاص ؟ ",
" ※ قول نكتة اذا و لازم احد الاعبين يضحك اذا محد ضحك يعطونك ميوت الى ان يجي دورك مرة ثانية ؟ ",
" ※ سامحتك خلاص مافيه عقاب لك  ؟ ",
" ※ اتصل على احد من اخوياكخوياتك , و اطلب منهم مبلغ على اساس انك صدمت بسيارتك ؟ ",
" ※ غير اسمك الى اسم من اختيار الاعبين الي معك ؟ ",
" ※ اتصل على امك و قول لها انك تحبها  ؟ ",
" ※ لا يوجد سؤال لك سامحتك  ؟ ",
" ※ قل لواحد ماتعرفه عطني كف ؟ ",
" ※ منشن الجميع وقل انا اكرهكم ؟ ",
" ※ اتصل لاخوك و قول له انك سويت حادث و الخ.... ؟ ",
" ※ روح المطبخ و اكسر صحن  ؟ ",
" ※ اعطي اي احد جنبك كف اذا مافيه احد جنبك اعطي نفسك و نبي نسمع صوت الكف ؟ ",
" ※ قول لاي بنت موجود في الروم كلمة حلوه ؟ ",
" ※ تكلم باللغة الانجليزية الين يجي دورك مرة ثانية لازم تتكلم اذا ما تكلمت تنفذ عقاب ثاني ؟ ",
" ※ لا تتكلم ولا كلمة الين يجي دورك مرة ثانية و اذا تكلمت يجيك باند لمدة يوم كامل من السيرفر ؟ ",
" ※ قول قصيدة  ؟ ",
" ※ تكلم باللهجة السودانية الين يجي دورك مرة ثانية ؟ ",
" ※ اتصل على احد من اخوياكخوياتك , و اطلب منهم مبلغ على اساس انك صدمت بسيارتك ؟ ",
" ※ اول واحد تشوفه عطه كف ؟ ",
" ※ سو مشهد تمثيلي عن اي شيء يطلبه منك الاعبين ؟ ",
" ※ سامحتك خلاص مافيه عقاب لك  ؟ ",
" ※ اتصل على ابوك و قول له انك رحت مع بنت و احين هي حامل.... ؟ ",
" ※ روح اكل ملح + ليمون اذا مافيه اكل اي شيء من اختيار الي معك ؟ ",
" ※ تاخذ عقابين ؟ ",
" ※ قول اسم امك افتخر بأسم امك ؟ ",
" ※ ارمي اي شيء قدامك على اي احد موجود او على نفسك ؟ ",
" ※ اذا انت ولد اكسر اغلى او احسن عطور عندك اذا انتي بنت اكسري الروج حقك او الميك اب حقك ؟ ",
" ※ اذهب الى واحد ماتعرفه وقل له انا كيوت وابي بوسه ؟ ",
" ※ تتصل على الوالدهو تقول لها خطفت شخص ؟ ",
" ※ تتصل على الوالدهو تقول لها تزوجت با سر ؟ ",
" ※ اتصل على الوالدهو تقول لهااحب وحده ؟ ",
" ※ تتصل على شرطي تقول له عندكم مطافي ؟ ",
" ※ خلاص سامحتك ؟ ",
" ※ تصيح في الشارع انامجنوون ؟ ",
" ※ تروح عند شخص وقول له احبك ؟"]
    bar = random.choice(selections)

    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    message.from_user.first_name,
                    url=f"https://t.me/{message.from_user.username}"
                )
            ]
        ]
    )
    await message.reply_text(text=bar, reply_markup=reply_markup)
    
    
    
##نكت ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ نكت ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
##نكت ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ نكت ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
##نكت ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ نكت ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
##نكت ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ نكت ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
##نكت ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ نكت ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓



@app.on_message(filters.command(["نكته","نكت"], ""), group=888736)
async def bottttt(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
        
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    selections = ["واحد مشغول أتجوز واحدة مشغولة خلفوا عيل مش فاضيلهم 👻😹",
"مرة القمر كان عايز يتجوز الشمس قالتله أتجوز واحد صايع طول الليل 👻😹",
"ولد بيسأل أبوه هو الحب أعمى رد عليه أبوه بص في وش أمك وأنت تعرف 👻😹",
"مرة مفتاح مات أهله ما زعلوش عليه عشان معاهم نسخة تانية 👻😹",
"ممرضة خلفت توأم سمت واحد عضل والتاني وليد 👻😹",
"مسطول أتجوز صينية قالتله مالك ساكت ليه؟ قالها مش عارف افتكرتك نايمة 👻😹",
"واحدة صعيدية جوزها رماها من الدور الثالث طلعتله وقالتله بلاش الهزار البايخ ده 👻😹",
"اتنين مساطيل حبوا يسرقوا عمارة فقالوا لبعض إحنا ناخد العمارة بعيد ونسرقها برحتنا 👻😹",
"منهم بص ورا ملقاش الهدوم فقال له كفاية كدة احنا بعدنا أوى 👻😹",
"حر جدًا، قالتله مفيش مشكلة نطلعها بالليل 👻😹",
"واحد رجع في كلامه خبط اللي وراه 👻😹",
"واحد خلقه ضاق أعطاه لأخوه الصغير 👻😹",
"مرة مدرس رياضيات خلف ولدين واستنتج التالت 👻😹",
"واحد كهربائي أتجوز أربعة جابلهم مشترك 👻😹",
"كفايه عليك كده ياد يبن الحلوهه 👻😹",
"واحدة اسمها ساندي دخلت هندسة بقت ساندي متر مربع 👻😹",
"مرة شرطي مرور خلّف ولد بيتكلم بالإشارة 👻😹",
"مره واحد اسمو جابوا  كان بيرجم ابليس ف الحج قالولو ليه؟ قال عشان يمكن احتاجو 👻😹",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ ﻗﺎﻟﻬﺎ اﻫﻮه ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه  👻😹",
"واحد بيشتكي لصاحبه بيقوله أنا مافيش حد بيحبني ولا يفتكرني أبدًا، ومش عارف أعمل إيه قاله سهلة استلف من الناس فلوس هيسألوا عليك كل يوم 👻😹",
" مرة واحد مصري دخل سوبر ماركت في الكويت عشان يشتري ولاعة راح عشان يحاسب بيقوله الولاعة ديه بكام قاله دينار قاله منا عارف ان هي نار بس بكام 👻😹",
"بنت حبت تشتغل مع رئيس عصابة شغلها في غسيل الأموال 👻😹",
"واحد بيشتكي لصاحبه بيقوله أنا مافيش حد بيحبني ولا يفتكرني أبدًا، ومش عارف أعمل إيه قاله سهلة استلف من الناس فلوس هيسألوا عليك كل يوم 👻😹",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ؟ ﻗﺎﻟﻬﺎ اﻫﻮه ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه 👻😹",
"واحده ست سايقه على الجي بي اي قالها انحرفي قليلًا قلعت الطرحة 👻😹",
"مرة واحد غبي معاه عربية قديمة جدًا وبيحاول يبيعها وماحدش راضي يشتريها.. راح لصاحبه حكاله المشكلة صاحبه قاله عندي لك فكرة جهنمية هاتخليها تتباع الصبح أنت تجيب علامة مرسيدس وتحطها عليها. بعد أسبوعين صاحبه شافه صدفة قاله بعت العربية ولا لاء؟ قاله انت  مجنون حد يبيع مرسيدس 👻😹",
"مره واحد بلديتنا كان بيدق مسمار فى الحائط فالمسمار وقع منه فقال له :تعالى ف مجاش, فقال له: تعالي ف مجاش. فراح بلديتنا رامي على المسمار شوية مسمامير وقال: هاتوه 👻😹",
"واحدة عملت حساب وهمي ودخلت تكلم جوزها منه ومبسوطة أوي وبتضحك سألوها بتضحكي على إيه قالت لهم أول مرة يقول لي كلام حلو من ساعة ما اتجوزنا 👻😹",
"بنت حبت تشتغل مع رئيس عصابة شغلها في غسيل الأموال 👻😹",
"مره واحد اشترى فراخ علشان يربيها فى قفص صدره 👻😹",
"مرة واحد من الفيوم مات اهله صوصوا عليه 👻😹",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ ﻗﺎﻟﻬﺎ اﻫﻮه ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه 👻😹",
"مره واحد شاط كرة فى المقص اتخرمت. 👻😹",
"مرة واحد رايح لواحد صاحبهفا البواب وقفه بيقول له انت طالع لمين قاله طالع أسمر شوية لبابايا قاله يا أستاذ طالع لمين في العماره 👻😹",
" وهه عاوز تانيي 👻😹 "]
    bar = random.choice(selections)

    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    message.from_user.first_name,
                    url=f"https://t.me/{message.from_user.username}"
                )
            ]
        ]
    )
    await message.reply_text(text=bar, reply_markup=reply_markup)
    
    

#انصحني ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#انصحني ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#انصحني ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#انصحني ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.command(["انصحني"], ""), group=88876)
async def bottttt(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
        
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    selections = ["عامل الناس بأخلاقك ولا بأخلاقهم", 
"الجمال يلفت الأنظار لكن الطيبه تلفت القلوب ", 
"الاعتذار عن الأخطاء لا يجرح كرامتك بل يجعلك كبير في نظر الناس ",
"لا ترجي السماحه من بخيل.. فما في البار لظمان ماء",
"لا تحقرون صغيره إن الجبال من الحصي",
"لا تستحي من إعطاء فإن الحرمان أقل منه ", 
"لا تظلم حتى لا تتظلم ",
"لا تقف قصاد الريح ولا تمشي معها ",
"لا تكسب موده التحكم الا بالتعقل",
"لا تمد عينك في يد غيرك ",
"لا تملح الا لمن يستحقاها ويحافظ عليها",
"لا حياه للإنسان بلا نبات",
"لا حياه في الرزق.. ولا شفاعه في الموت",
"كما تدين تدان",
"لا دين لمن لا عهد له ",
"لا سلطان على الدوق فيما يحب أو بكره",
"لا مروه لمن لادين له ",
"لا يدخل الجنه من لايأمن من جازه بوائقه",
"يسروا ولا تعسروا... ويشورا ولا تنفروا",
"يدهم الصدر ما يبني العقل الواسع ",
"أثقل ما يوضع في الميزان يوم القيامة حسن الخلق ",
"أجهل الناس من ترك يقين ما عنده لظن ما عند الناس ",
"أحياناً.. ويصبح الوهم حقيقه ",
"مينفعش تعاتب حد مبيعملش حساب لزعلك عشان متزعلش مرتين . ",
"السفر ومشاهده اماكن مختلفه وجديده ",
"عدم تضيع الفرص واسثمارها لحظه مجبئها ",
" اعطاء الاخرين اكثر من ما يتوقعون",
"معامله الناس بلطف ولكن عدم السماح لاحد بستغالال ذالك ",
"تكوين صدقات جديده مع الحفظ بلاصدقاء القودامي ",
"تعلم اصول المهنه بدلا من تضيع الوقت ف تعلم حيل المهنه ",
"مدح ع الاقل ثلاث اشخاص يوميا ",
"النظر ف عيون الشخاص عند مخاطبتهم ",
"التحلي بلسماح مع الاخرين او النفس ",
"الاكثار من قول كلمه شكرا ",
" مصافحه الاخرين بثبات وقوة ",
"الابتعاد عن المناطق السيئه السمعه لتجنب الاحداث السئه ",
" ادخار 10٪ع الاقل من الدخل",
" تجنب المخاوف من خلال التعلم من تجارب مختلفه",
" الحفاظ ع السمعه لانها اغلي ما يملك الانسان",
" تحويل الاعداء الي اصدقاء من خلال القيام بعمل جيد",
"لا تصدق كل ما تسمعع. ولا تنفق كل ما تمتلك . ولا تنم قدر ما ترغب ",
" اعتني بسمعتك جيدا فستثبت للك الايام انها اغلي ما تملك",
"حين تقول والدتك ستندم ع فعل ذالك ستندم عليه غالبا.. ",
" لا تخش العقبات الكبيره فخلفها تقع الفرص العظيمه",
"قد لا يتطلب الامر اكثر من شخص واحد لقلب حياتك رأس ع عقب ",
"اختر رفيقه حياتك بحرص فهو قرار سيشكل 90٪من سعادتك او بؤسك ",
" اقلب اداءك الاصدقاء بفعل شي جميل ومفجائ لهم",
"حين تدق الفرصه ع باباك ادعوها للبيت ",
"تعلم القواعد جيدا ثن اكسر بعدها ",
"احكم ع نجاحك من خلال قدرتك ع العطاء وليس الاخذ ",
" لا تتجاهل الشيطان مهما بدل ثيابه",
"ركز ع جعل الاشياء افضل وليس اكبر او اعظم ",
"كن سعيد  بما تمتلك واعمل لامتلاك ما تريد ",
"اعط الناس اكثر من ما يتوقعون ",
" لا تكن منشغل لدرجه عدم التعرف ع اصدقاء جدد",
"استحمه يوم العيد يمعفن🐰",
"مش تحب اي حد يقرب منك ",
" خليك مع البت راجل خليك تقيل",
" انصح نفسك بنفسك بمت😂",
" كنت نصحت نفسي ياخويا🗿"]
    bar = random.choice(selections)

    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    message.from_user.first_name,
                    url=f"https://t.me/{message.from_user.username}"
                )
            ]
        ]
    )
    await message.reply_text(text=bar, reply_markup=reply_markup)
    
    
    


##اسال ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
##اسال ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
##اسال ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
##اسال ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓



@app.on_message(filters.command(["لوخيروك","لو خيروك","اسال"], ""), group=8898778736)
async def bottttt(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
        
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    selections = ["**لو قالوا لك  تناول صنف واحد فقط من الطعام لمدة شهر .",
            "شخص تحب تستفزه ؟",
            "لو حلمت في شخص وصحيت وحصلت رساله من نفس الشخص . ارسل ايموجيي مثل ردة فعلك.",
            "هات صورة تحس إنك ابدعت بتصويرها.",
            "على إيش سهران ؟",
            "مين تتوقع يطالعك طول الوقت بدون ملل ؟",
            "وين جالس الحين ؟",
            "كم من عشرة تقيم يومك ؟",
            "أطول مدة نمت فيها كم ساعه ؟",
            "أجمل سنة ميلادية مرت عليك ؟",
            "أخر رسالة بالواتس جاتك من مين ؟",
            "ليه مانمت ؟",
            "تعتقد فيه أحد يراقبك ؟",
            "كم من عشره تعطي حظك ؟",
            "كلمه ماسكه معك الفترة هذي ؟",
            "شيء مستحيل تمل منه ؟",
            "متى تنام بالعادة ؟",
            "كم من عشرة جاهز للدراسة ؟",
            "منشن صديقك الفزعة",
            "يوم نفسك يرجع بكل تفاصيله ؟",
            "أجمل صورة بجوالك ؟",
            "ايش أغرب مكان قد صحتوا فيه؟",
            "اذا جاك خبر مفرح اول واحد تعلمه فيه مين ؟",
            "شيء لو يختفي تصير الحياة جميلة ؟",
            "كم من عشرة تشوف نفسك محظوظ ؟",
            "امدح نفسك بكلمة وحدة بس",
            "كلمة لأقرب شخص لقلبك ؟",
            "قوة الصداقة بالمدة ولا بالمواقف ؟",
            "تتابع مسلسلات ولا م تهتم ؟",
            "تاريخ يعني لك الكثير ؟",
            "كم عدد اللي معطيهم بلوك ؟",
            "من الغباء انك ؟",
            "اكثر شيء محتاجه الحين ؟",
            "ايش مسهرك ؟.",
            "حزين ولا مبسوط ؟",
            "تحب سوالف مين ؟",
            "كم من عشرة روتينك ممل ؟",
            "شيء مستحيل ترفضه ؟.",
            "كم من عشرة الإيجابية فيك ؟.",
            "تعتقد اشباهك الاربعين عايشين حياة حلوة ؟.",
            "مين جالس عندك ؟",
            "كم من عشرة تشوف نفسك انسان ناجح ؟",
            "شيء حظك فيه حلو ؟.",
            "كم من عشرة الصبر عندك ؟",
            "أخر مرة نزل عندكم مطر ؟",
            "اكثر مشاكلك بسبب ؟",
            "اكره شعور ممكن يحسه انسان ؟",
            "شخص تحب تنشبله ؟",
            "تنتظر شيء ؟",
            "جربت تسكن وحدك ؟",
            "اكثر لونين تحبهم مع بعض ؟",
            "متى تكره نفسك ؟",
            "كم من عشرة مروق ؟",
            "مدينة تتمنى تعيش وتستقر فيها طول عمرك ؟",
            "لو للحياة لون إيش بيكون لون حياتك ؟",
            "ممكن في يوم من الأيام تصبح شخص نباتي ؟.",
            "عمرك قابلت شخص يشبهك ؟",
            "اخر شخص تهاوشت معه ؟",
            "قبل ساعة ايش كنت تسوي ؟",
            "كلمة تقولها للي ببالك ؟",
            "أكثر شيء مضيع وقتك فيه ؟",
            "لو فتحتا خزانتك إيش اكثر لون بنشوف ؟",
            "قوة خارقة تتمنى تمتلكها ؟",
            "اكثر مصايبك مع مين ؟",
            "اذا زعلت إيش يرضيك ؟",
            "من النوع اللي تعترف بسرعه ولا تجحد ؟",
            "من الاشياء البسيطة اللي تسعدك ؟",
            "اخر مره بكيت",
            "ايموجي يعبر عن وضعك الحين ؟",
            "التاريخ المنتظر بالنسبة لك ؟",
            "كلنا بنسمعك إيش بتقول ؟",
            "مدينتك اللي ولدت فيها ؟",
            "عندك شخص مستحيل يمر يوم وما تكلمه ؟",
            "كلمة تقولها لنفسك ؟",
            "كم من عشرة متفائل بالمستقبل ؟",
            "ردك المعتاد اذا أحد ناداك ؟",
            "أكثر كلمه تسمعها من أمك ؟",
            "إيش تفضل عمل ميداني ولاعمل مكتبي ؟",
            "أكثر حيوان تحبه ؟",
            "اكثر مشاكلك بسبب ؟",
            "اكثر صوت تكرهه ؟",
            "اشياء تتمنى انها م تنتهي ؟",
            "اشياء صعب تتقبلها بسرعه ؟",
            "كم من عشرة راضي عن وضعك الحالي ؟",
            "متى م تقدر تمسك ضحكتك ؟",
            "اخر شخص قالك كلمة حلوة ؟",
            "اكثر شيء تحبه بنفسك ؟",
            "شيء نفسك يرجع ؟",
            "اغلب وقتك ضايع على ؟",
            "كيف تعرفت على اعز صديق لك ؟",
            "شايل هم شيء الفترة هذي ؟",
            "شخص م تحب تناقشه ؟",
            "تقييمك للديسكورد الفترة هذي ؟",
            "من النوع اللي اذا حطيت راسك على المخده نمت ولا تحتاج وقت ",
            "اهم برنامج عندك بالجوال الفترة هذي ؟",
            "كم تعطي نفسك من عشرة بتعاملك مع مشاكلك ؟",
            "اشياء تبين عليك اذا زعلت ؟",
            "كم من عشرة تحب الجلسة بالبيت ؟",
            "أطول مكالمة لك كم كانت مدتها ؟",
            "اسم تحس صاحبه فخم ؟",
            "تتكلم أكثر ولا تسمع ؟",
            "كم من عشرة تحب النوم ؟",
            "اخر شيء اكلته ؟",
            "أكثر مكان سافرت له بخيالك ؟",
            "كبرت وللحين اخاف من ؟",
            "كيف حالك وانت لحالك ؟",
            "أكثر اسم تحبه ؟.",
            "اكبر مبلغ ضاع منك ؟",
            "كلمة تختصر وضعك الحين ؟",
            "نظام نومك ...",
            "أكثر مكان تجلس فيه غير غرفتك ؟",
            "حرف تحبه ؟",
            "كم درجة الحرارة بمدينتك ؟",
            "تعطي اللي غلط بحقك فرصة ؟",
            "حياتك بكلمة ؟",
            "عندك مليون ريال بس مايمديك تشتري الا شيء  يبدأ بأول حرف من اسمك. وش بتشتري ؟",
            "اكثر شيء ساحب عليه الفترة هذي ؟",
            "شيء مستحيل تعطيه أحد ؟",
            "تنتظر شيء ؟",
            "ايش الوظيفة التي تستحق أعلى راتب؟",
            "كم مره تشحن جوالك باليوم ؟",
            "كم من عشرة عندك امل انك تصير مليونير ؟",
            "اشياء م تسويها غير اذا كنت مروق ؟",
            "لو بيدك تغير بالزمن, تقدمه ولا ترجعه ؟.",
            "دولة امنيتك تزورها ؟.",
            "اكثر  شخص فاهمك بالدنيا ؟",
            "تسامح بسرعة ؟.",
            "كم تحتاج وقت عشان تتعود على مكان جديد ؟",
            "كم من عشرة تحب الهدوء ؟",
            "تاريخ مهم جداً عندك ؟",
            "لعبة تشوف نفسك فنان فيها ؟",
            "أصعب قرار ممكن تتخذه ؟",
            "شيء نفسك تجربه ؟",
            "أشياء توترك ؟",
            "كم من عشرة تحب الاطفال ؟.",
            "اكثر شخص تتهاوش معه ؟",
            "لو خيروك بين يعطونك مليون أو راتب شهري متوسط بدون عمل مدى الحياة إيش تختار ؟",
            "الفلوس كل شيء ؟",
            "عشان تعيش مرتاح ؟",
            "ردة فعلك لو شفت شخص يبكي قدامك ؟",
            "كم مره أخذت عمره بـ رمضان ؟",
            "ردة فعلك لو مزح معك شخص م تعرفه ؟",
            "شيء تشوف نفسك مبدع فيه ؟",
            "ماذا تفعل الان ؟ ",
            "كم من عشرة تحب حياتك ؟.",
            "كم عدد الصور بجوالك ؟.",
            "كم عدد اصحابك المقربين منك كثير ؟.",
            "شكراً لأنك في حياتي ..تقولها لمين ؟",
            "كيف تتعامل مع الشخص اللي يرد متأخر دائماً ؟.",
            "اللوان داكنة  ولا فاتحه؟",
            "كيف تتعامل مع الاشخاص السلبيين ؟",
            "دايم الانطباع الاول عنك إنك شخص ؟",
            "شيء حلو صار لك اليوم ؟",
            "اول شيء يلفت انتباهك بشخص اول مرة تقابله ؟.",
            "جماد م تستغني عنه ؟.",
            "مع ، ضد : البكاء يقلل التوتر ..!",
            "إيش كان نكك ايام البيبي ؟.",
            "من النوع اللي تحفظ اسامي الناس  بسرعه ولا بس اشكالهم ؟.",
            "لو كان لك الحرية تغير اسمك إيش راح تختار اسم ؟",
            "اكثر شيء ضيعت عليه فلوسك ؟",
            "تعرف تمسك نفسك اذا عصبت ؟",
            "عمرك شاركت بمسابقة وربحت ؟",
            "إيش لون جوالك ؟.",
            "تعتقد إنك انسان لك فايدة ؟",
            "اذا احد سألك عن شيء م تعرفه تقول م اعرف ولا تتفلسف ؟",
            "أطول صداقة بينك وبين شخص كم مدتها ؟.",
            "تعرف تعبر عن الكلام اللي بداخلك ؟",
            "ردة فعلك اذا انحشرت بالنقاش ؟",
            "بالعادة برمضان تنحف ولاتسمن ؟",
            "تمارس رياضة معينة برمضان ؟",
            "عندك فوبيا من شيء ؟.",
            "الساعة كم اذان الفجر عندكم ؟",
            "شيء من الماضي للحين عندك ؟.",
            "عندك شخص انت حييل جريء معاه و ما تستحي منه ؟",
            "عمرك انتقمت من شخص؟",
            "اكثر شي يتعبك بالصيام العطش ولا الجوع ؟",
            "اكثر شخص يتصل عليك بالواتس ؟",
            "متى اخر مره جربت شعور ليتني سكت بس ؟",
            "اسم ولد وبنت تحسهم لايقين على بعض ؟.",
            "مسلسل ناوي تشوفه ؟",
            "عادي تتغير عشان شخص تحبه ؟",
            "شيء كل م تذكرته تستانس؟",
            "ايامك هالفترة عبارة عن ؟",
            "منشن شخصين تحسهم نفس الاسلوب او الشخصية ..",
            "اكثر شيء بتشتاق له اذا جاء رمضان ؟",
            "كم مره سامحت بقلبك بس عقلك رافض هالشيء ؟.",
            "مع او ضد .. البنت تحب انشاء المشاكل في العلاقات ..",
            "ماهي طريقتك في معاتبة شخص ؟",
            "لو كنت محتار بين شخص تحبه وشخص يحبك، من تختار؟",
            "الشيء الي تحسه يجذبك للشخص هو ؟",
            "اكثر شخص بينك وبينه تواصل دائم ؟",
            "اعلى نسبة جبتها بحياتك الدراسية ؟",
            "شايل هم شيء ؟ ",
            "إيش تفضل صح وخطأ ولا خيارات ؟",
            "اكثر ايموجي تستخدمه ؟",
            "جربت ينسحب جوالك فترة الاختبارات ؟.",
            "مادة دايم تجيب العيد فيها ؟",
            "وجبة ساحب عليها ؟",
            "تحب تتعرف على ناس جدد ولا مكتفي باللي عندك ؟",
            "مادة تكرها بس درجاتك عالية فيها ؟",
            "شيء بسيط قادر يعدل مزاجك بشكل سريع ؟",
            "اطول مدة جلسة تذاكر فيها بشكل متواصل كم ساعة ؟",
            "قبل امس الوقت هذا إيش كنت تسوي ؟",
            "منشن شخص لو م شفته تحس يومك ناقص ؟",
            "كلمتك اذا شفت حاجة حلوة ؟",
            "خوالك ولا عمامك ؟",
            "عادي تطلع وجوالك مافيه شحن كثير ؟",
            "شيء من صغرك ماتغير فيك ؟",
            "أصعب انتظار ؟",
            "أجمل بيت شعر سمعته ...",
            "مودك الحين ؟",
            "عندك صديق يحمل نفس اسمك ؟",
            "محادثة ولا مكالمة ؟",
            "كم مره يتقلب مزاجك باليوم ؟",
            "اكثر شخص يسوي فيك مقالب ؟",
            "مكان تبي تكون فيه الحين ؟.",
            "كم من عشرة تحب مهنة التدريس ؟",
            "شنو تتوقع بتصير بعد 10 سنين ؟ ",
            "متى تحب الطلعة ؟",
            "أغرب شي اشتهيت تأكله فجأة ؟",
            "اخر مره بكيت متى ؟",
            "اكثر شخص يقفل بوجهك اذا كلمك ؟",
            "كثر شخص يكرفك ؟",
            "تدخل بنقاش بموضوع ماتفهم فيه شيء ولا تسكت وتسمع بس ؟",
            "عمرك طحت بمكان عام ؟",
            "شخص يعرف عنك كل شي تقريباً ؟",
            "اكثر واحد يرسلك بالديسكورد ؟",
            "إيش اللي قدامك الحين ؟",
            "من النوع اللي تعتمد على غيرك ولا كل شي تسويه بنفسك ؟",
            "تقدر تعيش يوم كامل بدون نت ؟",
            "مع او ضد : الاعتراف بـ شيء في قلبك دام طويلاً ؟",
            "أبوك إيش يقرب لأمك ؟",
            "اكثر مدة جلستها بدون نت ؟",
            "لو رجعناك خمس سنين هل كنت تتوقع ان حياتك بتكون نفس وضعك الحين ؟",
            "تتقبل النصيحة من أي أحد ؟",
            "متى لازم تقول لا ؟",
            "أكثر ماده تحبها دراسياً والسبب؟.",
            "إيش نوع قهوتك المفضلة ؟",
            "شخص تشوفه بشكل يومي غير اهلك ؟",
            "شخص تحب ابتسامتة ؟",
            "من الاشياء اللي تجيب لك الصداع ؟",
            "وش تحب تسوي وقت فضاوتك ؟.",
            "كم تعطي نفسك من عشرة بالجدية بحياتك ",
            "أكثر شي يعتمدون عليك فيه ؟",
            "اكثر صفة عندك ؟",
            "كيف تعبر عن عصبيتك ؟",
            "كم داخل سيرفر فالديسكورد ؟",
            "حصلت الشخص اللي يفهمك ولا باقي ؟",
            "تفضل .. العيون الناعسة ... العيون الواسعة ؟",
            "اشياء تغيرت تظرتك لها",
            "الرقم السري حق جوالك ...",
            "لو قررت تقفل جوالك يوم كامل مين تتوقع أنه يفتقدك ؟",
            "اخر هوشه جلدت ولا انجلدت ؟",
            "نصيحه صغيرة من واقع تجربتّك؟.",
            "شخص يكلمك بشكل يومي ؟",
            "أسم وانطباعك عنه ؟",
            "العصر إيش كنت تسوي ؟",
            "كم من عشرة تعطي اهتمامك بدراستك أو عملك ؟",
            "كيف تفرغ غضبك بالعادة ؟",
            "أطول مدة قضيتها بعيد عن أهلك ؟",
            "شخص مستحيل تمسك ضحكتك معاه؟",
            "حاجة دايم تضيع منك ؟",
            "تجامل احد على حساب مصلحتك ؟",
            "كم لك فـ الديسكورد ؟",
            "اخر شخص تهاوشت معه مين ؟",
            "اكثر شيء تكره تنتظره ؟",
            "اخر مطعم اكلت منه ؟",
            "اكثر شيء تحبه بـ شكلك ؟",
            "تنام بـ اي مكان ، ولا بس غرفتك ؟",
            "اكتب اول كلمة جات في بالك الحين ؟",
            "تهمك التفاصيل ولا الزبدة من الموضوع ؟",
            "شيء واحد .. م عاد يهمك كثر اول ؟",
            "كم تقييمك لـ طبخك من 10 ، ولا م تطبخ ؟",
            "اتفه شيء ارسلوك عشانه ؟",
            "فن تحبه كثير ؟",
            "اكثر سوالفك عن ...؟",
            "صفة موجودة في جميع افراد عائلتك ؟",
            "شخص م تقدر تكذب عليه ؟",
            "كم من 10 تحس بـ الطفش ؟",
            "من النوع الي تجيك الردود القوية بعد الهوشة ولا فـ وقتها ؟",
            "تحب تجرب الاشياء الجديدة ، ولا تنتظر الناس يجربونها اول ؟",
            "وش اغبى شيء سويته ؟",
            "اكثر كلمة الناس تقولها عن شخصيتك ؟",
            "مراقبة شخص تركته .. فضول ولا بقايا مشاعر ؟",
            "برنامج كرهته الفترة هاذي",
            "مشهور ، او مشهورة .. يشبهونك فيه",
            "بالغالب وش تسوي فـ الويكند ؟",
            "وش اسم الحي الي ساكن فيه ؟",
            "اكثر شيء تخاف منه ؟",
            "عاده لاتستطيع تركها ؟ ",
            "كم من الوقت تحتاج عشان تصحصح من بعد م صحيت من النوم ؟",
            "اذا حسيت بـ غيرة تتكلم ولا تسكت ؟",
            "مع او ضد ... اقاربك يعرفون عن حساباتك في برامج التواصل ؟",
            "اخر مره سافرت بالطائرة والى وين؟",
            "وش اليوم الي تكرف فيه كثير ؟",
            "تفضل .. الاعمال الحرة ولا الوظيفة ؟",
            "حاجة تشوف نفسك مبدع فيها ؟",
            "ماركتك المفضلة ؟",
            "منشن ... اكثر شخص تثق فيه ؟",
            "اذا انسجنت وش تتوقع بتكون التهمة الي عليك ؟",
            "تعطي الناس فرصة تتقرب منك ؟",
            "منشن .. الشخص الي يستحق تدخل الديسكورد عشانه ..",
            "متى اخر مره نمت اكثر من 12 ساعة ؟",
            "رائحة عطر مدمن عليها ..",
            "وش تحس انك تحتاج الفترة هاذي ؟",
            "كم من 10 البرود فيك ؟",
            "وش اكثر فاكهة تحبها ؟",
            "اصعب وظيفة في نظرك ؟",
            "شيء بسيط قادر على حل كل مشاكلك ..",
            "اذا جلست عند ناس م تعرفهم .. تكتفي بالسكوت ، ولا تتكلم معهم ؟",
            "تتحمل المزح الثقيل ؟",
            "من النوع الي تنام فـ طريق السفر ؟",
            "لو شلنا من طولك 100 كم يبقى من طولك ؟",
            "موقفك من شخص أخفى عنك حقيقة ما، تخوفًا من خسارتك؟ ",
            "اكثر شخص ينرفزك الي ؟",
            "تعرف تتصرف في المواقف العصبة ؟",
            "متى حسيت انك مختلف عن الي غيرك ؟",
            "اصعب مرحلة دراسية مرت عليك ؟",
            "سويت شيء بالحياة وانت مو مقتنع فيه ؟",
            "اخر مره ضربوك فيها ... ووش كان السبب ؟",
            "من الاشياء الي تجيب لك الصداع ؟",
            "مين اول شخص تكلمه اذا طحت بـ مصيبة ؟",
            "مع او ضد : النوم افضل حل لـ مشاكل الحياة ...",
            "تجامل ولا صريح ؟",
            "تفضل المواد الي تعتمد على الحفظ ولا الفهم ؟",
            "صفة تخليك تكره الشخص مهما كان قربه منك ؟",
            "جربت احد يعطيك بلوك وانت تكتب له ؟",
            "تهتم بـ معرفة تاريخ ميلاد الي تحبهم ؟",
            "فيه شيء م تحب تطلبه حتى لو كنت محتاجة ؟",
            "دائما قوة الصداقة بـ ... ؟",
            "اخر شخص قالك كلمة حلوة ..",
            "كم من 10 الي تتوقعه يصير ؟",
            "اذا كنت بنقاش مع شخص وطلع الحق معه تعترف له ولا تصر على كلامك ؟",
            "فيه شخص تكرهه بشكل كبير ؟ ولك جرأة تمنشن اسمه ؟",
            "كيف الجو عندكم اليوم ؟",
            "ترتيبك بالعائلة ؟",
            "تسمع شيلات ؟",
            "تفضل السفر فـ الشتاء ولا الصيف ؟",
            "مع او ضد : الهدية بـ معناها وليس بـ قيمتها",
            "عندك صحبة من اشخاص خارج دولتك",
            "عندك صحبة من اشخاص خارج دولتك ؟",
            "تحب اصوات النساء فـ الاغاني ولا الرجال",
            "وش اول جوال شريته ؟",
            "وش النوع الي تحبه ف الافلام ؟",
            "اكثر مكان تحب تجلس فيه فالبيت ؟",
            "صفة قليل تحصلها فـ الناس حالياً ؟",
            "من النوع الي تعترف ولا تجحد ؟",
            "اول شخص تكلمه اذا صحيت من النوم ؟",
            "وش اجمل لهجة عرببية بالنسبة لك ؟",
            "اخر اتصال من مين كان ؟",
            "اجمل مدينة بدولتك ؟",
            "شاعرك المفضل ؟",
            "كم مره تشحن جوالك باليوم",
            "لو كنت مؤلف كتاب .. وش راح يكون اسمه ؟",
            "اطول مدة قضيتها بدون اكل ..",
            "كم من 10 نسبة الكسل فيك هالايام ؟",
            "نومك خفيف ولا ثقيل ؟",
            "كم من عشرة تشوف صوتك حلو ؟",
            "تجيك الضحكة بوقت غلط ؟",
            "تفضل التسوق من الانترنت ، ولا الواقع ؟",
            "اغرب اسم مر عليك ؟",
            "وش رقمك المفضل ؟",
            "شيء تبيه يصير الحين ...",
            "شاي ولا قهوة ؟",
            "صفة يشوفونها الناس سيئة ، وانت تشوفها كويسه",
            "لون تكرهه ...",
            "وظيفة تحسها لايقة عليك ...",
            "كم من 10 كتابتك بالقلم حلوة ؟",
            "اكلة ادمنتها الفترة ذي ...",
            "اجمل مرحلة دراسية مرت عليك ..",
            "اكثر شيء تكرهه فالديسكورد ..",
            "شيء مستحيل انك تاكله ...",
            "وش رايك بالي يقرأ ولا يرد ؟",
            "اسمك بدون اول حرفين ..",
            "متى تكره الطلعة ؟",
            "شخص من عائلتك يشبهونك فيه ...",
            "اكثر وقت تحب تنام فيه ...",
            "تنتظر احد يجيك ؟",
            "اسمك غريب ولا موجود منه كثير ؟",
            "وش الشيء الي يكرهه اقرب صاحب لك ؟",
            "كم من 10 حبك للكتب ؟",
            "جربت الشهرة او تتمناها ؟",
            "مين اقرب شخص لك بالعائلة ؟",
            "شيء جميل صار لك اليوم ؟",
            "كلمتك اذا احد حشرك بالنقاش ...",
            "اعمال يدوية نفسك تتقنها . ",
            "وش الي يغلب عليك دائما .. قلبك ولا عقلك ؟",
            "صفة تحمد الله انها مو موجودة في اصحابك ...",
            "كم وجبة تاكل فاليوم الفترة هاذي ؟",
            "جربت دموع الفرح ؟ وش كان السبب ؟",
            "لو فقط مسموح شخص واحد تتابعه فالسناب مين بيكون ؟",
            "‏لو حطوك بمستشفى المجانين كيف تقنعهم إنك مو مجنون ؟.",
            "اكثر شيء تحبه فالشتاء ...",
            "شيء ودك تتركه ...",
            "كم تعطي نفسك من 10 فاللغة الانجليزية ؟",
            "شخص فرحتك مرتبطة فيه ...",
            "اكتب اسم .. واكتب كيف تحس بيكون شكله ...",
            "متى اخر مره قلت ليتني سكت ؟",
            "ممكن تكره احد بدون سبب ؟",
            "اكثر وقت باليوم تحبه ...",
            "اكثر شيء حظك سيء فيه ...",
            "متى صحيت ؟",
            "كلمة صعب تقولها وثقيلة عليك ...",
            "ردك الدائم على الكلام الحلو ...",
            "سؤال دايم تتهرب من الاجابة عليه ...",
            "مين الشخص اللي مستعد تأخذ حزنه بس م تشوفه حزين ؟.",
            "جربت تروح اختبار بدون م تذاكر ؟",
            "كم مرة غشيت ف الاختبارات ؟",
            "وش اسم اول شخص تعرفت عليه فالديسكورد ؟",
            "تعطي فرصة ثانية للشخص الي كسرك ؟",
            "لو احتاج الشخص الي كسرك مساعدة بتوقف معه ؟",
            "@منشن... شخص ودك تطرده من السيرفر ...",
            "دعاء له اثر إبجابي في حياتك ...",
            "قل حقيقه عنك ؟",
            "انسان م تحب تتعامل معه ابد",
            "اشياء اذا سويتها لشخص تدل على انك تحبه كثير ؟",
            "الانتقاد الكثير يغيرك للافضل ولا يحطمك ويخليك للأسوأ ؟",
            "كيف تعرف اذا هذا الشخص يكذب ولا لا ؟",
            "مع او ضد : العتاب على قدر المحبة ...",
            "شيء عندك اهم من الناس",
            "تتفاعل مع الاشياء اللي تصير بالمجتمع ولا ماتهتم ؟.",
            "وش الشيء الحلو الي يميزك عن غيرك ؟",
            "كذبة كنت تصدقها وانت صغير ..",
            "@منشن .. شخص تخاف منه اذا عصب ...",
            "كلمة بـ لهجتك تحس م احد بيعرفها ...",
            "كمل ... انا من الاشخاص الي ...",
            "تراقب احد بالديسكورد ؟",
            "كيف تعرف ان هالشخص يحبك ؟",
            "هواية او تجربة كان ودك تستمر و تركتها ؟",
            "الديسكورد اشغلك عن حياتك الواقعية ؟",
            "اكمل ... تستمر علاقتك بالشخص اذا كان ...",
            "لو احد قالك اكرهك وش بتقول له ؟",
            "مع او ضد : عامل الناس كما يعاملوك ؟",
            "ارسل اخر صورة فـ الالبوم ...",
            "الصق وارسل اخر شيء نسخته ...",
            "ماهي اخر وجبة اكلتها ",
            "اكثر شيء تحس انه مات ف مجتمعنا",
            "برأيك ماهو افضل انتقام ...",
            "اكثر ريحة تجيب راسك ...",
            "شعور ودك يموت ...",
            "عمرك فضفضت لـ شخص وندمت ؟",
            "تقدر تتحمل عيوب شخص تحبه ؟",
            "يكبر الشخص ف عيونك لما ...",
            "وش تقول للشخص الي معك دائماً ف وقت ضيقتك ؟",
            "مقولة او حكمة تمشي عليها ...",
            "منشن ... شخص اذا وضعه على الجرح يل",
            "تشوف الي يفكر كثير نفسية ؟",
            "من النوع الي تخطط لامورك ولا تحب تغامر",
            "اكثر وقت تحب النوم فيه",
            "شيء ودك الناس تتركه",
            "اسم اول صديق لك",
            "مع او ضد : اهتمام الشخص بك يجعلك تحب وجوده",
            "@منشن : شخص واكتب صفة م تحبها فيه",
            "اخر مكان سافرت له وين ؟",
            "@منشن : شخص تحس انه نكبه",
            "وش اكثر سؤال يدور في بالك ؟",
            "شيء م تحب احد يشاركك فيه",
            "مع او ضد : الحب بدايته اهتمام",
            "مع او ضد : دائما يكون اهتمامنا مع الانسان الخطأ",
            "لو خيروك : ( قهوة عربية - قهوة تركية )",
            "تحب الشخص ( العفوي - الثقيل - الفلة )",
            "مع او ضد : المراة الجميلة لا تتدحث عن جمالها",
            "اذا جاك كلام ولا عرفت ترد عليه وش بتسوي ؟",
            "@منشن : شخص تشوفه نفسية",
            "تحب المكالمات الطويلة ؟",
            "@منشن : شخص تحس الوقت يطير معه",
            "تنتظر اتصال من مين ؟",
            "زمن تتمنى لو انك انولدت فيه",
            "تعاني من التفكير قبل النوم ؟",
            "مع او ضد : اكثر وقت يفكر فيه الشخص وقت النوم",
            "@منشن : شخص ودك تسافر معه",
            "مرتبطة سعادتك مع سعادة مين ؟",
            "تعتمد على غيرك كثير ؟",
            "كم نسبة الغيرة عندك من 10",
            "مع او ضد : الحقير من وجد البديل ونكر الجميل",
            "مرة سويت جميل و نكره شخص ؟",
            "وش اخر شيء اكلته امس ؟",
            "مع او ضد : ثق بـ نفسك فلا احد يستحق ان تثق به",
            "انت بنفسك تصنع للاشياء قيمة ؟",
            "اخر كلمة تقولها لو خلصت كلامك ؟",
            "كيف ينطق الطفل اسمك ؟",
            "تعتبر نفسك شخص عاطفي ولا عقلاني ؟",
            "مع او ضد : الانتقام افضل وسيلة للراحة",
            "اسف تقولها لمين ؟",
            "هات صفة بأول حرف من اسمك ",
            "شخص ودك م تعرفت عليه ؟",
            "اخر رسالة ديسكورد مع مين؟ ",
            "شخص ما يرد لك طلب ؟",
            "شخص مهما طلب مستحيل ترده ...",
            "وش ناقصك الحين ؟",
            "برايك السهر ممتع ، ولا مُتعب ؟ ",
            "اصدقاء الالكترون ، ولا الواقع ؟ ",
            "حط @منشن .... لـ شخص مُتنمر من الدرجة الاولى",
            "لو كنت شخصية كرتونية اي شخصية بتكون؟",
            "ردك لو احد غلط بحقك واعتذر لك ؟ ",
            "ردك على من يدور الزعل ؟",
            "نشوف نفسك تعرف تقنع الاشخاص ولا لا",
            "اكتب ثلاث اشياء تحبها ...",
            "شخص تحس السيرفر بدونه م يسوى ",
            "اخر شخص عصبت عليه ",
            "ما معنى اسمك ؟",
            "كملها ... انا عُمري ما ( .......)",
            "جربت تحب احد من طرف واحد؟",
            "لو ضاقت فيك الدنيا ... لـ مين تروح ؟",
            "لو كنت ممثل وش تتوقع الدور الي بتتقنه؟ ",
            "خُلق يجذبك فالاخرين ",
            "مهارة تتمنى تتقنها ",
            "وش رايك بالشخص الي يعطي شعور لـ شخصين؟",
            "برأيك الفضفضه .. . نهايتها (راحة ، ندم)",
            "لو التمني يصير حقيقة ... وش بتكون امنيتك ",
            "هل بـ مرة فكرت تنتحر ؟ ",
            "اكبر كذبة كذبتها على مين ؟ ووش كانت..؟",
            "شخصية تقهرك ",
            "وجه كلمه لشخصك ؟",
            "ذكرى جميلة ودك تتكرر ",
            "اول شيء تسويه لما تطفش ",
            "برأيك / ماهو اخطر عدو للانسان ",
            "وش ابشع شعور مريت فيه ",
            "لما تطلع من الديسكورد ، راح تندم على هالايام؟",
            "مع او ضد : الناس صارت م تعرف تسولف",
            "مع او ضد / مساواة المراة بالرجل  في كل شيء؟",
            "كمل : لو اهلي يقرأون افكاري كان (.........)",
            "وش مسمي اقرب شخص لك بالجوال ؟",
            "هل تكون العلاقة فاشلة لو لم تتم بالزواج؟",
            "شيء تفكر تشتريه ...",
            "منشن شخص وقوله كلمة بس  ..",
            "لو كانت عندك فرصة جريمة واحدة ومهما كانت لن تعاقب عليها فماذا ستفعل؟",
            "كم هو عمرك في حال قمت بإضافة 25 سنة إليه؟",
            "كم مرة تنظر إلى المرآة في اليوم؟",
            "هل تثق بالأشخاص الذي تتعرف إليهم عبر التيليقرام؟",
            "هل تؤمن بالصداقة بين الشباب والبنات؟",
            "هل يمكن لك التخلي عن حبك أمام كرامتك؟",
            "هل أنت سريع البديهة؟",
            "هل يمكنك تصنع البكاء؟",
            "هل تسببت بالأذى لشخص ما في حياتك؟",
            "ما الأهم من وجهة نظرك المظهر",
            "هل اشتريت ملابس فقط لكونها جميلة لكنها لا تناسبك؟",
            "كيف تواجه الظروف الصعبة والمشاكل؟",
            "هل رأي الآخرين مهم بالنسبة لك",
            "هل أنت سريع الغضب أم هادئ إلى حد بعيد؟",
            "هل أنت شخص واثق من نفسه أم خجول؟",
            "تحب السفر : ( لحالك ، اصحابك ، اهلك )",
            "تفضل :  ( فيتمو ، تانج ، بيبسي )",
            "رتبهم : ( الحب ، الصحة ، الكرامة ، المال )",
            "تكره الفئة الي ( كل شوي كلام ، دايم يحش )",
            "م تقدر تسيطر على ( ضحكتك ، نومك ، جوعك )",
            "بداية الحب تكون ( اهتمام ، تضحية ، شعور )",
            "مع او ضد : ( خير لك ان تكون مغفلاً من ان تستغفل غيرك )",
            "يبان عليك الحزن من ( صوتك - ملامحك )",
            "لو قلت لك عرف بنفسك بـ ( شطر ) كيف بتعرف بنفسك ؟",
            "اكتب الكلمة بـ لهجتك ( هربت )",
            "برأيك : كم العمر للزواج (مراة ، رجل )",
            "حط @منشن شخص تقوله: لاتتعب نفسك بالسهر م دريت عنك",
            "تفضل الاكل (البحري ولا المشوي)",
            "منشن.. شخص تقوله ( انت اسطورة )",
            "حط@ منشن لـ شخص تقوله (ارتحت لك)",
            "حط@منشن لـ شخص تقوله( ليه أنت جميل كذا ؟.)",
            "تؤمن ان في (حُب من أول نظرة) ولا لا ؟.",
            "حط@ ومنشن . شخص وقوله (الله يسامحك بس)",
            "ردّك على شخص قال (أنا بطلع من حياتك)؟.",
            "حط@منشن شخص تقوله (بطل تفكر فيني ابي انام)",
            "حط@منشن.  شخص وقوله (حركتك مالها داعي).",
            "أجمل شي بحياتك وش هو؟",
            "لو قابلت نفسك الصغيره وش ممكن تقول لها ؟",
            "لو كنت طبيب والمريض الي تعالجه توفى هل عندك القدره تعلم اهله بوفاته ؟",
            "مشروبك المفضل ؟",
            "هل يمكن أن تنتهك القانون لإنقاذ شخص ما ؟",
            "موهبة اكتشفتها في نفسك خلال فترة الحجر ؟",
            "هل الكل يستحق فرصة ثانية حتى مع اعمالهم السيئة ؟",
            "وقتك المفضل باليوم ؟",
            "يومك المفضل بالأسبوع ؟",
            "سويت شي وفخور بنفسك بسببه ؟",
            "ثلاث أشياء تحبها في نفسك ؟",
            "‏تفضل الأفلام: الوثائقية، الخيال، الرومانسي، الأكشن، الرعب ؟",
            "‏لو قالوا لك تقدر تغير شي واحد بنفسك وش بتغير ؟",
            "اغنيتك المفضلة ؟",
            "‏لو خيرت بين الصداقة او الحب أيهم الاختيار الافضل ؟",
            "كيف تقضي وقت فراغك ؟",
            "شيء تعلمته من الحياة ومستحيل تكرره ؟",
            "فخور بذاتك ؟",
            "سطر من أغنية تحبها ؟",
            "كلمة صرت تقولها كثير ؟",
            "وش اول شيء تسويه اذا عصبت ؟",
            "كم اطول فتره قعدت بدون جوال ؟",
            "لو خيروك تكون حيوان وش بتختار ؟",
            "وش افضل فصل عندك ؟",
            "تفضل غرفة لوحدك أو مع اخوانك ؟",
            "وش افضل جوال أمتلكته ؟",
            "وش أسم مسلسلك المفضل ؟",
            "وش أسم فلمك المفضل ؟",
            "وش شعورك الفترة ذي ؟",
            "يومك مر مثل ما خططت له ؟",
            "مين شخصك المفضل ؟",
            "أقرب ثلاث اشخاص لك ؟",
            "اغنية تهديها للي يحبك ؟",
            "اغنية تهديها للي يكرهك ؟",
            "تحب تقرأ الكتب ؟",
            "وش افضل كتاب عندك ؟",
            "مين الي تحسه مستحملك ؟",
            "تحب المطر و أجواء المطر  ؟",
            "نظرتك عن العلاقات والحب ؟",
            "وش المدينة الي تبي تزورها ؟",
            "متى اخر مره طلعت مع اصحابك ؟",
            "وش تسوي في هذه اللحظه ؟",
            "لو الجواب بيكون مستحيل ايش بيكون السؤال ؟",
            "لون حياتك زي لون تيشيرتك الحين ؟",
            "بكل صراحة عندك شخص يفز قلبك اذا جاك شعار منه ؟",
            "متى اخر هدية جتك ؟",
            "شيء فيك ما عجب أهلك ؟",
            "شيء فيك ما عجب اصحابك ؟",
            "ذوقك حلو في ايش ؟",
            "لو صحيت من النوم وحصلت صاحبك مبلكك وش بتسوي ؟",
            "لو الحياة طلعت حلم تفرح أو تحزن ؟",
            "ورينا أسمك بدون نقاط ؟",
            "عندك حظ في الاشياء الي تحبها ؟",
            "تقدر تتحكم بنفسك اذا غرت ؟",
            "كم مشكلة صارت لك في التلي ؟",
            "ورينا اخر 5 ايموجيات استخدمتها ؟",
            "لو شخص جاء يسرق من تحت مخدتك وش بيحصل ؟",
            "قول خمس اشياء تحبها في نفسك ؟",
            "لو الحرام صار حلال وش اول شيء بتسويه ؟",
            "حط قبل شاحن جوالك 1 وشوف كم يطلع ؟",
            "قد رسبت في مادة ؟",
            "اكله مستحيل تاكلها ؟",
            "قول بلهجتك ( أصمت أُريد التحدث )",
            "منشن @ شخص عشوائي يعطيك افتار",
            "هل انت راضي عن نفسك ؟",
            "‏هل انتِ من محبين الموسيقى الكلاسيكيه او الحديثه ؟",
            "اكله ودك تجربها ؟",
            "لو كانت للأيام الجميلة رائحة وش راح ستختار ؟",
            "شيء تحبه بس الناس تشوفه غريب ؟",
            "لو تكرهه جدًا ؟",
            "عطينا إقتباس تحبه من كِتاب أو اغنية ؟",
            "لو العالم مافيه احد غيرك وش اول شيء راح تسويه ؟",
            "انت إجتماعي أو انطوائي؟",
            "هل يومك جيد بنظرك ؟",
            "تفضل القهوه البارد أو الحاره ؟",
            "تفضل الشاي أو القهوه ؟",
            "تفكيرك صار مختلف عن السنة الماضية ؟",
            "لو يبعث الهدوء بنظرك ؟",
            "اذا بتروح مكتبه مثل جرير اول قسم تتوجه له دائمًا ؟",
            "تقدر تستغني عن جهازك لمدة اسبوع ؟",
            "انت صبور أو متسرع ؟",
            "شيء اساسي في يومك ؟",
            "رسالة لنفسك المستقبلية ؟",
            "وش هو نمط حياتك الأن ؟",
            "تتخذ القرار بالمنطق ام بالعاطفة ؟"]
    bar = random.choice(selections)

    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    message.from_user.first_name,
                    url=f"https://t.me/{message.from_user.username}"
                )
            ]
        ]
    )
    await message.reply_text(text=bar, reply_markup=reply_markup)
    
    




@app.on_message(filters.command(["صراحه","اصراحه","الصراحه"], ""), group=8886)
async def bottttt(client, message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    selections = [ "هل تخربني اسم والدتك ما هو.",


            "ليك اسم شهره بتحبو ؟",
            

            "ممكن تعمل اي في حياتك",
            
            
            "انت راضي عن حياتك",
            
            
            "اسم حببتك الاوله ايه",
            
            
            "ما هو هدفك في الحياه",
            
            
            "كم مجموعك الدراسي",
            
            
            "ما هو الاكل المفضل لك",
            
            
            "هل تحب سماع القران الكريم",
            
            
            "هل تامن بالحب",
            
            
            "ماهو اخطر سر اليك",
            
            
            "هل تامن بالارتباط السوشيال",
            
            
            "متي ستتزوج",
            
            
            "هل تحب الفتيات ام الصبيان",
            
            
            "ماهو قولك عندما تره ما تحب",
            
            
            "مانوع هاتفك الجوال",
            
            
            "ماذا تفعل في الشتاء",
            
            
            "هل تحب والديك ام خوتك",
            
            
            "هل لك اسم شهره",
            
            
            "سبق و فعلت شي ندمان علي فعله",
            
            
            "ما هو هدفك في الوقت الحالي",
            
            
            "ما اسم فلمك المفضل",
            
            
            "هل تحب ال• صراحه • ام الكذب",
            
            
            "• أوصف نفسك بكلمة؟",
            
            
            "ممكن تقدم نصيحه لاحدهم بعنوان متغلطش غلطتي",
            
            "تاريخ ميلادك ايه?",
            
            
            "مرتبط ولا سنجل ؟",
            
            
            "انت بخير حاليا ؟",
            
            
            "اسمك ايه",
            
            
            "منين داهيه",
            
            
            "عندك صحاب بنات",
            
            
            "عندك صحاب ولاد",
            
            
            "لونك المفضل",
            
            
            "جربت حاجه نجحت واي هي ؟",
            
            
            "رايك في البار",
            
            
            "مين اكتر حد بتحبه هنا",
            
            
            "هات رقمك",
            
            
            "بتحب المغامره",
            
            
            "احسن حاجه حصلتلك الفتره دي",
            
            
            "بتصلي",
            
            
            "كم فرد في الاسلام",
            
            
            "ممكن تقدم نصيحه لاحدهم بعنوان متغلطش غلطتي",
            
            
            "كم ركعه في صلاه العصر",
            
            
            "ما هيا اليلله التي خير من الف شهر",
            
            
            "سرقت قبل كدا",
            
            
            "هل تحب الموسيقى",
            
            
            "هل تحب مصر",
            
            
            "لو الحمه غلت تاكل ايه",
            
            
            "ايه رايك فيا كابوت موز",
            
            
            "بتحب مين من الفنانين",
            
            
            "امك حلوه",
            
            
            "عندك كم اخ",
            
            
            "تقدر تنصح غيرك",
            
            
            "عاوز تعمل نصيبه امتي",
            
            
            "اي اللي مخليك فجروب الزباله دا",
            
            
            "لابس ايه دلوقتي",
            
            
            "لابسه ايه دلوقتي",
            
            
            "حد باسك قبل كدا",
            
            
            "بوست حد قبل كدا",
            
            
            "بتحب الفلوس",
            
            
            "بتحب الكشري",
            
            
            "نفسك تسافر فيه",
            
            
            "عالطلاق انت كحيااان",
            
            
            "بتعرف ترقص",
            
            
            "بتعرف تغني",
            
            
            "بتحب المدرسه",
            
            
            "ارتبط من المدرسه قبل كدا",
            
            
            "اكتر اتنين بتحب تخرج معاهم",
            
            
            "بتحب الفصح",
            
            
            "بتحب المناسبات",
            
            
            "بتحب الفول",
            
            
            "عاوز تخرج فين",
            
            
            "جربت تموت من الجوع قبل كدا",
            
            
            "بتحب تربي القطط",
            
            
            "مامتك عايشه",
            
            
            "ايه رايك في تليجرام",
            
            
            "ايه رايك في بت اللي فكول دي",
            
            
            "ايه رايك في اسعار في البلد",
            
            
            "ناوي تغير فونك امتي",
            
            
            "تعرف تشتم حد بتحبو",
            
            
            "بتحب الصعيد",
            
            
            "بتحب اسكندريه",
            
            
            "متابع ايه في مسلسلات التركي",
            
            
            "عندك واتساب",
            
            
            "ايه رايك في الشتاء",
            
            
            "ايه رايك في الصيف",
            
            
            "ايه رايك في الخريف",
            
            
            "كم فصل في سنه",
            
            
            "قاعد فين دلوقتي",
            
            
            "شربت حشيش قبل كدا",
            
            
            "بتشرب سجاير",
            
            
            "بتشربي سجاير",
            
            
            "عيط علي حاجه قبل كدا",
            
            
            "بتنام امتي",
            
            
            "شغال ايه",
            
            
            "شغاله ايه",
            
            
            "بتحب شغالك",
            
            
            "نفسك تبقي غني",
            
            
            "بتعرف تخبي مشعارك",
            
            
            "لون عيونك ايه",
            
            
            "لون شعرك ايه",
             "حبيت كام مره 💏",
             
                "اتعاكست كام مره☹️☹️",
                
                "خونت كام مره 😈",
                
                "موقف محرج حصلك😳",
                
                "اكتر شخص حبيته وكسرك💔",
                
                "شايف نفسك فين  بعد 5 سنين🤑",
                
                "لو بقيت بنت ليوم اول حاجه هتعملها ايه والعكس لو بقيتي ولد ليوم اول حاجه هتعمليها ايه🤐🤐",
                
                "اغرب موقف حصلك🤨",
                
                "اقرب انسان لقلبك 💑",
                
                "قولي اغلي 5 اشخاص في حياتك 👨‍👩‍👦‍👦",
                
                "اوصف نفسك في كلمتين👼",
                
                "لو ليك 3 امنيات هيبقوا ايه 🧚‍♂️🧚‍♀️",
                
                "اكتر شخص بتحبه هنا مين😍",
                
                "اوصف صاحب ليك في 3 كلمات😌",
                
                "عاكست قبل كده وكان مين😘",
                
                "اتخانت قبل كده ؟🤣",
                
                "لو اتجبرت علي جواز صالونات هتوافق 👰🤵",
                
                "لو هترتبط بحد في الروم هيبقي مين 😉",
                
                "اهلك بيدلعوك بيقولولك ايه 😁😁",
                
                "صوتك حلو؟",
                
                "لقيت الناس اللي بوشين؟",
                
                "شيء وكنت تحقق اللسان؟",
                
                "أنا شخص ضعيف عندما؟",
                
                "هل ترغب في إظهار حبك ومرفق لشخص أو رؤية هذا الضعف؟",
                "هل الكذب يكون ضروري وقتا ما؟",
                
                "أتشعر بالوحدة على الرغم انه يحاط بك الكثير من البشر؟",
                
                "كيفية الكشف عن من يكمن عليك؟",
                
                "إذا حاول شخص ما أن يكرهه أن يقترب منك ويهتم بك تعطيه فرصة؟",
                
                "أشجع حاجه حلوه ف حياتك؟",
                
                "طريقة جيدة يقنع حتى لو كانت الفكرة خاطئة" 
                
                "كيف تتصرف مع من يسيئون فهمك ويأخذ على ذهنه ثم ينتظر أن يرفض؟",
                
                "التغيير العادي عندما يكون الشخص الذي يحبه؟",
                
                "المواقف الصعبة تضعف لك ولا ترفع؟",
                
                "نظرة و يفسد الصداقة؟",
                
                "‏‏لو حد قالك كلام سئ في الغالب اي رد فعلك؟",
                
                "شخص معاك بالحلوه والمُره؟",
                
                "‏هل تحب إظهار حبك وتعلقك بالشخص أم ترى ذلك ضعف؟",
                
                "تاخد بكلام اللي ينصحك وماتعملش اللي انت عاوزة؟",
                
                "اي تتمني الناس تعرفه عليك؟",
                
                "ابيع المجرة عشان؟",
                
                "أحيانا بحس ان الناس ، كمل؟",
                
                "صدفة العمر الحلوة هي اني؟",
                
                "الكُره العظيم دايم يجي بعد حُب قوي "
                "صفة تحبها في نفسك؟",
                
                "‏الفقر فقر العقول ليس الجيوب "
                
                "تصلي صلواتك الخمس كلها؟",
                
                "‏تجامل أحد على راحتك؟",
                
                "اشجع شيء عملته ف حياتك؟",
                
                "ناوي تعمل اي النهارده؟",
                
                "اي بيكون شعورك لما بتشوف المطر؟",
                "غيرتك هاديه ومابتعملش مشاكل؟",
                "اي اكتر حاجه ندمت عليها؟",
                "اي الدول اللي تتمنى تزورها؟",
                "اخره مره بكيت امتي؟",
                "تقييم حظك ؟ من عشره؟",
                "هل تعتقد ان حظك سيئ؟",
                "شـخــص تتمنــي الإنتقــام منـــه؟",
                "كلمة تود سماعها كل يوم؟",
                "**هل تُتقن عملك أم تشعر بالممل؟",
                "هل قمت بانتحال أحد الشخصيات لتكذب على من حولك؟",
                "متى آخر مرة قمت بعمل مُشكلة كبيرة وتسببت في خسائر؟",
                "ما هو اسوأ خبر سمعته بحياتك؟",
                
                "‏ هل جرحت شخص تحبه من قبل ؟",
                
                "ما هي العادة التي تُحب أن تبتعد عنها؟",
                "‏هل تحب عائلتك ام تكرههم؟",
                "‏من هو الشخص الذي يأتي في قلبك بعد الله – سبحانه وتعالى- ورسوله الكريم – صلى الله عليه وسلم؟",
                "‏هل خجلت من نفسك من قبل؟",
                
                "‏ما هو ا الحلم الذي لم تستطيع ان تحققه؟",
                
                "‏ما هو الشخص الذي تحلم به كل ليلة؟",
                
                "‏هل تعرضت إلى موقف مُحرج جعلك تكره صاحبهُ؟",
                "‏هل قمت بالبكاء أمام من تُحب؟",
                
                "‏ماذا تختار حبيبك أم صديقك؟",
                
                "‏ هل حياتك سعيدة أم حزينة؟",
                
                "ما هي أجمل سنة عشتها بحياتك؟",
                
                "‏ما هو عمرك الحقيقي؟",
                
                "ما هي أمنياتك المُستقبلية؟"]
    bar = random.choice(selections)

    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    message.from_user.first_name,
                    url=f"https://t.me/{message.from_user.username}"
                )
            ]
        ]
    )
    await message.reply_text(text=bar, reply_markup=reply_markup)





##كت و تويت  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
##كت و تويت  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
##كت و تويت  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
##كت و تويت  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.command(["كت","تويت","الكت","التويت"], ""), group=8887765333736)
async def bottttt(client, message):
    if message.chat.id in gamessof:
        return await message.reply_text("الالعاب معطله من قبل الادمن") 
        
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    selections = ["لو قالوا لك  تناول صنف واحد فقط من الطعام لمدة شهر .",


            "شخص تحب تستفزه ؟",


            "لو حلمت في شخص وصحيت وحصلت رساله من نفس الشخص . ارسل ايموجيي مثل ردة فعلك.",


            "هات صورة تحس إنك ابدعت بتصويرها.",


            "على إيش سهران ؟",


            "مين تتوقع يطالعك طول الوقت بدون ملل ؟",


            "وين جالس الحين ؟",


            "كم من عشرة تقيم يومك ؟",


            "أطول مدة نمت فيها كم ساعه ؟",


            "أجمل سنة ميلادية مرت عليك ؟",


            "أخر رسالة بالواتس جاتك من مين ؟",


            "ليه مانمت ؟",


            "تعتقد فيه أحد يراقبك ؟",


            "كم من عشره تعطي حظك ؟",


            "كلمه ماسكه معك الفترة هذي ؟",


            "شيء مستحيل تمل منه ؟",


            "متى تنام بالعادة ؟",


            "كم من عشرة جاهز للدراسة ؟",


            "منشن صديقك الفزعة",


            "يوم نفسك يرجع بكل تفاصيله ؟",


            "أجمل صورة بجوالك ؟",


            "ايش أغرب مكان قد صحتوا فيه؟",


            "اذا جاك خبر مفرح اول واحد تعلمه فيه مين ؟",


            "شيء لو يختفي تصير الحياة جميلة ؟",


            "كم من عشرة تشوف نفسك محظوظ ؟",


            "امدح نفسك بكلمة وحدة بس",


            "كلمة لأقرب شخص لقلبك ؟",


            "قوة الصداقة بالمدة ولا بالمواقف ؟",


            "تتابع مسلسلات ولا م تهتم ؟",


            "تاريخ يعني لك الكثير ؟",


            "كم عدد اللي معطيهم بلوك ؟",


            "من الغباء انك ؟",


            "اكثر شيء محتاجه الحين ؟",


            "ايش مسهرك ؟.",


            "حزين ولا مبسوط ؟",


            "تحب سوالف مين ؟",


            "كم من عشرة روتينك ممل ؟",


            "شيء مستحيل ترفضه ؟.",


            "كم من عشرة الإيجابية فيك ؟.",


            "تعتقد اشباهك الاربعين عايشين حياة حلوة ؟.",


            "مين جالس عندك ؟",


            "كم من عشرة تشوف نفسك انسان ناجح ؟",


            "شيء حظك فيه حلو ؟.",


            "كم من عشرة الصبر عندك ؟",


            "أخر مرة نزل عندكم مطر ؟",


            "اكثر مشاكلك بسبب ؟",


            "اكره شعور ممكن يحسه انسان ؟",


            "شخص تحب تنشبله ؟",


            "تنتظر شيء ؟",


            "جربت تسكن وحدك ؟",


            "اكثر لونين تحبهم مع بعض ؟",


            "متى تكره نفسك ؟",


            "كم من عشرة مروق ؟",


            "مدينة تتمنى تعيش وتستقر فيها طول عمرك ؟",


            "لو للحياة لون إيش بيكون لون حياتك ؟",


            "ممكن في يوم من الأيام تصبح شخص نباتي ؟.",


            "عمرك قابلت شخص يشبهك ؟",


            "اخر شخص تهاوشت معه ؟",


            "قبل ساعة ايش كنت تسوي ؟",


            "كلمة تقولها للي ببالك ؟",


            "أكثر شيء مضيع وقتك فيه ؟",


            "لو فتحتا خزانتك إيش اكثر لون بنشوف ؟",


            "قوة خارقة تتمنى تمتلكها ؟",


            "اكثر مصايبك مع مين ؟",


            "اذا زعلت إيش يرضيك ؟",


            "من النوع اللي تعترف بسرعه ولا تجحد ؟",


            "من الاشياء البسيطة اللي تسعدك ؟",


            "اخر مره بكيت",


            "ايموجي يعبر عن وضعك الحين ؟",


            "التاريخ المنتظر بالنسبة لك ؟",


            "كلنا بنسمعك إيش بتقول ؟",


            "مدينتك اللي ولدت فيها ؟",


            "عندك شخص مستحيل يمر يوم وما تكلمه ؟",


            "كلمة تقولها لنفسك ؟",


            "كم من عشرة متفائل بالمستقبل ؟",


            "ردك المعتاد اذا أحد ناداك ؟",


            "أكثر كلمه تسمعها من أمك ؟",


            "إيش تفضل عمل ميداني ولاعمل مكتبي ؟",


            "أكثر حيوان تحبه ؟",


            "اكثر مشاكلك بسبب ؟",


            "اكثر صوت تكرهه ؟",


            "اشياء تتمنى انها م تنتهي ؟",


            "اشياء صعب تتقبلها بسرعه ؟",


            "كم من عشرة راضي عن وضعك الحالي ؟",


            "متى م تقدر تمسك ضحكتك ؟",


            "اخر شخص قالك كلمة حلوة ؟",


            "اكثر شيء تحبه بنفسك ؟",


            "شيء نفسك يرجع ؟",


            "اغلب وقتك ضايع على ؟",


            "كيف تعرفت على اعز صديق لك ؟",


            "شايل هم شيء الفترة هذي ؟",


            "شخص م تحب تناقشه ؟",


            "تقييمك للديسكورد الفترة هذي ؟",


            "من النوع اللي اذا حطيت راسك على المخده نمت ولا تحتاج وقت ",


            "اهم برنامج عندك بالجوال الفترة هذي ؟",


            "كم تعطي نفسك من عشرة بتعاملك مع مشاكلك ؟",


            "اشياء تبين عليك اذا زعلت ؟",


            "كم من عشرة تحب الجلسة بالبيت ؟",


            "أطول مكالمة لك كم كانت مدتها ؟",


            "اسم تحس صاحبه فخم ؟",


            "تتكلم أكثر ولا تسمع ؟",


            "كم من عشرة تحب النوم ؟",


            "اخر شيء اكلته ؟",


            "أكثر مكان سافرت له بخيالك ؟",


            "كبرت وللحين اخاف من ؟",


            "كيف حالك وانت لحالك ؟",


            "أكثر اسم تحبه ؟.",


            "اكبر مبلغ ضاع منك ؟",


            "كلمة تختصر وضعك الحين ؟",


            "نظام نومك ...",


            "أكثر مكان تجلس فيه غير غرفتك ؟",


            "حرف تحبه ؟",


            "كم درجة الحرارة بمدينتك ؟",


            "تعطي اللي غلط بحقك فرصة ؟",


            "حياتك بكلمة ؟",


            "عندك مليون ريال بس مايمديك تشتري الا شيء  يبدأ بأول حرف من اسمك. وش بتشتري ؟",


            "اكثر شيء ساحب عليه الفترة هذي ؟",


            "شيء مستحيل تعطيه أحد ؟",


            "تنتظر شيء ؟",


            "ايش الوظيفة التي تستحق أعلى راتب؟",


            "كم مره تشحن جوالك باليوم ؟",


            "كم من عشرة عندك امل انك تصير مليونير ؟",


            "اشياء م تسويها غير اذا كنت مروق ؟",


            "لو بيدك تغير بالزمن, تقدمه ولا ترجعه ؟.",


            "دولة امنيتك تزورها ؟.",


            "اكثر  شخص فاهمك بالدنيا ؟",


            "تسامح بسرعة ؟.",


            "كم تحتاج وقت عشان تتعود على مكان جديد ؟",


            "كم من عشرة تحب الهدوء ؟",


            "تاريخ مهم جداً عندك ؟",


            "لعبة تشوف نفسك فنان فيها ؟",


            "أصعب قرار ممكن تتخذه ؟",


            "شيء نفسك تجربه ؟",


            "أشياء توترك ؟",


            "كم من عشرة تحب الاطفال ؟.",


            "اكثر شخص تتهاوش معه ؟",


            "لو خيروك بين يعطونك مليون أو راتب شهري متوسط بدون عمل مدى الحياة إيش تختار ؟",


            "الفلوس كل شيء ؟",


            "عشان تعيش مرتاح ؟",


            "ردة فعلك لو شفت شخص يبكي قدامك ؟",


            "كم مره أخذت عمره بـ رمضان ؟",


            "ردة فعلك لو مزح معك شخص م تعرفه ؟",


            "شيء تشوف نفسك مبدع فيه ؟",


            "ماذا تفعل الان ؟ ",


            "كم من عشرة تحب حياتك ؟.",


            "كم عدد الصور بجوالك ؟.",


            "كم عدد اصحابك المقربين منك كثير ؟.",


            "شكراً لأنك في حياتي ..تقولها لمين ؟",


            "كيف تتعامل مع الشخص اللي يرد متأخر دائماً ؟.",


            "اللوان داكنة  ولا فاتحه؟",


            "كيف تتعامل مع الاشخاص السلبيين ؟",


            "دايم الانطباع الاول عنك إنك شخص ؟",


            "شيء حلو صار لك اليوم ؟",


            "اول شيء يلفت انتباهك بشخص اول مرة تقابله ؟.",


            "جماد م تستغني عنه ؟.",


            "مع ، ضد : البكاء يقلل التوتر ..!",


            "إيش كان نكك ايام البيبي ؟.",


            "من النوع اللي تحفظ اسامي الناس  بسرعه ولا بس اشكالهم ؟.",


            "لو كان لك الحرية تغير اسمك إيش راح تختار اسم ؟",


            "اكثر شيء ضيعت عليه فلوسك ؟",


            "تعرف تمسك نفسك اذا عصبت ؟",


            "عمرك شاركت بمسابقة وربحت ؟",


            "إيش لون جوالك ؟.",


            "تعتقد إنك انسان لك فايدة ؟",


            "اذا احد سألك عن شيء م تعرفه تقول م اعرف ولا تتفلسف ؟",


            "أطول صداقة بينك وبين شخص كم مدتها ؟.",


            "تعرف تعبر عن الكلام اللي بداخلك ؟",


            "ردة فعلك اذا انحشرت بالنقاش ؟",


            "بالعادة برمضان تنحف ولاتسمن ؟",


            "تمارس رياضة معينة برمضان ؟",


            "عندك فوبيا من شيء ؟.",


            "الساعة كم اذان الفجر عندكم ؟",


            "شيء من الماضي للحين عندك ؟.",


            "عندك شخص انت حييل جريء معاه و ما تستحي منه ؟",


            "عمرك انتقمت من شخص؟",


            "اكثر شي يتعبك بالصيام العطش ولا الجوع ؟",


            "اكثر شخص يتصل عليك بالواتس ؟",


            "متى اخر مره جربت شعور ليتني سكت بس ؟",


            "اسم ولد وبنت تحسهم لايقين على بعض ؟.",


            "مسلسل ناوي تشوفه ؟",


            "عادي تتغير عشان شخص تحبه ؟",


            "شيء كل م تذكرته تستانس؟",


            "ايامك هالفترة عبارة عن ؟",


            "منشن شخصين تحسهم نفس الاسلوب او الشخصية ..",


            "اكثر شيء بتشتاق له اذا جاء رمضان ؟",


            "كم مره سامحت بقلبك بس عقلك رافض هالشيء ؟.",


            "مع او ضد .. البنت تحب انشاء المشاكل في العلاقات ..",


            "ماهي طريقتك في معاتبة شخص ؟",


            "لو كنت محتار بين شخص تحبه وشخص يحبك، من تختار؟",


            "الشيء الي تحسه يجذبك للشخص هو ؟",


            "اكثر شخص بينك وبينه تواصل دائم ؟",


            "اعلى نسبة جبتها بحياتك الدراسية ؟",


            "شايل هم شيء ؟ ",


            "إيش تفضل صح وخطأ ولا خيارات ؟",


            "اكثر ايموجي تستخدمه ؟",


            "جربت ينسحب جوالك فترة الاختبارات ؟.",


            "مادة دايم تجيب العيد فيها ؟",


            "وجبة ساحب عليها ؟",


            "تحب تتعرف على ناس جدد ولا مكتفي باللي عندك ؟",


            "مادة تكرها بس درجاتك عالية فيها ؟",


            "شيء بسيط قادر يعدل مزاجك بشكل سريع ؟",


            "اطول مدة جلسة تذاكر فيها بشكل متواصل كم ساعة ؟",


            "قبل امس الوقت هذا إيش كنت تسوي ؟",


            "منشن شخص لو م شفته تحس يومك ناقص ؟",


            "كلمتك اذا شفت حاجة حلوة ؟",


            "خوالك ولا عمامك ؟",


            "عادي تطلع وجوالك مافيه شحن كثير ؟",


            "شيء من صغرك ماتغير فيك ؟",


            "أصعب انتظار ؟",


            "أجمل بيت شعر سمعته ...",


            "مودك الحين ؟",


            "عندك صديق يحمل نفس اسمك ؟",


            "محادثة ولا مكالمة ؟",


            "كم مره يتقلب مزاجك باليوم ؟",


            "اكثر شخص يسوي فيك مقالب ؟",


            "مكان تبي تكون فيه الحين ؟.",


            "كم من عشرة تحب مهنة التدريس ؟",


            "شنو تتوقع بتصير بعد 10 سنين ؟ ",


            "متى تحب الطلعة ؟",


            "أغرب شي اشتهيت تأكله فجأة ؟",


            "اخر مره بكيت متى ؟",


            "اكثر شخص يقفل بوجهك اذا كلمك ؟",


            "كثر شخص يكرفك ؟",


            "تدخل بنقاش بموضوع ماتفهم فيه شيء ولا تسكت وتسمع بس ؟",


            "عمرك طحت بمكان عام ؟",


            "شخص يعرف عنك كل شي تقريباً ؟",


            "اكثر واحد يرسلك بالديسكورد ؟",


            "إيش اللي قدامك الحين ؟",


            "من النوع اللي تعتمد على غيرك ولا كل شي تسويه بنفسك ؟",


            "تقدر تعيش يوم كامل بدون نت ؟",


            "مع او ضد : الاعتراف بـ شيء في قلبك دام طويلاً ؟",


            "أبوك إيش يقرب لأمك ؟",


            "اكثر مدة جلستها بدون نت ؟",


            "لو رجعناك خمس سنين هل كنت تتوقع ان حياتك بتكون نفس وضعك الحين ؟",


            "تتقبل النصيحة من أي أحد ؟",


            "متى لازم تقول لا ؟",


            "أكثر ماده تحبها دراسياً والسبب؟.",


            "إيش نوع قهوتك المفضلة ؟",
            "شخص تشوفه بشكل يومي غير اهلك ؟",


            "شخص تحب ابتسامتة ؟",


            "من الاشياء اللي تجيب لك الصداع ؟",


            "وش تحب تسوي وقت فضاوتك ؟.",


            "كم تعطي نفسك من عشرة بالجدية بحياتك ",


            "أكثر شي يعتمدون عليك فيه ؟",


            "اكثر صفة عندك ؟",


            "كيف تعبر عن عصبيتك ؟",


            "كم داخل سيرفر فالديسكورد ؟",


            "حصلت الشخص اللي يفهمك ولا باقي ؟",


            "تفضل .. العيون الناعسة ... العيون الواسعة ؟",


            "اشياء تغيرت تظرتك لها",


            "الرقم السري حق جوالك ...",


            "لو قررت تقفل جوالك يوم كامل مين تتوقع أنه يفتقدك ؟",


            "اخر هوشه جلدت ولا انجلدت ؟",


            "نصيحه صغيرة من واقع تجربتّك؟.",


            "شخص يكلمك بشكل يومي ؟",


            "أسم وانطباعك عنه ؟",


            "العصر إيش كنت تسوي ؟",


            "كم من عشرة تعطي اهتمامك بدراستك أو عملك ؟",


            "كيف تفرغ غضبك بالعادة ؟",


            "أطول مدة قضيتها بعيد عن أهلك ؟",


            "شخص مستحيل تمسك ضحكتك معاه؟",


            "حاجة دايم تضيع منك ؟",


            "تجامل احد على حساب مصلحتك ؟",


            "كم لك فـ الديسكورد ؟",


            "اخر شخص تهاوشت معه مين ؟",


            "اكثر شيء تكره تنتظره ؟",


            "اخر مطعم اكلت منه ؟",


            "اكثر شيء تحبه بـ شكلك ؟",


            "تنام بـ اي مكان ، ولا بس غرفتك ؟",


            "اكتب اول كلمة جات في بالك الحين ؟",


            "تهمك التفاصيل ولا الزبدة من الموضوع ؟",


            "شيء واحد .. م عاد يهمك كثر اول ؟",


            "كم تقييمك لـ طبخك من 10 ، ولا م تطبخ ؟",


            "اتفه شيء ارسلوك عشانه ؟",


            "فن تحبه كثير ؟",


            "اكثر سوالفك عن ...؟",


            "صفة موجودة في جميع افراد عائلتك ؟",


            "شخص م تقدر تكذب عليه ؟",


            "كم من 10 تحس بـ الطفش ؟",


            "من النوع الي تجيك الردود القوية بعد الهوشة ولا فـ وقتها ؟",


            "تحب تجرب الاشياء الجديدة ، ولا تنتظر الناس يجربونها اول ؟",


            "وش اغبى شيء سويته ؟",


            "اكثر كلمة الناس تقولها عن شخصيتك ؟",


            "مراقبة شخص تركته .. فضول ولا بقايا مشاعر ؟",


            "برنامج كرهته الفترة هاذي",


            "مشهور ، او مشهورة .. يشبهونك فيه",


            "بالغالب وش تسوي فـ الويكند ؟",


            "وش اسم الحي الي ساكن فيه ؟",


            "اكثر شيء تخاف منه ؟",


            "عاده لاتستطيع تركها ؟ ",


            "كم من الوقت تحتاج عشان تصحصح من بعد م صحيت من النوم ؟",


            "اذا حسيت بـ غيرة تتكلم ولا تسكت ؟",


            "مع او ضد ... اقاربك يعرفون عن حساباتك في برامج التواصل ؟",


            "اخر مره سافرت بالطائرة والى وين؟",


            "وش اليوم الي تكرف فيه كثير ؟",


            "تفضل .. الاعمال الحرة ولا الوظيفة ؟",


            "حاجة تشوف نفسك مبدع فيها ؟",


            "ماركتك المفضلة ؟",


            "منشن ... اكثر شخص تثق فيه ؟",


            "اذا انسجنت وش تتوقع بتكون التهمة الي عليك ؟",


            "تعطي الناس فرصة تتقرب منك ؟",


            "منشن .. الشخص الي يستحق تدخل الديسكورد عشانه ..",


            "متى اخر مره نمت اكثر من 12 ساعة ؟",


            "رائحة عطر مدمن عليها ..",


            "وش تحس انك تحتاج الفترة هاذي ؟",


            "كم من 10 البرود فيك ؟",


            "وش اكثر فاكهة تحبها ؟",


            "اصعب وظيفة في نظرك ؟",


            "شيء بسيط قادر على حل كل مشاكلك ..",


            "اذا جلست عند ناس م تعرفهم .. تكتفي بالسكوت ، ولا تتكلم معهم ؟",


            "تتحمل المزح الثقيل ؟",


            "من النوع الي تنام فـ طريق السفر ؟",


            "لو شلنا من طولك 100 كم يبقى من طولك ؟",


            "موقفك من شخص أخفى عنك حقيقة ما، تخوفًا من خسارتك؟ ",


            "اكثر شخص ينرفزك الي ؟",


            "تعرف تتصرف في المواقف العصبة ؟",


            "متى حسيت انك مختلف عن الي غيرك ؟",


            "اصعب مرحلة دراسية مرت عليك ؟",


            "سويت شيء بالحياة وانت مو مقتنع فيه ؟",


            "اخر مره ضربوك فيها ... ووش كان السبب ؟",


            "من الاشياء الي تجيب لك الصداع ؟",


            "مين اول شخص تكلمه اذا طحت بـ مصيبة ؟",


            "مع او ضد : النوم افضل حل لـ مشاكل الحياة ...",


            "تجامل ولا صريح ؟",


            "تفضل المواد الي تعتمد على الحفظ ولا الفهم ؟",


            "صفة تخليك تكره الشخص مهما كان قربه منك ؟",


            "جربت احد يعطيك بلوك وانت تكتب له ؟",


            "تهتم بـ معرفة تاريخ ميلاد الي تحبهم ؟",


            "فيه شيء م تحب تطلبه حتى لو كنت محتاجة ؟",


            "دائما قوة الصداقة بـ ... ؟",


            "اخر شخص قالك كلمة حلوة ..",


            "كم من 10 الي تتوقعه يصير ؟",


            "اذا كنت بنقاش مع شخص وطلع الحق معه تعترف له ولا تصر على كلامك ؟",


            "فيه شخص تكرهه بشكل كبير ؟ ولك جرأة تمنشن اسمه ؟",


            "كيف الجو عندكم اليوم ؟",


            "ترتيبك بالعائلة ؟",


            "تسمع شيلات ؟",


            "تفضل السفر فـ الشتاء ولا الصيف ؟",


            "مع او ضد : الهدية بـ معناها وليس بـ قيمتها",


            "عندك صحبة من اشخاص خارج دولتك",


            "عندك صحبة من اشخاص خارج دولتك ؟",


            "تحب اصوات النساء فـ الاغاني ولا الرجال",


            "وش اول جوال شريته ؟",


            "وش النوع الي تحبه ف الافلام ؟",


            "اكثر مكان تحب تجلس فيه فالبيت ؟",


            "صفة قليل تحصلها فـ الناس حالياً ؟",


            "من النوع الي تعترف ولا تجحد ؟",


            "اول شخص تكلمه اذا صحيت من النوم ؟",


            "وش اجمل لهجة عرببية بالنسبة لك ؟",


            "اخر اتصال من مين كان ؟",


            "اجمل مدينة بدولتك ؟",


            "شاعرك المفضل ؟",


            "كم مره تشحن جوالك باليوم",


            "لو كنت مؤلف كتاب .. وش راح يكون اسمه ؟",


            "اطول مدة قضيتها بدون اكل ..",


            "كم من 10 نسبة الكسل فيك هالايام ؟",


            "نومك خفيف ولا ثقيل ؟",


            "كم من عشرة تشوف صوتك حلو ؟",


            "تجيك الضحكة بوقت غلط ؟",


            "تفضل التسوق من الانترنت ، ولا الواقع ؟",


            "اغرب اسم مر عليك ؟",


            "وش رقمك المفضل ؟",


            "شيء تبيه يصير الحين ...",


            "شاي ولا قهوة ؟",


            "صفة يشوفونها الناس سيئة ، وانت تشوفها كويسه",


            "لون تكرهه ...",


            "وظيفة تحسها لايقة عليك ...",


            "كم من 10 كتابتك بالقلم حلوة ؟",


            "اكلة ادمنتها الفترة ذي ...",


            "اجمل مرحلة دراسية مرت عليك ..",


            "اكثر شيء تكرهه فالديسكورد ..",


            "شيء مستحيل انك تاكله ...",


            "وش رايك بالي يقرأ ولا يرد ؟",


            "اسمك بدون اول حرفين ..",


            "متى تكره الطلعة ؟",


            "شخص من عائلتك يشبهونك فيه ...",


            "اكثر وقت تحب تنام فيه ...",


            "تنتظر احد يجيك ؟",


            "اسمك غريب ولا موجود منه كثير ؟",


            "وش الشيء الي يكرهه اقرب صاحب لك ؟",


            "كم من 10 حبك للكتب ؟",


            "جربت الشهرة او تتمناها ؟",


            "مين اقرب شخص لك بالعائلة ؟",


            "شيء جميل صار لك اليوم ؟",


            "كلمتك اذا احد حشرك بالنقاش ...",


            "اعمال يدوية نفسك تتقنها . ",


            "وش الي يغلب عليك دائما .. قلبك ولا عقلك ؟",


            "صفة تحمد الله انها مو موجودة في اصحابك ...",


            "كم وجبة تاكل فاليوم الفترة هاذي ؟",


            "جربت دموع الفرح ؟ وش كان السبب ؟",


            "لو فقط مسموح شخص واحد تتابعه فالسناب مين بيكون ؟",


            "‏لو حطوك بمستشفى المجانين كيف تقنعهم إنك مو مجنون ؟.",


            "اكثر شيء تحبه فالشتاء ...",


            "شيء ودك تتركه ...",


            "كم تعطي نفسك من 10 فاللغة الانجليزية ؟",


            "شخص فرحتك مرتبطة فيه ...",


            "اكتب اسم .. واكتب كيف تحس بيكون شكله ...",


            "متى اخر مره قلت ليتني سكت ؟",


            "ممكن تكره احد بدون سبب ؟",


            "اكثر وقت باليوم تحبه ...",


            "اكثر شيء حظك سيء فيه ...",


            "متى صحيت ؟",


            "كلمة صعب تقولها وثقيلة عليك ...",


            "ردك الدائم على الكلام الحلو ...",


            "سؤال دايم تتهرب من الاجابة عليه ...",


            "مين الشخص اللي مستعد تأخذ حزنه بس م تشوفه حزين ؟.",


            "جربت تروح اختبار بدون م تذاكر ؟",


            "كم مرة غشيت ف الاختبارات ؟",


            "وش اسم اول شخص تعرفت عليه فالديسكورد ؟",


            "تعطي فرصة ثانية للشخص الي كسرك ؟",


            "لو احتاج الشخص الي كسرك مساعدة بتوقف معه ؟",


            "@منشن... شخص ودك تطرده من السيرفر ...",


            "دعاء له اثر إبجابي في حياتك ...",


            "قل حقيقه عنك ؟",


            "انسان م تحب تتعامل معه ابد",


            "اشياء اذا سويتها لشخص تدل على انك تحبه كثير ؟",


            "الانتقاد الكثير يغيرك للافضل ولا يحطمك ويخليك للأسوأ ؟",


            "كيف تعرف اذا هذا الشخص يكذب ولا لا ؟",


            "مع او ضد : العتاب على قدر المحبة ...",


            "شيء عندك اهم من الناس",


            "تتفاعل مع الاشياء اللي تصير بالمجتمع ولا ماتهتم ؟.",


            "وش الشيء الحلو الي يميزك عن غيرك ؟",


            "كذبة كنت تصدقها وانت صغير ..",


            "@منشن .. شخص تخاف منه اذا عصب ...",


            "كلمة بـ لهجتك تحس م احد بيعرفها ...",


            "كمل ... انا من الاشخاص الي ...",


            "تراقب احد بالديسكورد ؟",


            "كيف تعرف ان هالشخص يحبك ؟",


            "هواية او تجربة كان ودك تستمر و تركتها ؟",


            "الديسكورد اشغلك عن حياتك الواقعية ؟",


            "اكمل ... تستمر علاقتك بالشخص اذا كان ...",


            "لو احد قالك اكرهك وش بتقول له ؟",


            "مع او ضد : عامل الناس كما يعاملوك ؟",


            "ارسل اخر صورة فـ الالبوم ...",


            "الصق وارسل اخر شيء نسخته ...",


            "ماهي اخر وجبة اكلتها ",


            "اكثر شيء تحس انه مات ف مجتمعنا",


            "برأيك ماهو افضل انتقام ...",


            "اكثر ريحة تجيب راسك ...",


            "شعور ودك يموت ...",


            "عمرك فضفضت لـ شخص وندمت ؟",


            "تقدر تتحمل عيوب شخص تحبه ؟",


            "يكبر الشخص ف عيونك لما ...",


            "وش تقول للشخص الي معك دائماً ف وقت ضيقتك ؟",


            "مقولة او حكمة تمشي عليها ...",


            "منشن ... شخص اذا وضعه على الجرح يلتهب زيادة",


            "منشن ... شخص يعجبك كلامه و اسلوبه ...",


            "لو السرقة حلال ... وش اول شيء بتسرقه ؟",


            "مع او ضد : المرأة تحتاج لرجل يقودها ويرشدها ...",


            "مع او ضد : لو دخل الشك ف اي علاقة ستنتهي ...",


            "منشن... اي شخص واوصفه بـ كلام بسيط ...",


            "مع او ضد : قلة العلاقات راحة ...",


            "لو خيروك : تعض لسانك بالغلط ، ولا يسكر على صبعك الباب؟",


            "كلمة غريبه و معناها ...",


            "نصيحة تقدمها للشخص الثرثار ...",


            "مع او ضد :  مساعدة الزوجة في اعمال المنزل مهما كانت ...",


            "منشن... شخص يجيك فضول تشوف وجهه ...",


            "كلمة لـ شخص عزيز عليك ...",


            "اكثر كذبة تقولها ...",


            "معروف عند اهلك انك ...",


            "وش اول طريقة تتبعها اذا جيت تراضي شخص",


            "ع او ضد : ما تعرف قيمة الشخص اذا فقدته ...",


            "تحب تختار ملابسك بنفسك ولا تحب احد يختار معك ...",


            "وش اكثر شيء انجلدت بسببه وانت صغير ؟",


            "فـ اي برنامج كنت قبل تجي الديسكورد ؟",


            "تنسد نفسك عن الاكل لو زعلت ؟",


            "وش الشيء الي تطلع حرتك فيه و زعلت ؟",


            "مع او ضد : الصحبة تغني عن الحب ... ",


            "منشن... اخر شخص خلاك تبتسم",


            "لو نطق قلبك ماذا سيقول ...",


            "ماذا يوجد على يسارك حالياً ؟",


            "مع او ضد : الشخص الي يثق بسرعة غبي ...",


            "شخصية كرتونية تأثرت فيها وانت صغير ...",


            "مع او ضد : الاهتمام الزائد يضايق",


            "لو خيروك : تتزوج ولا تكمل دراستك ...",


            "منشن... لو بتختار شخص تفضفض له مين بيكون ؟",


            "كمل : مهما كبرت بخاف من ....",


            "اخر عيدية جاتك وش كانت ...",


            "وش حذفت من قاموس حياتك ...",


            "شيء تتمنى م ينتهي ...",


            "اكره شعور ممكن يحس فيه الانسان هو ...",


            "مع او ضد : يسقط جمال المراة بسبب قبح لسانها ...",


            "ماهي الخسارة في نظرك ...",


            "لو المطعم يقدم الوجبه على حسب شكلك وش راح تكون وجبتك ؟",


            "مع او ضد : يموت الحب لو طال الغياب",


            "وش الشيء الي يحبه اغلب الناس وانت م تحبه ..",


            "تحدث عن نفسك ؟",


            "اقوى جملة عتاب وصلتك",


            "على ماذا ندمت ؟",


            "اخر مرة انضربت فيها من احد اهلك ، ولماذا ؟",


            "افضل طريقة تراضي فيها شخص قريب منك",


            "لو بإمكانك تقابل شخص من الديسكورد مين بيكون ؟",


            "كمل : كذاب من يقول ان ...",


            "طبعك صريح ولا تجامل ؟",


            "مين اقرب لك ؟ اهل امك ، اهل ابوك  ...",


            "وش لون عيونك ؟",


            "مع او ضد : الرجال اكثر حقداً من النساء",


            "مع او ضد : ينحب الشخص من اهتمامه",


            "@منشن: شخص تقوله اشتقت لك",


            "بصراحة : تحب تفضفض وقت زعلك ، ولا تنعزل ؟",


            "مع او ضد : حبيبك يطلب منك حذف اصحابك بحكم الغيرة",


            "متى تحس بـ شعور حلو ؟",


            "لو حياتك عبارة عن كتاب .. وش بيكون اسمه ؟",


            "@منشن: شخص واسأله سؤال ...",


            "كم مره سويت نفسك غبي وانت فاهم ،  ومع مين ؟",


            "اكتب شطر من اغنية او قصيدة جا فـ بالك",


            "كم عدد الاطفال عندكم فالبيت ؟",


            "@منشن : شخص وعطه وظيفة تحس تناسبه",


            "اخر مكالمة فـ الخاص كانت مع مين ؟",


            "عمرك ضحيت باشياء لاجل شخص م يسوى ؟",


            "كمل : حلو يومك بـ وجود ...",


            "مع او ضد : المرأة القوية هي اكثر انسانه انكسرت",


            "نصيحة تقدمها للغارقين فالحب ...",


            "مبدأ تعتمد عليه فـ حياتك",


            "ترد بالمثل على الشخص لو قذفك ؟",


            "شيء مهما حطيت فيه فلوس بتكون مبسوط",


            "@منشن: اكثر شخص يفهمك",


            "تاريخ ميلادك + هدية بخاطرك تجيك",


            "كم كان عمرك لما اخذت اول جوال ؟",


            "عمرك كتبت كلام كثير بعدين مسحته ، مع مين كان؟",


            "برأيك : وش اكثر شيء يرضي البنت الزعلانه ؟",


            "مساحة فارغة (..............) اكتب اي شيء تبين",


            "تترك احد عشان ماضيه سيء ؟",


            "تهتم بالابراج ، واذا تهتم وش برجك ؟",


            "لو ستبدأ حياتك من جديد ، وش راح تغير بـ نفسك ؟",


            "تتوقع فيه احد حاقد عليك ويكرهك ؟",


            "وش يقولون لك لما تغني ؟",


            "مين المغني المفضل عندك ؟",


            "ميزة ودك يضيفها البرنامج",


            "وش الي مستحيل يكون لك اهتمام فيه ؟",


            "البنت : تتزوجين احد اصغر منك ",


            "الرجل : تتزوج وحده اكبر منك",


            "احقر الناس هو من ...",


            "البنت : وش تتمنين تكون وظيفة زوجك ",


            "الرجل : وش تتمنى وظيفة زوجتك",


            "برأيك : هل الانتقام من الشخص الذي اخطأ بحقك راحة ؟",


            "اهم شيء يكون معك فـ كل طلعاتك ؟",


            "وش الخدمة الالكترونية الي تتمنى تصير ؟",


            "كلمة تخليك تلبي الطلب حق الشخص بدون تفكير",


            "وش الفايدة الي اخذتها من الديسكورد ؟",


            "مع ام ضد : غيرة البنات حب تملك وانانية",


            "هل سبق ان ندمت انك رفضت شيء ، وش كان ؟",


            "تشوف انك قادر على تحمل المسؤولية ؟",


            "مع او ضد : الناس يفضلون الصداقة وعندما يأتي الحب يتركون الصداقة",


            "اعلى نسبة جبتها ف حياتك الدراسية",


            "تحب احد يتدخل ف امورك الشخصية  ؟",


            "لو واحد يتدخل ف امورك وانت م طلبت منه وش بتقوله ؟",


            "تاخذ بنصيحة  الاهل ام من الاصحاب ؟",


            "فيه شيء م تقدر تسيطر عليه ؟",


            "@منشن : شخص تحب سوالفه",


            "وش الكذبة المعتادة الي تسويها لو بتقفل من احد ؟",


            "@منشن: الشخص الي عادي تقوله اسرارك",


            "لو زعلت بقوة وش بيرضيك ؟",


            "كلمة تقولها لـ بعض الاشخاص في حياتك",


            "ندمت انك اعترف بمشاعرك لـ شخص",


            "وش الاكلة المفضلة عندك ؟",


            "وش تتخيل يصير معك فـ المستقبل ؟",


            "اسم الطف شخص مر عليك الكترونياً",


            "مع او ضد : الاستقرار النفسي اهم استقرار",


            "مع او ضد : كل شيء راح يتعوض",


            "برأيك : وش الشيء الي مستحيل يتعوض ؟",


            "تفضل : الدجاج ، اللحم ، السمك",


            "تفضل : الصباح ، الليل",


            "كمل : النفس تميل لـ ...",


            "عندك القوة انك تبين اعجابك لـ شخص ؟",


            "مع او ضد : الرد المتأخر يهدم العلاقات",


            "مشروبك المفضل ...",


            "اقوى كذبة كذبتها على اهلك",


            "@منشن : شخص واكتب شعور نفسك يجربه",


            "وش ردة فعلك من الشخص الي يرد عليك بعد ايام او ساعات ...",


            "كيف تعبر عن عصبيتك ؟",


            "عمرك بكيت على شخص مات في مسلسل ؟",


            "تتأثر بالمسلسلات او الافلام وتتضايق معهم ؟",


            "لو خيروك : بين شخص تحبه وشخص يحبك",


            "اقسى نهاية عندك ...",


            "مع او ضد : كل م زاد المال في الزواج زادت السعادة",


            "لو سمح لك بسرقة شيء ويكون ملك لك .. ماذا ستسرق ؟",


            "تقدر تنام وخاطرك مكسور ؟",


            "برأيك : اقرب لهجة عربية قريبة للفصحى ؟",


            "مر عليك شخص ف حياتك مستحيل انك تسامحه ",


            "عندك صاحب له معك اكثر من 5 سنين ؟",


            "وش معنى اسمك ؟",


            "عندك الصاحب الي تقول للناس اتحداكم تفرقونا ؟",


            "تقييمك لـ صوتك ف الغناء من 10",


            "كم طولك ؟",


            "كم وزنك ؟",


            "وش طموحك بالحياة ؟",
            "لو بيدك توقف شيء يصير ، وش راح توقف ؟",


            "وش اسم قبيلتك ؟",


            "اقرب فعل لقلبك ؟",


            "وش نوع جوالك ؟",


            "وش المطعم المفضل عندك ؟",


            "مين الشخص الي محلي حياتك ؟",


            "انا مدمن على ...",


            "مع او ضد : الصدق هو سر استمرار العلاقات فترة طويلة",


            "تكون اجمل شخص اذا ...",


            "شكلك يعطي لأي جنسية ؟",


            "وش اكثر دولة تحب الشعب حقها ؟",


            "اول بيت تزوره فالعيد ..",


            "جمال المراة يكمن في ...",


            "مشهور تعجبك سناباته ..",


            "مشهور تكرهه",


            "يكفيك عطر واحد ولا تحب تحط اكثر من عطر ؟",


            "مرة جاك احد بيذكرك فيه وانت ناسي ؟",


            "لو احد بيذكرك فيه وانت ناسي بتسلك له ؟",


            "اغنيتك المفضلة ...",


            "مع او ضد : لو م اخذت شيء معك وقت زيارة احد انت مقصر",


            "يهمك ملابسك تكون ماركة ؟",


            "مع او ضد : او اهتزت مكانة الشخص مستيحل ترجع",


            "لو رجع لك شخص تعرفه بعد علاقته بالخيانة ، راح ترجع نفس اول ؟",


            "صفة لا تتمنى ان تكون فـ عيالك",


            "وش اسم قروبك انت واصحابك المقربين ؟",


            "وش اسم قروب عائلتك فالواتس اب ؟",


            "مع او ضد : تكون الزوجة عندما تشترط خادمة في العقد سيئة",


            "لعبة ندمت انك لعبتها ...",


            "مع او ضد : يمكن للبنت تغيير رأي الرجل بسهولة",


            "كلمة او عبارة مستحيل تنساها",


            "ارسل اكثر ايموجي تحبه",


            "شيء تتمنى يتحقق",


            "مع او ضد : الدنيا لم تتغير ، بل النفوس التي تغيرت",


            "وش جمع اسمك ؟",


            "كلمة لـ شخص زعلان منك ...",


            "عادة غريبة تسويها ..",


            "تحب ريحة الحناء ؟",


            "نومك : ثقيل ولا خفيف",


            "اكثر شيء يرفع ضغطك",


            "اكتب تاريخ مستحيل تنساه",


            "لو حظك يباع ، بكم بيكون ؟",


            "@منشن : شخص تشوف انه يجذبك",


            "البنت : عادي تحضنين اخوك ؟",


            "الولد : عادي تحضن ابوك ؟",


            "كلمة تحب تسمعها حتى لو كنت زعلان",


            "قوة الاستيعاب عندك من 10",


            "افضل نوع عطر استخدمته",


            "وش بتختار اسم لأول مولود لك ؟",


            "متى تصير نفسية ؟",


            "كيف ينطق الطفل اسمك ؟",


            "تشوف نفسك شخص عاطفي ولا علاقني ؟",


            "متى لازم تقول لا ؟",


            "تحب توجه الكلام عن طريق ( الكتابة ، الصوت )",


            "مين اقرب لك : (خوالك ، عمامك )",


            "تحب تتعرف على ناس جديدة ولا اكتفيت بالي عندك ؟",


            "شيء كل م تذكرته تبتسم ...",


            "كم قروب واتس داخل ؟",


            "كم سيرفر داخل فالديسكورد ؟",


            "مع او ضد : المسامحة بعد الخيانة ...",


            "وش الامنية الي ودك تتحقق ؟",


            "كيف تتصرف مع الشخص الفضولي ؟",


            "الرجل : متى تفقد البنت انوثتها",


            "ماهي اسباب نهاية العلاقات ؟",


            "@منشن : شخص ودك تعطيه كتم ",


            "مين الي تحب يكون مبتسم دائما",


            "حصلت الشخص الي يفهمك ولا باقي ؟",


            "كم تحتاج وقت عشان تصحصح من نومك ؟",


            "كيف تعالج الغيرة الزائدة ؟",


            "مع او ضد : كل شيء حلو يكون فالبداية فقط",


            "اطول مدة قضيتها بعيد عن اهلك",


            "شيء دايم يضيع منك",


            "اغنية ناشبه ف مخك",


            "رسالة للناس الي بيدخلون حياتك",


            "جملة او كلمة تكررها",


            "اكثر اغنية تكرهها ؟",


            "صوت مغني م تحبه",


            "مع او ضد : الغيرة بين الاصدقاء",


            "اكثر وقت تحب تنام فيه",


            "وش اثقل مشوار ممكن تسويه ؟",


            "اقرب شخص لك بالعائلة",


            "اخر مكان سافرت له",


            "مع او ضد : حنا اكثر الناس عندنا حكم لكن م نطبقها",


            "مع و ضد : العتاب اكثر من مره دليل على ان الشخص م يقدرك",


            "كم مشاهداتك باسناب؟ ",


            "مع او ضد : اكثر من في الديسكورد أُناس يتصنعون",


            "شيء نفسك تعيشه من جديد",


            "كلمة تحسسك بالامان",


            "كم تعطي نفسك من 10 فـ تعاملك مع مشاكلك",


            "مع او ضد : اكثر من يحلون مشاكل الناس ، هم اكثر الناس لديهم مشاكل",


            "مع او ضد : علاج الخطأ بالخطأ في زمننا هذا هو الحل",


            "وش اكثر شيء يضيع منك ؟",


            "مع او ضد : السفر يصلح ما افسده الدهر",


            "جربت شعور حب من طرف واحد ؟",


            "ما ترد الطلعة لو كانت الى ...",


            "كم لك في الديسكورد ؟",


            "شيء كل ما تتذكره تنبسط",


            "اكتب كلام ودك الناس يطبقونه ( ......... )",


            "كيف تعالج الغيرة الزائدة ؟",


            "مع او ضد : من حق الشخص ما يبدا بالرسالة لانه مو متعود",


            "عندك شخص يكلمك يومياً ، تستحي تقوله لا ترسل",


            "مع او ضد : من يهتم بك لا تخسره قد لا تعيد لك الحياة شخصاً مثله",


            "اصعب مرحلة دراسية مرت عليك",


            "هل انت مدمن تفكير ؟",


            "تشوف الي يفكر كثير نفسية ؟",


            "من النوع الي تخطط لامورك ولا تحب تغامر",


            "اكثر وقت تحب النوم فيه",


            "شيء ودك الناس تتركه",


            "اسم اول صديق لك",


            "مع او ضد : اهتمام الشخص بك يجعلك تحب وجوده",


            "@منشن : شخص واكتب صفة م تحبها فيه",


            "اخر مكان سافرت له وين ؟",


            "@منشن : شخص تحس انه نكبه",


            "وش اكثر سؤال يدور في بالك ؟",


            "شيء م تحب احد يشاركك فيه",


            "مع او ضد : الحب بدايته اهتمام",


            "مع او ضد : دائما يكون اهتمامنا مع الانسان الخطأ",


            "لو خيروك : ( قهوة عربية - قهوة تركية )",


            "تحب الشخص ( العفوي - الثقيل - الفلة )",


            "مع او ضد : المراة الجميلة لا تتدحث عن جمالها",


            "اذا جاك كلام ولا عرفت ترد عليه وش بتسوي ؟",


            "@منشن : شخص تشوفه نفسية",


            "تحب المكالمات الطويلة ؟",


            "@منشن : شخص تحس الوقت يطير معه",


            "تنتظر اتصال من مين ؟",


            "زمن تتمنى لو انك انولدت فيه",


            "تعاني من التفكير قبل النوم ؟",


            "مع او ضد : اكثر وقت يفكر فيه الشخص وقت النوم",


            "@منشن : شخص ودك تسافر معه",


            "مرتبطة سعادتك مع سعادة مين ؟",


            "تعتمد على غيرك كثير ؟",


            "كم نسبة الغيرة عندك من 10",


            "مع او ضد : الحقير من وجد البديل ونكر الجميل",


            "مرة سويت جميل و نكره شخص ؟",


            "وش اخر شيء اكلته امس ؟",


            "مع او ضد : ثق بـ نفسك فلا احد يستحق ان تثق به",


            "انت بنفسك تصنع للاشياء قيمة ؟",


            "اخر كلمة تقولها لو خلصت كلامك ؟",


            "كيف ينطق الطفل اسمك ؟",


            "تعتبر نفسك شخص عاطفي ولا عقلاني ؟",


            "مع او ضد : الانتقام افضل وسيلة للراحة",


            "اسف تقولها لمين ؟",


            "هات صفة بأول حرف من اسمك ",


            "شخص ودك م تعرفت عليه ؟",


            "اخر رسالة ديسكورد مع مين؟ ",


            "شخص ما يرد لك طلب ؟",


            "شخص مهما طلب مستحيل ترده ...",


            "وش ناقصك الحين ؟",


            "برايك السهر ممتع ، ولا مُتعب ؟ ",


            "اصدقاء الالكترون ، ولا الواقع ؟ ",


            "حط @منشن .... لـ شخص مُتنمر من الدرجة الاولى",


            "لو كنت شخصية كرتونية اي شخصية بتكون؟",


            "ردك لو احد غلط بحقك واعتذر لك ؟ ",


            "ردك على من يدور الزعل ؟",


            "نشوف نفسك تعرف تقنع الاشخاص ولا لا",


            "اكتب ثلاث اشياء تحبها ...",


            "شخص تحس السيرفر بدونه م يسوى ",


            "اخر شخص عصبت عليه ",


            "ما معنى اسمك ؟",


            "كملها ... انا عُمري ما ( .......)",


            "جربت تحب احد من طرف واحد؟",


            "لو ضاقت فيك الدنيا ... لـ مين تروح ؟",


            "لو كنت ممثل وش تتوقع الدور الي بتتقنه؟ ",


            "خُلق يجذبك فالاخرين ",


            "مهارة تتمنى تتقنها ",


            "وش رايك بالشخص الي يعطي شعور لـ شخصين؟",


            "برأيك الفضفضه .. . نهايتها (راحة ، ندم)",


            "لو التمني يصير حقيقة ... وش بتكون امنيتك ",


            "هل بـ مرة فكرت تنتحر ؟ ",


            "اكبر كذبة كذبتها على مين ؟ ووش كانت..؟",


            "شخصية تقهرك ",


            "وجه كلمه لشخصك ؟",


            "ذكرى جميلة ودك تتكرر ",


            "اول شيء تسويه لما تطفش ",


            "برأيك / ماهو اخطر عدو للانسان ",


            "وش ابشع شعور مريت فيه ",


            "لما تطلع من الديسكورد ، راح تندم على هالايام؟",


            "مع او ضد : الناس صارت م تعرف تسولف",


            "مع او ضد / مساواة المراة بالرجل  في كل شيء؟",


            "كمل : لو اهلي يقرأون افكاري كان (.........)",


            "وش مسمي اقرب شخص لك بالجوال ؟",


            "هل تكون العلاقة فاشلة لو لم تتم بالزواج؟",


            "شيء تفكر تشتريه ...",


            "منشن شخص وقوله كلمة بس  ..",


            "لو كانت عندك فرصة جريمة واحدة ومهما كانت لن تعاقب عليها فماذا ستفعل؟",


            "كم هو عمرك في حال قمت بإضافة 25 سنة إليه؟",


            "كم مرة تنظر إلى المرآة في اليوم؟",


            "هل تثق بالأشخاص الذي تتعرف إليهم عبر التيليقرام؟",


            "هل تؤمن بالصداقة بين الشباب والبنات؟",


            "هل يمكن لك التخلي عن حبك أمام كرامتك؟",


            "هل أنت سريع البديهة؟",


            "هل يمكنك تصنع البكاء؟",


            "هل تسببت بالأذى لشخص ما في حياتك؟",


            "ما الأهم من وجهة نظرك المظهر",


            "هل اشتريت ملابس فقط لكونها جميلة لكنها لا تناسبك؟",


            "كيف تواجه الظروف الصعبة والمشاكل؟",


            "هل رأي الآخرين مهم بالنسبة لك",


            "هل أنت سريع الغضب أم هادئ إلى حد بعيد؟",


            "هل أنت شخص واثق من نفسه أم خجول؟",


            "تحب السفر : ( لحالك ، اصحابك ، اهلك )",


            "تفضل :  ( فيتمو ، تانج ، بيبسي )",


            "رتبهم : ( الحب ، الصحة ، الكرامة ، المال )",


            "تكره الفئة الي ( كل شوي كلام ، دايم يحش )",


            "م تقدر تسيطر على ( ضحكتك ، نومك ، جوعك )",


            "بداية الحب تكون ( اهتمام ، تضحية ، شعور )",


            "مع او ضد : ( خير لك ان تكون مغفلاً من ان تستغفل غيرك )",


            "يبان عليك الحزن من ( صوتك - ملامحك )",


            "لو قلت لك عرف بنفسك بـ ( شطر ) كيف بتعرف بنفسك ؟",


            "اكتب الكلمة بـ لهجتك ( هربت )",


            "برأيك : كم العمر للزواج (مراة ، رجل )",


            "حط @منشن شخص تقوله: لاتتعب نفسك بالسهر م دريت عنك",


            "تفضل الاكل (البحري ولا المشوي)",


            "منشن.. شخص تقوله ( انت اسطورة )",


            "حط@ منشن لـ شخص تقوله (ارتحت لك)",


            "حط@منشن لـ شخص تقوله( ليه أنت جميل كذا ؟.)",


            "تؤمن ان في (حُب من أول نظرة) ولا لا ؟.",


            "حط@ ومنشن . شخص وقوله (الله يسامحك بس)",


            "ردّك على شخص قال (أنا بطلع من حياتك)؟.",


            "حط@منشن شخص تقوله (بطل تفكر فيني ابي انام)",


            "حط@منشن.  شخص وقوله (حركتك مالها داعي).",


            "أجمل شي بحياتك وش هو؟",


            "لو قابلت نفسك الصغيره وش ممكن تقول لها ؟",


            "لو كنت طبيب والمريض الي تعالجه توفى هل عندك القدره تعلم اهله بوفاته ؟",


            "مشروبك المفضل ؟",


            "هل يمكن أن تنتهك القانون لإنقاذ شخص ما ؟",


            "موهبة اكتشفتها في نفسك خلال فترة الحجر ؟",


            "هل الكل يستحق فرصة ثانية حتى مع اعمالهم السيئة ؟",


            "وقتك المفضل باليوم ؟",


            "يومك المفضل بالأسبوع ؟",


            "سويت شي وفخور بنفسك بسببه ؟",


            "ثلاث أشياء تحبها في نفسك ؟",


            "‏تفضل الأفلام: الوثائقية، الخيال، الرومانسي، الأكشن، الرعب ؟",


            "‏لو قالوا لك تقدر تغير شي واحد بنفسك وش بتغير ؟",


            "اغنيتك المفضلة ؟",


            "‏لو خيرت بين الصداقة او الحب أيهم الاختيار الافضل ؟",


            "كيف تقضي وقت فراغك ؟",


            "شيء تعلمته من الحياة ومستحيل تكرره ؟",


            "فخور بذاتك ؟",


            "سطر من أغنية تحبها ؟",


            "كلمة صرت تقولها كثير ؟",


            "وش اول شيء تسويه اذا عصبت ؟",


            "كم اطول فتره قعدت بدون جوال ؟",


            "لو خيروك تكون حيوان وش بتختار ؟",


            "وش افضل فصل عندك ؟",


            "تفضل غرفة لوحدك أو مع اخوانك ؟",


            "وش افضل جوال أمتلكته ؟",


            "وش أسم مسلسلك المفضل ؟",


            "وش أسم فلمك المفضل ؟",


            "وش شعورك الفترة ذي ؟",


            "يومك مر مثل ما خططت له ؟",


            "مين شخصك المفضل ؟",


            "أقرب ثلاث اشخاص لك ؟",
            "اغنية تهديها للي يحبك ؟",


            "اغنية تهديها للي يكرهك ؟",


            "تحب تقرأ الكتب ؟",


            "وش افضل كتاب عندك ؟",


            "مين الي تحسه مستحملك ؟",


            "تحب المطر و أجواء المطر  ؟",


            "نظرتك عن العلاقات والحب ؟",


            "وش المدينة الي تبي تزورها ؟",


            "متى اخر مره طلعت مع اصحابك ؟",


            "وش تسوي في هذه اللحظه ؟",


            "لو الجواب بيكون مستحيل ايش بيكون السؤال ؟",


            "لون حياتك زي لون تيشيرتك الحين ؟",


            "بكل صراحة عندك شخص يفز قلبك اذا جاك شعار منه ؟",


            "متى اخر هدية جتك ؟",


            "شيء فيك ما عجب أهلك ؟",


            "شيء فيك ما عجب اصحابك ؟",


            "ذوقك حلو في ايش ؟",


            "لو صحيت من النوم وحصلت صاحبك مبلكك وش بتسوي ؟",


            "لو الحياة طلعت حلم تفرح أو تحزن ؟",


            "ورينا أسمك بدون نقاط ؟",


            "عندك حظ في الاشياء الي تحبها ؟",


            "تقدر تتحكم بنفسك اذا غرت ؟",


            "كم مشكلة صارت لك في التلي ؟",


            "ورينا اخر 5 ايموجيات استخدمتها ؟",


            "لو شخص جاء يسرق من تحت مخدتك وش بيحصل ؟",


            "قول خمس اشياء تحبها في نفسك ؟",


            "لو الحرام صار حلال وش اول شيء بتسويه ؟",


            "حط قبل شاحن جوالك 1 وشوف كم يطلع ؟",


            "قد رسبت في مادة ؟",


            "اكله مستحيل تاكلها ؟",


            "قول بلهجتك ( أصمت أُريد التحدث )",


            "منشن @ شخص عشوائي يعطيك افتار",


            "هل انت راضي عن نفسك ؟",


            "‏هل انتِ من محبين الموسيقى الكلاسيكيه او الحديثه ؟",


            "اكله ودك تجربها ؟",


            "لو كانت للأيام الجميلة رائحة وش راح ستختار ؟",


            "شيء تحبه بس الناس تشوفه غريب ؟",


            "لو تكرهه جدًا ؟",


            "عطينا إقتباس تحبه من كِتاب أو اغنية ؟",


            "لو العالم مافيه احد غيرك وش اول شيء راح تسويه ؟",


            "انت إجتماعي أو انطوائي؟",


            "هل يومك جيد بنظرك ؟",


            "تفضل القهوه البارد أو الحاره ؟",


            "تفضل الشاي أو القهوه ؟",


            "تفكيرك صار مختلف عن السنة الماضية ؟",


            "لو يبعث الهدوء بنظرك ؟",


            "اذا بتروح مكتبه مثل جرير اول قسم تتوجه له دائمًا ؟",


            "تقدر تستغني عن جهازك لمدة اسبوع ؟",


            "انت صبور أو متسرع ؟",


            "شيء اساسي في يومك ؟",


            "رسالة لنفسك المستقبلية ؟",


            "وش هو نمط حياتك الأن ؟",


            "تتخذ القرار بالمنطق ام بالعاطفة ؟",


            "خمس اشياء مُمتن لها ؟",


            "أنا مُميز لأنّي _________ ؟",


            "كِلمة تتمنئ أنها تُحذف مِن قأموس مجتمعك ؟",


            "هل لديك حيوان اليف ؟",


            "أفضل أنمي عندك ؟",


            "أفضل فِلم عندك ؟",


            "أفضل مسلسل عندك ؟",


            "وش الفِلم أو الانمي الي تتمنئ الناس تشوفه ؟",


            "لحظات صغيرة من الصعب نسيانها ؟",


            "ماهي اساسيات العلاقة بالنسبة لك ؟",


            "عندك ڤوبيا من وش ؟",


            "ماهي اكثر المناظر التي تحبها ؟",


            "متى شعرت أنك كبرت ؟",


            "كِلمة تُسعد وتُحب سَماعها دائمًا ؟",


            "أكثر جُملة أثرت في حياتك ؟",


            "شخص أثر في حياتك ؟",


            "كِلمة توجهها للي يسطرون ؟",


            "كيف تتوقع حياتك اذا حبيت وخانتك حبيبتك ؟",


            "أخر مره تحدثت في الخاص ؟",


            "كم محادثة في الخاص ؟",


            "كم قروب عندك ؟",


            "عندك قروبات محد يدري عنها ؟",


            "عندك اشخاص مخبيهم عن الناس ؟",


            "تغار على صديقك أو صديقتك ؟",


            "كِلمة للي بيتيكن ؟",


            "قد كرهت أحد بسبب إسلوبه ؟",


            "قد حبيت شخص وخذلك ؟",


            "قد تعرضت للخيانه ؟",


            "قد صار لك حادث ؟",


            "قد حفظت كِتاب الله الكريم ؟",


            "عندك رتبة في القروب ؟",


            "لو قالوا أحظر شخص من الموجودين مين بتختار ؟",


            "اخر صوره حفظتها ؟",


            "تحب التجمعات ؟",


            "كلمة محتاج تسمعها عشان تفرح وتنبسط ؟",


            "اغنيه تحب تسمعها ؟",


            "مدينه تتمنى تسافر لها ؟",


            "( أنتِ غيمة قلبي وأطيَب أشخاصي ) لمن تهدي هالكلام ؟",


            "أذكر 5 اشخاص لازم تسولف معهم ؟",


            "صورة لشيء تتمنى إمتلاكه ؟",


            "اغلب وقتك اليوم قضيته في ؟",


            "منشن اول شخص طرأ على بالك بهاللحظه ؟",


            "قاعده تمشي عليها عند اختيارك للملابس ؟",


            "منشن شخص هنا ودك تكلمه تحظره ؟",


            "اشياء جميلة صارت لك اليوم ؟",


            "منشن شخص وحاول تقلد أسلوبه ؟",


            "اكثر 5 اشياء تكرهها في التلي ؟",


            "تحب الميمز ؟",


            "وش الشيء الي بشخصيتك تعتبره شيء مميز ؟",


            "دولة تتمنئ تزورها ؟",


            "( يا صديقي إن لم يُنصفك كتفي هاك ضلعي، اتكِئ ) منشن شخص يحتاج هالكلام ؟",


            "وش هي افضل سنه في حياتك وليش ؟",


            "‎الكتاب او الفيلم الي تتمنى تعيش فيه، و السبب ؟",


            "وش هي هوايتك المفضله ؟",


            "اذا حياتك هي نفس لون لبسك وش راح تكون ؟",


            "وش هو افضل برنامج عندك ؟",


            "انت شخص صريح ؟",


            "انت شخص تستحي ولا ما عليك ؟",


            "هل شخصيتك بالواقع نفس المواقع ؟",


            "وش اكبر مخاوفك او كوابيسك ؟",


            "تجربة في حياتك تتمنى تعيدها ؟",


            "صفه تحبها فيك سواًء كانت شكليًا او اخلاقيًا ؟",


            "صفة يصفك فيها شخص مقرب لك ؟",


            "أوصف أعز صديق لك ؟",


            "عبر عن مودك ب إيموجي ؟",


            "عندك شخص تفتقده اذا ما سولف ؟",


            "أختراع تتمنى يكون موجود ؟",


            "أول ما تصحى تكلم مين ؟",


            "أول ما تطيح في مصيبة تكلم مين ؟",


            "أول من تفضفض له مين ؟",


            "أكثر مرحله دراسية تحبها ؟",


            "وش اول شيء تسويه اذا تضايقت ؟",


            "اكثر شيء معروف بشخصيتك ؟",


            "كم عدد الاشخاص الي متهاوش معهم ؟",


            "وش تسوي الأن ؟",


            "متى أخر هديه جاتك ؟",


            "شيء فيك ما يعجب أهلك ؟",


            "تحس ذوقك حلو في ايش ؟",


            "اذا صحيت من النوم وحصلت شخصك المفضل مبلكك وش تسوي ؟",


            "أكتب أسمك وأنت مغمض ؟",


            "وش هو أفضل بوت ؟",


            "تقدر تتحكم في ذاتك اذا غرت ؟",


            "كم مشكلة دخلتها حتى الأن ؟",


            "اذا جيت بسرق الي تحت مخدتك وش بحصل ؟",


            "قول أشياء إيجابية عن نفسك ؟",


            "اذا شحن جوالك هو نسبة نعاسك، كم ؟",


            "سوي منشن @ عشوائي وقوله أحبك ؟",


            "قد صديقك سحب عليك عشان حبيبته ؟",


            "أفضل حافز للشخص ؟",


            "مسلسل/فلم تتابعة هالفترة ؟",


            "بماذا تختلف عن الآخرين ؟",


            "ماذا سرقت منك الحياة ؟",


            "صفة تجمّل الشخص برأيك ؟",


            "أفضل شيء تعلمته برأيك ؟",


            "ماذا تشتهي روحك ؟",


            "صورة لها ذكرى لا تنساها ؟",


            "إيموجي يوصف مزاجك حاليًا ؟",


            "الأهم بالنسبة لك، القلب أوم العقل ؟",


            "ما معنى أسمك ؟",


            "أشياء تجيب السعادة ؟",


            "يومك ما يكتمل إلا بـ_____ ؟",


            "أجمل شيء صار لك اليوم ؟",


            "بلد تحب شعبها ؟",


            "كم أسم ( منال ) تعرف في حياتك ؟",


            "هل تعود المياه إلى مجاريها بعد الاعتذار ؟",


            "متى تتقبل الهزيمة في الحب ؟",


            "أول بداية لطريق النجاح ؟",


            "كلمة لأصحاب الشائعات والأخبار الكاذبة ؟",


            "يومك في كلمة ؟",


            "انطباعك عن أسم ( الوليد، العنود ) ؟",


            "بلد تود الإقامة فيها ؟",


            "درس تعلمته في التلي ؟",


            "حيوان تخاف منه ؟",


            "طريقتك على الحصول الرأحة النفسية ؟",


            "أعظم إنجاز لك ؟",


            "نسبة رضاك عن نفسك في الفترة الأخيرة ؟",


            "جنسية غير جنسية بلدك تود لو تحصل عليها ؟",


            "هل للحزن دواء ؟",


            "دعاء وأذكار ترا لها أثر في حياتك ؟",


            "كلمات لا تتحمل سماعها ؟",


            "عطنا اعتراف أو شي حصل معك وإذا حكيت عنه محد صدقك ؟",


            "كيف علاقتك مع الحب ؟",


            "أي ترغب به الآن ؟",


            "متى تكون البراءه ذئب ؟",


            "هل تتوقع أن يصل البشر لمرحلة من التطور تجعلهم يتنقلون بين الكواكب بسهولة ؟",


            "أشياء ومنتجات جربتها في السفر أعجبتك ؟",


            "( الحياة مرة )/ هل قرأتها بالضمة أم بالفتحة ؟",


            "يتجاهلك بالقصد بعد صداقة طويلة، ما مقصده برأيك ؟",


            "شعورك الحالي في جملة ؟",


            "عندكم في الشلة ذلك الشخص الخجول جدًا ؟",


            "أشياء تجعلك تستمر وتتحمّل صعوبات الحياة ؟",


            "فنان/ة تحلم بلقائه ؟",


            "بتنام ولا بتواصل ؟",


            "ردة فعلك لو أوقفتك الشرطة في الطريق وسمعتهم يقولون هذا هو القاتل ؟",


            "شاركنا افضل قناة عندك ؟",


            "شيء جميل حصل معك اليوم ؟",


            "شاركنا صوره تمثل تخصصك ؟",


            "للإناث | لديكِ الجرأة لمصارحة الشخص اللي أذاك بكل شيء في قلبك ؟",


            "أكثر طبع غريب فيك وتحبه ؟",


            "أبسط شيء بعدل يومك كامل ؟",


            "سؤال تسأل نفسك فيه دائمًا ولا حصلت جواب ؟",


            "أسم تحب تقوله ؟",


            "أسم بنت تحبه ؟",


            "أسم ولد تحبه ؟",


            "وش تحس من يوم يناديك أبوك ؟",


            "مين أشد عصبية أمك أو أبوك ؟",


            "عادي تتابع فلم/مسلسل أكثر من مره ؟",


            "تقدر ترسل أخر صوره حفظتها ؟",


            "وش هي أكلتك المفظلة ؟",


            "وش الصفة الي تميزك عن غيرك ؟",


            "أنت شخص مسالم ؟",


            "شيء تسمعه كثير من الناس عنك ؟",


            "تحس أنك غامض ولا سراويلك منشوره ؟",


            "صفة تكرهها ؟",


            "أنت من النوع الي يعرف يسولف ويفتح مواضيع ؟",


            "موضوع ما تتقبل المزح فيه ؟",


            "كِلمة توجهها لوالديك ؟",


            "سطر من أخر أغنية سمعتها ؟",


            "عندك شخص تقوله كل تفاصيل يومك ؟",


            "ليش الاغلب يفضلون العلاقات الإكترونية ؟",


            "وش رأيك بالأهل الي يفتشون الجوالات ؟",


            "أهلك يفتشون جوالك ؟",


            "هل أنت راضي عن نفسك الفترة ذي ؟",


            "أنت من مُحبين الموسيقى القديمة أو الجديدة ؟",


            "أكله ودك تجربها ؟",


            "لو كانت للأيام الجميلة رائحه ماذا ستكون ؟",


            "تاريخ ودك تعيش فيه ؟",


            "لو تكرهه جدًا ؟",


            "عطينا إقتباس تحبه ؟",


            "عطينا حكمة لليوم ؟",


            "حكمتك الي ماشي عليها ؟",


            "أنت فاشل دراسيًا ؟",


            "انت متوظف ؟",


            "أسمك الي بالبرنامج غير عن الواقعي ؟",


            "مين الي أختار لك أسمك ؟",


            "كذبت في الأسئلة الي راحت ؟",


            "لو العالم مافيه أحد غيرك وش بتسوي ؟",


            "هل يومك جيد ؟",


            "القهوة بنظرك ؟",


            "تفكيرك الأن مُختلف عن العام الماضي ؟",


            "لو تروح مكتبه مثل جرير اول قسم تتوجه له دائمًا ؟",


            "تقدر تستغني عن هاتفك لأسبوع ؟",


            "شيء تحس لو ما سويته ليوم تفقده ؟",


            "رسالة لنفسك المستقبيلة ؟",


            "وش رأيك في الي يطلب السناب ؟",


            "تقدر تعطي سنابك أحد ؟",


            "كم شخص مسوي له بلوك ؟",


            "مفهوم الصداقة بالنسبة لك ؟",


            "يزيد حُبي لكِ لمّا ... ؟",


            "مِن نِعْم الحياة ... ؟",


            "اذا فضفضت ترتاح ؟",


            "اكثر شي ينرفزك ؟",


            "اخر مكان رحتله ؟",


            "شخص @ تعترفلة بشي ؟",


            "تغار ؟",


            "تعتقد فيه أحد يراقبك 👩🏼‍💻؟",


            "ولادتك بنفس المكان الي عايش فيه ولا لا؟",


            "اكثر شي ينرفزك ؟",


            "تغار ؟",


            "كم تبلغ ذاكرة هاتفك؟",


            "صندوق اسرارك ؟",


            "شخص @ تعترفله بشي ؟",


            "يومك ضاع على ؟",


            "اغرب شيء حدث في حياتك ؟",


            " نسبة حبك للاكل ؟",


            " حكمة تأمان بيها ؟",


            " اكثر شي ينرفزك ؟",


            " هل تعرضت للظلم من قبل؟",


            " خانوك ؟",


            " تزعلك الدنيا ويرضيك ؟",


            " تاريخ غير حياتك ؟",


            " أجمل سنة ميلادية مرت عليك ؟",


            " ولادتك بنفس المكان الي هسة عايش بي او لا؟",


            " تزعلك الدنيا ويرضيك ؟",


            " ماهي هوايتك؟",


            " دوله ندمت انك سافرت لها ؟",


            "شخص اذا جان بلطلعة تتونس بوجود؟",


            " تاخذ مليون دولار و تضرب خويك؟",


            " تاريخ ميلادك؟",


            "اشكم مره حبيت ؟",


            " يقولون ان الحياة دروس ، ماهو أقوى درس تعلمته من الحياة ؟",


            " هل تثق في نفسك ؟",


            " اسمك الثلاثي ؟",


            "كلمة لشخص خذلك؟",


            "هل انت متسامح ؟",


            "طريقتك المعتادة في التخلّص من الطاقة السلبية؟",


            "عصير لو قهوة؟",


            " صديق أمك ولا أبوك. ؟",


            "تثق بـ احد ؟",


            "كم مره حبيت ؟",


            " اوصف حياتك بكلمتين ؟",


            " حياتك محلوا بدون ؟",


            " وش روتينك اليومي؟",


            " شي تسوي من تحس بلملل؟",


            " يوم ميلادك ؟",


            " اكثر مشاكلك بسبب ؟",


            " تزعلك الدنيا ويرضيك ؟",


            " تتوقع فيه احد حاقد عليك ويكرهك ؟",


            "كلمة غريبة من لهجتك ومعناها؟",


            " • هل تحب اسمك أو تتمنى تغييره وأي الأسماء ستختار",


            "• كيف تشوف الجيل ذا؟",


            "• تاريخ لن تنساه📅؟",


            "• هل من الممكن أن تقتل أحدهم من أجل المال؟",
            "• تؤمن ان في حُب من أول نظرة ولا لا ؟.",


            "• ‏ماذا ستختار من الكلمات لتعبر لنا عن حياتك التي عشتها الى الآن؟💭",


            "• طبع يمكن يخليك تكره شخص حتى لو كنت تُحبه🙅🏻‍♀️؟",


            "• ما هو نوع الموسيقى المفضل لديك والذي تستمع إليه دائمًا؟ ولماذا قمت باختياره تحديدًا؟",


            "• أطول مدة نمت فيها كم ساعة؟",


            "• كلمة غريبة من لهجتك ومعناها؟🤓",


            "• ردة فعلك لو مزح معك شخص م تعرفه ؟",


            "• شخص تحب تستفزه😈؟",


            "• تشوف الغيره انانيه او حب؟",


            "• مع او ضد : النوم افضل حل لـ مشاكل الحياة؟",


            "• اذا اكتشفت أن أعز أصدقائك يضمر لك السوء، موقفك الصريح؟",


            "• ‏للعيال - آخر مرة وصلك غزل من بنت؟",


            "• أوصف نفسك بكلمة؟",


            "• شيء من صغرك ماتغير فيك؟",


            "• ردة فعلك لو مزح معك شخص م تعرفه ؟",


            "• اذا شفت حد واعجبك وعندك الجرأه انك تروح وتتعرف عليه ، مقدمة الحديث وش راح تكون ؟.",


            "• كلمة لشخص أسعدك رغم حزنك في يومٍ من الأيام ؟",


            "• حاجة تشوف نفسك مبدع فيها ؟",


            "• يهمك ملابسك تكون ماركة ؟",


            "• يومك ضاع على؟",


            "• اذا اكتشفت أن أعز أصدقائك يضمر لك",


            " السوء، موقفك الصريح؟",


            "• هل من الممكن أن تقتل أحدهم من أجل المال؟",


            "• كلمه ماسكه معك الفترة هذي ؟",


            "• كيف هي أحوال قلبك؟",


            "• صريح، مشتاق؟",


            "• اغرب اسم مر عليك ؟",


            "• تختار أن تكون غبي أو قبيح؟",


            "• آخر مرة أكلت أكلتك المفضّلة؟",


            "• اشياء صعب تتقبلها بسرعه ؟",


            "• كلمة لشخص غالي اشتقت إليه؟",


            "• اكثر شيء تحس انه مات ف مجتمعنا؟",


            "• هل يمكنك مسامحة شخص أخطأ بحقك لكنه قدم الاعتذار وشعر بالندم؟",


            "• آخر شيء ضاع منك؟",


            "• تشوف الغيره انانيه او حب؟",


            "• لو فزعت/ي لصديق/ه وقالك مالك دخل وش بتسوي/ين؟",


            "• شيء كل م تذكرته تبتسم ...",


            "• هل تحبها ولماذا قمت باختيارها؟",


            "• هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",


            "• متى تكره الشخص الذي أمامك حتى لو كنت مِن أشد معجبينه؟",


            "• أقبح القبحين في العلاقة: الغدر أو الإهمال🤷🏼؟",


            "• هل وصلك رسالة غير متوقعة من شخص وأثرت فيك ؟",


            "• هل تشعر أن هنالك مَن يُحبك؟",


            "• وش الشيء الي تطلع حرتك فيه و زعلت ؟",


            "• صوت مغني م تحبه",


            "• كم في حسابك البنكي ؟",


            "• اذكر موقف ماتنساه بعمرك؟",


            "• ردة فعلك لو مزح معك شخص م تعرفه ؟",


            "• عندك حس فكاهي ولا نفسية؟",


            "• من وجهة نظرك ما هي الأشياء التي تحافظ على قوة وثبات العلاقة؟",


            "• ما هو نوع الموسيقى المفضل لديك والذي تستمع إليه دائمًا؟ ولماذا قمت باختياره تحديدًا؟",


            "• هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",


            "• هل وصلك رسالة غير متوقعة من شخص وأثرت فيك ؟",


            "• شيء من صغرك ماتغير فيك؟",


            "• هل يمكنك أن تضحي بأكثر شيء تحبه وتعبت للحصول عليه لأجل شخص تحبه؟",


            "• هل تحبها ولماذا قمت باختيارها؟",


            "• كلمة لشخص أسعدك رغم حزنك في يومٍ من الأيام ؟",


            "• كم مره تسبح باليوم",


            "• أفضل صفة تحبه بنفسك؟",


            "• أجمل شيء حصل معك خلال هاليوم؟",


            "• ‏شيء سمعته عالق في ذهنك هاليومين؟",


            "• هل يمكنك تغيير صفة تتصف بها فقط لأجل شخص تحبه ولكن لا يحب تلك الصفة؟",


            "• ‏أبرز صفة حسنة في صديقك المقرب؟",


            "• ما الذي يشغل بالك في الفترة الحالية؟",


            "• آخر مرة ضحكت من كل قلبك؟",


            "• احقر الناس هو من ...",


            "• اكثر دوله ودك تسافر لها؟",


            "• آخر خبر سعيد، متى وصلك؟",


            "• ‏نسبة احتياجك للعزلة من 10؟",


            "• هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",


            "• أكثر جملة أثرت بك في حياتك؟",


            "• لو قالوا لك  تناول صنف واحد فقط من الطعام لمدة شهر .",


            "• هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",


            "• آخر مرة ضحكت من كل قلبك؟",


            "• وش الشيء الي تطلع حرتك فيه و زعلت ؟",


            "• تزعلك الدنيا ويرضيك ؟",


            "• متى تكره الشخص الذي أمامك حتى لو كنت مِن أشد معجبينه؟",


            "• تعتقد فيه أحد يراقبك؟",


            "• احقر الناس هو من ...",


            "• شيء من صغرك ماتغير فيك؟",


            "• وين نلقى السعاده برايك؟",


            "• هل تغارين من صديقاتك؟",


            "• أكثر جملة أثرت بك في حياتك؟",


            "• كم عدد اللي معطيهم بلوك؟",


            "• أجمل سنة ميلادية مرت عليك ؟",


            "• أوصف نفسك بكلمة؟"]
    bar = random.choice(selections)

    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    message.from_user.first_name,
                    url=f"https://t.me/{message.from_user.username}"
                )
            ]
        ]
    )
    await message.reply_text(text=bar, reply_markup=reply_markup)




    



board = ["⬜️"] * 9
players = []
current_player = 0
fanish_game = None  

def create_board():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(board[0], callback_data="10"), InlineKeyboardButton(board[1], callback_data="11"), InlineKeyboardButton(board[2], callback_data="12")],
        [InlineKeyboardButton(board[3], callback_data="13"), InlineKeyboardButton(board[4], callback_data="14"), InlineKeyboardButton(board[5], callback_data="15")],
        [InlineKeyboardButton(board[6], callback_data="16"), InlineKeyboardButton(board[7], callback_data="17"), InlineKeyboardButton(board[8], callback_data="18")],
    ])

@app.on_message(filters.command(["اكس او","اكس","xo","ox"], ""), group=76468513) 
async def sta54t_game(client, message):
    global players, board, fanish_game, current_player
    current_player = 0
    fanish_game = False
    players = [message.from_user.id]
    board = ["⬜️"] * 9
    await message.reply_text("""
قم بضغط  بالاسفل للعب""", reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("بدء اللعب 🎮", callback_data="join_game")]
    ]))

@app.on_callback_query(filters.regex("join_game"), group=768513) 
async def join_game(client, call):
    global players, current_player
    current_player = 0
    if call.from_user.id not in players:
        players.append(call.from_user.id)
        await client.edit_message_text(
            call.message.chat.id, call.message.id,
            f"دور الاعب الاول : ❌",
            reply_markup=create_board())

def check_winner():
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "⬜️":
            return board[combo[0]] 
    return None

def is_draw():
    return all(cell != "⬜️" for cell in board)

@app.on_callback_query(
    filters.regex("10") | filters.regex("11") | filters.regex("12") |
    filters.regex("13") | filters.regex("14") | filters.regex("15") |
    filters.regex("16") | filters.regex("17") | filters.regex("18"), group=768513) 
async def handle_button(client, call):
    global current_player, players, fanish_game
    if fanish_game == True:
        await call.answer("اللعبة انتهت ⚡️", show_alert=True)
        return
    if call.from_user.id not in players:
        await call.answer("✋", show_alert=True)
        return
    if call.from_user.id != players[current_player]:
        await call.answer("ليس دورك", show_alert=True)
        return
    index = int(call.data) - 10
    if board[index] == "⬜️":
        board[index] = "❌" if current_player == 0 else "⭕️"
        current_player = 1 if current_player == 0 else 0
        user = await client.get_users(players[current_player])
        user_mention = user.mention()
        emo_xo = "❌" if current_player == 0 else "⭕️"
        await call.message.edit(
            f"دور الاعب : {emo_xo}\n{user_mention}",
            reply_markup=create_board())
        
        winner = check_winner()
        if winner:
            winner_mention =(await client.get_users(players[0 if winner == "❌" else 1])).mention
            await call.message.edit(
                f"الفائز 🎉: {winner_mention}")
            fanish_game = True 
            board[:] = ["⬜️"] * 9
        elif is_draw():
            await call.message.edit(
                "التعادل! 🤝")
            fanish_game = True
            board[:] = ["⬜️"] * 9
        if fanish_game==True:
            return
