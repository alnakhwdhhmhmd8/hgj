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
 






 
restricted_users = []

@app.on_message(filters.command(["تقيد"], ""), group=728)
async def mute_user(client: Client, message: Message):
    global restricted_users    

    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user = await client.get_users(message.reply_to_message.from_user.id)
        name = user.first_name
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        target = message.command[1].strip("@")
        user = await client.get_users(target)
    else:
        await message.reply_text("لا يمكن العثور على المستخدم")
        return
    
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name
    
    if chat_member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        if target == message.from_user.id:
            await message.reply_text("هييه مايمديك تقيد نفسك ياورع!")
            return
            
            
        if target == "7728230165":
            await message.reply_text("هييه مايمديك تقيد جاك ياورع!")
            return
            
        if target == OWNER_ID:
            await message.reply_text("هييه مايمديك تقيد مطوري ياورع!")
            return       
            
        member = await message.chat.get_member(target)
        if member.status in [ChatMemberStatus.OWNER]:
            return await message.reply("هييه مايمديك تقيد مالك اساسي ياورع!")
        
        member = await message.chat.get_member(target)
        if member.status in [ChatMemberStatus.ADMINISTRATOR]:
            return await message.reply("هييه مايمديك تقيد ادمن ياورع!")

        if target not in restricted_users and target != OWNER_ID:
            mute_permission = ChatPermissions(can_send_messages=False)
            await app.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=target,
                permissions=mute_permission,
            )
            restricted_users.append(target)
            user = await client.get_users(target) 
            name = user.first_name  
            mention = f"<a href='tg://user?id={target}'>{name}</a>"
            await message.reply_text(f"<blockquote>「 {user.mention} 」</blockquote>\nقييدته.", parse_mode=enums.ParseMode.HTML)
        else:
            await message.reply_text(f"<blockquote>「 {user.mention} 」</blockquote>\nمقيد من قبل.", parse_mode=enums.ParseMode.HTML)
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")




@app.on_message(filters.command(["الغاء تقيد","الغاء التقيد"], ""), group=94) 
async def mute(client: Client, message: Message):
    global restricted_users    

    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user = await client.get_users(message.reply_to_message.from_user.id)
        name = user.first_name
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        target = message.command[1].strip("@")
        user = await client.get_users(target)
    else:
        await message.reply_text("لا يمكن العثور على المستخدم")
        return
    
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name
    
    if chat_member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        if target == message.from_user.id:
            await message.reply_text("هييه ما متقيده نفسك ياورع!")
            return
            
        if target == OWNER_ID:
            await message.reply_text("هييه ما متقيد مطوري ياورع!")
            return       
            
        member = await message.chat.get_member(target)
        if member.status in [ChatMemberStatus.OWNER]:
            return await message.reply("هييه ما متقيد المالك الاساسي ياورع!")
        
        member = await message.chat.get_member(target)
        if member.status in [ChatMemberStatus.ADMINISTRATOR]:
            return await message.reply("هييه ما متقيد الادمن ياورع!")

        if target != OWNER_ID:
            mute_permission = ChatPermissions(can_send_messages=False)
            await app.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=target,
                permissions=unmute_permissions,
            )
            restricted_users.append(target)
            user = await client.get_users(target)  
            name = user.first_name  
            mention = f"<a href='tg://user?id={target}'>{name}</a>"
            await message.reply_text(f"</blockquote>「 {user.mention} 」</blockquote>\nابشر الغيت تقيدته", parse_mode=enums.ParseMode.HTML)
        else:
            await message.reply_text(f"<blockquote>「 {user.mention} 」</blockquote>\nهييه ما متقيد", parse_mode=enums.ParseMode.HTML)
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")





@app.on_message(filters.command(["مسح المقيدين"], ""), group=40)
async def unmute(client: Client, message: Message):
    global restricted_users
    user_id = message.from_user.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        count = len(restricted_users)
        for user_id in restricted_users:
            await client.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=user_id,
                permissions=unmute_permissions,
            )
        restricted_users = []
        await message.reply_text(f"↢ مسحت {count} من المقيدين")
    else:
        await message.reply_text(f"هذا الامر يخص ❪ الادمن وفوق ❫ بس")





    

@app.on_message(filters.command(["المقيدين"], ""), group=4770)
async def get_restr_users(client: Client, message: Message):
   usr = await client.get_chat(message.from_user.id)
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 7728230165:
         count = len(restricted_users)
         response = f" <blockquote><u>قائمة المقيدين وعددهم :</u></blockquote> {count}\n"
         for user in restricted_users:
             user = await client.get_users(user)
             response += f"{user.mention} \n"
         await message.reply_text(response)
   else:
        await message.reply_text(f"حجي هذا الامر ليس لك ")







# كتم ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# كتم ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


