import pyrogram
import asyncio
import requests
from pyrogram import Client as client
from pyrogram import Client, idle
from pyrogram import filters, Client
import random
import platform
import re
import socket
import uuid
import os
import speedtest
import asyncio
import platform
import asyncio
import time
import requests
from sys import version as pyver
from datetime import datetime
import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid, FloodWait
from pyrogram.types import CallbackQuery, InputMediaPhoto, Message, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from pytgcalls.__version__ import __version__ as pytgver
from config import SUPPORT_CHANNEL
from config import OWNER_ID
from VeGaXMusic import YouTube, app
from VeGaXMusic import app as Client
from VeGaXMusic.core.userbot import assistants
from VeGaXMusic.misc import SUDOERS, pymongodb
from VeGaXMusic.plugins import ALL_MODULES
from VeGaXMusic.utils.database import get_served_chats, get_served_users, get_sudoers
from VeGaXMusic.utils.decorators.language import language, languageCB
from VeGaXMusic.utils.inline.stats import back_stats_buttons, stats_buttons
import asyncio
from pyrogram import Client, filters
from strings import get_command
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from VeGaXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
import json
import os
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import enums
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from VeGaXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from VeGaXMusic import app
from random import  choice, randint






import os
import json



devchannel = {} 
devphots = {} 




def is_sudoer(_, __, message):
    return message.from_user.id == SUDOERS
other_filters = filters.group &  ~filters.via_bot & ~filters.forwarded
other_filters2 = (
    filters.private &  ~filters.via_bot & ~filters.forwarded
)

def load_bank_data():
    try:
        if os.path.exists('bank_tom.json') and os.path.getsize('bank_tom.json') > 0:
            with open('bank_tom.json', 'r') as file:
                bank_data = json.load(file)
        else:
            bank_data = {}
    except FileNotFoundError:
        bank_data = {}
    except json.JSONDecodeError:
        bank_data = {}
    return bank_data

def save_bank_data(bank_data):
    with open('bank_tom.json', 'w') as file:
        json.dump(bank_data, file)

cooldown_time = 12 * 60 * 60  

def check_cooldown(user_id):
    cooldown_data = load_cooldown_data()
    current_time = int(time.time())
    if str(user_id) in cooldown_data:
        last_use_time = cooldown_data[str(user_id)]
        time_passed = current_time - last_use_time
        remaining_time = cooldown_time - time_passed
        if time_passed < cooldown_time:
            hours = remaining_time // 3600
            minutes = (remaining_time % 3600) // 60
            response = f"<b><blockquote>عذرًا، يجب الانتظار {hours} ساعة و {minutes} دقيقة قبل استخدام الكنز مرة أخرى</b></blockquote>"
            return False, response
    cooldown_data[str(user_id)] = current_time
    save_cooldown_data(cooldown_data)
    return True, None
def load_cooldown_data():
    try:
        with open('cooldown_data.json', 'r') as file:
            cooldown_data = json.load(file)
    except FileNotFoundError:
        cooldown_data = {}
    return cooldown_data
def save_cooldown_data(cooldown_data):
    with open('cooldown_data.json', 'w') as file:
        json.dump(cooldown_data, file)
def get_remaining_time(user_id):
    cooldown_data = load_cooldown_data()
    current_time = int(time.time())
    if str(user_id) in cooldown_data:
        last_use_time = cooldown_data[str(user_id)]
        remaining_time = 20 * 60 - (current_time - last_use_time)
        if remaining_time < 0:
            remaining_time = 0
        return remaining_time
    return 0
##############££££££££££#############££££££££££#########££££#
LUCK_COOLDOWN = 1200  

last_luck_times = {}

def get_luck_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_luck_times:
        last_luck_time = last_luck_times[user_id]
        elapsed_time = current_time - last_luck_time
        remaining_time = LUCK_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time
def update_luck_time(user_id):
    last_luck_times[user_id] = int(time.time())
##############££££££££££#############££££££££££#########££££#
TRANSFER_COOLDOWN = 1200  


last_transfer_times = {}

def get_transfer_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_transfer_times:
        last_transfer_time = last_transfer_times[user_id]
        elapsed_time = current_time - last_transfer_time
        remaining_time = TRANSFER_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time

