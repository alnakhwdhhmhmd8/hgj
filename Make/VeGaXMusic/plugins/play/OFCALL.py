import asyncio
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from VeGaXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from VeGaXMusic.core.call import KIM
from VeGaXMusic.utils.database.assistantdatabase import get_assistant
from typing import Optional
from random import randint
from pyrogram.types import Message, ChatPrivileges
from pyrogram import Client, filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from VeGaXMusic.utils.database import *
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant, ChatAdminRequired
from VeGaXMusic import app , Userbot

##مكاتب مين فكول

from pyrogram import filters, Client
from VeGaXMusic import app
import asyncio
from pytgcalls import PyTgCalls, filters
from pytgcalls.types import MediaStream
from VeGaXMusic.core.call import KIM
from VeGaXMusic.utils.database import *
from pytgcalls.exceptions import NoActiveGroupCall, AlreadyJoinedError
from ntgcalls import TelegramServerError
###تحكم
import asyncio
import re
from pyrogram import Client, filters
from pyrogram import filters, Client
from datetime import datetime
from pyrogram import enums
from pyrogram import Client
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
from VeGaXMusic.utils.database.memorydatabase import set_loop
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










async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    assistant = await get_assistant(message.chat.id)
    chat_peer = await assistant.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (
                await assistant.invoke(GetFullChannel(channel=chat_peer))
            ).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await assistant.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await app.send_message(f"**No group call Found** {err_msg}")
    return False


@app.on_message(filters.regex("^افتح الكول$"), group=752)
@app.on_message(filters.regex("^افتح الكول$") & filters.channel, group=752)
async def start_group_call(client: Client, message: Message):
    msg = await message.reply("🎁")
    await asyncio.sleep(2)
    await msg.delete()
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name    
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7623838169:
        chat_id = message.chat.id
        assistant = await get_assistant(chat_id)
        ass = await assistant.get_me()
        assid = ass.id
        if assistant is None:
            await app.send_message(chat_id, "<b><blockquote>خطأ في المساعد</b></blockquote>")
            return
        msg = await app.send_message(chat_id, "<b><blockquote>جاري فتح الكول..</b></blockquote>")
        try:
            peer = await assistant.resolve_peer(chat_id)
            await assistant.invoke(
                CreateGroupCall(
                    peer=InputPeerChannel(
                        channel_id=peer.channel_id,
                        access_hash=peer.access_hash,
                    ),
                    random_id=assistant.rnd_id() // 9000000000,
                )
            )
            await msg.edit_text("<b><blockquote>تم فتح الكول بنجاح!!</b></blockquote>")
        except ChatAdminRequired:
            try:    
                await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
                        can_manage_chat=False,
                        can_delete_messages=False,
                        can_manage_video_chats=True,
                        can_restrict_members=False,
                        can_change_info=False,
                        can_invite_users=False,
                        can_pin_messages=False,
                        can_promote_members=False,
                    ),
                )
                peer = await assistant.resolve_peer(chat_id)
                await assistant.invoke(
                    CreateGroupCall(
                        peer=InputPeerChannel(
                            channel_id=peer.channel_id,
                            access_hash=peer.access_hash,
                        ),
                        random_id=assistant.rnd_id() // 9000000000,
                    )
                )
                await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
                    can_manage_chat=False,
                    can_delete_messages=False,
                    can_manage_video_chats=False,
                    can_restrict_members=False,
                    can_change_info=False,
                    can_invite_users=False,
                    can_pin_messages=False,
                    can_promote_members=False,
                    ),
                )                              
                await msg.edit_text("<b><blockquote>تم فتح الكول بنجاح !!</b></blockquote>")
            except:
                await msg.edit_text("<b><blockquote>╮◉ يرجي اعطاء البوت صلاحيه اضافه\n╯◉  مشرفين و تحكم في المحادثة الصوتيه</b></blockquote>")
    else:
        await message.reply_text("<b><blockquote>هذا الامر يخص ❪ الادمن وفوق ❫ بس</b></blockquote>")   


@app.on_message(filters.regex("^اقفل الكول$"), group=732)
@app.on_message(filters.regex("^اقفل الكول$") & filters.channel, group=732)
async def stop_group_call(client: Client, message: Message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7623838169:
        chat_id = message.chat.id
        assistant = await get_assistant(chat_id)
        ass = await assistant.get_me()
        assid = ass.id
        if assistant is None:
            await app.send_message(chat_id, "<b><blockquote>خطأ في المساعد</b></blockquote>")
            return
        msg = await app.send_message(chat_id, "<b><blockquote>جاري قفل الكول</b></blockquote>")
        try:
            if not (
               group_call := (
                   await get_group_call(assistant, message, err_msg=", group call already ended")
               )
            ):  
               return
            await assistant.invoke(DiscardGroupCall(call=group_call))
            await msg.edit_text("<b><blockquote>تم اغلاق الكول بنجاح!</b></blockquote>")

        except Exception as e:
            if "GROUPCALL_FORBIDDEN" in str(e):
                try:    
                    await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
                        can_manage_chat=False,
                        can_delete_messages=False,
                        can_manage_video_chats=True,
                        can_restrict_members=False,
                        can_change_info=False,
                        can_invite_users=False,
                        can_pin_messages=False,
                        can_promote_members=False,
                    ))
                    if not (
                        group_call := (
                            await get_group_call(assistant, message, err_msg=", group call already ended")
                        )
                    ):  
                        return
                    await assistant.invoke(DiscardGroupCall(call=group_call))
                    await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
                        can_manage_chat=False,
                        can_delete_messages=False,
                        can_manage_video_chats=False,
                        can_restrict_members=False,
                        can_change_info=False,
                        can_invite_users=False,
                        can_pin_messages=False,
                        can_promote_members=False,
                    ))                              
                    await msg.edit_text("<b><blockquote>تم اغلاق الكول بنجاح!!</b></blockquote>")
                except:
                    await msg.edit_text("<b><blockquote>╮◉ يرجي اعطاء البوت صلاحيه اضافه\n╯◉  مشرفين و تحكم في المحادثة الصوتيه</b></blockquote>")
    else:
        await message.reply_text("<b><blockquote>هذا الامر يخص ❪ الادمن وفوق ❫ بس</b></blockquote>")   