muted_users = []
        
        
@app.on_message(filters.command(["كتم"], ""), group=726262728)
async def mute_user(client, message):
    global muted_users    
    
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
    
    if chat_member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:      
        if user_id == str(message.from_user.id):
            await message.reply_text("هييه مايمديك تكتم نفسك ياورع!")
            return
            
        if user_id == "7728230165":
            await message.reply_text("هييه مايمديك تكتم جاك ياورع!")
            return
            
        if user_id == OWNER_ID:
            await message.reply_text("هييه مايمديك تكتم مطور ياورع!")
            return       
            
        member = await message.chat.get_member(user_id)
        if member.status in [ChatMemberStatus.OWNER]:
            return await message.reply("هييه مايمديك تكتم مالك اساسي ياورع!")
        
        member = await message.chat.get_member(user_id)
        if member.status in [ChatMemberStatus.ADMINISTRATOR]:
            return await message.reply("هييه مايمديك تكتم الادمن ياورع!")

        if user_id not in muted_users and user_id != OWNER_ID:
            muted_users.append(user_id)
            user = await client.get_users(int(user_id))
            await message.reply_text(f"<blockquote>「 {user.mention} 」</blockquote>\nكتمته")
        else:
            await message.reply_text(f"<blockquote>「 {user.mention} 」</blockquote>\nمكتوم  من قبل")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")
        
       
@app.on_message(filters.text)
async def handle_message(client, message):
    if message.from_user and str(message.from_user.id) in muted_users:
        await client.delete_messages(chat_id=message.chat.id, message_ids=message.id)
        


        

#الغاء الكتم ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.command(["الغاء الكتم","الغاء كتم"], ""), group=2)
async def unmute_user(client, message):
    global muted_users    
    
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
    
    if chat_member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        
        if user_id not in muted_users:
            await message.reply_text(f"<blockquote>「 {user.mention} 」</blockquote>\nولك مو مكتوم")
        else:
            muted_users.remove(user_id)
            user = await client.get_users(int(user_id))
            await message.reply_text(f"<blockquote>「 {user.mention} 」</blockquote>\nابشر الغيت كتمه")            
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")

#اامكتومين ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

@app.on_message(filters.command(["المكتومين"], ""), group=137762627)
async def get_rmuted_users(client, message):
    global muted_users

    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and message.from_user.id != 7728230165 or message.from_user.id == 7728230165:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")
        return

    count = len(muted_users)
    user_mentions = [await client.get_chat_member(message.chat.id, user_id) for user_id in muted_users]
    response = f"<blockquote><u>قائمة المكتومين وعددهم:</u></blockquote> {count}\n"
    response += "...\n"
    for i, user in enumerate(user_mentions, start=1):
        mention = user.user.mention()
        response += f"{i}- {mention}\n"
    await message.reply_text(response, parse_mode=enums.ParseMode.HTML)

# مسح المكتومين  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

@app.on_message(filters.command(["مسح المكتومين"], ""), group=136)
async def unmute_all(client, message):
   usr = await client.get_chat(message.from_user.id)
   name = usr.first_name
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
    global muted_users
    count = len(muted_users)
    chat_id = message.chat.id
    failed_count = 0

    for member in muted_users.copy():
        user_id = member
        try:
            muted_users.remove(member)
        except Exception:
            failed_count += 1

    successful_count = count - failed_count

    if successful_count > 0:
        await message.reply_text(f"مسحت {successful_count} من المكتومين")
    else:
        await message.reply_text(" ⇜ مافيه مكتومين")

    if failed_count > 0:
        await message.reply_text(f"↢ فشل في مسح {failed_count}\nمن المكتومين")
   else:
        await message.reply_text(f"هذا الامر يخص ❪ الادمن وفوق ❫ بس")



# حظر  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# حظر  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


banned_users = []

@app.on_message(filters.command(["حظر"], ""), group=726262728656)
async def ban_user(client, message):
    global banned_users

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

    if chat_member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
        if user_id == str(message.from_user.id):
            await message.reply_text("هييه مايمديك حظر نفسك ياورع!")
            return

        if user_id == "7728230165":
            await message.reply_text("هييه مايمديك تحظر جاك ياورع!")
            return
            
        if user_id == OWNER_ID:
            await message.reply_text("هييه مايمديك تحظر مطور ياورع!")
            return       

        member = await message.chat.get_member(user_id)
        if member.status in [ChatMemberStatus.OWNER]:
            return await message.reply("هييه مايمديك تحظر المالك ياورع!!")

        member = await message.chat.get_member(user_id)
        if member.status in [ChatMemberStatus.ADMINISTRATOR]:
            return await message.reply("مايمدي احظره لانه مشرف")

        if user_id not in banned_users:
            banned_users.append(user_id)
            await client.ban_chat_member(message.chat.id, user_id)
            user = await client.get_users(int(user_id))
            await message.reply_text(f"<blockquote>「 {user.mention} 」</blockquote>\nحظرته.")
        else:
         user = await client.get_users(int(user_id))
         await message.reply_text(f"<blockquote>「 {user.mention} 」</blockquote>\nمحظور من قبل")
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")