def update_transfer_time(user_id):
    last_transfer_times[user_id] = int(time.time())

@app.on_message(filters.command(["تحويل"], ""), group=53)
async def transfer(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_transfer_remaining_time(user_id)
        if remaining_time <= 0:
            args = message.text.split(' ')
            if len(args) == 2 and args[1].isdigit():
                amount = int(args[1])
                if amount <= bank_data['accounts'][str(user_id)]['balance']:
                    await message.reply_text(f'<b><blockquote>تم تحويل {amount} جنيه مصري بنجاح</b></blockquote>')
                    update_transfer_time(user_id)
                else:
                    await message.reply_text('<b><blockquote>رصيدك الحالي غير كافي</b></blockquote>')
            else:
                await message.reply_text('<b><blockquote>الرجاء استخدام الأمر بالشكل الصحيح: تحويل + المبلغ</b></blockquote>')
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            await message.reply_text(f'<b><blockquote>عذرًا، يجب الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى</b></blockquote>')
    else:
        await message.reply_text('<b><blockquote>ليس لديك حساب بنكي</b></blockquote>')
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["استثمار"], ""), group=53)
async def invest(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_remaining_time(user_id)
        if remaining_time <= 0:
            args = message.text.split(' ')
            if len(args) == 2 and args[1].isdigit():
                amount = int(args[1])
                if amount <= bank_data['accounts'][str(user_id)]['balance']:
                    bank_data['accounts'][str(user_id)]['balance'] -= amount
                    save_bank_data(bank_data)
                    # قم بتنفيذ الاستثمار وحساب العائد المحتمل
                    return_amount = amount * random.randint(50, 100) / 100
                    bank_data['accounts'][str(user_id)]['balance'] += return_amount
                    save_bank_data(bank_data)
                    cooldown_data = load_cooldown_data()
                    cooldown_data[str(user_id)] = int(time.time())
                    save_cooldown_data(cooldown_data)
                    await message.reply_text(f'تهانينا! لقد استثمرت {amount} جنيه مصري وحصلت على عائد بقيمة {return_amount} جنيه مصري')
                else:
                    await message.reply_text('<b><blockquote>رصيدك الحالي غير كافي</b></blockquote>')
            else:
                await message.reply_text('<b><blockquote>الرجاء استخدام الأمر بالشكل الصحيح: استثمار + المبلغ</b></blockquote>')
        else:
            remaining_minutes = int(remaining_time / 60)
            remaining_seconds = remaining_time % 60
            await message.reply_text(f'<b><blockquote>عذرًا، يجب الانتظار {remaining_minutes} دقيقة و {remaining_seconds} ثانية بين كل عملية استثمار</b></blockquote>')
    else:
        await message.reply_text('<b><blockquote>ليس لديك حساب بنكي</b></blockquote>')
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["حظ"], ""), group=53)
async def luck(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_luck_remaining_time(user_id)
        if remaining_time <= 0:
            args = message.text.split(' ')
            if len(args) == 2 and args[1].isdigit():
                amount = int(args[1])
                if amount <= bank_data['accounts'][str(user_id)]['balance']:
                    bank_data['accounts'][str(user_id)]['balance'] -= amount
                    save_bank_data(bank_data)
                    chance = random.randint(0, 1)
                    if chance == 1:
                        win_amount = amount * random.uniform(1, 3)
                        bank_data['accounts'][str(user_id)]['balance'] += win_amount
                        save_bank_data(bank_data)
                        await message.reply_text(f'<b><blockquote>تهانينا! لقد ربحت {win_amount} جنيه مصري</b></blockquote>')
                    else:
                        await message.reply_text('<b><blockquote>للأسف، لم تربح أي شيء</b></blockquote>')
                    update_luck_time(user_id)
                else:
                    await message.reply_text('<b><blockquote>رصيدك الحالي غير كافي</b></blockquote>')
            else:
                await message.reply_text('<b><blockquote>الرجاء استخدام الأمر بالشكل الصحيح: حظ + المبلغ</b></blockquote>')
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            await message.reply_text(f'<b><blockquote>عذرًا، يجب الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى</b></blockquote>')
    else:
        await message.reply_text('<b><blockquote>ليس لديك حساب بنكي</b></blockquote>')
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["اضف"], "") & filters.create(is_sudoer), group=46468)
async def add_mhzboney(client, message):
    reply_message = message.reply_to_message
    if reply_message is not None and reply_message.from_user is not None:
        user_id = reply_message.from_user.id
        args = message.text.split(" ")
        if len(args) == 2 and args[1].isdigit():
            amount = int(args[1])
            bank_data = load_bank_data()
            if 'accounts' not in bank_data:
                bank_data['accounts'] = {}
            if str(user_id) in bank_data['accounts']:
                bank_data['accounts'][str(user_id)]['balance'] += amount
            else:
                bank_data['accounts'][str(user_id)] = {'balance': amount}
            save_bank_data(bank_data)
            await message.reply_text(f'<b><blockquote>تمت إضافة {amount} فلوس للمستخدم {user_id}</b></blockquote>')
        else:
            await message.reply_text('<b><blockquote>الرجاء استخدام الأمر بالشكل الصحيح: اضف + المبلغ</b></blockquote>')
