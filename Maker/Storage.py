import os
import asyncio
from pyrogram import Client, filters
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram import types
from pyrogram import enums
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from pyrogram.errors import PeerIdInvalid
from bot import bot, bot_id, db, SUDORS
from pyrogram import types
from pyrogram import enums
from pyrogram import __version__ as pyrover
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pymongo import MongoClient
from bot import SUDORS
from motor.motor_asyncio import AsyncIOMotorClient as mongo_client
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from Maker.Makr import *
from Maker.Makr import mongo_client
from pyrogram.types import ReplyKeyboardRemove


BROADCAST_TYPES = {
    "normal": f":broadcast:{bot_id}",
    "forward": f":fbroadcast:{bot_id}",
    "pin": f":pinbroadcast:{bot_id}"
}

# ============ دوال إدارة المستخدمين ============

def add_new_user(user_id: int) -> None:
    if not is_user(user_id):
        db.sadd(f"botusers&{bot_id}", user_id)

def is_user(user_id: int) -> bool:
    try:
        return user_id in get_users()
    except Exception:
        return False

def get_users() -> list:
    try:
        return db.get(f"botusers&{bot_id}")["set"] or []
    except Exception:
        return []

def users_backup() -> str:
    users = "\n".join(str(user) for user in get_users())
    with open("users.txt", "w+") as f:
        f.write(users)
    return "users.txt"

def del_user(user_id: int) -> bool:
    if is_user(user_id):
        db.srem(f"botusers&{bot_id}", user_id)
        return True
    return False		

