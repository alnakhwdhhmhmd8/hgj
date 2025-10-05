

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
from VeGaXMusic import Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app
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

 




# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂[𝗩.𝗘.𝗚.𝗔]▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂


  
amaerrof = []

@app.on_message(filters.command(["قفل الاوامر", "تعطيل الاوامر"], ""), group=277288870000127181882)
async def amaerrlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 6753126490:
      if message.chat.id in amaerrof:
        return await message.reply_text("الاوامر معطله من قبل")
      amaerrof.append(message.chat.id)
      return await message.reply_text("تم تعطيل الاوامر بنجاح")
   else:
      return await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")

@app.on_message(filters.command(["فتح الاوامر", "تفعيل الالاوامر"], ""), group=726262766000288)
async def amaerropen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 6753126490:
      if not message.chat.id in amaerrof:
        return await message.reply_text("الاوامر مفعله من قبل\n")
      amaerrof.remove(message.chat.id)
      return await message.reply_text("تم تفعيل الاوامر بنجاح")
   else:
      return await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس")




user = ""

@app.on_message(filters.command(["اوامر", "الاوامر"], ""), group=726272728281)
async def mmmy(client: Client, message: Message):
    global user
    user = message.from_user.id
    if message.chat.id in amaerrof:
        return await message.reply_text("الاوامر معطله من قبل الادمن")
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 6753126490:
        await message.reply_video(
            video="https://t.me/kafra_wi_1/124",
            caption=f"<b> ˚‧ꜱʜᴇɪᴋʜ˳+\n╮❖ مـرحـبـا بـك: {message.from_user.mention()}\n╯❖ لـيك قـايـمـة الاوامـر مـن الشيخ</b>",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "꙳. ❶.꙳", callback_data="lockdd"
                        ),
                        InlineKeyboardButton(
                            "꙳.❷.꙳", callback_data="abimnn"
                        ),

                        InlineKeyboardButton(
                            "꙳.❸.꙳", callback_data="Maalek"
                        ),
                    ],
                    [
                        InlineKeyboardButton("꙳.❹.꙳", callback_data="deeev"),
                        InlineKeyboardButton("꙳.❺.꙳", callback_data="playyy"),
                    ],
                    [
                        InlineKeyboardButton("꙳.❻.꙳", callback_data="gamess"),
                    ],
                    [
                        InlineKeyboardButton("ꜱʜᴇɪᴋʜ", url=SUPPORT_CHANNEL),
                    ],
                ]
            )
        )
    else:
        await message.reply("هذا الامر يخص ❪ الادمن وفوق ❫ بس")


# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂[𝗩.𝗘.𝗚.𝗔]▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂



@app.on_callback_query(filters.regex("Musicvega"), group=1863738666666655582)
async def mpdtsf(client, query: CallbackQuery):
    global user
    chat = query.message.chat
    get = await client.get_chat_member(chat.id, query.from_user.id)
    user_status = get.status
    if query.from_user.id != user:
        await client.answer_callback_query(query.id, text="هييه مايمديك الامر ياروعه!!", show_alert=True)
        return

    await client.answer_callback_query(query.id)
        
    await query.answer("Musicvega")
    await query.edit_message_text(
        f"""<b> ˚‧ꜱʜᴇɪᴋʜ˳+\n╮❖ مـرحـبا بـك عزيـزي ليـك\n╯❖ قـايـمـة الاوامـر مـن الشيخ</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                    "꙳.❶.꙳", callback_data="lockdd"),       
                    InlineKeyboardButton(
                    "꙳.❷.꙳", callback_data="abimnn"),
                    InlineKeyboardButton(
                    "꙳.❸.꙳", callback_data="Maalek"),
                ],[
                    InlineKeyboardButton("꙳.❹.꙳", callback_data="deeev"),
                   InlineKeyboardButton("꙳.❺.꙳", callback_data="playyy"),
                ],[
                   InlineKeyboardButton("꙳.❻.꙳", callback_data="gamess"),   
                ],[        
                    InlineKeyboardButton("ꜱʜᴇɪᴋʜ", url=SUPPORT_CHANNEL),
                ],
            ]
        )
    )

# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂[𝗩.𝗘.𝗚.𝗔]▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂


@app.on_callback_query(filters.regex("playyy"), group=14)
async def playyy(client, query: CallbackQuery):
    global user
    chat = query.message.chat
    get = await client.get_chat_member(chat.id, query.from_user.id)
    user_status = get.status
    if query.from_user.id != user:
        await client.answer_callback_query(query.id, text="هييه مايمديك الامر ياروعه!!", show_alert=True)
        return

    await client.answer_callback_query(query.id)
    
    await query.answer ("playyy")
    await query.edit_message_text(
        f"""<b><b> ˚‧ꜱʜᴇɪᴋʜ˳+</b>
       
❖  <b><u>اوامر تشغيل في الجروب و القنوات</u>

╮❖  لتشغيل اغنيه  : تشغيل او شغل 
│᚜❖ لتشغيل فيديو  : فيديو او فديو
│᚜❖ لأنهاء الاغنيه  : ايقاف /end
│᚜❖ لايقاف مؤقت : وقف /pause
│᚜❖ لتكملة المؤقت : كمل 
│᚜❖ لفتح المحادثه الصوتية: افتح الكول
│᚜❖ لقفل المحادثه الصوتية: اقفل الكول
│᚜❖ لتخطي الاغنيه  : تخطي او /skip
│᚜❖ لتحميل موسيقي او فيديو : تحميل
╯❖  لتقديم الاغنيه : قدم وعدد ثوان
     
⫢ <u>قايمه اوامر اضافيه</u>

╮❖  لعرض سرعه البوت  : بنج
│᚜❖ للتحكم في لغه البوت: اللغه
│᚜❖ جلب الكولات النشطه : كولات النشطه 
│᚜❖ جلب الفيديوهات النشطه : الفيديوهات النشطه 
│᚜❖ لعرض اعدادات البوت: الاعدادات
│᚜❖ لتغير وضع تشغيل : وضع التشغيل 
│᚜❖ لتحكم في اوامر ميوزك: المساعده
│᚜❖ لحل مشكله بتوجهك : مطورين
│᚜❖ لتحويل الفويس الي كتابه : بيقول ايه
│᚜❖ لتحميل اغنيه اكتب: تحميل 
│᚜❖ لمشاهده اغنيه او فيديو : الاوامر
│᚜❖ لمشاهده يوتيوب: يوتيوب مع اسم
╯❖  لظهر لوحه السرعه : لوحه السرعه
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("˹➻ٰ", callback_data="Musicvega")]]
        ),
    )





# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂[𝗩.𝗘.𝗚.𝗔]▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂



@app.on_callback_query(filters.regex("lockdd"), group=120517665581)
async def lockdd(client, query: CallbackQuery):
    global user
    chat = query.message.chat
    get = await client.get_chat_member(chat.id, query.from_user.id)
    user_status = get.status
    if query.from_user.id != user:
        await client.answer_callback_query(query.id, text="هييه مايمديك الامر ياروعه!!", show_alert=True)
        return

    await client.answer_callback_query(query.id)
    
    await query.answer ("lockdd")
    await query.edit_message_text(
        f"""<b><b> ˚‧ꜱʜᴇɪᴋʜ˳+</b>
       
<u><b>اوامر القفل و الفتح للحمايه:</b></u>

╮❖  الدردشه 
│᚜❖ تفعيل
│᚜❖ تعطيل 
│᚜❖ الكلايش
│᚜❖ الصور
│᚜❖ الردود
│᚜❖ الروابط
│᚜❖ السب
│᚜❖ التوجيه
│᚜❖ الفيديو
│᚜❖ التثبيت 
│᚜❖ الكل
│᚜❖ الابراج
│᚜❖ الاوامر
│᚜❖ الملصقات
│᚜❖ الايدي
│᚜❖ جمالي
│᚜❖ الحظر
│᚜❖ الكتم
│᚜❖ تقيد
│᚜❖ البايو
│᚜❖ الدعوه
│᚜❖ المتحركات
│᚜❖ الاباحي
│᚜❖ الترحيب
│᚜❖ بيقول ايه
│᚜❖ قولي
│᚜❖ مهنتي
│᚜❖ الريكورد
│᚜❖ الصوتيات
│᚜❖ مشاهده
│᚜❖ بيقول ايه
│᚜❖ صورتي 
│᚜❖ كت و تويت
│᚜❖ الكشف
│᚜❖ التحميل
│᚜❖ بحث
│᚜❖ الانذار
│᚜❖ الاذكار
│᚜❖ تفعيل نداء
│᚜❖ مصنع
╯❖  اليوتيوب 
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("˹➻ٰ", callback_data="Musicvega")]]
        ),
    )





# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂[𝗩.𝗘.𝗚.𝗔]▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂



@app.on_callback_query(filters.regex("abimnn"), group=119340009986)
async def abinmnn(client, query: CallbackQuery):
    global user
    chat = query.message.chat
    get = await client.get_chat_member(chat.id, query.from_user.id)
    user_status = get.status
    if query.from_user.id != user:
        await client.answer_callback_query(query.id, text="هييه مايمديك الامر ياروعه!!", show_alert=True)
        return

    await client.answer_callback_query(query.id)
    
    await query.answer ("abimnn")
    await query.edit_message_text(
        f"""<b><b> ˚‧ꜱʜᴇɪᴋʜ˳+</b>

<u><b> اوامر الطرد والحظر :</b></u>

╮❖  تقييد 
│᚜❖ حظر 
│᚜❖ طرد 
│᚜❖ كتم
│᚜❖ الغاء الحظر
│᚜❖ طرد البوتات
│᚜❖ الغاء الكتم
╯❖  الغاء التقييد 

<u><b>اوامر الرفع و تنزيل:</b></u>
 
╮❖  رفع مالك
│᚜❖ رفع ادمن
│᚜❖ رفع مطور
│᚜❖ تنزيل مطور
│᚜❖ تنزيل مالك
╯❖  تنزيل ادمن

 <u><b>لظهار قوائم:</b></u>
 
╮❖  قائمة المكتومين
│᚜❖ قائمة المحظورين
│᚜❖ قائمة المقيدين
│᚜❖ قائمة المطورين
│᚜❖ قائمة المالكين
│᚜❖ قائمة المشرفين
╯❖  قائمة الادمنيه

<u><b>اوامر المسح :</b></u>

╮❖  مسح الادمنيه
│᚜❖ مسح المحظورين
│᚜❖ مسح المكتومين
│᚜❖ مسح المقيدين
│᚜❖ مسح المالكين
│᚜❖ مسح الادمنيه
╯❖  مسح المطورين 

</b>""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("˹➻ٰ", callback_data="Musicvega")]]
        ),
    )





# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
# ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂[𝗩.𝗘.𝗚.𝗔]▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂


@app.on_callback_query(filters.regex("Maalek"), group=119366065445687746)
async def Maalek(client, query: CallbackQuery):
    global user
    chat = query.message.chat
    get = await client.get_chat_member(chat.id, query.from_user.id)
    user_status = get.status
    if query.from_user.id != user:
        await client.answer_callback_query(query.id, text="هييه مايمديك الامر ياروعه!!", show_alert=True)
        return

    await client.answer_callback_query(query.id)
    
    await query.answer ("Maalek")
    await query.edit_message_text(
        f"""<b><b> ˚‧ꜱʜᴇɪᴋʜ˳+</b>

<u><b> اوامر تحكم لمالك ومنشئين الأساسيين:</b></u>

╮❖  تغير اسم الجروب 
│᚜❖ تغير بايو الجروب
│᚜❖ تغير صوره الجروب
│᚜❖ مسح صوره الجروب 
│᚜❖ تثبيت
│᚜❖ الغاء تثبيت
│᚜❖ الغاء تثبيت الكل
│᚜❖ قفل التثبيت
│᚜❖ فتح التثبيت 
│᚜❖ فحص الجروب
│᚜❖ نقل ملكية البوت
│᚜❖ رفع مشرف فالقنوات
│᚜❖ فحص الجروب
│᚜❖ رفع مميز
│᚜❖ رفع مدير
│᚜❖ رفع منشئ اساسي
│᚜❖ تنزيل مميز
│᚜❖ تنزيل تنزيل مدير
│᚜❖ تنزيل منشي اساسي
│᚜❖ قفل الدردشه
│᚜❖ فتح الدردشه
│᚜❖ قفل تاك
╯❖  فتح تاك
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("˹➻ٰ", callback_data="Musicvega")]]
        ),
    )
    



@app.on_callback_query(filters.regex("gamess"), group=1445687746)
async def gamess(client, query: CallbackQuery):
    global user
    chat = query.message.chat
    get = await client.get_chat_member(chat.id, query.from_user.id)
    user_status = get.status
    if query.from_user.id != user:
        await client.answer_callback_query(query.id, text="هييه مايمديك الامر ياروعه!!", show_alert=True)
        return

    await client.answer_callback_query(query.id)
    
    await query.answer ("gamess")
    await query.edit_message_text(
        f"""<b><b> ˚‧ꜱʜᴇɪᴋʜ˳+</b>

<u><b> العاب و تسالي احلي عالم:</b></u>

╮❖ لعبه بنك كامله
│᚜❖ تسالي
╯❖ لعبة ورقه حجره 

╮❖ لوخيروك
│᚜❖ كت
│᚜❖ نمله
│᚜❖ صرصار
│᚜❖ خنزير
│᚜❖ رقص
│᚜❖ ابراج
│᚜❖ تويت
│᚜❖ قتل
│᚜❖ تف
│᚜❖ مح
│᚜❖ صور
│᚜❖ اعلام
│᚜❖ معاني
│᚜❖ نداء
│᚜❖ زوجني
│᚜❖ الساعه
│᚜❖ رفع كلب
│᚜❖ رفع حمار
│᚜❖ رفع بقره
│᚜❖ رفع قرد
│᚜❖ رفع تيس
│᚜❖ رفع خروف
│᚜❖ رفع خنزير
│᚜❖ رفع نسناس
│᚜❖ رفع رقاصه 
│᚜❖ مشاهير
│᚜❖ صور بنات
│᚜❖ صور شباب 
│᚜❖ صور انميي
│᚜❖ قرآن 
│᚜❖ غنيلي
│᚜❖ نكت
│᚜❖ الساعه
│᚜❖ قرآن
│᚜❖ المصحف
│᚜❖ مهنتي
│᚜❖ حظ
│᚜❖ سله
│᚜❖ كوره
│᚜❖ سهم
│᚜❖ بول
│᚜❖ دمنو
│᚜❖ اقتباس
│᚜❖ متحركه
│᚜❖ انصحني
│᚜❖ اصراحه
│᚜❖ حكمه
│᚜❖ اذكار
│᚜❖ اغاني عشوائي 
│᚜❖ اسال
│᚜❖ تليجرام مميز
│᚜❖ البوت فازر
╯❖  تويتر
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("˹➻ٰ", callback_data="Musicvega")]]
        ),
    )



@app.on_callback_query(filters.regex("deeev"), group=777)
async def deeeeev(client, query: CallbackQuery):
    global user
    chat = query.message.chat
    get = await client.get_chat_member(chat.id, query.from_user.id)
    user_status = get.status
    if query.from_user.id != user:
        await client.answer_callback_query(query.id, text="هييه مايمديك الامر ياروعه!!", show_alert=True)
        return

    await client.answer_callback_query(query.id)
    
    await query.answer("deeev")
    await query.edit_message_text(
        f"""<b> ˚‧ꜱʜᴇɪᴋʜ˳+

 اوامر تحكم للمطور:
╮❖  تغيير اسم البوت
│᚜❖ ترويج
│᚜❖ احصائيات
│᚜❖ اذاعه
│᚜❖ غادر لخروج البوت
│᚜❖ المجموعات 
│᚜❖ المستخدمين 
│᚜❖ معلومات التنصيب
│᚜❖ غادر لخراج البوت
│᚜❖ حظر عام من البوت
│᚜❖ الغاء حظر عام من البوت
│᚜❖ رفع مطور فالبوت
│᚜❖ تنزيل مطور فالبوت
│᚜❖ تفعيل الترويج
│᚜❖ تعطيل الترويج
│᚜❖ قفل انضام البوت
│᚜❖ فتح انضمام البوت
│᚜❖ تنزيل مشرف من القنوات
│᚜❖ رفع كل رتب
│᚜❖ تنزيل كل رتب
│᚜❖ تصفير الاحصائيات
│᚜❖ جلب نسخة
╯❖  رفع نسخة

</b>""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("˹➻ٰ", callback_data="Musicvega")]]
        ),
    )