##############££££££££££#############££££££££££#########££££
@app.on_message(filters.command(["حذف حسابه"], "") & filters.create(is_sudoer), group=5)
async def delete_account(client, message):
    reply_message = message.reply_to_message
    if reply_message is not None and reply_message.from_user is not None:
        user_id = reply_message.from_user.id
        bank_data = load_bank_data()
        if str(user_id) in bank_data['accounts']:
            del bank_data['accounts'][str(user_id)]
            save_bank_data(bank_data)
            await message.reply_text(f'<b><blockquote>تم حذف حساب المستخدم {user_id}</b></blockquote>')
        else:
            await message.reply_text('<b><blockquote>المستخدم المحدد لا يملك حساب بنكي</b></blockquote>')
    else:
        await message.reply_text('<b><blockquote>الرجاء الرد على شخص لحذف حسابه</b></blockquote>')
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["حذف حسابي"], ""), group=6)
async def delete_my_account(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        del bank_data['accounts'][str(user_id)]
        save_bank_data(bank_data)
        await message.reply_text(f'<b><blockquote>تم حذف حسابك البنكي</b></blockquote>')
    else:
        await message.reply_text('<b><blockquote>لا تمتلك حسابًا بنكيًا</b></blockquote>')
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["تصفير البنك"], "") & filters.create(is_sudoer), group=7)
async def reset_bank(client, message):
    bank_data = {'accounts': {}}
    save_bank_data(bank_data)
    await message.reply_text('<b><blockquote>تم مسح جميع حسابات البنك</b></blockquote>')  
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["فتح البنك"], "") & filters.create(is_sudoer), group=8)
async def enable_bank_game(client, message):
    chat_id = message.chat.id
    bank_data = load_bank_data()
    if 'game_enabled' in bank_data:
        await client.send_message(chat_id, '<b><blockquote>لعبة البنك مفعلة بالفعل في المجموعة</b></blockquote>')
    else:
        bank_data['game_enabled'] = True
        save_bank_data(bank_data)
        await client.send_message(chat_id, '<b><blockquote>تم تفعيل لعبة البنك في المجموعة</b></blockquote>')
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["قفل البنك"], "") & filters.create(is_sudoer), group=9)
async def disable_bank_game(client, message):
    chat_id = message.chat.id
    bank_data = load_bank_data()
    if 'game_enabled' in bank_data:
        del bank_data['game_enabled']
        save_bank_data(bank_data)
        await client.send_message(chat_id, '<b><blockquote>تم إيقاف لعبة البنك في المجموعة</b></blockquote>')
    else:
        await client.send_message(chat_id, '<b><blockquote>لعبة البنك معطلة بالفعل في المجموعة</b></blockquote>')
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["انشاء", "انشاء حساب بنكي"], ""), group=7536566)
async def create_account(client, message):
    user_id = message.from_user.id
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{SUPPORT_CHANNEL}"
    ff = devphots.get(bot_username) if devphots.get(bot_username) else f"{START_IMG_URL}"   
    username = message.from_user.username
    bank_data = load_bank_data()
    account_number = random.randint(100000000000000, 999999999999999)
    if 'accounts' not in bank_data:
        bank_data['accounts'] = {}
    if str(user_id) in bank_data['accounts']:
        await message.reply_text('<b><blockquote>لديك بالفعل حساب بنكي</b></blockquote>')
    else:
        bank_data['accounts'][str(user_id)] = {
            'username': username,
            'balance': 50,
            'account_number': account_number,
            'thief': 0
        }
        save_bank_data(bank_data)
        await message.reply_photo(
            photo=f"{ff}",
            caption=f"<b><blockquote>↤︎ تم إنشاء حساب بنكي بنجاح</b></blockquote>\n<b><blockquote>↤︎ اكتب بنكي لترى حسابك 😇</b></blockquote>\n<b><blockquote>↤︎ نوع البنك : بنك </b></blockquote>\n<b><blockquote>↤︎ رقم حسابك {account_number}</b></blockquote>",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ",
                            url=f"{soesh}"
                        ),
                    ],
                ]
            ),
        )
        