#تنبيه بقفل الكول ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#تنبيه بقفل الكول ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#تنبيه بقفل الكول ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.video_chat_started)
async def stcall(client: Client, message: Message): 
      Startt = "<b><blockquote>انــا جـييــــت 😁</b></blockquote>"
      await message.reply_text(Startt)

@app.on_message(filters.video_chat_ended)
async def encall(client: Client, message: Message): 
      Enddd = "<b><blockquote>قـفـله فـي دمـاغـك 😒</b></blockquote>"
      await message.reply_text(Enddd)

@app.on_message(filters.video_chat_members_invited)
async def mevegaa(client: Client, message: Message): 
           text = f"<b><blockquote>◉ قـام: {message.from_user.mention}</b></blockquote>\n\n<b><blockquote>◉ بـدعـوه : </b></blockquote>"
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"<blockquote><a href=\"tg://user?id={user.id}\">{user.first_name}</a> </blockquote>"
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text} ")
           except:
             pass
 
#مين في الكول ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#مين في الكول ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓



@app.on_message(filters.regex("مين في الكول"), group=854367796)
async def strcall(client, message):
    msg = await message.reply("🤔")
    await asyncio.sleep(2)
    await msg.delete()
    chat_id = message.chat.id
    assistant = await group_assistant(KIM,message.chat.id)
    audio_stream_quality = await get_audio_bitrate(chat_id)
    try:
        await assistant.play(message.chat.id, MediaStream("./assets/vgaa.mp3", audio_parameters=audio_stream_quality))
        text=" <u><b>الموجودين بالكول</b></u>:\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="يتحدث √"
            else:
                mut="اصم ✘"
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k} - {user.mention} - {mut}\n"
        text += f"\nعددهم : {len(participants)}\n༄"    
        await message.reply(f"{text}")
        await asyncio.sleep(4)
        await assistant.leave_group_call(chat_id)
    except NoActiveGroupCall:
        await message.reply(f"حجي انت مخبول مافي كول مفتوح\n༄")
    except TelegramServerError:
        await message.reply(f"ارسل الامر تاني في مشكله في سيرفر التلجرام\n༄")
    except AlreadyJoinedError:
        text=" <u><b>الموجودين بالكول:</b></u>\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="يتحدث √"
            else:
                mut="اصم ✘"
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k} - {user.mention} - {mut}\n"
        text += f"\nعددهم : {len(participants)}\n༄"    
        await message.reply(f"{text}")

@app.on_message(filters.regex("^call$"), group=854367796)
async def strcall(client, message):
    chat_id = message.chat.id
    assistant = await group_assistant(KIM, chat_id)
    audio_stream_quality = await get_audio_bitrate(chat_id)
    user_list = []    
    try:
        try:
            await assistant.play(
                chat_id,
                MediaStream(
                    "./assets/vgaa.mp3",
                    audio_parameters=audio_stream_quality,
                    video_flags=MediaStream.Flags.IGNORE
                )
            )
        except AlreadyJoinedError:
            await assistant.change_stream(
                chat_id,
                MediaStream(
                    "./assets/vgaa.mp3",
                    audio_parameters=audio_stream_quality
                )
            )
        except NoActiveGroupCall:
            await message.reply("<b>⚠️ يرجى بدء محادثة صوتية أولاً!</b>")
            return
        await asyncio.sleep(15)
        max_retries = 3
        participants = []
        for _ in range(max_retries):
            participants = await assistant.get_participants(chat_id)
            if participants:
                break
            await asyncio.sleep(5)
        else:
            await message.reply("<b>⚠️ لا يوجد مشاركون في المحادثة!</b>")
            await assistant.leave_group_call(chat_id)
            return
        total = 0
        for participant in participants:
            try:
                user = await client.get_users(participant.user_id)
                status = "🎤 يتحدث" if not participant.muted else "🔇 صامت"
                user_list.append(f"{total+1}. {user.mention} ({status})")
                total += 1
            except Exception as e:
                print(f"Error getting user info: {e}")
                continue
        msg_text = (
            f"<b>👥 أعضاء المحادثة الصوتية ({total}):</b>\n\n" +
            "\n".join(user_list) +
            "\n\n<b>✅ تم تشغيل المناداة بنجاح</b>"
        )
        sent_msg = await message.reply(msg_text, disable_web_page_preview=True)
        await asyncio.sleep(25)        
        await assistant.stop_stream(chat_id)
        await assistant.leave_group_call(chat_id)
        await sent_msg.edit(f"<b>⏹️ تم إنهاء المناداة بنجاح ({total} مستخدم)</b>")
    except Exception as e:
        print(f"Error: {e}")
        await message.reply("<b>⚠️ حدث خطأ أثناء المعالجة!</b>")
        try:
            await assistant.leave_group_call(chat_id)
        except:
            pass