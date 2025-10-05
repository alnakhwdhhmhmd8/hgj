import requests
import asyncio
import glob
import os
import time
import requests
import random
import aiohttp
import wget
import yt_dlp
import traceback
from pyrogram.types import InputMediaAudio
import asyncio
import os
import re
from typing import Union
from VeGaXMusic.utils.exceptions import DownloadError
import yt_dlp
from yt_dlp import YoutubeDL
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from youtubesearchpython.__future__ import VideosSearch

from VeGaXMusic.utils.database import is_on_off
from VeGaXMusic.utils.formatters import time_to_seconds
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from youtubesearchpython import SearchVideos
import requests
import wget
from config import *
import config
from config import OWNER_ID
from config import BANNED_USERS
from config import BANNED_USERS, OWNER_ID
from config import START_IMG_URL
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from VeGaXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from VeGaXMusic import app
from random import  choice, randint
from pytube import Search
from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from youtubesearchpython import VideosSearch
from yt_dlp import YoutubeDL
from VeGaXMusic import app
import speech_recognition as sr
from pyrogram import Client, filters
from pydub import AudioSegment
from os import remove
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
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from pySmartDL import SmartDL
from VeGaXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube)
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram import filters
import random
from pyrogram import Client

import requests
import yt_dlp
from youtube_search import YoutubeSearch


#مكاتب كود قولي

import asyncio
import aiohttp

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import*
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.enums import ChatMembersFilter
from pyrogram import enums
from pyrogram import Client
from pyrogram import enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from VeGaXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from VeGaXMusic import app
from random import  choice, randint
from pyrogram import Client, filters
from pyrogram.types import Message
from gtts import gTTS
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait
from pydub import AudioSegment
from playsound import playsound
from pyrogram import Client, filters
from gtts import gTTS


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

 

#تحميل اغاني ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#تحميل اغاني ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


def cookies():
    folder_path = "/root/cookies"
    txt_files = glob.glob(os.path.join(folder_path, "*.txt"))
    if not txt_files:
        raise FileNotFoundError("No .txt files found in /root/cookies")
    selected_file = random.choice(txt_files)
    logs_path = os.path.join(folder_path, "logs.csv")
    with open(logs_path, "a", encoding='utf-8') as file:
        file.write(f"Chosen File: {selected_file}\n")
    return selected_file

def get_ytdl_options(
    ytdl_opts: Union[str, dict, list], commandline: bool = True
) -> Union[str, dict, list]:
    token_data = os.getenv("TOKEN_DATA")

    if isinstance(ytdl_opts, list):
        if token_data:
            ytdl_opts += [
                "--username" if commandline else "username",
                "oauth2",
                "--password" if commandline else "password",
                "''",
            ]
        else:
            ytdl_opts += ["--cookies" if commandline else "cookiefile", cookies()]

    elif isinstance(ytdl_opts, str):
        if token_data:
            ytdl_opts += (
                "--username oauth2 --password '' "
                if commandline
                else "username oauth2 password '' "
            )
        else:
            ytdl_opts += (
                f"--cookies {cookies()}" if commandline else f"cookiefile {cookies()}"
            )

    elif isinstance(ytdl_opts, dict):
        if token_data:
            ytdl_opts.update({"username": "oauth2", "password": ""})
        else:
            ytdl_opts["cookiefile"] = cookies()

    return ytdl_opts
    

dowof = []
@app.on_message(filters.command(["قفل التحميل", "تعطيل التحميل"], ""), group=82826389)
async def iddlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 6760053475 or message.from_user.id == 6753126490 or message.from_user.id == 6760053475:
      if message.chat.id in dowof:
        return await message.reply_text("التحميل معطل من قبل\n༄")
      dowof.append(message.chat.id)
      return await message.reply_text("تم تعطيل التحميل بنجاح \n༄")
   else:
      return await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس\n༄")

@app.on_message(filters.command(["فتح التحميل", "تفعيل التحميل"], ""), group=8272689)
async def iddopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 6760053475 or message.from_user.id == 6753126490 or message.from_user.id == 6760053475:
      if not message.chat.id in dowof:
        return await message.reply_text("التحميل مفعل من قبل \n༄")
      dowof.remove(message.chat.id)
      return await message.reply_text("تم تفعيل التحميل بنجاح \n༄")
   else:
      return await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس\n༄")


def remove_if_exists(path):
    if os.path.exists(path):
        os.remove(path)