@app.on_message(filters.command(["فلوسي"], ""), group=11)
async def check_balance(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    accounts = bank_data.get('accounts', {})
    if str(user_id) in accounts:
        balance = accounts[str(user_id)]['balance']
        await message.reply_text(f'<b><blockquote>رصيدك الحالي هو: {balance} جنيه مصري</b></blockquote>')
    else:
        await message.reply_text('<b><blockquote>ليس لديك حساب بنكي</b></blockquote>')
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["فلوسه"], ""), group=12)
async def check_user_balance(client, message):
    reply = message.reply_to_message
    if reply:
        user_id = reply.from_user.id
        bank_data = load_bank_data()
        if str(user_id) in bank_data['accounts']:
            balance = bank_data['accounts'][str(user_id)]['balance']
            await message.reply_text(f'<b><blockquote>رصيد {reply.from_user.username} هو: {balance} جنيه مصري</b></blockquote>')
        else:
            await message.reply_text(f'<b><blockquote>المستخدم {reply.from_user.username} ليس لديه حساب بنكي</b></blockquote>')
    else:
        await message.reply_text('<b><blockquote>الرجاء الرد على رسالة المستخدم للحصول على معلومات الحساب</b></blockquote>')
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["حسابي"], ""), group=13)
async def view_account(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        username = bank_data['accounts'][str(user_id)]['username']
        balance = bank_data['accounts'][str(user_id)]['balance']
        account_number = bank_data['accounts'][str(user_id)]['account_number']
        await message.reply_text(f'<b><blockquote>حسابك البنكي:</b></blockquote>\n<b><blockquote>المستخدم: @{username}</b></blockquote>\n<b><blockquote>الرصيد: {balance} جنيه مصري</b></blockquote>\n<b><blockquote>رقم الحساب : {account_number}</b></blockquote>')
    else:
        await message.reply_text('<b><blockquote>ليس لديك حساب بنكي</b></blockquote>')
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["بنكه"], ""), group=14)
async def view_user_account(client, message):
    reply = message.reply_to_message
    if reply:
        user_id = reply.from_user.id
        bank_data = load_bank_data()
        if str(user_id) in bank_data['accounts']:
            username = bank_data['accounts'][str(user_id)]['username']
            balance = bank_data['accounts'][str(user_id)]['balance']
            account_number = bank_data['accounts'][str(user_id)]['account_number']
            await message.reply_text(f'<b><blockquote>حساب {reply.from_user.username} البنكي:</b></blockquote>\n<b><blockquote>المستخدم: {username}</b></blockquote>\n<b><blockquote>الرصيد: {balance} جنيه مصري</b></blockquote>\n<b><blockquote>رقم حسابه : {account_number}</b></blockquote>')
        else:
            await message.reply_text(f'<b><blockquote>المستخدم {reply.from_user.username} ليس لديه حساب بنكي</b></blockquote>')
    else:
        await message.reply_text('<b><blockquote>الرجاء الرد على رسالة المستخدم لعرض حسابه البنكي</b></blockquote>')
##############££££££££££#############££££££££££#########££££#
OPERATION_COOLDOWN = 1200  

