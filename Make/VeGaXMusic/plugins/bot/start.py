#
# Copyright (C) 2024 by MISH0009@Github, < https://github.com/MISH0009 >.
#
# This file is part of < https://github.com/MISH0009/KIM > project,
# and is released under the MIT License.
# Please see < https://github.com/MISH0009/KIM/blob/master/LICENSE >
#
# All rights reserved.
#
import asyncio
import time

from pyrogram import filters
from pyrogram.enums import ChatType, ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from config import BANNED_USERS, START_video_URL
from config import OWNER_ID
from strings import get_string
from VeGaXMusic import HELPABLE, Telegram, YouTube, app
from VeGaXMusic.misc import SUDOERS, _boot_
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from VeGaXMusic.plugins.play.playlist import del_plist_msg
from VeGaXMusic.plugins.sudo.sudoers import sudoers_list
from VeGaXMusic.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_assistant,
    get_lang,
    get_userss,
    is_on_off,
    is_served_private_chat,
)
from VeGaXMusic.utils.decorators.language import LanguageStart
from VeGaXMusic.utils.formatters import get_readable_time
from VeGaXMusic.utils.functions import MARKDOWN, WELCOMEHELP
from VeGaXMusic.utils.inline import alive_panel, private_panel, start_pannel
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from .help import paginate_modules
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import *
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.enums import ChatMembersFilter
from config import *
from pyrogram.enums import ChatMembersFilter
from telegraph import upload_file
from asyncio import gather
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import *
from pyrogram.enums import ChatMembersFilter
import asyncio

loop = asyncio.get_running_loop()



async def get_admin_users(chat_id):
    admin_list = []
    async for member in app.get_chat_members(chat_id):
        if member.status in [ChatMemberStatus.ADMINISTRATOR]:
            admin_list.append(member.user.mention)
    return admin_list


@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS, group=38874)
@LanguageStart
async def start_comm(client, message: Message, _):
    chat_id = message.chat.id
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = InlineKeyboardMarkup(
                paginate_modules(0, HELPABLE, "help", close=True)
            )
            if config.START_video_URL:
                return await message.reply_video(
                    video=config.START_video_URL,
                    caption=_["help_1"],
                    reply_markup=keyboard,
                )
            else:
                return await message.reply_text(
                    text=_["help_1"],
                    reply_markup=keyboard,
                )
        if name[0:4] == "song":
            await message.reply_text(_["song_2"])
            return
        if name == "mkdwn_help":
            await message.reply(
                MARKDOWN,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            )
        if name == "greetings":
            await message.reply(
                WELCOMEHELP,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            )
        if name[0:3] == "sta":
            m = await message.reply_text("🔎 ғᴇᴛᴄʜɪɴɢ ʏᴏᴜʀ ᴘᴇʀsᴏɴᴀʟ sᴛᴀᴛs.!")
            stats = await get_userss(message.from_user.id)
            tot = len(stats)
            if not stats:
                await asyncio.sleep(1)
                return await m.edit(_["ustats_1"])

            def get_stats():
                msg = ""
                limit = 0
                results = {}
                for i in stats:
                    top_list = stats[i]["spot"]
                    results[str(i)] = top_list
                    list_arranged = dict(
                        sorted(
                            results.items(),
                            key=lambda item: item[1],
                            reverse=True,
                        )
                    )
                if not results:
                    return m.edit(_["ustats_1"])
                tota = 0
                videoid = None
                for vidid, count in list_arranged.items():
                    tota += count
                    if limit == 10:
                        continue
                    if limit == 0:
                        videoid = vidid
                    limit += 1
                    details = stats.get(vidid)
                    title = (details["title"][:35]).title()
                    if vidid == "telegram":
                        msg += f"🔗[ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇs ᴀɴᴅ ᴀᴜᴅɪᴏs]({config.SUPPORT_GROUP}) ** played {count} ᴛɪᴍᴇs**\n\n"
                    else:
                        msg += f"🔗 [{title}](https://www.youtube.com/watch?v={vidid}) ** played {count} times**\n\n"
                msg = _["ustats_2"].format(tot, tota, limit) + msg
                return videoid, msg

            try:
                videoid, msg = await loop.run_in_executor(None, get_stats)
            except Exception as e:
                print(e)
                return
            thumbnail = await YouTube.thumbnail(videoid, True)
            await m.delete()
            await message.reply_photo(photo=thumbnail, caption=msg)
            return
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            await asyncio.sleep(1)
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_mention = message.from_user.mention
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} ʜᴀs ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <code>sᴜᴅᴏʟɪsᴛ </code>\n\n**ᴜsᴇʀ ɪᴅ :** {sender_id}\n**ᴜsᴇʀ ɴᴀᴍᴇ:** {sender_name}",
                )
            return
        if name[0:3] == "lyr":
            query = (str(name)).replace("lyrics_", "", 1)
            lyrical = config.lyrical
            lyrics = lyrical.get(query)
            if lyrics:
                await Telegram.send_split_text(message, lyrics)
                return
            else:
                await message.reply_text("ғᴀɪʟᴇᴅ ᴛᴏ ɢᴇᴛ ʟʏʀɪᴄs.")
                return
        if name[0:3] == "del":
            await del_plist_msg(client=client, message=message, _=_)
            await asyncio.sleep(1)
        if name[0:3] == "inf":
            m = await message.reply_text("🔎 ғᴇᴛᴄʜɪɴɢ ɪɴғᴏ!")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