# الغاء الحظر ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

@app.on_message(filters.command(["الغاء الحظر","الغاء حظر"], ""), group=726262782)
async def unban_user(client, message):
    global banned_users
    
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
    
    if chat_member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:  
        
        if user_id not in banned_users:
         user = await client.get_users(int(user_id))
         await message.reply_text(f"<blockquote>「 {user.mention} 」</blockquote>\nولك مو محظور")
        else:
            await app.unban_chat_member(message.chat.id, user_id)
            banned_users.remove(user_id)
            user = await client.get_users(int(user_id))
            await message.reply_text(f"<blockquote>「 {user.mention} 」</blockquote>\nابشر الغيت حظره")          
    else:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")        
 
 
# المحظورين  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
        
               
@app.on_message(filters.command(["المحظورين"], ""), group=137762627)
async def banned_userss(client, message):
    global banned_users

    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and message.from_user.id != 7728230165 or message.from_user.id == 7728230165:
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")
        return

    count = len(banned_users)
    user_mentions = [await client.get_chat_member(message.chat.id, user_id) for user_id in banned_users]
    response = f"<blockquote><u>قائمة المحظورين وعددهم:</u></blockquote> {count}\n"
    response += "...\n"
    for i, user in enumerate(user_mentions, start=1):
        mention = user.user.mention()
        response += f"{i}- {mention}\n"
    await message.reply_text(response, parse_mode=enums.ParseMode.HTML)
    
                                                              
# مسح المحظورين  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

@app.on_message(filters.command(["مسح المحظورين"], ""), group=19)
async def unban_all(client: Client, message: Message):
   usr = await client.get_chat(message.from_user.id)
   usr = await client.get_chat(message.from_user.id)
   name = usr.first_name
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165:
    global banned_users
    count = len(banned_users)
    chat_id = message.chat.id
    failed_count = 0

    for member in banned_users.copy():
        user_id = member
        try:
            await client.unban_chat_member(chat_id, user_id)
            banned_users.remove(member)
        except Exception:
            failed_count += 1

    successful_count = count - failed_count

    if successful_count > 0:
        await message.reply_text(f"مسحت {successful_count} من المحظورين")
    else:
        await message.reply_text("⇜ مافيه محظورين")

    if failed_count > 0:
        await message.reply_text(f"↢ فشل في مسح {failed_count}\nمن المحظورين")
   else:
         await message.reply_text(f"هذا الامر يخص ❪ الادمن وفوق ❫ بس")  



        






#كود كتم ننينيمصكش

# muted_users = []

# @app.on_message(filters.command(["كتم"], ""), group=726262728)
# async def mute_user(client, message):
    # global muted_users    
    
    # if message.reply_to_message and message.reply_to_message.from_user:
        # target = message.reply_to_message.from_user.id
        # user_id = str(target)
    # elif len(message.text.split()) > 2:
        # target = message.text.split()[2]
        # user = await client.get_users(target)
        # if user:
            # user_id = str(user.id)
        # else:
            # await message.reply_text("لا يمكن العثور على المستخدم")
            # return
    # else:
        # target = message.text.split()[1].strip("@")
        # user = await client.get_users(target)
        # if user:
            # user_id = str(user.id)
        # else:
            # await message.reply_text("لا يمكن العثور على المستخدم")
            # return
    
    # chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    # name = chat_member.user.first_name
    
    # if chat_member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 7728230165:       
        # if user_id == message.from_user.id:
            # await message.reply_text("هييه مايمديك تكتم نفسك ياورع!")
            # return
            
        # if user_id == "7728230165":
            # await message.reply_text("هييه مايمديك تكتم جاك ياورع!")
            # return

        # if user_id == "5675627801":
            # await message.reply_text("هييه مايمديك تكتم زومبي ياورع!")
            # return

        # if user_id == OWNER_ID:
            # await message.reply_text("هييه مايمديك تكتم مالك البوت ياورع!")
            # return
            
        # member = await message.chat.get_member(user_id)
        # if member.status in [ChatMemberStatus.OWNER]:
            # return await message.reply("هييه مايمديك تكتم مالك اساسي ياورع!")
        
        # member = await message.chat.get_member(user_id)
        # if member.status in [ChatMemberStatus.ADMINISTRATOR]:
            # return await message.reply("هييه مايمديك تكتم ادمن ياورع!")

        # if user_id not in muted_users:
            # muted_users.append(user_id)
            # user = await client.get_users(int(user_id))
            # await message.reply_text(f"「 {user.mention} 」\nكتمته")
        # else:
            # await message.reply_text(f"「 {user.mention} 」\nمكتوم  من قبل")
    # else:
        # await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")
 
# @app.on_message(filters.text)
# async def handle_message(client, message):
    # if message.from_user and str(message.from_user.id) in muted_users:
        # await client.delete_messages(chat_id=message.chat.id, message_ids=message.id)        