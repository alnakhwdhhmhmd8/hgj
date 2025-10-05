import asyncio
import os
from config import *
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from VeGaXMusic import app
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait

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


array = []

@app.on_message(filters.command(["قفل تاك", "تعطيل التاك"], ""), group=277288870000127181882)
async def mooslock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165 or message.from_user.id == 7728230165:
      if message.chat.id in array:
        return await message.reply_text("<b><blockquote>التاك معطله من قبل</b></blockquote>")
      array.append(message.chat.id)
      return await message.reply_text("<b><blockquote>تم تعطيل تاك بنجاح</b></blockquote>")
   else:
      return await message.reply_text("<b><blockquote>هذا الامر يخص ❪ الادمن وفوق ❫ بس</b></blockquote>")

@app.on_message(filters.command(["فتح تاك", "تفعيل التاك"], ""), group=726262766000288)
async def moosopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 7728230165 or message.from_user.id == 7728230165:
      if not message.chat.id in array:
        return await message.reply_text("<b><blockquote>تاك مفعله من قبل</b></blockquote>")
      array.remove(message.chat.id)
      return await message.reply_text("<b><blockquote>تم تفعيل تاك بنجاح</b></blockquote>")
   else:
      return await message.reply_text("<b><blockquote>هذا الامر يخص ❪ الادمن وفوق ❫ بس</b></blockquote>")

from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait
import asyncio
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait


@app.on_message(filters.command(["@all", "تاك", "all"], "") & ~filters.private, group=767667)
async def mention_all(client, message):
    # التحقق من إيقاف التاك في المجموعة
    if message.chat.id in array:
        return await message.reply("<b>⛔ التاك معطلة في هذه المجموعة!</b>")
    
    # التحقق من صلاحيات المستخدم
    try:
        member = await client.get_chat_member(message.chat.id, message.from_user.id)
        if member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await message.reply("<b>❌ هذا الأمر متاح فقط للمشرفين والمالك!</b>")
    except Exception as e:
        return await message.reply(f"<b>⚠️ حدث خطأ: {e}</b>")

    await message.reply("<b>⏳ جاري بدء التاك...\n\nيمكنك إرسال /cancel لإيقاف العملية</b>")
    
    stats = {
        'deleted': 0,
        'no_username': 0,
        'success': 0,
        'no_mention': 0
    }
    
    batch_size = 15  # عدد الأعضاء في كل رسالة
    delay_between_messages = 3  # تأخير بين الرسائل بالثواني
    txt = ""
    zz = message.text or message.caption or ""
    media = None
    media_type = None
    
    # معالجة الميديا المرفقة
    if message.photo:
        media = message.photo.file_id
        media_type = "photo"
    elif message.video:
        media = message.video.file_id
        media_type = "video"
    
    # تنظيف النص من أوامر التاك
    zz = zz.replace("@all", "").replace("تاك", "").replace("all", "").strip()
    
    array.append(message.chat.id)
    
    try:
        async for member in client.get_chat_members(message.chat.id):
            if message.chat.id not in array:
                break
                
            if member.user.is_deleted:
                stats['deleted'] += 1
                continue
                
            mention = member.user.mention if member.user.username else f"[{member.user.first_name or 'مستخدم'}](tg://user?id={member.user.id})"
            
            if not (member.user.username or member.user.first_name):
                stats['no_mention'] += 1
                continue
                
            stats['success'] += 1
            txt += f" {mention} ›"
            
            if stats['success'] % batch_size == 0:  # إرسال كل مجموعة من الأعضاء
                try:
                    if media_type == "photo":
                        await client.send_photo(
                            chat_id=message.chat.id,
                            photo=media,
                            caption=f"<blockquote>{zz}\n{txt}</blockquote>" if zz else txt,
                            reply_to_message_id=message.id
                        )
                    elif media_type == "video":
                        await client.send_video(
                            chat_id=message.chat.id,
                            video=media,
                            caption=f"<blockquote>{zz}\n{txt}</blockquote>" if zz else txt,
                            reply_to_message_id=message.id
                        )
                    else:
                        await client.send_message(
                            chat_id=message.chat.id,
                            text=f"<blockquote>{zz}\n{txt}</blockquote>" if zz else txt,
                            reply_to_message_id=message.id
                        )
                    
                    txt = ""
                    await asyncio.sleep(delay_between_messages)
                
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                except Exception as e:
                    print(f"Error: {e}")
                    continue
    
        # إرسال الأعضاء المتبقين إذا كان هناك أي
        if txt and message.chat.id in array:
            try:
                if media_type == "photo":
                    await client.send_photo(
                        chat_id=message.chat.id,
                        photo=media,
                        caption=f"<blockquote>{zz}\n{txt}</blockquote>" if zz else txt,
                        reply_to_message_id=message.id
                    )
                elif media_type == "video":
                    await client.send_video(
                        chat_id=message.chat.id,
                        video=media,
                        caption=f"<blockquote>{zz}\n{txt}</blockquote>" if zz else txt,
                        reply_to_message_id=message.id
                    )
                else:
                    await client.send_message(
                        chat_id=message.chat.id,
                        text=f"<blockquote>{zz}\n{txt}</blockquote>" if zz else txt,
                        reply_to_message_id=message.id
                    )
            except Exception as e:
                print(f"Error sending final batch: {e}")
    
    finally:
        if message.chat.id in array:
            array.remove(message.chat.id)
        
        # إرسال تقرير بالنتيجة
        report_msg = (
            f"<b><blockquote>✅ تم الانتهاء من التاك بنجاح!</blockquote></b>\n\n"
            f"<b>• عدد المذكرين:</b> {stats['success']}\n"
            f"<b>• الحسابات المحذوفة:</b> {stats['deleted']}\n"
            f"<b>• الحسابات بدون معرف:</b> {stats['no_username']}\n"
            f"<b>• الحسابات غير القابلة للتذكير:</b> {stats['no_mention']}\n\n"
            f"<i>~ {message.chat.title}</i>"
        )
        await message.reply(report_msg, reply_to_message_id=message.id)


@app.on_message(filters.command(["/cancel", "ايقاف التاك", "بس منشن"], ""), group=666111111)
async def stop_mention(client, message):
    # التحقق من صلاحيات المستخدم
    try:
        member = await client.get_chat_member(message.chat.id, message.from_user.id)
        if member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await message.reply("<b>❌ هذا الأمر متاح فقط للمشرفين والمالك!</b>")
    except Exception as e:
        return await message.reply(f"<b>⚠️ حدث خطأ: {e}</b>")

    if message.chat.id not in array:
        return await message.reply("<b>⚠️ لا يوجد عملية تاك جارية لإيقافها!</b>")
    
    array.remove(message.chat.id)
    await message.reply("<b>⏹ تم إيقاف عملية التاك بنجاح!</b>", reply_to_message_id=message.id)