🔍__**ᴠɪᴅᴇᴏ ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ**__

❇️**ᴛɪᴛʟᴇ:** {title}

⏳**ᴅᴜʀᴀᴛɪᴏɴ:** {duration} Mins
👀**ᴠɪᴇᴡs:** `{views}`
⏰**ᴘᴜʙʟɪsʜᴇᴅ ᴛɪᴍᴇ:** {published}
🎥**ᴄʜᴀɴɴᴇʟ ɴᴀᴍᴇ:** {channel}
📎**ᴄʜᴀɴɴᴇʟ ʟɪɴᴋ:** [ᴠɪsɪᴛ ғʀᴏᴍ ʜᴇʀᴇ]({channellink})
🔗**ᴠɪᴅᴇᴏ ʟɪɴᴋ:** [ʟɪɴᴋ]({link})
"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="🎥 ᴡᴀᴛᴄʜ ", url=f"{link}"),
                        InlineKeyboardButton(text="🔄 ᴄʟᴏsᴇ", callback_data="close"),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=key,
            )
            await asyncio.sleep(1)
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} ʜᴀs ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ<code> ᴠɪᴅᴇᴏ ɪɴғᴏʀᴍᴀᴛɪᴏɴ </code>\n\n**ᴜsᴇʀ ɪᴅ:** {sender_id}\n**ᴜsᴇʀ ɴᴀᴍᴇ** {sender_name}",
                )
    else:
        try:
            await app.resolve_peer(OWNER_ID[0])
            OWNER = OWNER_ID[0]
        except:
            OWNER = None
        out = private_panel(_, app.username, OWNER)
        if config.START_video_URL:
            try:
                await message.reply_video(
                    video=config.START_video_URL,
                    caption=_["start_1"].format(app.mention),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            except:
                await message.reply_text(
                    text=_["start_1"].format(app.mention),
                    reply_markup=InlineKeyboardMarkup(out),
                )
        else:
            await message.reply_text(
                text=_["start_1"].format(app.mention),
                reply_markup=InlineKeyboardMarkup(out),
            )
            await sleep(3)
        if await is_on_off(config.LOG):
           sender_id = message.from_user.id
           sender_name = message.from_user.first_name
           usr = await client.get_chat(message.from_user.id)
           name = usr.first_name
           if usr.photo:
                photo = await app.download_media(usr.photo.big_file_id)
                return await app.send_photo(
                    config.LOG_GROUP_ID,
                    photo=photo,
                    caption=f"<b>⭓«ꜱʜᴇɪᴋʜ»♪\n<blockquote>╮❖ قــام : {message.from_user.mention} \n╯❖ بالضغط علي start في البوت\n\n╭⭗ ᴜꜱᴇʀ : @{message.from_user.username}\n╰⭗ ɪᴅ : {sender_id}</b></blockquote>",
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(name, url=f"https://t.me/{message.from_user.username}")]])
                )
           return await app.send_message(
               chat_id=config.LOG_GROUP_ID,
               text=f"<b>⭓ᴘʀɪᴠᴀᴛᴇ✘ʙᴏᴛ♪\n<blockquote>╮❖ قــام : {message.from_user.mention} \n╯❖ بالضغط علي start في البوت\n\n╭⭗ ᴜꜱᴇʀ : @{message.from_user.username}\n╰⭗ ɪᴅ : {sender_id}</b></blockquote>",
               reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(name, url=f"https://t.me/{message.from_user.username}")]])
           )
           
           