last_operation_times = {}

def get_operation_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_operation_times:
        last_operation_time = last_operation_times[user_id]
        elapsed_time = current_time - last_operation_time
        remaining_time = OPERATION_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time
def update_operation_time(user_id):
    last_operation_times[user_id] = int(time.time())

@app.on_message(filters.command(["مضاربه", "مضاربة"], ""), group=15) 
async def multiply(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_operation_remaining_time(user_id)
        if remaining_time <= 0:
            args = message.text.split(' ')
            if len(args) == 2 and args[1].isdigit():
                amount = int(args[1])
                if amount <= bank_data['accounts'][str(user_id)]['balance']:
                    bank_data['accounts'][str(user_id)]['balance'] -= amount
                    save_bank_data(bank_data)
                    multiplier = random.randint(2, 5)
                    result_amount = amount * multiplier
                    bank_data['accounts'][str(user_id)]['balance'] += result_amount
                    save_bank_data(bank_data)
                    await message.reply_text(f'<b><blockquote>تهانينا! لقد قمت بالمضاعفة وحصلت على {result_amount} جنيه مصري</b></blockquote>')
                    update_operation_time(user_id)
                else:
                    await message.reply_text('<b><blockquote>رصيدك الحالي غير كافي</b></blockquote>')
            else:
                await message.reply_text('<b><blockquote>الرجاء استخدام الأمر بالشكل الصحيح: مضاعفة + المبلغ</b></blockquote>')
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            await message.reply_text(f'<b><blockquote>عذرًا، يجب الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى</b></blockquote>')
    else:
        await message.reply_text('<b><blockquote>ليس لديك حساب بنكي</b></blockquote>')
##############££££££££££#############££££££££££#########££££#
OPERATION_COOLDOWN = 1200  

last_bribe_times = {}

def get_bribe_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_bribe_times:
        last_bribe_time = last_bribe_times[user_id]
        elapsed_time = current_time - last_bribe_time
        remaining_time = OPERATION_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time

def update_bribe_time(user_id):
    last_bribe_times[user_id] = int(time.time())

@app.on_message(filters.command(["رشوة", "رشوه"], ""), group=16)
async def bribe_command(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_bribe_remaining_time(user_id)
        if remaining_time <= 0:
            args = message.text.split(' ')
            if len(args) == 1:
                amount = random.randint(300, 4000)
                if amount <= bank_data['accounts'][str(user_id)]['balance']:
                    if message.reply_to_message is None:
                        await message.reply_text('<b><blockquote>الرجاء الرد على رسالة لإرسال الرشوة</b></blockquote>')
                        return
                    receiver_id = message.reply_to_message.from_user.id
                    if receiver_id == user_id:
                        await message.reply_text('<b><blockquote>لا يمكنك إرسال رشوة لنفسك</b></blockquote>')
                        return
                    bank_data['accounts'][str(user_id)]['balance'] -= amount
                    bank_data['accounts'][str(receiver_id)]['balance'] += amount
                    save_bank_data(bank_data)
                    await message.reply_text(f'<b><blockquote>تمت عملية الرشوة بنجاح! قمت بتحويل {amount} جنيه مصري إلى المستلم</b></blockquote>')
                    update_bribe_time(user_id)
                else:
                    await message.reply_text('<b><blockquote>رصيدك الحالي غير كافي</b></blockquote>')
            else:
                await message.reply_text('<b><blockquote>الرجاء استخدام الأمر بالشكل الصحيح: رشوة</b></blockquote>')
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            await message.reply_text(f'<b><blockquote>عذرًا، يجب الانتظار {minutes} دقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى</b></blockquote>')
    else:
        await message.reply_text('<b><blockquote>ليس لديك حساب بنكي</b></blockquote>')
##############££££££££££#############££££££££££#########££££#
OPERATION_COOLDOWN = 1200

last_wheel_times = {}

def get_wheel_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_wheel_times:
        last_wheel_time = last_wheel_times[user_id]
        elapsed_time = current_time - last_wheel_time
        remaining_time = OPERATION_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time
def update_wheel_time(user_id):
    last_wheel_times[user_id] = int(time.time())

@app.on_message(filters.command(["عجلة الحظ", "عجله الحظ"], ""), group=17)
async def wheel_of_fortune(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_wheel_remaining_time(user_id)
        if remaining_time <= 0:
            win_amount = random.randint(100, 5000)
            bank_data['accounts'][str(user_id)]['balance'] += win_amount
            save_bank_data(bank_data)
            if win_amount > 0:
                await message.reply_text(f'<b><blockquote>تهانينا! لقد فزت بمبلغ {win_amount} جنيه مصري في عجلة الحظ</b></blockquote>')
            else:
                await message.reply_text('<b><blockquote>عذرًا، لم تفز بأي مبلغ في عجلة الحظ هذه المرة</b></blockquote>')
            update_wheel_time(user_id)
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            await message.reply_text(f'<b><blockquote>عذرًا، يجب الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى</b></blockquote>')
    else:
        await message.reply_text('<b><blockquote>ليس لديك حساب بنكي</b></blockquote>')
##############££££££££££#############££££££££££#########££££#
OPERATION_COOLDOWN = 1200  

last_tip_times = {}

def get_custom_tip_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_tip_times:
        last_tip_time = last_tip_times[user_id]
        elapsed_time = current_time - last_tip_time
        remaining_time = OPERATION_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time
    
def update_custom_tip_time(user_id):
    last_tip_times[user_id] = int(time.time())

@app.on_message(filters.command(["بقشيش"], ""), group=18)
async def custom_tip_command(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_custom_tip_remaining_time(user_id)
        if remaining_time <= 0:
            args = message.text.split(' ')
            if len(args) == 2 and args[1].isdigit():
                amount = int(args[1])
                if amount <= bank_data['accounts'][str(user_id)]['balance']:
                    if message.reply_to_message is None:
                        await message.reply_text('<b><blockquote>الرجاء الرد على رسالة لإرسال البقشيش</b></blockquote>')
                        return
                    receiver_id = message.reply_to_message.from_user.id
                    if receiver_id == user_id:
                        await message.reply_text('<b><blockquote>لا يمكنك إرسال بقشيش لنفسك</b></blockquote>')
                        return
                    bank_data['accounts'][str(user_id)]['balance'] -= amount
                    bank_data['accounts'][str(receiver_id)]['balance'] += amount
                    save_bank_data(bank_data)
                    await message.reply_text(f'<b><blockquote>تمت عملية البقشيش بنجاح! قمت بتحويل {amount} جنيه مصري إلى المستلم</b></blockquote>')
                    update_custom_tip_time(user_id)
                else:
                    await message.reply_text('<b><blockquote>رصيدك الحالي غير كافي</b></blockquote>')
            else:
                await message.reply_text('<b><blockquote>الرجاء استخدام الأمر بالشكل الصحيح: بقشيش + المبلغ</b></blockquote>')
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            await message.reply_text(f'<b><blockquote>عذرًا، يجب الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى</b></blockquote>')
    else:
        await message.reply_text('<b><blockquote>ليس لديك حساب بنكي</b></blockquote>')
##############££££££££££#############££££££££££#########££££#
SALARY_COOLDOWN = 1200  

last_salary_times = {}

def get_salary_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_salary_times:
        last_salary_time = last_salary_times[user_id]
        elapsed_time = current_time - last_salary_time
        remaining_time = SALARY_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time
def update_salary_time(user_id):
    last_salary_times[user_id] = int(time.time())

@app.on_message(filters.command(["راتب"], ""), group=19)
async def salary(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_salary_remaining_time(user_id)
        if remaining_time <= 0:
            salary_amount = 3500
            bank_data['accounts'][str(user_id)]['balance'] += salary_amount
            save_bank_data(bank_data)
            await message.reply_text(f'<b><blockquote>تم صرف راتبك الشهري بمبلغ {salary_amount} جنيه مصري</b></blockquote>')
            update_salary_time(user_id)
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            await message.reply_text(f'<b><blockquote>عذرًا، يجب الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى</b></blockquote>')
    else:
        await message.reply_text('<b><blockquote>ليس لديك حساب بنكي</b></blockquote>')
##############££££££££££#############££££££££££#########££££#
STEAL_COOLDOWN = 1200  
POLICE_COOLDOWN = 1200  

last_steal_times = {}
last_police_times = {}
last_protection_times = {}

def get_steal_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_steal_times:
        last_steal_time = last_steal_times[user_id]
        elapsed_time = current_time - last_steal_time
        remaining_time = STEAL_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time

def get_police_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_police_times:
        last_police_time = last_police_times[user_id]
        elapsed_time = current_time - last_police_time
        remaining_time = POLICE_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time
def get_protection_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_protection_times:
        last_protection_time = last_protection_times[user_id]
        elapsed_time = current_time - last_protection_time
        remaining_time = STEAL_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time
def update_steal_time(user_id):
    last_steal_times[user_id] = int(time.time())
def update_police_time(user_id):
    last_police_times[user_id] = int(time.time())
def update_protection_time(user_id):
    last_protection_times[user_id] = int(time.time())

@app.on_message(filters.command(["سرقة", "سرقه"], ""), group=20640)
async def steal_mo55ney(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_steal_remaining_time(user_id)
        if remaining_time > 0:
            await message.reply_text(f'<b><blockquote>يجب عليك الانتظار لمدة {remaining_time} ثانية قبل استخدام الأمر مرة أخرى</b></blockquote>')
        else:
            target_id = message.reply_to_message.from_user.id
            if str(target_id) in bank_data['accounts']:
                if target_id == user_id:
                    await message.reply_text('<b><blockquote>لا يمكنك سرقة نفسك!</b></blockquote>')
                else:
                    stolen_amount = random.randint(10, 50)
                    if stolen_amount <= bank_data['accounts'][str(target_id)]['balance']:
                        bank_data['accounts'][str(user_id)]['balance'] += stolen_amount
                        bank_data['accounts'][str(target_id)]['balance'] -= stolen_amount
                        bank_data['accounts'][str(user_id)]['thief'] += stolen_amount
                        save_bank_data(bank_data)
                        update_steal_time(user_id)
                        await message.reply_text(f'<b><blockquote>تمت عملية السرقة بنجاح! تم سرقة {stolen_amount} جنيه مصري من المستخدم</b></blockquote>')
                    else:
                        await message.reply_text('<b><blockquote>لا يمكنك سرقته لانه فقي</b></blockquote>ر')
            else:
                await message.reply_text('<b><blockquote>المستخدم المحدد لا يملك حساب بنكي</b></blockquote>')
    else:
        await message.reply_text('<b><blockquote>ليس لديك حساب بنكي</b></blockquote>')

@app.on_message(filters.command(["شرطة", "شرطه"], ""), group=21)
async def police_usehcr(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_police_remaining_time(user_id)
        if remaining_time > 0:
            await message.reply_text(f'<b><blockquote>يجب عليك الانتظار لمدة {remaining_time} ثانية قبل استخدام الأمر مرة أخرى</b></blockquote>')
        else:
            target_id = message.reply_to_message.from_user.id
            if str(target_id) in bank_data['accounts']:
                if target_id == user_id:
                    await message.reply_text('<b><blockquote>لا يمكنك استخدام الأمر على نفسك!</b></blockquote>')
                else:
                    stolen_amount = random.randint(10, 50)
                    if stolen_amount <= bank_data['accounts'][str(user_id)]['balance']:
                        bank_data['accounts'][str(user_id)]['balance'] -= stolen_amount
                        bank_data['accounts'][str(target_id)]['balance'] += stolen_amount
                        save_bank_data(bank_data)
                        update_police_time(user_id)
                        await message.reply_text(f'<b><blockquote>تمت عملية القبض على المستخدم! تم خصم {stolen_amount} جنيه مصري من حسابك</b></blockquote>')
                    else:
                        await message.reply_text('<b><blockquote>رصيدك الحالي غير كافي للقبض على المستخدم</b></blockquote>')
            else:
                await message.reply_text('<b><blockquote>المستخدم المحدد لا يملك حساب بنكي</b></blockquote>')
    else:
        await message.reply_text('<b><blockquote>ليس لديك حساب بنكي</b></blockquote>')

@app.on_message(filters.command(["حماية", "حمايه"], ""), group=22)
async def protect_money(client, message):
    user_id = message.from_user.id
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_protection_remaining_time(user_id)
        if remaining_time > 0:
            await message.reply_text(f'<b><blockquote>يجب عليك الانتظار لمدة {remaining_time} ثانية قبل استخدام الأمر مرة أخرى</b></blockquote>')
        else:
            protection_amount = random.randint(10, 50)
            if protection_amount <= bank_data['accounts'][str(user_id)]['balance']:
                bank_data['accounts'][str(user_id)]['balance'] -= protection_amount
                save_bank_data(bank_data)
                update_protection_time(user_id)
                await message.reply_text(f'<b><blockquote>تم تنفيذ عملية حماية الأموال بنجاح! تم خصم {protection_amount} جنيه مصري من حسابك</b></blockquote>')
            else:
                await message.reply_text('<b><blockquote>رصيدك الحالي غير كافي لحماية الأموال</b></blockquote>')
    else:
        await message.reply_text('<b><blockquote>ليس لديك حساب بنكي</b></blockquote>')

@app.on_message(filters.command(["توب الحراميه", "توب سرقه", "توب السرقة", "توب السرقه", "توب سرقة"], ""), group=22)
async def top_thieves(client, message):
    bank_data = load_bank_data()
    sorted_accounts = sorted(bank_data['accounts'], key=lambda x: bank_data['accounts'][x]['thief'], reverse=True)
    top_thieves = sorted_accounts[:5]  
    response = "<b><blockquote>أعلى الحرامية في البنك:</b></blockquote>\n\n"    
    for thief_id in top_thieves:
        thief_username = await client.get_chat(int(thief_id)).username
        thief_balance = bank_data['accounts'][thief_id]['thief']
        response += f"<b><blockquote>@{thief_username}: {thief_balance} جنيه مصري</b></blockquote>\n"
    await message.reply_text(response)
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["توب فلوس","توب الفلوس"], ""), group=20543)
async def top_m659oney(client, message):
    bank_data = load_bank_data()
    sorted_accounts = sorted(bank_data['accounts'], key=lambda x: bank_data['accounts'][x]['balance'], reverse=True)
    top_accounts = sorted_accounts[:5]  
    response = "<b><blockquote>أعلى الأموال في البنك:</b></blockquote>\n\n"
    for account_id in top_accounts:
        account_username = await client.get_chat(account_id).username
        account_balance = bank_data['accounts'][account_id]['balance']
        response += f"<b><blockquote>@{account_username}: {account_balance} جنيه مصري</b></blockquote>\n"
    
    await message.reply_text(response)


@app.on_message(filters.command(["بنك","البنك"], ""), group=8866666600011287601108)
async def mmmezat(client, message):
        await message.reply_text(f"""
 <blockquote> أوامر خاصه بالمطور</blockquote>
 
 `اضف فلوس` + المبلغ - ❬ بالرد علي الشخص المراد اضافه الفلوس له ❭
 `حذف حسابه` - ❬ بالرد علي الشخص المراد حذف حسابه ❭
 `حذف حساب` + اليوزر - ❬ لحذف حساب الشخص ❭
 `تصفير البنك` - ❬ لمسح كل الحسابات ❭

<blockquote>اوامر خاصه بالاعضاء</blockquote>

`انشاء` - فتح حساب بنكي
`فلوسي` - اموالي
 `فلوسه` - امواله ❬ بالرد علي الشخص ❭
`بنكي` - حسابي
`بنكه` - حسابه ❬ بالرد علي الشخص ❭
`تحويل` + المبلغ
`كنز`
`استثمار` + المبلغ
`حظ` + المبلغ
`مضاعفه` - `مضاربه` + المبلغ
`عجله الحظ`
 `رشوه`
 `بقشيش`
`راتب`
`سرقه` - `اسرق` ❬ بالرد علي الشخص ❭
`شرطه` - `شرطة` ❬ بالرد علي الشخص ❭
`حمايه اموالي` - ❬ لحمايه اموالك من السرقه ❭
شرطه + اليوزر
`توب الحراميه` - `توب السرقه`
 `توب الفلوس` - `توب فلوس`

""")