@bot.on_message(filters.command("start") & filters.private)
async def new_user(bot, msg):
    if not is_user(msg.from_user.id):
        add_new_user(msg.from_user.id)
        text = f"""
<blockquote> ⦿  دخل عضو جديد لـ.» الشيخ</blockquote>

<blockquote>╮⦿  الاسم : {msg.from_user.first_name}</blockquote>
<blockquote>│᚜⦿ منشن : {msg.from_user.mention}</blockquote>
<blockquote>╯⦿  الايدي : {msg.from_user.id}</blockquote>
        """
        
        username = msg.from_user.username if msg.from_user.username else "unknown"
        buttons = [
            [InlineKeyboardButton(msg.from_user.first_name, url=f"https://t.me/{username}")],
            [InlineKeyboardButton(f"» عدد الاعضاء: {len(get_users())}", callback_data=f"user_count_{msg.from_user.id}")]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        
        if SUDORS:  
            for user_id in SUDORS:
                await bot.send_message(int(user_id), text, reply_markup=reply_markup)
        else:
            LOGGER.warning("قائمة SUDORS فارغة! لا يمكن إرسال الإشعار.")
							
@bot.on_message(filters.command("start") & filters.private, group=162728)
async def start_command(bot, msg):
    await show_main_menu(bot, msg)

@bot.on_message(filters.command(["رجوع"], "") & filters.private, group=7262737)
async def back_command(bot, msg):
    await show_main_menu(bot, msg)

async def show_main_menu(bot, msg):
    if msg.from_user.id in SUDORS:
        reply_markup = ReplyKeyboardMarkup([
            [KeyboardButton("ꜱʜᴇɪᴋʜ")],
            [KeyboardButton("صنع بوت"), KeyboardButton("حذف بوت")],
            [KeyboardButton("فتح الصانع"), KeyboardButton("قفل الصانع")],
            [KeyboardButton("البوتات المصنوعه")],
            [KeyboardButton("ايقاف البوت"), KeyboardButton("تشغيل البوت")],
            [KeyboardButton("تحديث الصانع")],
            [KeyboardButton("ايقاف البوتات"), KeyboardButton("تشغيل البوتات")],
            [KeyboardButton("حذف البوتات")],
            [KeyboardButton("تفعيل التواصل"), KeyboardButton("تعطيل التواصل")],
            [KeyboardButton("معلومات الصانع")],
            [KeyboardButton("الاحصائيات")],
            [KeyboardButton("الاسكرينات المفتوحه")],
            [KeyboardButton("رفع مطور"), KeyboardButton("تنزيل مطور")],
            [KeyboardButton("المطورين")],
            [KeyboardButton("حظر"), KeyboardButton("المحظورين"), KeyboardButton("الغاء حظر")],
            [KeyboardButton("مسح المحظورين")],
            [KeyboardButton("اذاعه"), KeyboardButton("اذاعه بالتوجيه"), KeyboardButton("اذاعه بالتثبيت")],
            [KeyboardButton("جلب نسخه"), KeyboardButton("رفع نسخه")],
            [KeyboardButton("تعين كوكيز"), KeyboardButton("إعادة تهيئة")],
            [KeyboardButton("INFO")],
            [KeyboardButton("الغاء"), KeyboardButton("رجوع")],
            [KeyboardButton("اخفاء الكيبورد")]
        ], resize_keyboard=True)
        
        await msg.reply(
            f"<b><blockquote>╮⦿ مرحبًا بك: {msg.from_user.mention}\n╯⦿ عزيزي المطور في الشيخ</b></blockquote>",
            reply_markup=reply_markup,
            quote=True
        )
    else:
        reply_markup = ReplyKeyboardMarkup([
            [KeyboardButton("صنع بوت"), KeyboardButton("حذف بوت")],
            [KeyboardButton("INFO")]
        ], resize_keyboard=True)
        
        await msg.reply(
            "<blockquote><b>تم تطويري من قبل الشيخ: @M_D_O_2</blockquote>\n<blockquote>أقوى تيم برمجيات مصري</b></blockquote>",
            reply_markup=reply_markup,
            quote=True
        )
 
# ============ معالجات الأوامر ============

@bot.on_message(filters.text & filters.private, group=5662)
async def handle_commands(bot, msg):
    if msg.from_user.id not in SUDORS:
        return    
    command = msg.text
    user_id = msg.from_user.id
    commands = {
        "الغاء": cancel_command,
        "اخفاء الكيبورد": hide_keyboard,
        "الاحصائيات": show_stats,
        "تفعيل التواصل": enable_communication,
        "تعطيل التواصل": disable_communication,
        "اذاعه": prepare_broadcast,
        "اذاعه بالتوجيه": prepare_forward_broadcast,
        "اذاعه بالتثبيت": prepare_pin_broadcast,
        "جلب نسخه": backup_users,
        "رفع نسخه": prepare_users_upload
    }
    if command in commands:
        await commands[command](bot, msg)

async def cancel_command(bot, msg):
    for broadcast_type in BROADCAST_TYPES.values():
        db.delete(f"{msg.from_user.id}{broadcast_type}")
    db.delete(f"{msg.from_user.id}:users_up:{bot_id}")
    await msg.reply("<blockquote><b>تم الغاء الامر</b></blockquote>")

async def hide_keyboard(bot, msg):
    await msg.reply(
        "<blockquote><b>» تم اخفاء الكيبورد ارسل /start لعرضه مره اخري</b></blockquote>",
        reply_markup=ReplyKeyboardRemove(selective=True),
        quote=True
    )

async def show_stats(bot, msg):
    stats = (
        f"<blockquote><b>╮⦿ عدد الاعضاء: {len(get_users())}</b></blockquote>\n"
        f"<blockquote><b>╯⦿ عدد مطورين الشيخ: {len(SUDORS)}</b></blockquote>"
    )
    await msg.reply(stats, quote=True)

async def enable_communication(bot, msg):
    if not db.get(f"{msg.from_user.id}:twasl:{bot_id}"):
        await msg.reply("<blockquote><b>» تم تفعيل التواصل</b></blockquote>", quote=True)
        db.set(f"{msg.from_user.id}:twasl:{bot_id}", 1)
    else:
        await msg.reply("<blockquote><b>» التواصل مفعل من قبل</b></blockquote>", quote=True)

async def disable_communication(bot, msg):
    if db.get(f"{msg.from_user.id}:twasl:{bot_id}"):
        await msg.reply("<blockquote><b>» تم تعطيل التواصل</b></blockquote>", quote=True)
        db.delete(f"{msg.from_user.id}:twasl:{bot_id}")
    else:
        await msg.reply("<blockquote><b>» التواصل غير مفعل</b></blockquote>", quote=True)

async def prepare_broadcast(bot, msg):
    await msg.reply(
        "<blockquote><b>ارسل الاذاعه :-\n❰❪ نص + ملف +متحركه + ملصق + صوره ❫❱</b></blockquote>", 
        quote=True
    )
    db.set(f"{msg.from_user.id}{BROADCAST_TYPES['normal']}", 1)
    clear_other_broadcasts(msg.from_user.id)

async def prepare_forward_broadcast(bot, msg):
    await msg.reply(
        "<blockquote>ارسل الاذاعه :-\n❰❪ نص + ملف +متحركه + ملصق + صوره ❫❱</blockquote>", 
        quote=True
    )
    db.set(f"{msg.from_user.id}{BROADCAST_TYPES['forward']}", 1)
    clear_other_broadcasts(msg.from_user.id)

async def prepare_pin_broadcast(bot, msg):
    await msg.reply(
        "<blockquote>ارسل الاذاعه :-\n❰❪ نص + ملف +متحركه + ملصق + صوره ❫❱</blockquote>", 
        quote=True
    )
    db.set(f"{msg.from_user.id}{BROADCAST_TYPES['pin']}", 1)
    clear_other_broadcasts(msg.from_user.id)

async def backup_users(bot, msg):
    wait_msg = await msg.reply("<blockquote><b>» يـرجـئ الانتـظار...</b></blockquote>", quote=True)
    await bot.send_document(msg.chat.id, users_backup())
    await wait_msg.delete()
    os.remove("users.txt")

async def prepare_users_upload(bot, msg):
    await msg.reply("<blockquote>» ارسل الان نسخه ملف الاعضاء</blockquote>", quote=True)
    db.set(f"{msg.from_user.id}:users_up:{bot_id}", 1)

def clear_other_broadcasts(user_id: int):
    for key, value in BROADCAST_TYPES.items():
        if key != current_type:
            db.delete(f"{user_id}{value}")

# ============ معالجة الإذاعة ============
@bot.on_message(filters.private, group=368388)
async def handle_broadcasts(bot, msg):
    if msg.from_user.id not in SUDORS:
        return
    if msg.text in ["اذاعه", "اذاعه بالتوجيه", "اذاعه بالتثبيت", "الغاء", 
                   "رفع نسخه", "• اوامر الاذاعه •", "تعطيل التواصل", 
                   "تفعيل التواصل", "• اوامر التواصل •", "اخفاء الكيبورد", 
                   "الاحصائيات"]:
        return        
    user_id = msg.from_user.id
    broadcast_stats = {
        "success": 0,
        "failed": 0,
        "total": len(get_users()),
        "deleted_users": 0
    }    
    broadcast_type = None
    for key, value in BROADCAST_TYPES.items():
        if db.get(f"{user_id}{value}"):
            broadcast_type = key
            db.delete(f"{user_id}{value}")
            break    
    if not broadcast_type:
        return    
    progress_msg = await msg.reply("<blockquote><b>» جاري الإذاعة ..</b></blockquote>", quote=True)
    for current, user in enumerate(get_users(), 1):
        try:
            user = int(user)
            await send_broadcast(bot, msg, user, broadcast_type)
            broadcast_stats["success"] += 1
            if not db.get(f"{user_id}:flood:{bot_id}"):
                progress = (current / broadcast_stats["total"]) * 100
                await progress_msg.edit(f"» نسبه الاذاعه {int(progress)}%")
                db.set(f"{user_id}:flood:{bot_id}", 1)
                db.expire(f"{user_id}:flood:{bot_id}", 4)                
        except PeerIdInvalid:
            del_user(user)
            broadcast_stats["deleted_users"] += 1
            broadcast_stats["failed"] += 1
        except Exception as e:
            broadcast_stats["failed"] += 1    
    report = (
        f"<blockquote>╭─ تقرير الإذاعة ──</blockquote>\n"
        f"<blockquote>├⦿ نوع الإذاعة: {broadcast_type}</blockquote>\n"
        f"<blockquote>├⦿ عدد المستخدمين: {broadcast_stats['total']}</blockquote>\n"
        f"<blockquote>├⦿ ناجحة: {broadcast_stats['success']}</blockquote>\n"
        f"<blockquote>├⦿ فاشلة: {broadcast_stats['failed']}</blockquote>\n"
        f"<blockquote>╰⦿ حسابات محذوفة: {broadcast_stats['deleted_users']}</blockquote>"
    )    
    await progress_msg.edit(report)

async def send_broadcast(bot, msg, user_id: int, broadcast_type: str):
    if broadcast_type == "normal":
        await msg.copy(user_id)
    elif broadcast_type == "forward":
        await msg.forward(user_id)
    elif broadcast_type == "pin":
        m = await msg.copy(user_id)
        await m.pin(disable_notification=False, both_sides=True)

# ============ معالجة رفع النسخة ============

@bot.on_message(filters.document & filters.private, group=793874)
async def handle_users_upload(bot, msg):
    if msg.from_user.id not in SUDORS:
        return    
    if not db.get(f"{msg.from_user.id}:users_up:{bot_id}"):
        return    
    message = await msg.reply("<blockquote><b>» يـرجـئ الانتـظار...</b></blockquote>", quote=True)
    await msg.download("./users.txt")
    db.delete(f"botusers&{bot_id}")    
    with open("./users.txt", "r", encoding="utf8", errors="ignore") as file:
        for user in file.read().splitlines():
            if user and not is_user(user):
                add_new_user(user)    
    report = (
        f"<blockquote>╮⦿ تم رفع نسخه الاعضاء</blockquote>\n"
        f"<blockquote>╯⦿ عدد الاعضاء : {len(get_users())}</blockquote>"
    )    
    await message.edit(report)
    try:
        os.remove("./users.txt")
        db.delete(f"{msg.from_user.id}:users_up:{bot_id}")
    except Exception:
        pass

# ============ معالجة التواصل ============

@bot.on_message(filters.private, group=793874)
async def twasl(bot, msg):
	if msg.from_user.id not in SUDORS:
		for user in SUDORS:
			if db.get(f"{user}:twasl:{bot_id}"):
				await msg.forward(user)
	if msg.from_user.id in SUDORS:
		if msg.reply_to_message:
			if msg.reply_to_message.forward_from:
				try:
					await msg.copy(msg.reply_to_message.forward_from.id)
					await msg.reply(f"<blockquote><b>╮⦿ تم إرسال رسالتك إلى {msg.reply_to_message.forward_from.first_name}\n╯⦿ بنجاح</b></blockquote>", quote=True)
				except Exception as Error:
					await msg.reply(f"<blockquote><b>• لم يتم ارسال رسالتك بسبب: {str(Error)}</b></blockquote>", quote=True)
					pass