@app.on_message(filters.command(["تحميل","يوت","حمل"], ""), group=56)
async def song_downloader(_, message):
    if message.chat.id in dowof:
        return await message.reply_text("التحميل معطل من قبل الادمن\n༄")
    
    if len(message.command) > 1:
        query = " ".join(message.command[1:])
    else:
        ask = await app.ask(message.chat.id, "<blockquote>ارسل اسم الاغنيه لتحميل</blockquote>")
        query = ask.text
    
    m = await message.reply("🔎")
    ydl_ops = {
        'format': 'bestaudio[ext=m4a]',
        'keepvideo': True,
        'prefer_ffmpeg': False,
        'geo_bypass': True,
        'outtmpl': '%(title)s.%(ext)s',
        'quite': True,
        "cookiefile": cookies(),
    }
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        chat_id = message.chat.id
        usr = await app.get_chat(message.from_user.id)
        name = usr.first_name
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]
        views = results[0]["views"]

    except Exception as e:
        await m.edit("خطاء في جلب المسار حاول مره اخري!")
        print(str(e))
        return
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"<b><blockquote>╭◉ᚐᴛɪᴛʟᴇ : {title[:25]}\n│᚜◉ ᴅᴜʀᴀᴛɪᴏɴ : <code>{duration}</code>\n╰◉ᚐnᴠɪᴇᴡs : {views}</blockquote></b>"
        reply_markup = InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("ᴠᴇɢᴧ", url=SUPPORT_CHANNEL)
            ]]
        )
        host = str(info_dict["uploader"])
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        await message.reply_audio(
            audio_file,
            caption=rep,
            performer=host,
            thumb=thumb_name,
            title=title,
            duration=dur,
            reply_markup=reply_markup,
        )
        await m.delete()

    except Exception as e:
        await m.edit("حدث خطأ ما. أو لم يتم العثور على الأغنية!")
        print(e)
    try:
        remove_if_exists(audio_file)
        remove_if_exists(thumb_name)
    except Exception as e:
        print(e)










# قفل المشاهده ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#قفل المشاهده  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓







#بحث ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#بحث ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓



@app.on_message(filters.command(["بحث"], ""), group=4458890044)
async def ytsearch(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        if len(message.command) < 2:
            return await message.reply_text("يمكن البحث عبر فيجا")
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("⏳")
        results = YoutubeSearch(query, max_results=4).to_dict()
        i = 0
        text = ""
        while i < 4:
            text += f"◉ العنوان : {results[i]['title']}\n"
            text += f"◉ المدة : <code>{results[i]['duration']}</code>\n"
            text += f"◉ المشاهدات : <code>{results[i]['views']}</code>\n"
            text += f"◉ القناه : {results[i]['channel']}\n"
            text += f"◉ الرابط : https://youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        key = InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                        "⸢ᴠᴇɢᴧ⸥", url=SUPPORT_CHANNEL),
                ],[
                    InlineKeyboardButton(
                        text="⸢✘⸥",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        )
        await m.edit_text(
            text=text,
            reply_markup=key,
            disable_web_page_preview=True,
        )
    except Exception as e:
        await message.reply_text(str(e))
    


#قولي او قوله ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#قولي او قوله ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓




kolyof = []

@app.on_message(filters.command(["قفل قولي", "تعطيل قولي"], ""), group=27727181882)
async def iddlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6753126490 or message.from_user.id == 6760053475:
      if message.chat.id in kolyof:
        return await message.reply_text("قولي معطل من قبل\n༄")
      kolyof.append(message.chat.id)
      return await message.reply_text("تم تعطيل قولي بنجاح\n༄")
   else:
      return await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس\n༄")

@app.on_message(filters.command(["فتح قولي", "تفعيل قولي"], ""), group=7262627288)
async def iddopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6753126490 or message.from_user.id == 6760053475:
      if not message.chat.id in kolyof:
        return await message.reply_text("قولي مفعل من قبل\n")
      kolyof.remove(message.chat.id)
      return await message.reply_text("تم تفعيل قولي بنجاح\n༄")
   else:
      return await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس\n༄")





@app.on_message(filters.command(['ترجم'], ''), group=125060901007)
async def translate_text(_, message: Message):
    if len(message.command) < 2:
        return await message.reply('الرجاء إرسال النص المطلوب ترجمته بعد الأمر "ترجم"\n༄', reply_to_message_id=message.id)
    
    text_to_translate = message.text.split(maxsplit=1)[1]
    
    # تحديد اللغة المصدر (إذا كانت النص عربي نترجمه للإنجليزي والعكس)
    if any(char in text_to_translate for char in ['ء', 'آ', 'أ', 'ؤ', 'إ', 'ئ', 'ا', 'ب', 'ة', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ى', 'ي']):
        # النص عربي، نترجمه للإنجليزي
        translated = translator.translate(text_to_translate, src='ar', dest='en')
    else:
        # النص إنجليزي (أو لغة أخرى)، نترجمه للعربي
        translated = translator.translate(text_to_translate, src='en', dest='ar')
    
    await message.reply(f'الترجمة:\n{translated.text}\n\nالنص الأصلي:\n{text_to_translate}', reply_to_message_id=message.id)




becallllof = []

@app.on_message(filters.command(["قفل بيقول ايه", "تعطيل بيقول ايه"], ""), group=27727181882)
async def iddlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6753126490 or message.from_user.id == 6760053475:
      if message.chat.id in becallllof:
        return await message.reply_text("تحويل لنص معطل من قبل\n༄")
      becallllof.append(message.chat.id)
      return await message.reply_text("تم تعطيل تحويل لنص بنجاح\n༄")
   else:
      return await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس\n༄")

@app.on_message(filters.command(["فتح بيقول ايه", "تفعيل بيقول ايه"], ""), group=7262627288)
async def iddopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6753126490 or message.from_user.id == 6760053475:
      if not message.chat.id in becallllof:
        return await message.reply_text("تحويل لنص مفعل من قبل\n")
      becallllof.remove(message.chat.id)
      return await message.reply_text("تم تفعيل تحويل لنص بنجاح\n༄")
   else:
      return await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس\n༄")
      



@app.on_message(filters.command(["بيقول ايه"], ""), group=92820)
async def speech_to_text(client, message):
    if message.chat.id in becallllof:
        return await message.reply_text('تحويل لنص معطل من قبل الادمن\n༄')
        
    if not message.reply_to_message:
        await message.reply("قم بي الرد علي الصوت اولا")
        return
    voice_down = await message.reply_to_message.download("./recyad.wav")
    voice = sr.Recognizer()
    sound = AudioSegment.from_ogg(voice_down)
    wav_file = sound.export(voice_down, format="wav")
    with sr.AudioFile(wav_file) as source:
        audio_source = voice.record(source)
    msg = await message.reply("🧐")
    await asyncio.sleep(2)
    await msg.delete()
    try:
        text = voice.recognize_google(audio_source, language='ar-EG')
    except Exception as e:
        text = f"فشل التعرف علي الكلام\n{e}"
    await message.reply(text)
    remove("recyad.wav") 
    




import asyncio
from pyrogram import Client, filters

@app.on_message(filters.command(["هكرو"], ""), group=9282230)
async def tahker_1(client, msg):
    user_id = (
        msg.reply_to_message.from_user.id
        if msg.reply_to_message
        else msg.from_user.id
    )
    chat_id = msg.chat.id
    animation_chars = [
        "**يتم الربط بقاعدة بيانات التلجرام**",
        "يتم تهكير من : [ @TopVeGa ]",
        "جار الاختراق. 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ \n\n\n  الترمنال:\nيتم تحميل: \n  Bruteforce-Telegram-0.1.tar.gz (9.3 kB)",
        (
            "حساب الضحية تم اختراقه...\n\nادفع المال $ وسيتم حذف معلوماتك\n\n\n"
            "الترمنال:\nيتم تحميل:\n  Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n"
            "يتم تجميع حزمة البيانات \n  يتم تحميل Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\n"
            "يتم التصنيع لـ Tg-Bruteforcing (setup.py):\n تم الانتهاء مع عملية 'النجاح'\n"
            "جار الإنشاء للتلجرام ملف:\n filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 "
            "sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n"
            "يتم الحفظ في الجهاز:\n /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n"
            "**تم بنجاح اختراق قاعدة بيانات التلجرام**\n\n\n"
            "✰︎ تم حفظ بيانات الواتساب  ✅\n"
            "✰︎ تم حفظ بيانات الفيسبوك ✅\n"
            "✰︎ تم حفظ بيانات التلجرام  ✅\n"
            "✰︎ تم حفظ صورة المعرض  ✅\n"
            "✰︎ تم حفظ جهات الاتصال  ✅\n"
            "✰︎ تم حفظ جميع الرسائل  ✅\n"
            "سيتم نشرها علي دارك ويب ✅"
            
        )
    ]
    
    message = await msg.reply_text(animation_chars[0])
    for i in range(1, len(animation_chars)):
        await asyncio.sleep(5)
        try:
            await message.edit_text(animation_chars[i])
        except Exception as e:
            print(f"⚠️ خطأ في تحديث الرسالة: {e}")
            break
    
    # التأكد من إرسال الرسالة النهائية
    await asyncio.sleep(1)
    await message.edit_text(animation_chars[-1])