@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS, group=38874)
@LanguageStart
async def testbot(client, message: Message, _):
    out = alive_panel(_)
    uptime = int(time.time() - _boot_)
    chat_id = message.chat.id
    if config.START_video_URL:
        await message.reply_video(
            video=config.START_video_URL,
            caption=_["start_7"].format(app.mention, get_readable_time(uptime)),
            reply_markup=InlineKeyboardMarkup(out),
        )
    else:
        await message.reply_text(
            text=_["start_7"].format(app.mention, get_readable_time(uptime)),
            reply_markup=InlineKeyboardMarkup(out),
        )
    return await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    chat_id = message.chat.id
    if config.PRIVATE_BOT_MODE == str(True):
        if not await is_served_private_chat(message.chat.id):
            await message.reply_text(
                "**ᴛʜɪs ʙᴏᴛ's ᴘʀɪᴠᴀᴛᴇ ᴍᴏᴅᴇ ʜᴀs ʙᴇᴇɴ ᴇɴᴀʙʟᴇᴅ ᴏɴʟʏ ᴍʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ɪғ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ᴛʜɪs ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ sᴏ sᴀʏ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ ᴛᴏ ᴀᴜᴛʜᴏʀɪᴢᴇ ʏᴏᴜʀ ᴄʜᴀᴛ."
            )
            return await app.leave_chat(message.chat.id)
    else:
        await add_served_chat(chat_id)
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if member.id == app.id:
                chat_type = message.chat.type
                if chat_type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_5"])
                    return await app.leave_chat(message.chat.id)
                if chat_id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_6"].format(
                            f"https://t.me/{app.username}?start=sudolist"
                        )
                    )
                    return await app.leave_chat(chat_id)
                userbot = await get_assistant(message.chat.id)
                out = start_pannel(_)
                await message.reply_text(
                    _["start_2"].format(
                        app.mention,
                        userbot.username,
                        userbot.id,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            if member.id in config.OWNER_ID:
                return await message.reply_text(
                    _["start_3"].format(app.mention, member.mention)
                )
            if member.id in SUDOERS:
                return await message.reply_text(
                    _["start_4"].format(app.mention, member.mention)
                )
            return
        except:

            return


# تفعيل الجروب  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# تفعيل الجروب  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
        



feeetg = []
@app.on_message(filters.command(["تفعيل"], prefixes=""), group=996255)
async def get_admin(_, message):
    if message.text.strip() == "تفعيل":
        get = await app.get_chat_member(message.chat.id, message.from_user.id)
        if (get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]) or (message.from_user.id == 8040979911):
            if message.chat.id not in feeetg:
                chat_id = message.chat.id
                chat_name = message.chat.title
                admin_users = await get_admin_users(chat_id)
                count = len(admin_users)
                await message.reply_text(f"<b>╮◉ تم تفعيل حمايه لجروب: {chat_name}\n╯◉ وتم رفع : {count} من الادمنيه بنجاح</b>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ꜱʜᴇɪᴋʜ", url="https://t.me/kafra_wi_1")]]))
                feeetg.append(message.chat.id)
            else:
                await message.reply_text(" المجموعة مفعله من قبل يالطيب")
        else:
            await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس\n༄")
                    



# تعطيل حمايه  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# تعطيل حمايه  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   


vggat = []

@app.on_message(filters.command(["تعطيل"], prefixes=""), group=955)
async def get_admin(_, message):
    if message.text.strip() == "تعطيل":
        get = await app.get_chat_member(message.chat.id, message.from_user.id)
        if (get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]) or (message.from_user.id == 8040979911):
            if message.chat.id not in vggat:
                chat_id = message.chat.id
                chat_name = message.chat.title
                admin_users = await get_admin_users(chat_id)
                count = len(admin_users)
                await message.reply_text(f"<b>╮◉ تم تعطيل حمايه لجروب: {chat_name}\n╯◉ وتم تنزيل : {count} من الادمنيه بنجاح</b>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ꜱʜᴇɪᴋʜ", url="https://t.me/kafra_wi_1")]]))
                vggat.append(message.chat.id)
            else:
                await message.reply_text(" المجموعة معطله من قبل يالطيب")
        else:
            await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس\n༄")
            

__MODULE__ = "Boᴛ"
__HELP__ = f"""
<b><blockquote>✦ قايمه اوامر البوت</blockquote>

<blockquote>
╮❖  لعرض سرعه البوت  : بنج /peng
│᚜❖ للتحكم في لغه البوت: اللغه /lug
│᚜❖ لعرض اعدادات البوت: الاعدادات / Settings
│᚜❖ الاحصائيات لجلب Tᴏᴘ 10 : /top /stats
│᚜❖ لتغير وضع تشغيل : وضع التشغيل /play mod
│᚜❖ لتحكم في اوامر ميوزك: المساعده /help
│᚜❖ لتحويل الفويس الي كتابه : بيقول ايه 
│᚜❖ لتحميل اغنيه اكتب: تحميل /download
│᚜❖ لمشاهده اغنيه او فيديو : الاوامر /Commands
╯❖  لمشاهده يوتيوب: يوتيوب مع اسم /YouTube

</b></blockquote>
"""
